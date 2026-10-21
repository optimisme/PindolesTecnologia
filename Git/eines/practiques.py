#!/usr/bin/env python3
"""Genera els scripts de pràctica: el punt de partida de cada vídeo, a l’abast de l’alumnat.

Cada `Git/practiques/NN-nom.sh` es construeix a partir de la `preparacio` del
`llico.yaml`, la mateixa que fa servir la repetició automàtica. Així el repositori
que obté l’alumna coincideix amb el del vídeo (excepte els identificadors, que
depenen de la data i l’autoria de cadascú).

    python Git/eines/practiques.py Git              # escriu els scripts
    python Git/eines/practiques.py Git --comprova   # falla si no estan al dia
    python Git/eines/practiques.py Git --prova      # executa'ls en carpetes temporals i compara amb la repetició
"""
import argparse
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from motor.serie import load_series  # noqa: E402

LABEL = re.compile(r'\{([A-Z][0-9′]?)\}')
HEADER = '''#!/usr/bin/env bash
# Píndoles de Git · Lliçó {number} · {title}
#
# Crea el punt de partida del vídeo en una carpeta nova. A Windows, executa-ho des de Git Bash.
#     bash {name}.sh            # crea la carpeta practica-{name}
#     bash {name}.sh una-altra   # o la carpeta que indiquis
# {remote_note}
# Generat per Git/eines/practiques.py a partir de {name}/llico.yaml. No l’editeu a mà.
set -euo pipefail

DESTI="${{1:-practica-{name}}}"
if [ -e "$DESTI" ]; then
  echo "Ja existeix $DESTI: tria una altra carpeta." >&2
  exit 1
fi
mkdir -p "$DESTI"
cd "$DESTI"
ARREL="$PWD"

# Si encara no has configurat Git (lliçó 1), els commits d’aquest exemple fan servir un nom provisional.
git config user.name >/dev/null || export GIT_AUTHOR_NAME="Alumne" GIT_COMMITTER_NAME="Alumne"
git config user.email >/dev/null || export GIT_AUTHOR_EMAIL="alumne@example.com" GIT_COMMITTER_EMAIL="alumne@example.com"

nou_repositori() {{  # git init amb main com a branca inicial, també en versions antigues de Git
  git init -q "$@"
  git -C "${{@: -1}}" symbolic-ref HEAD refs/heads/main
}}
'''


def variable(label):
    return 'COMMIT_' + label.replace('′', 'P')


def resolve(text):
    return LABEL.sub(lambda m: '"$'+variable(m.group(1))+'"', text)


def lines_for(action, folder):
    if 'fitxer' in action:
        content = (folder/action['origen']).read_text() if 'origen' in action else action['contingut']
        content = content.rstrip('\n')
        marker = 'FI_DEL_FITXER'
        out = [f'mkdir -p {shlex.quote(str(Path(action["fitxer"]).parent))}'] if '/' in action['fitxer'] else []
        out += [f"cat > {shlex.quote(action['fitxer'])} <<'{marker}'", content, marker]
        if action.get('executable'):
            out.append(f'chmod +x {shlex.quote(action["fitxer"])}')
        return out
    if 'esborra' in action:
        return [f'rm -rf {shlex.quote(action["esborra"])}']
    if 'git' in action:
        command = 'git ' + resolve(action['git'])
        return [command + (' || true  # aquest pas deixa una operació pendent a propòsit' if action.get('falla') else '')]
    if 'sh' in action:
        return [resolve(action['sh'])]
    if 'commit' in action:
        return [f"git commit -q -m {shlex.quote(action['missatge'])}",
                f'{variable(action["commit"])}=$(git rev-parse --short HEAD)']
    if 'etiqueta' in action:
        return [f'{variable(action["etiqueta"])}=$(git rev-parse --short {shlex.quote(action.get("ref", "HEAD"))})']
    if 'repositori' in action:
        return [f'nou_repositori "$ARREL/{action["repositori"]}"', f'cd "$ARREL/{action["repositori"]}"']
    if 'remot_nu' in action:
        return [f'nou_repositori --bare "$ARREL/{action["remot_nu"]}.git"']
    if 'clona' in action:
        return [f'git clone -q "$ARREL/{action["de"]}.git" "$ARREL/{action["clona"]}"']
    if 'cd' in action:
        return [f'cd "$ARREL/{action["cd"]}"' if action['cd'] != '.' else 'cd "$ARREL"']
    if 'carpeta' in action:
        return [f'mkdir -p "$ARREL/{action["carpeta"]}"']
    if 'servidor' in action:
        remote = action.get('remot', 'origin')
        body = ' && '.join(resolve(c) for c in action['servidor'])
        return ['# Simula un canvi fet per una altra persona directament al remot.',
                'TEMPORAL=$(mktemp -d)',
                f'git clone -q "$ARREL/{remote}.git" "$TEMPORAL/w"',
                f'(cd "$TEMPORAL/w" && {body} && git push -q origin --all && git push -q origin --tags)',
                'rm -rf "$TEMPORAL"']
    raise ValueError(f'Acció sense equivalent de pràctica: {action}')


