#!/usr/bin/env python3
"""Produeix una lliçó de la sèrie Git: veu, animacions, subtítols i verificació.

    python Git/eines/render.py Git/08-branques              # vídeo complet a Git/output/
    python Git/eines/render.py Git/08-branques --audio-only # només veu, subtítols i guió temporitzat
    python Git/eines/render.py Git/08-branques --verifica   # torna a verificar el vídeo existent

Abans de produir comprova que el guió compilat i la repetició de l’exemple estan al
dia. Les lliçons amb vistes fetes a mida (0 i 3) les dibuixen els seus mòduls; la
resta es dibuixa a partir de l’estat real de cada pas (escenes.py).
"""
import argparse
import asyncio
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from motor import dibuix  # noqa: E402
from motor.guions import compile_series, ScriptError  # noqa: E402
from motor.muntatge import render_episode, verify_episode  # noqa: E402
from motor.serie import load_series  # noqa: E402
import escenes  # noqa: E402


def drawer(config, execution):
    def draw(d, scene, t):
        views = [b.get('view') for b in scene['beats']]
        if any(views):
            if config['slug'].startswith('00-'):
                from visuals_introduccio import draw_general
                return draw_general(d, scene, t, dibuix)
            from visuals_primer_commit import draw_intro
            return draw_intro(d, scene, t, dibuix)
        return escenes.draw_scene(d, scene, t, execution)
    return draw


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('lliço', type=Path)
    parser.add_argument('--audio-only', action='store_true')
    parser.add_argument('--verifica', action='store_true', help='Verifica el vídeo ja produït, amb descodificació')
    args = parser.parse_args()
    root = args.lliço.resolve()
    series = load_series(root.parent)
    videos = series['videos']
    if args.verifica:
        print(json.dumps(verify_episode(root, videos, decode=True), ensure_ascii=False, indent=2))
        return
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
        raise SystemExit('Cal instal·lar ffmpeg i ffprobe.')
    try:
        compile_series(root.parent, check=True)
    except ScriptError as error:
        raise SystemExit(f'El guió no està al dia; executeu primer la repetició i el compilador.\n{error}')
    config = json.loads((root/'guio.json').read_text())
    path = root/'execucio.json'
    execution = json.loads(path.read_text()) if path.exists() else None
    prepare = None
    if config['slug'].startswith('03-'):
        from visuals_primer_commit import prepare_demo
        prepare = lambda build, _config: prepare_demo(build)  # noqa: E731
    asyncio.run(render_episode(root, config, drawer(config, execution), videos, prepare=prepare,
                               audio_only=args.audio_only))


if __name__ == '__main__':
    main()
