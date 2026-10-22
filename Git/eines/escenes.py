#!/usr/bin/env python3
"""Visuals generats a partir de l’estat real de cada pas (execucio.json).

Les lliçons sense vistes fetes a mida es dibuixen totes amb aquest mateix model:
graf de commits amb branques i HEAD, estat del treball i terminal amb la comanda,
el fragment subratllat i la sortida real. Així, refer una lliçó no exigeix escriure
codi de dibuix nou; només cal que el guió i la repetició estiguin al dia.

    python Git/eines/escenes.py Git 08-branques   # full de contacte a 08-branques/build/

Només genera imatges fixes de revisió (storyboard); no produeix àudio ni vídeo.
"""
import argparse
import json
import math
import re
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from PIL import Image, ImageDraw  # noqa: E402
from motor import dibuix as r  # noqa: E402
from motor.serie import load_series  # noqa: E402

GRAPH = (64, 196, 604, 572)
STATUS = (628, 196, 1216, 372)
TERMINAL = (628, 386, 1216, 572)
LEGEND = {'M': 'MODIFICAT', 'A': 'NOU, PREPARAT', 'D': 'ESBORRAT', 'U': 'CONFLICTE', '?': 'NO SEGUIT', 'R': 'REANOMENAT'}


def state_for(execution, beat):
    index = beat.get('state', -1)
    if not execution:
        return {}
    if index is None or index < 0:
        return execution['inici']
    return execution['etapes'][min(index, len(execution['etapes'])-1)]['estat']


def lanes(state):
    """Assigna una fila a cada commit: la de main primer, després la resta de branques."""
    commits = {c['id']: c for c in state.get('commits', [])}
    refs = state.get('refs', {})
    order = sorted(refs, key=lambda name: (name != 'main', name.startswith(('origin/', 'upstream/')), name))
    lane_of = {}
    for lane, name in enumerate(order):
        sha = refs[name]
        while sha in commits and sha not in lane_of:
            lane_of[sha] = min(lane, 2)
            parents = commits[sha]['pares']
            sha = parents[0] if parents else None
    # Els commits que només s’hi arriben pel segon pare d’una fusió (branca ja esborrada)
    # conserven una fila pròpia, perquè no semblin posteriors a la línia principal.
    lane = len(order)
    for commit in commits.values():
        for sha in commit['pares'][1:]:
            if sha in lane_of:
                continue
            while sha in commits and sha not in lane_of:
                lane_of[sha] = min(max(lane, 1), 2)
                parents = commits[sha]['pares']
                sha = parents[0] if parents else None
            lane += 1
    for sha in commits:
        lane_of.setdefault(sha, 0)
    return lane_of


