#!/usr/bin/env python3
"""Revisa la composició de tots els fotogrames de la sèrie sense produir cap vídeo.

Dibuixa cada pas de cada lliçó (vistes generades i vistes fetes a mida) i registra on
queda cada text, panell, línia i fletxa. Avisa quan:

- un text surt del panell que el conté o del fotograma;
- un text entra a la zona reservada als subtítols;
- dos textos se superposen;
- un subratllat no coincideix amb el text que té a sobre;
- una fletxa talla un panell.

    python Git/eines/revisa_visuals.py Git                  # totes les lliçons
    python Git/eines/revisa_visuals.py Git 00-introduccio   # una sola
"""
import argparse
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT), str(Path(__file__).resolve().parent)]
from PIL import ImageDraw  # noqa: E402
from motor import dibuix as r  # noqa: E402
from motor.serie import load_series  # noqa: E402
import escenes  # noqa: E402
import render  # noqa: E402

SUBTITLES_TOP = 588
TOLERANCE = 2


class Recorder:
    """Intercepta les crides de dibuix per saber on queda cada element."""

    def __init__(self):
        self.reset()
        self.original = {name: getattr(ImageDraw.ImageDraw, name) for name in ('text', 'rounded_rectangle', 'line')}
        self.original_arrow = r.arrow

    def reset(self):
        self.texts, self.boxes, self.lines, self.arrows = [], [], [], []

    def __enter__(self):
        recorder = self

        def text(draw, xy, content, fill=None, font=None, anchor=None, *args, **kwargs):
            if content and str(content).strip():
                box = draw.textbbox(xy, content, font=font, anchor=anchor)
                recorder.texts.append((box, str(content)))
            return recorder.original['text'](draw, xy, content, fill, font, anchor, *args, **kwargs)

        def rounded_rectangle(draw, xy, *args, **kwargs):
            recorder.boxes.append(tuple(xy))
            return recorder.original['rounded_rectangle'](draw, xy, *args, **kwargs)

        def line(draw, xy, fill=None, width=0, *args, **kwargs):
            flat = [v for point in xy for v in (point if isinstance(point, tuple) else (point,))]
            if len(flat) == 4:
                recorder.lines.append((tuple(flat), width))
            return recorder.original['line'](draw, xy, fill, width, *args, **kwargs)

        def arrow(d, start, end, color=r.MINT, width=4):
            recorder.arrows.append((min(start[0], end[0]), min(start[1], end[1]) - width * 2.2,
                                    max(start[0], end[0]), max(start[1], end[1]) + width * 2.2))
            return recorder.original_arrow(d, start, end, color, width)

        ImageDraw.ImageDraw.text = text
        ImageDraw.ImageDraw.rounded_rectangle = rounded_rectangle
        ImageDraw.ImageDraw.line = line
        r.arrow = arrow
        return self

    def __exit__(self, *exc):
        for name, function in self.original.items():
            setattr(ImageDraw.ImageDraw, name, function)
        r.arrow = self.original_arrow


def inside(inner, outer, slack=TOLERANCE):
    return (inner[0] >= outer[0]-slack and inner[1] >= outer[1]-slack and
            inner[2] <= outer[2]+slack and inner[3] <= outer[3]+slack)


def overlap(a, b):
    width = min(a[2], b[2]) - max(a[0], b[0])
    height = min(a[3], b[3]) - max(a[1], b[1])
    return width > 1 and height > 1


