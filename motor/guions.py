#!/usr/bin/env python3
"""Compila els `llico.yaml` d’una sèrie en guions per produir i per llegir.

Per a cada lliçó escriu `guio.json` (entrada del muntatge: escenes, passos, idiomes,
subratllats, pauses i sortides reals) i `guio.md` (text per revisar). També escriu
l’índex `GUIONS.md` de la sèrie. No sintetitza veu ni genera vídeo.

    python -m motor.guions Git              # compila
    python -m motor.guions Git --comprova   # falla si els fitxers generats no estan al dia

Abans d’escriure res, el compilador revisa el text: idioma de cada terme, cap
pregunta, cap hash ni marcador llegit en veu alta, pauses dins del rang, opcions
explicades la primera vegada que apareixen a la sèrie i resum de tres idees.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shlex
import sys
import xml.etree.ElementTree as ET

from motor.serie import load_series, spoken_number
from motor.veu import make_ssml

FORMAT = 'pindoles-guio-v3'
LABEL = re.compile(r'\{([A-Z][0-9′]?)\}')
SUSPICIOUS = [
    (re.compile(r'\b(?=[0-9a-f]*\d)[0-9a-f]{7,40}\b'), 'un hash no s’ha de llegir en veu alta'),
    (re.compile(r'\bV\d\b'), 'cal anomenar la versió amb paraules, no V1/V2'),
    (re.compile(r'__|~'), 'símbols de camí o de memòria cau no s’han de llegir'),
    (re.compile(r'\b[A-H]\s*[–-]\s*[A-H]\b'), 'un interval de lletres no s’entén en veu alta'),
    (re.compile(r'\?'), 'les lliçons no fan preguntes'),
    (re.compile(r'\bguia\b|acompanya el vídeo|material extern', re.I), 'el vídeo ha de ser autònom'),
    (re.compile(r'\{[^}]*\}'), 'marcador sense substituir'),
]


class ScriptError(ValueError):
    pass


# ---------------------------------------------------------------- idiomes
class Language:
    def __init__(self, config):
        terms = sorted(config.get('termes_angles', []), key=len, reverse=True)
        self.terms = terms
        self.pattern = re.compile(r'(?<![\w/.-])(?:' + '|'.join(re.escape(t) for t in terms) +
                                  r')(?![\w/-])', re.I) if terms else None
        self.forms = config.get('formes_parlades', {})

    def spoken(self, text):
        for written, spoken in self.forms.items():
            text = re.sub(r'(?<![\w-])'+re.escape(written)+r'(?![\w])', spoken, text)
        return text

    def segments(self, text, explicit_only=False):
        text = self.spoken(text)
        pieces = []
        for index, chunk in enumerate(re.split(r'\[\[(.*?)\]\]', text)):
            if not chunk:
                continue
            if index % 2:
                pieces.append(dict(lang='en-US', text=chunk))
                continue
            end = 0
            if self.pattern and not explicit_only:
                for match in self.pattern.finditer(chunk):
                    if match.start() > end:
                        pieces.append(dict(lang='ca-ES', text=chunk[end:match.start()]))
                    pieces.append(dict(lang='en-US', text=match.group()))
                    end = match.end()
            if end < len(chunk):
                pieces.append(dict(lang='ca-ES', text=chunk[end:]))
        # Els espais entre dos termes anglesos no han d’esdevenir canvis d’idioma.
        for i in range(1, len(pieces)-1):
            if pieces[i]['text'].isspace() and pieces[i-1]['lang'] == pieces[i+1]['lang'] == 'en-US':
                pieces[i]['lang'] = 'en-US'
        merged = []
        for part in pieces:
            if merged and merged[-1]['lang'] == part['lang']:
                merged[-1]['text'] += part['text']
            else:
                merged.append(dict(part))
        return ''.join(p['text'] for p in merged), merged

    def untagged(self, segments):
        """Termes anglesos coneguts que han quedat dins d’un fragment català."""
        found = []
        for segment in segments:
            if segment['lang'] == 'ca-ES' and self.pattern:
                found += [m.group() for m in self.pattern.finditer(segment['text'])]
        return found


def plain(text):
    return re.sub(r'\[\[(.*?)\]\]', r'\1', text)


# ---------------------------------------------------------------- plantilles
def expand(stage, templates):
    """Aplica una plantilla de serie.yaml; els camps de l’etapa tenen prioritat."""
    if 'plantilla' not in stage:
        return dict(stage)
    if stage['plantilla'] not in templates:
        raise ScriptError(f'Plantilla desconeguda: {stage["plantilla"]}')
    base = json.loads(json.dumps(templates[stage['plantilla']]))
    base.update({k: v for k, v in stage.items() if k != 'plantilla'})
    values = {'fitxer': base.get('fitxer') or 'helloGit.py', 'branca': base.get('branca', ''),
              'missatge': base.get('missatge', '')}
    values['missatge_parlat'] = values['missatge']

    def fill(value):
        if isinstance(value, str):
            return value.replace('{fitxer}', values['fitxer']).replace('{branca}', values['branca']) \
                        .replace('{missatge_parlat}', values['missatge_parlat']).replace('{missatge}', values['missatge'])
        if isinstance(value, list):
            return [fill(v) for v in value]
        if isinstance(value, dict):
            return {fill(k): fill(v) for k, v in value.items()}
        return value
    for key in ('ordre', 'text', 'visual', 'parts', 'resultat'):
        if key in base:
            base[key] = fill(base[key])
    return base


def parts_of(stage):
    parts = []
    for item in stage.get('parts') or []:
        if isinstance(item, dict):
            (fragment, explanation), = item.items()
        else:
            fragment, explanation = item
        parts.append((str(fragment), explanation))
    return parts


def action_of(command):
    words = command.split()
    if command.startswith('git -C '):
        return ' '.join(words[:4]) if len(words) > 3 else command
    if command.startswith(('git stash ', 'git bisect ', 'git worktree ', 'git remote add ', 'gh auth ')):
        return ' '.join(words[:3])
    if command.startswith(('git ', 'gh ')):
        return ' '.join(words[:2])
    return words[0]


# ---------------------------------------------------------------- compilació
class Compiler:
    def __init__(self, series):
        self.series = series
        self.config = series['config']
        self.language = Language(self.config)
        self.templates = self.config.get('plantilles', {})
        self.known_options = set()

    def compile(self, item):
        lesson = item['data']
        if not lesson:
            raise ScriptError(f'{item["name"]}: falta llico.yaml')
        execution = None
        if (item['folder']/'execucio.json').exists():
            execution = json.loads((item['folder']/'execucio.json').read_text())
        explicit = lesson.get('etiquetatge') == 'explicit'
        number = item['number']
        voice = self.config['veu']
        intro_text = f"{spoken_number(number)}. {lesson['presentacio']}."
        narration, segments = self.language.segments(intro_text, explicit)
        config = {
            'script_format': FORMAT, 'series': self.config['nom'], 'episode_number': number,
            'slug': item['name'], 'title': lesson['titol'], 'short_title': lesson['titol_curt'],
            'card': lesson['capcalera'], 'lesson_kind': lesson.get('tipus', 'practica'),
            'voice': voice['nom'], 'language_rates': voice['velocitats'],
            'language_switch_pause_ms': voice['pausa_canvi_idioma_ms'],
            'speech_endpoint': voice.get('endpoint'), 'fps': self.config.get('fps', 24),
            'output_name': f"{item['name']}.mp4", 'questions': False,
            'subtitles': {'english': 'quotes-and-italic', 'shared_baseline': True},
            'intro': {'enabled': True, 'narration': narration, 'segments': segments},
            'objective': lesson['objectiu'], 'start_note': lesson['inici'],
            'start_spoken': plain(self.language.spoken(lesson['inici_parlat'])),
            'summary': [plain(self.language.spoken(s)) for s in lesson.get('resum', [])],
            'practice': plain(self.language.spoken(lesson.get('practica', ''))),
            'practice_script': f"practiques/{item['name']}.sh" if lesson.get('preparacio') else None,
            'scenes': [], 'commands': []}
        self.counter = 0
        self.number = number
        self.explicit = explicit
        self.config_out = config
        if 'escenes' in lesson:
            self.compile_scenes(lesson)
        else:
            self.compile_stages(lesson, execution)
        self.validate(config, item)
        return config

    def beat(self, text, visual, pause=3, beat_id=None, **extra):
        self.counter += 1
        narration, segments = self.language.segments(text, self.explicit)
        return dict(id=beat_id or f'pas_{self.counter:03}', narration=narration, segments=segments,
                    visual=visual, pause_after=pause, commands=[], **extra)

    def scene(self, title, beats, label, mode='principal', visual='', scene_id=None, **extra):
        scenes = self.config_out['scenes']
        item = dict(id=scene_id or f'e{self.number:02}_{len(scenes):02}', label=label, title=title,
                    mode=mode, visual=visual or (beats[0]['visual'] if beats else ''), beats=beats, **extra)
        item['narration'] = ' '.join(b['narration'] for b in beats)
        scenes.append(item)

    def compile_scenes(self, lesson):
        """Format d’escenes explícites amb vistes pròpies (lliçons amb visuals fets a mida)."""
        for scene in lesson['escenes']:
            beats = []
            for step in scene['passos']:
                beat = self.beat(step['text'], scene['visual'], step.get('pausa', 3), step['id'],
                                 view=step['vista'])
                beat['commands'] = list(step.get('ordres', []))
                for command in beat['commands']:
                    if command not in self.config_out['commands']:
                        self.config_out['commands'].append(command)
                beats.append(beat)
            self.scene(scene['titol'], beats, scene['etiqueta'], visual=scene['visual'], scene_id=scene['id'])

    def compile_stages(self, lesson, execution):
        paths = lesson.get('camins', {})
        goal = lesson['objectiu']
        self.scene('Objectiu i punt de partida', [
            self.beat('En aquesta lliçó aprendrem a '+goal[0].lower()+goal[1:],
                      'Objectiu en una frase; esquema general del resultat.', 2.5),
            self.beat(lesson['inici_parlat'], 'Punt de partida: '+lesson['inici'], 3.5, state=-1)],
            'OBJECTIU')
        stages = [expand(s, self.templates) for s in lesson['etapes']]
        if execution and len(execution['etapes']) < len(stages):
            raise ScriptError('execucio.json no està al dia: torneu a executar la repetició')
        for index, stage in enumerate(stages):
            run = execution['etapes'][index] if execution else None
            labels = run['etiquetes'] if run else {}
            mode = stage.get('cami', 'principal')
            label = 'EXPLICACIÓ'
            if mode != 'principal':
                spec = paths.get(mode)
                if not spec:
                    raise ScriptError(f'Camí no definit: {mode}')
                label = spec['titol'].upper()

            def resolve(text):
                def replace(match):
                    if match.group(1) not in labels:
                        raise ScriptError(f'No hi ha identificador real per a {{{match.group(1)}}}: '
                                          'executeu Git/eines/repeticio.py')
                    return labels[match.group(1)]
                return LABEL.sub(replace, text)

            visual = resolve(stage.get('visual', ''))
            if 'explica' in stage:
                texts = stage['text'] if isinstance(stage['text'], list) else [stage['text']]
                beats = [self.beat(t, visual, stage.get('pausa', 3), state=index) for t in texts]
                self.scene(stage['explica'], beats, label, mode, visual)
                continue
            command = resolve(stage['ordre'])
            if command not in self.config_out['commands'] and stage.get('tipus') != 'interactiu':
                self.config_out['commands'].append(command)
            kind = stage.get('tipus', 'terminal')
            persistent = ('Mantenir visible el text complet: '+command+'. Conservar l’estat de partida mentre '
                          's’explica; encara no executar ni mostrar-ne el resultat.')
            action = command if kind == 'interactiu' else action_of(command)
            beats = [self.beat(stage['text'], persistent+' Subratllar l’acció: '+action+'.', 2.5,
                               command_display=command, highlight=action, state=index-1)]
            for fragment, explanation in parts_of(stage):
                fragment = resolve(fragment)
                if fragment not in command:
                    raise ScriptError(f'«{fragment}» no forma part de «{command}»')
                beats.append(self.beat(explanation, persistent+' Subratllar únicament: '+fragment+'.', 2.5,
                                       command_display=command, highlight=fragment, state=index-1))
            execute = self.beat('Introduïm la resposta.' if kind == 'interactiu' else 'Executem l’ordre.',
                                persistent+' Executar després de la locució, sense mostrar abans el resultat.',
                                1.5, command_display=command, event='execute', effect_after='speech', state=index-1)
            execute['commands'] = [command]
            beats.append(execute)
            output = (run or {}).get('sortida', '')
            sample = stage.get('sortida_mostra')
            result = self.beat(stage['resultat'], visual+' Mostrar el resultat concret i conservar l’estat anterior '
                               'per comparar.', stage.get('pausa', 3.5), command_display=command, event='result',
                               state=index, simulated=bool(stage.get('simulat') or sample))
            # Les sortides de mostra substitueixen les reals quan contenen rutes locals de la
            # prova (remots) o quan l’ordre depèn d’un servei que la prova no pot executar.
            if sample:
                result['terminal_output'] = resolve(sample).rstrip('\n').splitlines()
            elif output.strip() and not stage.get('simulat'):
                result['terminal_output'] = output.rstrip('\n').splitlines()
            beats.append(result)
            self.scene(command, beats, 'TERMINAL' if label == 'EXPLICACIÓ' else label, mode, visual,
                       input_kind=kind)
        self.scene('Resum final', [self.beat(t, 'Tres idees finals; ressaltar només la idea que s’està explicant.',
                                             2.5) for t in lesson['resum']], 'RESUM')
        self.scene('Pràctica final', [self.beat(lesson['practica'], 'Instrucció pràctica completa en pantalla. '
                                                'Mantenir la referència visual final, sense formular preguntes.', 4)],
                   'PRÀCTICA')

    # ------------------------------------------------------------ revisió
    def validate(self, config, item):
        problems = []
        where = item['name']
        if config['intro']['narration'] != ''.join(s['text'] for s in config['intro']['segments']):
            problems.append('presentació mal segmentada')
        for scene in config['scenes']:
            ET.fromstring(make_ssml(scene, config))
            highlights = []
            for beat in scene['beats']:
                text = beat['narration']
                if text != ''.join(s['text'] for s in beat['segments']):
                    problems.append(f'{beat["id"]}: segments i text no coincideixen')
                for pattern, reason in SUSPICIOUS:
                    match = pattern.search(text)
                    if match:
                        problems.append(f'{scene["title"]} · «{match.group()}»: {reason}')
                for written in self.language.forms:
                    if re.search(r'(?<![\w-])'+re.escape(written)+r'(?![\w])', text):
                        problems.append(f'{beat["id"]}: «{written}» s’ha de pronunciar en català')
                if not self.explicit:
                    for term in self.language.untagged(beat['segments']):
                        problems.append(f'{scene["title"]}: «{term}» quedaria pronunciat en català')
                if not 1.5 <= beat['pause_after'] <= 4:
                    problems.append(f'{beat["id"]}: pausa fora del rang 1,5–4 s')
                if beat.get('highlight') and beat.get('event') is None:
                    highlights.append(beat['highlight'])
            command = next((b['command_display'] for b in scene['beats'] if b.get('event') == 'execute'), None)
            if command and scene.get('input_kind') != 'interactiu':
                verb = action_of(command)
                try:
                    tokens = shlex.split(command)
                except ValueError:
                    tokens = command.split()
                for option in [t for t in tokens if t.startswith('-') and t != '--']:
                    # Les opcions llargues signifiquen el mateix a totes les ordres; les curtes
                    # (-u, -c, -d...) canvien de sentit segons l’ordre i s’expliquen per ordre.
                    key = option.split('=')[0] if option.startswith('--') else (verb, option)
                    if option not in highlights and key not in self.known_options:
                        problems.append(f'«{command}»: cal explicar {option} la primera vegada que surt a la sèrie')
                    if option in highlights:
                        self.known_options.add(key)
                if '-m' in highlights:
                    values = [h for h in highlights if h.startswith('"')]
                    if not values or highlights.index('-m') > highlights.index(values[0]):
                        problems.append(f'«{command}»: el missatge s’explica després de -m')
        if 'escenes' not in item['data']:
            if len(config['summary']) != 3:
                problems.append('el resum ha de tenir tres idees')
            if not config['practice']:
                problems.append('falta la pràctica final')
        card = item['data'].get('capcalera')
        if not (isinstance(card, list) and len(card) == 2 and all(isinstance(x, str) for x in card)):
            problems.append('capcalera ha de ser [títol, subtítol]; poseu-hi cometes si hi ha comes')
        if problems:
            raise ScriptError(where+':\n  - '+'\n  - '.join(problems))


# ---------------------------------------------------------------- documents
def spoken_md(beat):
    """Locució amb els fragments anglesos en cursiva, com als subtítols."""
    return ''.join(('*'+seg['text'].strip()+'*' + (' ' if seg['text'].endswith(' ') else '')
                    if seg['lang'] == 'en-US' and seg['text'].strip() else seg['text'])
                   for seg in beat['segments'])


def markdown(config):
    lines = [f"# Lliçó {config['episode_number']} · {config['title']}", '',
             f"**Sèrie:** {config['series']} · **Capçalera:** {config['card'][0]} — {config['card'][1]}  ",
             f"**Veu:** {config['voice']}; català {config['language_rates']['ca-ES']}, anglès "
             f"{config['language_rates']['en-US']}; {config['language_switch_pause_ms']} ms en cada canvi d’idioma.  ",
             '**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.', '']
    if config.get('practice_script'):
        lines += [f"**Punt de partida reproduïble:** [`{config['practice_script']}`](../{config['practice_script']})", '']
    lines += ['## Capçalera i presentació', '', '4 s de música comuna. Després, la veu llegeix:', '',
              '> '+spoken_md({'segments': config['intro']['segments']}), '']
    for scene in config['scenes']:
        command = next((b['command_display'] for b in scene['beats'] if b.get('command_display')), None)
        if command:
            kind = 'Resposta interactiva' if scene.get('input_kind') == 'interactiu' else 'Terminal'
            lines += [f'## {kind} · `{command}`', '']
        else:
            lines += ['## '+scene['title'], '']
        if scene['mode'] != 'principal':
            lines += [f"> **{scene['label'].capitalize()}.** Parteix del seu propi punt; no s’encadena amb el camí principal.", '']
        if not command:
            for beat in scene['beats']:
                lines += [spoken_md(beat)+f" *(pausa {beat['pause_after']:g} s)*", '']
            lines += ['**Visual:** '+scene['visual'], '']
            continue
        lines += ['| Subratllat | Locució | Pausa |', '| --- | --- | ---: |']
        result = None
        for beat in scene['beats']:
            if beat.get('event') == 'result':
                result = beat
                continue
            mark = 'execució' if beat.get('event') == 'execute' else '`'+beat['highlight'].replace('|', '\\|')+'`'
            lines.append(f"| {mark} | {spoken_md(beat)} | {beat['pause_after']:g} s |")
        lines += ['', f"**Resultat:** {spoken_md(result)} *(pausa {result['pause_after']:g} s)*", '']
        if result.get('terminal_output'):
            lines += ['Sortida '+('de mostra' if result.get('simulated') else 'real')+':', '',
                      '```text', *result['terminal_output'][:16], '```', '']
        elif not result.get('simulated'):
            lines += ['Sortida real: *cap línia*.', '']
        lines += ['**Visual:** '+scene['visual'], '']
    return '\n'.join(lines)


def compile_series(folder, check=False):
    series = load_series(folder)
    compiler = Compiler(series)
    errors, outputs, index = [], {}, []
    for item in series['lessons']:
        if item['folder'].name != item['name']:
            errors.append(f'{item["folder"].name}: la carpeta hauria de ser {item["name"]} '
                          '(python -m motor.serie <sèrie> --renumera)')
            continue
        try:
            config = compiler.compile(item)
        except (ScriptError, KeyError) as error:
            text = str(error)
            errors.append(text if text.startswith(item['name']) else f'{item["name"]}: {text}')
            continue
        text = json.dumps(config, ensure_ascii=False, indent=2)+'\n'
        outputs[item['folder']/'guio.json'] = text
        outputs[item['folder']/'guio.md'] = markdown(config)
        beats = [b for s in config['scenes'] for b in s['beats']]
        words = sum(len(b['narration'].split()) for b in beats)
        pauses = sum(b['pause_after'] for b in beats)
        # Estimació calibrada amb les lliçons ja produïdes (0 i 3): unes 2,1 paraules per
        # segon a +5%, les pauses explícites, la capçalera i ~0,85 s de marge per escena.
        estimate = words/2.1 + pauses + 7 + .85*len(config['scenes'])
        index.append((item, config, len(config['scenes']), len(beats), words, estimate))
    if errors:
        raise ScriptError('\n'.join(errors))
    lines = [f"# Guions · {series['name']}", '',
             'Generat per `python -m motor.guions` a partir dels `llico.yaml`. No editeu aquest fitxer.', '',
             '| Lliçó | Títol | Escenes | Passos | Paraules | Durada estimada |',
             '| --- | --- | ---: | ---: | ---: | ---: |']
    for item, config, scenes, beats, words, estimate in index:
        lines.append(f"| {item['number']:02} | [{config['title']}]({item['name']}/guio.md) | {scenes} | {beats} | "
                     f"{words} | {int(estimate//60)}:{int(estimate%60):02} |")
    outputs[series['root']/'GUIONS.md'] = '\n'.join(lines)+'\n'
    stale = [path for path, text in outputs.items() if not path.exists() or path.read_text() != text]
    if check:
        if stale:
            raise ScriptError('Fitxers generats desactualitzats:\n  - ' +
                              '\n  - '.join(str(p.relative_to(series['root'])) for p in stale))
        return index
    for path in stale:
        path.write_text(outputs[path])
    return index


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('serie', type=Path)
    parser.add_argument('--comprova', action='store_true', help='No escriu; falla si cal recompilar')
    args = parser.parse_args()
    try:
        index = compile_series(args.serie, check=args.comprova)
    except ScriptError as error:
        print(error, file=sys.stderr)
        sys.exit(1)
    total = sum(entry[5] for entry in index)
    print(f'{len(index)} guions correctes · durada estimada total {int(total//60)} min. Cap àudio generat.')


if __name__ == '__main__':
    main()
