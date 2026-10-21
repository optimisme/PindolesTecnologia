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
            lane_of[sha] = min(lane, 3)
            parents = commits[sha]['pares']
            sha = parents[0] if parents else None
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
    step = min(92, (x1-x0-90)/max(1, len(commits)-1)) if len(commits) > 1 else 0
    position = {}
    for i, commit in enumerate(commits):
        position[commit['id']] = (x0+55+i*step, y0+150+lane_of[commit['id']]*86)
    for commit in commits:
        for parent in commit['pares']:
            if parent in position:
                d.line((*position[parent], *position[commit['id']]), fill=r.BORDER, width=5)
    head_commit = state.get('head_commit')
    for commit in commits:
        x, y = position[commit['id']]
        color = r.MINT if commit['id'] == head_commit else r.ORANGE
        r.node(d, x, y, None, color, scale=.8)
        label = commit['lletra'] or ''
        r.text(d, (x, y), label, 'label', r.BG, 'mm')
        r.text(d, (x, y+28), commit['id'], 'tinycode', r.MUTED, 'mt')
    stacked = {}
    for name, sha in sorted(state.get('refs', {}).items()):
        if sha not in position:
            continue
        x, y = position[sha]
        level = stacked.get(sha, 0)
        stacked[sha] = level+1
        active = name == state.get('head')
        text = ('HEAD → ' if active else '') + name
        color = r.MINT if active else (r.PURPLE if name.startswith(('origin/', 'upstream/')) or '.' in name else r.WHITE)
        width = d.textlength(text, font=r.F['small'])+16
        top = y-58-level*28
        d.rounded_rectangle((x-width/2, top, x+width/2, top+24), 8, fill='#1E2A3D', outline=color, width=2)
        r.text(d, (x, top+12), text, 'small', color, 'mm')
    if not state.get('head') and head_commit in position:
        x, y = position[head_commit]
        r.text(d, (x, y+50), 'HEAD SEPARAT', 'small', r.MINT, 'mt')


def draw_status(d, state):
    r.panel(d, STATUS)
    x0, y0, _, _ = STATUS
    branch = state.get('head') or 'HEAD separat'
    r.text(d, (x0+22, y0+16), f'TREBALL · branca {branch}', 'label', r.MINT)
    lines = state.get('status', [])
    if not lines:
        r.text(d, (x0+22, y0+62), 'Sense canvis pendents', 'body', r.MUTED)
    for i, line in enumerate(lines[:4]):
        code, name = line[:2], line[3:]
        meaning = ' / '.join(LEGEND.get(c, '') for c in code if c.strip()) or ''
        r.text(d, (x0+22, y0+58+i*30), code.replace(' ', '·'), 'code', r.ORANGE)
        r.text(d, (x0+80, y0+58+i*30), name, 'code', r.WHITE)
        r.text(d, (x0+330, y0+62+i*30), meaning, 'small', r.MUTED)
    files = state.get('fitxers', {})
    main_file = 'helloGit.py' if 'helloGit.py' in files else next(iter(files), None)
    if main_file and len(lines) < 3:
        content = files[main_file].rstrip('\n').splitlines()[:3]
        r.text(d, (x0+22, y0+120), main_file, 'small', r.MUTED)
        for i, line in enumerate(content):
            r.text(d, (x0+22, y0+142+i*22), line[:46], 'tinycode', r.WHITE)


def draw_terminal(d, beat, output, executed):
    x0, y0, x1, _ = TERMINAL
    command = beat.get('command_display')
    r.terminal(d, TERMINAL, 'TERMINAL')
    if not command:
        return
    font = r.F['tinycode'] if len(command) > 40 else r.F['code']
    style = 'tinycode' if font is r.F['tinycode'] else 'code'
    r.text(d, (x0+22, y0+52), '$', style, r.MINT)
    r.text(d, (x0+44, y0+52), command, style)
    highlight = beat.get('highlight')
    if highlight and highlight in command and not executed:
        left = x0+44+d.textlength(command.split(highlight, 1)[0], font=font)
        d.line((left, y0+80, left+d.textlength(highlight, font=font), y0+80), fill=r.PURPLE, width=4)
    if executed:
        for i, line in enumerate(output[:4]):
            r.text(d, (x0+22, y0+92+i*22), line[:58], 'tinycode', r.MINT)
        if len(output) > 4:
            r.text(d, (x0+22, y0+92+4*22), f'… {len(output)-4} línies més', 'small', r.MUTED)


def draw_beat(d, scene, beat, execution, executed=None):
    state = state_for(execution, beat)
    draw_graph(d, state)
    draw_status(d, state)
    if executed is None:
        executed = beat.get('event') == 'result'
    output = next((b.get('terminal_output', []) for b in scene['beats'] if b.get('event') == 'result'), [])
    draw_terminal(d, beat, output, executed)


def draw_scene(d, scene, t, execution):
    """Funció de dibuix per al muntatge: tria el pas actual segons els temps reals de la veu."""
    beats = scene['_timed_beats']
    beat = next((b for b in reversed(beats) if t >= b['at']), beats[0])
    executed = beat.get('event') == 'result' or (beat.get('event') == 'execute' and t >= beat['effect_at'])
    draw_beat(d, scene, beat, execution, executed)


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
            draw_beat(ImageDraw.Draw(im), scene, beat, execution)
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