def draw_graph(d, state):
    x0, y0, x1, y1 = GRAPH
    r.panel(d, GRAPH)
    r.text(d, (x0+22, y0+16), 'HISTORIAL · ' + state.get('directori', ''), 'label', r.ORANGE)
    commits = state.get('commits', [])
    if not commits:
        r.text(d, (x0+22, y0+80), 'Encara sense commits', 'body', r.MUTED)
        return
    lane_of = lanes(state)
    head_commit = state.get('head_commit')
    # Etiquetes de cada commit: branques, etiquetes i, si cal, HEAD separat.
    labels = {}
    for name, sha in sorted(state.get('refs', {}).items()):
        active = name == state.get('head')
        color = r.MINT if active else (r.PURPLE if name.startswith(('origin/', 'upstream/')) or '.' in name else r.WHITE)
        labels.setdefault(sha, []).append((('HEAD → ' if active else '') + name, color))
    if not state.get('head') and head_commit:
        labels.setdefault(head_commit, []).insert(0, ('HEAD SEPARAT', r.MINT))
    lanes_used = max(lane_of.values()) + 1
    above = max([len(labels.get(c['id'], [])) for c in commits if lane_of[c['id']] == 0] or [0])
    below = max([len(labels.get(c['id'], [])) for c in commits if lane_of[c['id']] > 0] or [0])
    # Alçada disponible: capçalera, etiquetes a sobre, files de commits, identificadors i etiquetes a sota.
    top_needed = 44 + above*28 + 30
    bottom_needed = 46 + below*28
    available = (y1-y0) - top_needed - bottom_needed
    gap = 0 if lanes_used == 1 else max(56, min(105, available/(lanes_used-1)))
    used = top_needed + gap*(lanes_used-1) + bottom_needed
    first_lane = y0 + top_needed + max(0, ((y1-y0) - used)/2)
    step = min(120, (x1-x0-130)/max(1, len(commits)-1)) if len(commits) > 1 else 0
    start = x0 + (x1-x0 - step*(len(commits)-1))/2
    position = {c['id']: (start+i*step, first_lane+lane_of[c['id']]*gap) for i, c in enumerate(commits)}
    for commit in commits:
        for parent in commit['pares']:
            if parent in position:
                d.line((*position[parent], *position[commit['id']]), fill=r.BORDER, width=5)
    for commit in commits:
        x, y = position[commit['id']]
        r.node(d, x, y, None, r.MINT if commit['id'] == head_commit else r.ORANGE)
        r.text(d, (x, y), commit['lletra'] or '', 'label', r.BG, 'mm')
        if step >= 85 or len(commits) == 1:  # amb molts commits, els identificadors no hi caben
            r.text(d, (x, y+30), commit['id'], 'tinycode', r.MUTED, 'mt')
    placed = []
    for sha in sorted(labels, key=lambda c: position.get(c, (0, 0))[0]):
        if sha not in position:
            continue
        x, y = position[sha]
        level = 0
        for text, color in labels[sha]:
            width = d.textlength(text, font=r.F['small'])+16
            # Sempre dins del panell, encara que el commit sigui a la vora.
            center = min(max(x, x0+12+width/2), x1-12-width/2)
            # Les etiquetes de la fila principal van a sobre; les de les altres files, a sota.
            # Si el lloc ja és ocupat per l’etiqueta d’un altre commit, puja (o baixa) un nivell.
            while True:
                top = y-62-level*28 if lane_of[sha] == 0 else y+50+level*28
                box = (center-width/2-4, top, center+width/2+4, top+24)
                if not any(box[0] < b[2] and b[0] < box[2] and box[1] < b[3] and b[1] < box[3] for b in placed):
                    break
                level += 1
            placed.append(box)
            level += 1
            d.rounded_rectangle((center-width/2, top, center+width/2, top+24), 8, fill='#1E2A3D', outline=color, width=2)
            r.text(d, (center, top+12), text, 'small', color, 'mm')


