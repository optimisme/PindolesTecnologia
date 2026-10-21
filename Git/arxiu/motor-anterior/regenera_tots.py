#!/usr/bin/env python3
"""Regenera les lliçons amb concurrència limitada i registres independents."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent


def render(episode, logs):
    start = time.monotonic()
    log = logs/f"{episode.name}.log"
    print(f"Inici: {episode.name}", flush=True)
    with log.open("w") as output:
        result = subprocess.run([sys.executable, str(ROOT/"render.py"), str(episode)],
                                stdout=output, stderr=subprocess.STDOUT)
    print(f"{'Complet' if result.returncode == 0 else 'ERROR'}: {episode.name} "
          f"({time.monotonic()-start:.0f} s)", flush=True)
    return {"episode": episode.name, "returncode": result.returncode,
            "log": str(log.relative_to(ROOT))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs", type=int, default=3, choices=range(1, 5))
    parser.add_argument("episodes", nargs="*", help="Carpetes opcionals; per defecte, tota la sèrie")
    args = parser.parse_args()
    episodes = ([ROOT/name for name in args.episodes] if args.episodes else
                sorted(path.parent for path in ROOT.glob("[0-9][0-9]-*/episodi.json")))
    if not episodes or any(not (episode/"episodi.json").exists() for episode in episodes):
        parser.error("No s'han trobat tots els episodis indicats")
    logs = ROOT/"registres-pronuncia"
    logs.mkdir(exist_ok=True)
    results = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(render, episode, logs) for episode in episodes]
        for future in as_completed(futures):
            results.append(future.result())
            (logs/"resultat.json").write_text(json.dumps(results, indent=2))
    failed = [result["episode"] for result in results if result["returncode"]]
    print(f"Final: {len(results)-len(failed)}/{len(results)} vídeos completats", flush=True)
    if failed:
        print("Cal repetir: " + " ".join(failed), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