def script_for(item):
    lesson = item['data']
    folder = item['folder']
    remotes = any('remot_nu' in a for a in lesson['preparacio'])
    note = ('Els remots són carpetes .git locals que fan el paper de GitHub; no cal connexió.'
            if remotes else 'No cal cap connexió: tot passa al teu ordinador.')
    lines = [HEADER.format(number=item['number'], title=lesson['titol'], name=item['name'], remote_note=note)]
    for action in lesson['preparacio']:
        lines += lines_for(action, folder)
    workdir = lesson.get('carpeta', 'HelloGit')
    lines += ['', f'cd "$ARREL/{workdir}"' if workdir != '.' else 'cd "$ARREL"',
              'echo "Punt de partida preparat a: $PWD"',
              'if git rev-parse -q --verify HEAD >/dev/null 2>&1; then',
              '  git log --oneline --graph --all',
              '  git status --short',
              'fi', '']
    return '\n'.join(lines)


def run_script(path, expected):
    with tempfile.TemporaryDirectory(prefix='practica-') as temporary:
        env = {'HOME': temporary, 'PATH': '/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin', 'LC_ALL': 'C',
               'GIT_CONFIG_NOSYSTEM': '1'}
        subprocess.run(['bash', str(path), 'prova'], cwd=temporary, env=env, check=True,
                       capture_output=True, text=True)
        work = Path(temporary)/'prova'/expected['directori'].removeprefix('~/').removeprefix('~')
        def git(*args):
            return subprocess.run(['git', *args], cwd=work, env=env, capture_output=True, text=True).stdout
        refs = sorted(line.split()[0] for line in git('for-each-ref', '--format=%(refname:short) x',
                                                      'refs/heads', 'refs/remotes', 'refs/tags').splitlines()
                      if not line.split()[0].endswith('/HEAD'))
        status = git('status', '--short').rstrip('\n').splitlines()
        commits = git('log', '--branches', '--remotes', '--tags', '--format=%s').splitlines() if expected.get('commits') else []
        problems = []
        if refs != sorted(expected.get('refs', {})):
            problems.append(f'referències {refs} ≠ {sorted(expected.get("refs", {}))}')
        if status != expected.get('status', []):
            problems.append(f'estat {status} ≠ {expected.get("status")}')
        if sorted(commits) != sorted(c['missatge'] for c in expected.get('commits', [])):
            problems.append('els commits no coincideixen amb la repetició')
        return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('serie', type=Path)
    parser.add_argument('--comprova', action='store_true')
    parser.add_argument('--prova', action='store_true')
    args = parser.parse_args()
    series = load_series(args.serie)
    target = series['root']/'practiques'
    target.mkdir(exist_ok=True)
    expected_files, stale, failures = set(), [], []
    for item in series['lessons']:
        if not item['data'].get('preparacio'):
            continue
        path = target/f'{item["name"]}.sh'
        expected_files.add(path)
        text = script_for(item)
        if not path.exists() or path.read_text() != text:
            stale.append(path)
            if not args.comprova:
                path.write_text(text)
                path.chmod(0o755)
        if args.prova:
            execution = json.loads((item['folder']/'execucio.json').read_text())
            problems = run_script(path, execution['inici'])
            print(('ERROR ' if problems else 'OK ') + item['name'] + (': ' + '; '.join(problems) if problems else ''))
            failures += problems
    extra = [p for p in target.glob('*.sh') if p not in expected_files]
    if args.comprova and (stale or extra):
        print('Scripts de pràctica desactualitzats: ' + ', '.join(p.name for p in stale + extra), file=sys.stderr)
        sys.exit(1)
    for path in extra:
        if not args.comprova:
            path.unlink()
    if failures:
        sys.exit(1)
    if not args.prova:
        print(f'{len(expected_files)} scripts de pràctica al dia a {target.relative_to(series["root"].parent)}')


if __name__ == '__main__':
    main()