def draw_status(d, state, box=STATUS):
    r.panel(d, box)
    x0, y0, x1, y1 = box
    if state.get('head'):
        where = f'branca {state["head"]}'
    else:
        where = 'HEAD separat' if state.get('head_commit') else 'sense commits'
    r.text(d, (x0+22, y0+16), f'TREBALL · {where}', 'label', r.MINT)
    lines = state.get('status', [])
    y = y0+52
    if not lines:
        r.text(d, (x0+22, y), 'Sense canvis pendents', 'body', r.MUTED)
        y += 28
    shown = lines[:3]
    for line in shown:
        code, name = line[:2], line[3:]
        # «??» és un sol estat (no seguit), no dues columnes.
        meaning = LEGEND['?'] if code == '??' else ' / '.join(LEGEND.get(c, '') for c in code if c.strip())
        r.text(d, (x0+22, y), code.replace(' ', '·'), 'code', r.ORANGE)
        name = fit(d, name, r.F['code'], x1-x0-120)
        r.text(d, (x0+80, y), name, 'code', r.WHITE)
        # La llegenda només es mostra si hi cap al costat del nom.
        legend_x = x0+80+d.textlength(name, font=r.F['code'])+18
        if meaning and legend_x+d.textlength(meaning, font=r.F['small']) <= x1-16:
            r.text(d, (legend_x, y+4), meaning, 'small', r.MUTED)
        y += 28
    if len(lines) > len(shown):
        r.text(d, (x0+22, y), f'… {len(lines)-len(shown)} més', 'small', r.MUTED)
        y += 24
    files = state.get('fitxers', {})
    main_file = 'helloGit.py' if 'helloGit.py' in files else next(iter(files), None)
    room = int((y1-14 - (y+22)) // 20)
    if main_file and room >= 1:
        content = files[main_file].rstrip('\n').splitlines()
        r.text(d, (x0+22, y+4), main_file, 'small', r.MUTED)
        # Si el fitxer no hi cap sencer, l’última fila ho diu en lloc d’amagar línies en silenci.
        shown = content[:room] if len(content) <= room else content[:room-1]
        for i, line in enumerate(shown):
            r.text(d, (x0+22, y+22+i*20), fit(d, line, r.F['tinycode'], x1-x0-44), 'tinycode', r.WHITE)
        if len(content) > len(shown):
            r.text(d, (x0+22, y+22+len(shown)*20), f'… {len(content)-len(shown)} línies més', 'small', r.MUTED)


FULL = (64, 196, 1216, 572)
RIGHT = (628, 196, 1216, 572)


def fit(d, text, font, width):
    """Retalla una línia perquè no surti del panell, amb punts suspensius."""
    if d.textlength(text, font=font) <= width:
        return text
    while text and d.textlength(text+'…', font=font) > width:
        text = text[:-1]
    return text+'…'


def split_command(d, command, font, width):
    """Parteix una ordre llarga en línies pels espais; retorna (text, posició inicial) de cada línia."""
    lines, current, start, position = [], '', 0, 0
    for token in command.split(' '):
        candidate = (current + ' ' + token) if current else token
        if current and d.textlength(candidate, font=font) > width:
            lines.append((current, start))
            start = position
            current = token
        else:
            current = candidate
        position += len(token) + 1
    lines.append((current, start))
    return lines


def draw_terminal(d, beat, output, executed, box=TERMINAL):
    x0, y0, x1, y1 = box
    command = beat.get('command_display')
    r.terminal(d, box, 'TERMINAL')
    if not command:
        return
    inner = x1-x0-66
    style = 'code' if d.textlength(command, font=r.F['code']) <= inner else 'tinycode'
    font = r.F[style]
    # Les ordres que no hi caben en una línia continuen a la següent, sense retallar-les.
    lines = split_command(d, command, font, inner)
    height = 30 if style == 'code' else 24
    r.text(d, (x0+22, y0+52), '$', style, r.MINT)
    for i, (text, _) in enumerate(lines):
        r.text(d, (x0+44, y0+52+i*height), text, style)
    highlight = beat.get('highlight')
    if highlight and highlight in command and not executed:
        begin = command.index(highlight)
        end = begin + len(highlight)
        # Un fragment que continua a la línia següent es subratlla a trossos, línia per línia.
        for row, (text, start) in enumerate(lines):
            first, last = max(begin, start), min(end, start+len(text))
            if first >= last:
                continue
            left = x0+44+d.textlength(command[start:first], font=font)
            right = left+d.textlength(command[first:last], font=font)
            base = y0+52+row*height+(32 if style == 'code' else 26)
            d.line((left, base, right, base), fill=r.PURPLE, width=4)
    if executed:
        wide = x1-x0 > 900
        out_style, step = ('code', 30) if wide else ('tinycode', 24)
        top = y0+102+(len(lines)-1)*height
        rows = max(1, int((y1-12-top)//step))
        shown = output[:rows] if len(output) <= rows else output[:rows-1]
        for i, line in enumerate(shown):
            r.text(d, (x0+22, top+i*step), fit(d, line.expandtabs(8), r.F[out_style], x1-x0-44), out_style, r.MINT)
        if len(output) > len(shown):
            r.text(d, (x0+22, top+len(shown)*step), f'… {len(output)-len(shown)} línies més', 'small', r.MUTED)
        if beat.get('simulated'):
            r.text(d, (x1-22, y0+12), 'SORTIDA DE MOSTRA', 'small', r.PURPLE, 'ra')


def output_rows(d, beat, box=TERMINAL):
    """Línies de sortida que caben a la terminal, amb la mateixa disposició que draw_terminal."""
    x0, y0, x1, y1 = box
    command = beat.get('command_display') or ''
    style = 'code' if d.textlength(command, font=r.F['code']) <= x1-x0-66 else 'tinycode'
    lines = split_command(d, command, r.F[style], x1-x0-66)
    top = y0+102+(len(lines)-1)*(30 if style == 'code' else 24)
    step = 30 if x1-x0 > 900 else 24
    return max(1, int((y1-12-top)//step))


CODE = re.compile(r'^(git|gh|python3|brew|winget|code)\b|[()"/=<>*~:_]|--|^-|^\.|\.\w+$|^[A-Z0-9 ()\\]+$')
# Paraules soltes que són noms de Git (branques, accions del rebase...).
GIT_WORDS = {'main', 'pick', 'squash', 'salutacio', 'comiat', 'correccio', 'origin', 'upstream', 'menu', 'proves'}


def is_code(value):
    """Ordres, codi o noms de fitxer es mostren en monoespai; les frases, en text normal."""
    return bool(CODE.search(value)) or value in GIT_WORDS or bool(re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)+', value))


SIZES = [  # text, codi, alçada de línia, alçada de parella
    ('lead', 'leadcode', 40, 44),
    ('body', 'code', 33, 37),
    ('small', 'tinycode', 25, 28),
]


def card_rows(d, lines, width, size):
    text_style, code_style, line_height, pair_height = size
    rows = []
    for index, paragraph in enumerate(lines):
        if '  ' in paragraph:
            name, value = (part.strip() for part in paragraph.split('  ', 1))
            style = code_style if is_code(value) else text_style
            column = max(d.textlength(name, font=r.F[text_style])+24, 230 if text_style == 'lead' else 190)
            if d.textlength(value, font=r.F[style]) <= width-column:
                rows.append(('pair', name, value, style, column, pair_height, index))
            else:
                rows.append(('lead', name, None, 'muted', 0, line_height, index))
                for piece in r.wrap(d, value, width-30, style):
                    rows.append(('value', piece, None, style, 30, line_height, index))
        else:
            rows += [('lead', line, None, 'ink', 0, line_height, index) for line in r.wrap(d, paragraph, width, text_style)]
        rows.append(('gap', '', None, None, 0, 10, index))
    if rows:
        rows.pop()
    return rows


def text_card(d, box, label, lines, color=r.MINT, active=True, current=None):
    """Targeta de text centrada verticalment; redueix la mida de la lletra si el text no hi cap.

    «Etiqueta:  valor» col·loca el valor al costat de l’etiqueta si hi cap, o a la línia
    següent si no; els valors que són ordres o codi es mostren en monoespai. Amb `current`,
    la línia que s’explica es marca i la resta s’atenua.
    """
    x0, y0, x1, y1 = box
    r.panel(d, box, outline=color if active else r.BORDER)
    top = y0+16
    if label:
        r.text(d, (x0+26, y0+16), label, 'label', color if active else r.MUTED)
        top = y0+44
    width = x1-x0-52
    for size in SIZES:
        rows = card_rows(d, lines, width, size)
        height = sum(row[5] for row in rows)
        if height <= y1-12-top:
            break
    text_style = size[0]
    y = max(top, (top+y1-12)/2 - height/2)
    for kind, first, second, style, column, step, index in rows:
        ink = r.WHITE if active else r.MUTED
        accent = r.MINT if active else r.MUTED
        if current is not None and kind != 'gap':
            if index == current:
                d.line((x0+12, y+2, x0+12, y+step-6), fill=r.PURPLE, width=4)
            else:
                ink = accent = r.BORDER
        if kind == 'lead':
            r.text(d, (x0+26, y), first, text_style, (r.MUTED if ink != r.BORDER else ink) if style == 'muted' else ink)
        elif kind == 'pair':
            r.text(d, (x0+26, y+2), first, text_style, r.MUTED if current is None or index == current else r.BORDER)
            r.text(d, (x0+26+column, y+3), second, style, accent if style in ('leadcode', 'code', 'tinycode') else ink)
        elif kind == 'value':
            r.text(d, (x0+26+column, y+2), fit(d, first, r.F[style], width-column), style,
                   accent if style in ('leadcode', 'code', 'tinycode') else ink)
        y += step


def annotated_file(d, box, name, lines, current=None):
    """Fitxer real a l’esquerra i, separada amb una fletxa, l’explicació de cada línia a la dreta.

    Les notes no formen part del fitxer: es dibuixen en una altra columna i amb text normal.
    """
    x0, y0, x1, y1 = box
    r.terminal(d, box, name)
    rows = [line.split('  ←  ') + [None] if '  ←  ' not in line else line.split('  ←  ') for line in lines]
    for code, note in ((('leadcode', 'lead'), 44), (('code', 'body'), 36), (('tinycode', 'small'), 28)):
        (code_style, note_style), step = code, note
        if y0+60 + sum(step if rule else step//2 for rule, _ in rows) <= y1-12:
            break
    column = max(d.textlength(rule, font=r.F[code_style]) for rule, _ in rows) + 48
    height = sum(step if rule else step//2 for rule, _ in rows)
    y, annotated = max(y0+60, (y0+48+y1-12)/2 - height/2), -1
    for rule, note in rows:
        if not rule:
            y += step//2
            continue
        if note is not None:
            annotated += 1
        here = current is None or (note is not None and annotated == current)
        if current is not None and here:
            d.line((x0+14, y+2, x0+14, y+step-8), fill=r.PURPLE, width=4)
        comment = rule.startswith('#')
        r.text(d, (x0+30, y), rule, code_style, (r.MUTED if comment else r.MINT) if here else r.BORDER)
        if note:
            r.text(d, (x0+30+column, y+2), '← ' + note, note_style, r.WHITE if here else r.BORDER)
        y += step


def draw_cards(d, scene, beat, config):
    """Objectiu, resum i pràctica: el text escrit de la locució es converteix en targetes."""
    beats = scene['beats']
    current = next((i for i, b in enumerate(beats) if b['id'] == beat['id']), 0)
    written = [b.get('screen_text', b['narration']) for b in beats]
    if scene['label'] == 'PRÀCTICA':
        lines = [written[0]]
        if config.get('practice_script'):
            lines.append('Punt de partida del vídeo:  Git/' + config['practice_script'])
        text_card(d, FULL, 'AL TEU REPOSITORI DE PRÀCTIQUES', lines, r.PURPLE)
        return
    if scene['label'] == 'RESUM':
        titles, color = [f'IDEA {i+1}' for i in range(len(written))], r.ORANGE
    else:
        titles, color = ['OBJECTIU', 'PUNT DE PARTIDA'], r.MINT
        written = written[:2]
    # Cada targeta té l’alçada que necessita el seu text, dins de l’espai disponible.
    gap, area = 12, FULL[3]-FULL[1]
    needs = [60 + 40*len(r.wrap(d, text, FULL[2]-FULL[0]-52, 'lead')) for text in written]
    scale = min(1, (area - gap*(len(needs)-1)) / sum(needs))
    top = FULL[1]
    for i, (text, need) in enumerate(zip(written, needs)):
        bottom = top + need*scale
        text_card(d, (FULL[0], top, FULL[2], bottom), titles[i], [text], color, i <= current)
        top = bottom + gap


def draw_beat(d, scene, beat, execution, executed=None, config=None):
    result = next((b for b in scene['beats'] if b.get('event') == 'result'), None)
    # Quan l’ordre ja s’ha executat, els panells mostren l’estat posterior, igual que la terminal.
    state = state_for(execution, result if executed and result else beat)
    # Sense commits (fora d’un repositori o en un de buit) no hi ha historial per dibuixar.
    history = bool(state.get('commits'))
    if executed is None:
        executed = beat.get('event') == 'result'
    output = next((b.get('terminal_output', []) for b in scene['beats'] if b.get('event') == 'result'), [])
    if scene['label'] in ('OBJECTIU', 'RESUM', 'PRÀCTICA'):
        draw_cards(d, scene, beat, config or {})
        return
    screen = scene.get('screen')
    command = beat.get('command_display')
    if not history:
        if command:
            draw_terminal(d, beat, output, executed, FULL)
        else:
            text_card(d, FULL, None, screen or [scene['title']], r.MINT)
        return
    if scene.get('screen_file') and screen and not command:
        current = None
        if scene.get('screen_step'):
            current = next((i for i, b in enumerate(scene['beats']) if b['id'] == beat['id']), None)
        annotated_file(d, FULL, scene['screen_file'], screen, current)
        return
    draw_graph(d, state)
    if command and len(output) > output_rows(d, beat):
        # La sortida no hi cap: la terminal ocupa tota la columna durant l’escena.
        draw_terminal(d, beat, output, executed, RIGHT)
    elif command:
        draw_status(d, state)
        draw_terminal(d, beat, output, executed)
    elif screen:
        current = None
        if scene.get('screen_step'):
            current = next((i for i, b in enumerate(scene['beats']) if b['id'] == beat['id']), None)
        text_card(d, RIGHT, None, screen, r.MINT, current=current)
    else:
        draw_status(d, state, RIGHT)


def draw_scene(d, scene, t, execution, config=None):
    """Funció de dibuix per al muntatge: tria el pas actual segons els temps reals de la veu."""
    beats = scene['_timed_beats']
    beat = next((b for b in reversed(beats) if t >= b['at']), beats[0])
    executed = beat.get('event') == 'result' or (beat.get('event') == 'execute' and t >= beat['effect_at'])
    draw_beat(d, scene, beat, execution, executed, config)


def storyboard(folder):
    config = json.loads((folder/'guio.json').read_text())
    path = folder/'execucio.json'
    execution = json.loads(path.read_text()) if path.exists() else None
    frames = []
    for index, scene in enumerate(config['scenes']):
        if any(b.get('view') for b in scene['beats']):
            continue
        for beat in scene['beats']:
            if beat.get('event') == 'execute':
                continue
            im = r.base(scene, index, len(config['scenes']), config)
            draw_beat(ImageDraw.Draw(im), scene, beat, execution, config=config)
            frames.append(im)
    build = folder/'build'
    build.mkdir(exist_ok=True)
    columns = 3
    sheet = Image.new('RGB', (1280, math.ceil(len(frames)/columns)*240), r.BG)
    for i, im in enumerate(frames):
        sheet.paste(im.resize((426, 240), Image.Resampling.LANCZOS), ((i % columns)*427, (i//columns)*240))
    target = build/'storyboard-escenes.jpg'
    sheet.save(target, quality=88)
    return target, frames


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('serie', type=Path)
    parser.add_argument('llicons', nargs='+')
    args = parser.parse_args()
    for item in load_series(args.serie)['lessons']:
        if item['name'] in args.llicons or item['slug'] in args.llicons:
            target, frames = storyboard(item['folder'])
            print(f'{item["name"]}: {len(frames)} imatges → {target}')


if __name__ == '__main__':
    main()
