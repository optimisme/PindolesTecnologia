#!/usr/bin/env python3
"""Reprodueix cada lliçó en repositoris temporals i comprova el que explica el guió.

Per a cada `llico.yaml` es construeix el punt de partida (`preparacio`), s’executen
les ordres de les etapes en l’ordre del vídeo i es comproven les afirmacions
(`comprova`). Els camins alternatius i condicionals s’executen en una còpia
separada, a partir del punt que indiquen. Les dates i l’autoria són fixes, de
manera que els identificadors dels commits són reproduïbles: el compilador de
guions els fa servir en lloc de hashes inventats.

    python Git/eines/repeticio.py Git              # totes les lliçons
    python Git/eines/repeticio.py Git 08-branques  # només una
    python Git/eines/repeticio.py Git --sense-desar  # comprova sense escriure execucio.json

Mai no toca el repositori real ni cap servei remot: els remots són repositoris
nus locals dins del directori temporal.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from motor.guions import expand  # noqa: E402
from motor.serie import load_series  # noqa: E402

AUTHOR = ('Anna Puig', 'anna@example.com')
LABEL = re.compile(r'\{([A-Z][0-9′]?)\}')
DATE0 = 1792490400  # 20-10-2026 12:00 (+0200): data fixa per a hashes reproduïbles


class StepFailed(AssertionError):
    pass


class Replay:
    def __init__(self, base, lesson, folder):
        base.mkdir()
        base = base.resolve()
        self.base = base
        self.lesson = lesson
        self.folder = folder
        self.cwd = base/lesson.get('carpeta', 'HelloGit')
        self.labels = {}
        self.clock = 0
        self.snapshots = {}
        home = base.parent/'home'
        home.mkdir()
        # La lliçó de configuració parteix d’un usuari sense configuració global.
        (home/'.gitconfig').write_text('' if lesson.get('configuracio_neta') else
            f'[user]\n\tname = {AUTHOR[0]}\n\temail = {AUTHOR[1]}\n[init]\n\tdefaultBranch = main\n')
        self.env = dict(os.environ, HOME=str(home), GIT_CONFIG_GLOBAL=str(home/'.gitconfig'),
                        GIT_CONFIG_NOSYSTEM='1', LC_ALL='C', LANG='C', GIT_EDITOR='true',
                        GIT_PAGER='cat', PAGER='cat', TERM='dumb', NO_COLOR='1')
        for key in ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'PYTHONDONTWRITEBYTECODE', 'PYTHONPYCACHEPREFIX'):
            self.env.pop(key, None)

    # ---------- execució ----------
    def tick(self, env):
        self.clock += 60
        date = f'@{DATE0+self.clock} +0200'
        env.update(GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
        return env

    def resolve(self, text):
        def replace(match):
            label = match.group(1)
            if label not in self.labels:
                raise StepFailed(f'Etiqueta de commit desconeguda: {{{label}}}')
            return self.labels[label][:7]
        text = LABEL.sub(replace, text)
        for marker, remote in (self.lesson.get('urls') or {}).items():
            text = text.replace(marker, str(self.remote_path(remote)))
        return text

    def remote_path(self, name):
        return self.base/f'{name}.git'

    def sh(self, command, cwd=None, stdin=None, env=None, check=True):
        env = self.tick(dict(self.env, **(env or {})))
        result = subprocess.run(['bash', '-c', command], cwd=cwd or self.cwd, env=env, input=stdin,
                                capture_output=True, text=True)
        if check and result.returncode:
            raise StepFailed(f'Ha fallat «{command}» ({result.returncode}):\n{result.stdout}{result.stderr}')
        return result

    def git(self, *args, cwd=None):
        return self.sh(shlex.join(['git', *args]), cwd=cwd).stdout.strip()

    def rev(self, ref, cwd=None):
        result = self.sh(shlex.join(['git', 'rev-parse', '--verify', '-q', ref+'^{commit}']), cwd=cwd, check=False)
        return result.stdout.strip() or None

    # ---------- accions de preparació ----------
    def action(self, item):
        item = dict(item)
        if 'fitxer' in item:
            path = self.cwd/item['fitxer']
            path.parent.mkdir(parents=True, exist_ok=True)
            content = (self.folder/item['origen']).read_text() if 'origen' in item else item['contingut']
            path.write_text(content if content.endswith('\n') or not content else content+'\n')
            if item.get('executable'):
                path.chmod(0o755)
        elif 'esborra' in item:
            target = self.cwd/item['esborra']
            shutil.rmtree(target) if target.is_dir() else target.unlink()
        elif 'git' in item:
            result = self.sh('git '+self.resolve(item['git']), stdin=item.get('entrada'), check=False)
            if bool(result.returncode) != bool(item.get('falla')):
                raise StepFailed(f'Preparació: git {item["git"]} ha retornat {result.returncode}:\n'
                                 f'{result.stdout}{result.stderr}')
        elif 'sh' in item:
            self.sh(self.resolve(item['sh']))
        elif 'commit' in item:
            self.sh(shlex.join(['git', 'commit', '-q', '-m', item['missatge']]))
            self.labels[item['commit']] = self.rev('HEAD')
        elif 'etiqueta' in item:
            self.labels[item['etiqueta']] = self.rev(item.get('ref', 'HEAD'))
        elif 'repositori' in item:
            folder = self.base/item['repositori']
            folder.mkdir(parents=True)
            self.sh('git init -q -b main', cwd=folder)
            self.cwd = folder
        elif 'remot_nu' in item:
            self.sh(shlex.join(['git', 'init', '-q', '--bare', '-b', 'main', str(self.remote_path(item['remot_nu']))]),
                    cwd=self.base)
        elif 'clona' in item:
            self.sh(shlex.join(['git', 'clone', '-q', str(self.remote_path(item['de'])), item['clona']]), cwd=self.base)
        elif 'cd' in item:
            self.cwd = (self.base/item['cd']).resolve()
        elif 'carpeta' in item:
            (self.base/item['carpeta']).mkdir(parents=True, exist_ok=True)
        elif 'servidor' in item:
            # Simula una operació feta a la web (per exemple, fusionar una pull request).
            remote = self.remote_path(item.get('remot', 'origin'))
            work = self.base/'.servidor'
            self.sh(shlex.join(['git', 'clone', '-q', str(remote), str(work)]), cwd=self.base)
            for command in item['servidor']:
                self.sh(self.resolve(command), cwd=work)
            self.sh('git push -q origin --all && git push -q origin --tags', cwd=work)
            if item.get('crea'):
                self.labels[item['crea']] = self.rev('HEAD', cwd=work)
            shutil.rmtree(work)
        elif 'desa' in item:
            self.save(item['desa'])
        elif 'recupera' in item:
            self.restore(item['recupera'])
        else:
            raise StepFailed(f'Acció desconeguda: {item}')

    def save(self, name):
        target = Path(tempfile.mkdtemp(prefix='snap-'))
        shutil.copytree(self.base, target/'tree', symlinks=True)
        self.snapshots[name] = (target, dict(self.labels), self.cwd.relative_to(self.base))

    def restore(self, name):
        target, labels, cwd = self.snapshots[name]
        shutil.rmtree(self.base)
        shutil.copytree(target/'tree', self.base, symlinks=True)
        self.labels = dict(labels)
        self.cwd = self.base/cwd

    # ---------- comprovacions ----------
    def label_of(self, value, cwd):
        if value is None:
            return None
        if value in self.labels:
            return self.labels[value]
        return self.rev(value, cwd=cwd)

    def check(self, spec, output):
        spec = dict(spec)
        cwd = (self.cwd/spec.pop('dir')).resolve() if 'dir' in spec else self.cwd
        for key, expected in spec.items():
            if key == 'refs':
                for ref, label in expected.items():
                    actual, wanted = self.rev(ref, cwd=cwd), self.label_of(label, cwd)
                    if actual != wanted:
                        raise StepFailed(f'{ref} apunta a {actual} i s’esperava {label} ({wanted})')
            elif key == 'head':
                symbolic = self.sh('git symbolic-ref -q --short HEAD', cwd=cwd, check=False).stdout.strip()
                if expected.startswith('separat:'):
                    label = expected.split(':', 1)[1]
                    if symbolic or self.rev('HEAD', cwd=cwd) != self.labels[label]:
                        raise StepFailed(f'HEAD hauria d’estar separat a {label}')
                elif symbolic != expected:
                    raise StepFailed(f'Branca activa {symbolic!r}; s’esperava {expected!r}')
            elif key == 'status':
                actual = self.sh('git status --short', cwd=cwd).stdout.rstrip('\n')
                if actual != expected.rstrip('\n'):
                    raise StepFailed(f'status --short:\n{actual!r}\ns’esperava:\n{expected!r}')
            elif key == 'programa':
                result = self.sh('python3 helloGit.py', cwd=cwd, check=False)
                actual = (result.stdout+result.stderr).strip()
                if expected not in actual:
                    raise StepFailed(f'El programa mostra {actual!r}; s’esperava {expected!r}')
            elif key in ('treball', 'index'):
                for name, content in expected.items():
                    if key == 'treball':
                        path = cwd/name
                        actual = path.read_text().rstrip('\n') if path.exists() else None
                    else:
                        result = self.sh(shlex.join(['git', 'show', ':'+name]), cwd=cwd, check=False)
                        actual = result.stdout.rstrip('\n') if not result.returncode else None
                    if actual != (content.rstrip('\n') if content is not None else None):
                        raise StepFailed(f'{key} {name}: {actual!r}; s’esperava {content!r}')
            elif key in ('treball_igual_a', 'index_igual_a'):
                zone = 'treball' if key.startswith('treball') else 'index'
                self.check({zone: {name: (self.folder/source).read_text()
                                   for name, source in expected.items()}, 'dir': str(cwd)}, output)
            elif key == 'existeix':
                for name in expected:
                    if not (cwd/name).exists():
                        raise StepFailed(f'Hauria d’existir {name}')
            elif key == 'no_existeix':
                for name in expected:
                    if (cwd/name).exists():
                        raise StepFailed(f'No hauria d’existir {name}')
            elif key == 'pares':
                for label, parents in expected.items():
                    actual = self.sh(f'git rev-list --parents -n 1 {self.labels[label]}', cwd=cwd).stdout.split()[1:]
                    wanted = [self.label_of(p, cwd) for p in parents]
                    if actual != wanted:
                        raise StepFailed(f'Pares de {label}: {actual}; s’esperava {parents}')
            elif key == 'mateix_arbre':
                trees = {self.git('rev-parse', self.label_of(x, cwd)+'^{tree}', cwd=cwd) for x in expected}
                if len(trees) != 1:
                    raise StepFailed(f'{expected} haurien de tenir el mateix contingut')
            elif key == 'stash':
                count = len(self.sh('git stash list', cwd=cwd).stdout.splitlines())
                if count != expected:
                    raise StepFailed(f'Entrades de stash: {count}; s’esperaven {expected}')
            elif key == 'remot':
                for remote, refs in expected.items():
                    for ref, label in refs.items():
                        result = self.sh(f'git --git-dir={shlex.quote(str(self.remote_path(remote)))} '
                                         f'rev-parse -q --verify {ref}^{{commit}}', check=False)
                        actual = result.stdout.strip() or None
                        if actual != self.label_of(label, cwd):
                            raise StepFailed(f'Al remot {remote}, {ref} és {actual}; s’esperava {label}')
            elif key == 'sortida':
                for fragment in expected:
                    if self.resolve(fragment) not in output:
                        raise StepFailed(f'La sortida no conté {fragment!r}:\n{output}')
            elif key == 'commits':
                count = int(self.git('rev-list', '--count', expected['ref'], cwd=cwd))
                if count != expected['nombre']:
                    raise StepFailed(f'{expected["ref"]} té {count} commits; s’esperaven {expected["nombre"]}')
            elif key == 'ignorat':
                for name in expected:
                    if self.sh(shlex.join(['git', 'check-ignore', '-q', name]), cwd=cwd, check=False).returncode:
                        raise StepFailed(f'{name} hauria d’estar ignorat')
            else:
                raise StepFailed(f'Comprovació desconeguda: {key}')

    # ---------- estat per als visuals ----------
    def state(self):
        if not (self.cwd/'.git').exists() and not self.cwd.joinpath('.git').is_file():
            return {'directori': self.display(str(self.cwd))}
        names = {}
        for label, sha in self.labels.items():
            names.setdefault(sha, label)
        refs = {}
        for line in self.sh('git for-each-ref --format="%(refname:short) %(objectname)" '
                            'refs/heads refs/remotes refs/tags', check=False).stdout.splitlines():
            ref, sha = line.rsplit(' ', 1)
            if ref.endswith('/HEAD'):
                continue
            commit = self.rev(ref) or sha
            refs[ref] = commit
        commits = []
        listing = self.sh('git log --branches --remotes --tags HEAD --topo-order --reverse --format="%H %P%x09%s"', check=False).stdout
        for line in listing.splitlines():
            ids, subject = line.split('\t', 1)
            sha, *parents = ids.split()
            commits.append({'id': sha[:7], 'lletra': names.get(sha), 'pares': [p[:7] for p in parents],
                            'missatge': subject})
        head = self.sh('git symbolic-ref -q --short HEAD', check=False).stdout.strip()
        head_commit = self.rev('HEAD')
        files = {}
        listing = self.sh('git ls-files --cached --others --exclude-standard', check=False).stdout
        for name in sorted(set(listing.splitlines()))[:12]:
            path = self.cwd/name
            if path.is_file() and path.stat().st_size <= 3000:
                try:
                    files[name] = path.read_text()
                except UnicodeDecodeError:
                    pass
        return {'directori': self.display(str(self.cwd)), 'head': head or None, 'fitxers': files,
                'head_commit': head_commit[:7] if head_commit else None,
                'refs': {k: v[:7] for k, v in refs.items()}, 'commits': commits,
                'status': self.sh('git status --short', check=False).stdout.rstrip('\n').splitlines(),
                'stash': len(self.sh('git stash list', check=False).stdout.splitlines())}

    def display(self, text):
        return text.replace(str(self.base)+'/', '~/').replace(str(self.base), '~')

    # ---------- etapes ----------
    def run_stage(self, stage):
        output, code = '', 0
        for item in stage.get('accions', []):
            self.action(item)
        command = stage.get('ordre')
        if command and not stage.get('simulat') and stage.get('tipus') != 'interactiu':
            command = self.resolve(command)
            env = {}
            if 'editor' in stage:
                message = self.base/'.missatge'
                message.write_text(self.resolve(stage['editor']))
                env['GIT_EDITOR'] = f'cp {shlex.quote(str(message))}'
            if 'sequencia' in stage:
                todo = self.base/'.sequencia'
                todo.write_text(self.resolve(stage['sequencia']))
                env['GIT_SEQUENCE_EDITOR'] = f'cp {shlex.quote(str(todo))}'
            if command.startswith('cd '):
                self.cwd = (self.cwd/shlex.split(command)[1]).resolve()
            else:
                result = self.sh(command, stdin=stage.get('entrada'), env=env, check=False)
                output, code = self.display(result.stdout+result.stderr), result.returncode
                if bool(code) != bool(stage.get('falla')):
                    raise StepFailed(f'«{command}» ha retornat {code} '
                                     f'({"s’esperava un error" if stage.get("falla") else "s’esperava èxit"}):\n{output}')
        for item in stage.get('despres', []):
            self.action(item)
        if stage.get('crea'):
            self.labels[stage['crea']] = self.rev('HEAD')
        if stage.get('comprova'):
            self.check(stage['comprova'], output)
        return output, code


def replay_lesson(item, templates):
    lesson = item['data']
    report = {'llico': item['name'], 'autoria': list(AUTHOR), 'etapes': [], 'verificat': True}
    with tempfile.TemporaryDirectory(prefix='pindoles-') as temporary:
        replay = Replay(Path(temporary)/'w', lesson, item['folder'])
        for action in lesson.get('preparacio', []):
            replay.action(action)
        replay.save('inici')
        report['inici'] = replay.state()
        report['etiquetes_inici'] = {k: v[:7] for k, v in replay.labels.items()}
        stages = [expand(s, templates) for s in lesson.get('etapes', []) + lesson.get('verificacio', [])]
        paths = lesson.get('camins', {})
        current = 'principal'
        for index, stage in enumerate(stages):
            path = stage.get('cami', 'principal')
            if path != current:
                if current == 'principal':
                    replay.save('principal')
                if path == 'principal':
                    replay.restore('principal')
                else:
                    spec = paths[path]
                    replay.restore(spec.get('des_de', 'principal'))
                    for action in spec.get('preparacio', []):
                        replay.action(action)
                current = path
            try:
                output, code = replay.run_stage(stage)
            except StepFailed as error:
                raise StepFailed(f'{item["name"]} · etapa {index+1} '
                                 f'({stage.get("ordre") or stage.get("explica")}): {error}') from None
            if stage.get('desa'):
                replay.save(stage['desa'])
            report['etapes'].append({
                'index': index, 'cami': path,
                'ordre': replay.resolve(stage['ordre']) if stage.get('ordre') else None,
                'sortida': output, 'codi': code, 'simulat': bool(stage.get('simulat')),
                'etiquetes': {k: v[:7] for k, v in replay.labels.items()},
                'estat': replay.state()})
        for snapshot, *_ in replay.snapshots.values():
            shutil.rmtree(snapshot, ignore_errors=True)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('serie', type=Path)
    parser.add_argument('llicons', nargs='*')
    parser.add_argument('--sense-desar', action='store_true',
                        help='Comprova les lliçons i compara els identificadors amb execucio.json sense escriure res')
    args = parser.parse_args()
    series = load_series(args.serie)
    templates = series['config']['plantilles']
    failures = 0
    for item in series['lessons']:
        if args.llicons and item['name'] not in args.llicons and item['slug'] not in args.llicons:
            continue
        lesson = item['data']
        if not lesson.get('preparacio') and not lesson.get('etapes') and not lesson.get('verificacio'):
            continue
        try:
            report = replay_lesson(item, templates)
        except StepFailed as error:
            failures += 1
            print(f'ERROR {error}', file=sys.stderr)
            continue
        target = item['folder']/'execucio.json'
        if args.sense_desar:
            if target.exists():
                saved = json.loads(target.read_text())
                if [s['etiquetes'] for s in saved['etapes']] != [s['etiquetes'] for s in report['etapes']]:
                    failures += 1
                    print(f'ERROR {item["name"]}: els identificadors no coincideixen amb execucio.json', file=sys.stderr)
                    continue
        else:
            target.write_text(json.dumps(report, ensure_ascii=False, indent=1)+'\n')
        print(f'OK {item["name"]}: {len(report["etapes"])} etapes comprovades')
    if failures:
        sys.exit(1)


if __name__ == '__main__':
    main()
