#!/usr/bin/env python3
"""Fitxes per publicar a YouTube: títol, descripció, capítols, etiquetes i llista.

Per a cada lliçó escriu `youtube.md` a partir del guió compilat. Si la lliçó ja
s’ha produït, els capítols surten dels temps reals de `output/produccio.json`;
si no, la fitxa ho indica i els capítols s’omplen en tornar-la a generar.
També escriu `YOUTUBE.md`, l’ordre de la llista de reproducció.

    python -m motor.youtube Git
    python -m motor.youtube Git --comprova
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

from motor.serie import load_series

TITLE_LIMIT = 100
MIN_CHAPTER = 10


def timestamp(seconds):
    seconds = int(seconds)
    return f'{seconds//60}:{seconds%60:02}' if seconds < 3600 else f'{seconds//3600}:{seconds//60%60:02}:{seconds%60:02}'


def chapters(production):
    """Capítols vàlids per a YouTube: el primer a 0:00 i cadascun de 10 s com a mínim."""
    items = [(0.0, 'Capçalera i presentació')]
    for scene in production['scenes']:
        title = scene.get('title') or scene['id']
        if title.startswith(('git ', 'python3 ', 'cd ', 'gh ', 'chmod ')):
            title = '$ ' + title
        items.append((scene['start'], title))
    merged = []
    for start, title in items:
        if merged and start - merged[-1][0] < MIN_CHAPTER:
            continue
        merged.append((start, title))
    if production['duration'] - merged[-1][0] < MIN_CHAPTER and len(merged) > 1:
        merged.pop()
    return merged if len(merged) >= 3 else []


def sheet(series, item, previous, following):
    config = json.loads((item['folder']/'guio.json').read_text())
    settings = series['config']
    number = f'{item["number"]:02}'
    title = f'{config["title"]} · {series["name"]} {number}'
    if len(title) > TITLE_LIMIT:
        title = f'{config["short_title"].capitalize()} · {series["name"]} {number}'
    web = (settings.get('web') or '').rstrip('/')
    script = config.get('practice_script')
    link = (f'{web}/{script}' if web else f'{series["root"].name}/{script}') if script else None
    description = [config['objective'][0].upper() + config['objective'][1:], '',
                   'Punt de partida: ' + config['start_spoken'], '']
    if config['commands']:
        description += ['Ordres que surten al vídeo:', *[f'  {c}' for c in config['commands']], '']
    description += ['Practica-ho: ' + config['practice']]
    if link:
        description += [f'Script per preparar el mateix punt de partida: {link}']
    description += ['']
    production = item['folder']/'output'/'produccio.json'
    source = hashlib.sha256((item['folder']/'guio.json').read_bytes()).hexdigest()
    data = json.loads(production.read_text()) if production.exists() else None
    current = bool(data) and data.get('source_sha256') == source
    marks = chapters(data) if current else []
    if marks:
        description += ['Capítols:', *[f'{timestamp(s)} {t}' for s, t in marks], '']
    if previous:
        description.append(f'Lliçó anterior: {previous["number"]:02} · {previous["title"]}')
    if following:
        description.append(f'Lliçó següent: {following["number"]:02} · {following["title"]}')
    description += ['', f'Llista: {settings["youtube"]["llista"]}. Subtítols en català inclosos.']
    lines = [f'# YouTube · lliçó {number}', '',
             'Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.', '',
             f'**Títol** ({len(title)}/{TITLE_LIMIT} caràcters)', '', '```text', title, '```', '',
             '**Descripció**', '', '```text', *description, '```', '',
             f'**Etiquetes:** {", ".join(settings["youtube"]["etiquetes"] + [config["short_title"].lower()])}  ',
             f'**Llista:** {settings["youtube"]["llista"]}, posició {item["number"]+1}  ',
             '**Idioma del vídeo i dels subtítols:** català  ',
             f'**Vídeo:** `{series["root"].name}/{settings["videos"]}/{item["name"]}.mp4`  ',
             f'**Subtítols:** `{item["name"]}/output/{item["name"]}.ca.srt`  ',
             f'**Miniatura:** `{item["name"]}/output/portada.png`', '']
    if not data:
        lines += ['> Encara no s’ha produït el vídeo: els capítols s’afegiran quan existeixi `output/produccio.json`.', '']
    elif not current:
        lines += ['> El vídeo produït correspon a un guió anterior: cal tornar-lo a produir abans de publicar-lo.', '']
    elif not marks:
        lines += ['> El vídeo no té prou escenes de 10 s o més per definir capítols a YouTube.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('serie', type=Path)
    parser.add_argument('--comprova', action='store_true')
    args = parser.parse_args()
    series = load_series(args.serie)
    infos = []
    for item in series['lessons']:
        config = json.loads((item['folder']/'guio.json').read_text())
        infos.append({'number': item['number'], 'title': config['title'], 'name': item['name']})
    outputs = {}
    for index, item in enumerate(series['lessons']):
        outputs[item['folder']/'youtube.md'] = sheet(series, item, infos[index-1] if index else None,
                                                     infos[index+1] if index+1 < len(infos) else None)
    playlist = [f'# Llista de YouTube · {series["config"]["youtube"]["llista"]}', '',
                'Ordre de publicació. Generat per `python -m motor.youtube`.', '',
                '| Posició | Lliçó | Fitxa | Vídeo produït |', '| ---: | --- | --- | --- |']
    for info, item in zip(infos, series['lessons']):
        produced = (item['folder']/'output'/'produccio.json').exists()
        playlist.append(f'| {info["number"]+1} | {info["title"]} | [youtube.md]({info["name"]}/youtube.md) | '
                        f'{"sí" if produced else "pendent"} |')
    outputs[series['root']/'YOUTUBE.md'] = '\n'.join(playlist)+'\n'
    stale = [path for path, text in outputs.items() if not path.exists() or path.read_text() != text]
    if args.comprova:
        if stale:
            print('Fitxes de YouTube desactualitzades: ' + ', '.join(str(p) for p in stale), file=sys.stderr)
            sys.exit(1)
        return
    for path in stale:
        path.write_text(outputs[path])
    print(f'{len(outputs)-1} fitxes de YouTube i la llista al dia.')


if __name__ == '__main__':
    main()