def problems(recorder):
    found = []
    content_texts = [(box, text) for box, text in recorder.texts if box[1] > 190]  # sota el títol de l’escena
    for box, text in recorder.texts:
        if box[0] < -TOLERANCE or box[2] > 1280+TOLERANCE or box[1] < 0 or box[3] > 720:
            found.append(f'«{text}» surt del fotograma')
    for box, text in content_texts:
        if box[3] > SUBTITLES_TOP:
            found.append(f'«{text}» entra a la zona dels subtítols (fins a y={box[3]})')
        # El panell que conté l’inici del text ha de contenir-lo sencer.
        containers = [b for b in recorder.boxes if b[0] <= box[0] <= b[2] and b[1] <= box[1] <= b[3]]
        if containers:
            smallest = min(containers, key=lambda b: (b[2]-b[0])*(b[3]-b[1]))
            if not inside(box, smallest):
                found.append(f'«{text}» surt del seu panell ({int(box[2]-smallest[2])} px)')
    for i, (a, first) in enumerate(content_texts):
        for b, second in content_texts[i+1:]:
            if overlap(a, b) and not (inside(a, b) or inside(b, a)):
                found.append(f'«{first}» i «{second}» se superposen')
    for (x0, y0, x1, y1), width in recorder.lines:
        if y0 != y1 or width < 3 or abs(x1-x0) > 500:
            continue
        above = [(box, text) for box, text in content_texts if 0 <= y0 - box[3] <= 16 and box[0] < max(x0, x1) and box[2] > min(x0, x1)]
        if above:
            box, text = min(above, key=lambda item: y0 - item[0][3])
            if min(x0, x1) < box[0]-6 or max(x0, x1) > box[2]+6:
                found.append(f'el subratllat de «{text}» no coincideix amb el text')
    for arrow in recorder.arrows:
        for panel in recorder.boxes:
            if overlap(arrow, panel) and not inside(arrow, panel):
                found.append('una fletxa talla un panell')
                break
    return found


def frames_generic(item, config, execution):
    for index, scene in enumerate(config['scenes']):
        for beat in scene['beats']:
            if beat.get('event') == 'execute':
                continue
            def paint(scene=scene, beat=beat, index=index):
                im = r.base(scene, index, len(config['scenes']), config)
                escenes.draw_beat(ImageDraw.Draw(im), scene, beat, execution, config=config)
            yield scene, beat, None, paint


def frames_custom(item, config):
    draw = render.drawer(config, None)
    demo = {}
    if config['slug'].startswith('03-'):
        from visuals_primer_commit import prepare_demo
        demo = prepare_demo(Path(tempfile.mkdtemp()))
    for index, scene in enumerate(config['scenes']):
        scene['_timed_beats'] = [{**b, 'at': k*5.0, 'effect_at': k*5+1} for k, b in enumerate(scene['beats'])]
        scene['_demo'] = demo
        for k, beat in enumerate(scene['beats']):
            for moment in (k*5+.5, k*5+4.9):  # abans i després de l’efecte del pas
                def paint(scene=scene, index=index, t=moment):
                    im = r.base(scene, index, len(config['scenes']), config)
                    draw(ImageDraw.Draw(im), scene, t)
                yield scene, beat, None, paint


def check_lesson(item):
    config = json.loads((item['folder']/'guio.json').read_text())
    path = item['folder']/'execucio.json'
    execution = json.loads(path.read_text()) if path.exists() else None
    custom = any(b.get('view') for s in config['scenes'] for b in s['beats'])
    report = {}
    with Recorder() as recorder:
        frames = frames_custom(item, config) if custom else frames_generic(item, config, execution)
        for scene, beat, _, paint in frames:
            recorder.reset()
            paint()
            for problem in problems(recorder):
                report.setdefault(problem, f'{scene["title"]} · {beat["id"]}')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('serie', type=Path)
    parser.add_argument('llicons', nargs='*')
    args = parser.parse_args()
    total = 0
    for item in load_series(args.serie)['lessons']:
        if args.llicons and item['name'] not in args.llicons and item['slug'] not in args.llicons:
            continue
        report = check_lesson(item)
        total += len(report)
        print(('OK ' if not report else 'REVISAR ') + item['name'])
        for problem, where in report.items():
            print(f'   - {problem}  [{where}]')
    if total:
        sys.exit(1)


if __name__ == '__main__':
    main()
