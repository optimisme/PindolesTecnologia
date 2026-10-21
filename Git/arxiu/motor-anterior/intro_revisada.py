"""Exemple Git executable en directoris temporals i visuals de la introducció."""
import json
import math
import os
from pathlib import Path
import subprocess
import tempfile

FIRST = 'print("Hello Git!")'
SECOND = 'print("Hola, Anna!")'
NOTES = 'Salutació personalitzada per a l’Anna.'
SECOND_MESSAGE = 'Personalitza la salutacio i afegeix notes'


def prepare_demo(build):
    env = dict(os.environ, LC_ALL='C', GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull,
               GIT_AUTHOR_DATE='2026-10-20T12:00:00+02:00', GIT_COMMITTER_DATE='2026-10-20T12:00:00+02:00')
    with tempfile.TemporaryDirectory(prefix='git-intro-') as temporary:
        base = Path(temporary)
        def git(*args, cwd=None):
            return subprocess.run(['git', *args], cwd=cwd or base, env=env,
                                  capture_output=True, text=True, check=True).stdout.strip()
        git('init', '--bare', '--initial-branch=main', 'remot.git')
        git('clone', str(base/'remot.git'), 'HelloGit')
        repo = base/'HelloGit'
        git('config', 'user.name', 'Demo', cwd=repo)
        git('config', 'user.email', 'demo@example.invalid', cwd=repo)
        assert git('symbolic-ref', '--short', 'HEAD', cwd=repo) == 'main'
        file = repo/'helloGit.py'
        file.write_text(FIRST+'\n')
        first_result = subprocess.check_output(['python3', str(file)], text=True).strip()
        status_new = git('status', '--short', cwd=repo)
        assert status_new == '?? helloGit.py'
        full_status=git('status',cwd=repo)
        assert 'Untracked files:' in full_status and 'helloGit.py' in full_status
        git('add', 'helloGit.py', cwd=repo)
        # stdout.strip() retira l’espai final de columna; comprovem la línia exacta útil.
        status_staged = git('status', '--short', cwd=repo)
        assert status_staged == 'A  helloGit.py'
        git('commit', '-m', 'Afegeix la salutacio inicial', cwd=repo)
        first_hash = git('rev-parse', '--short=7', 'HEAD', cwd=repo)
        first_log = git('log', '--oneline', cwd=repo)
        full_log=git('log',cwd=repo)
        assert first_hash in full_log and 'Afegeix la salutacio inicial' in full_log
        assert git('status', '--short', cwd=repo) == ''
        git('push', '-u', 'origin', 'main', cwd=repo)
        assert git('rev-parse', 'main', cwd=repo) == git('--git-dir='+str(base/'remot.git'), 'rev-parse', 'main')
        file.write_text(SECOND+'\n')
        (repo/'notes.txt').write_text(NOTES+'\n')
        second_result = subprocess.check_output(['python3', str(file)], text=True).strip()
        assert git('diff', '--name-only', cwd=repo) == 'helloGit.py'
        assert git('ls-files', '--others', '--exclude-standard', cwd=repo) == 'notes.txt'
        git('add', '.', cwd=repo)
        dot_staged = git('diff', '--cached', '--name-status', cwd=repo)
        assert dot_staged.splitlines() == ['M\thelloGit.py', 'A\tnotes.txt']
        git('commit', '-m', SECOND_MESSAGE, cwd=repo)
        second_hash = git('rev-parse', '--short=7', 'HEAD', cwd=repo)
        assert git('show', 'HEAD:notes.txt', cwd=repo) == NOTES
        assert git('rev-list', '--count', 'HEAD', cwd=repo) == '2'
        assert git('rev-parse', 'HEAD~1', cwd=repo) == git('rev-parse', 'origin/main', cwd=repo)
        git('push', cwd=repo)
        assert git('rev-parse', 'HEAD', cwd=repo) == git('rev-parse', 'origin/main', cwd=repo)
        assert git('status', '--short', cwd=repo) == ''
        report = {'verified': True, 'scope': 'temporary repositories only', 'first': first_hash,
                  'second': second_hash, 'first_log': first_log, 'final_log': git('log', '--oneline', cwd=repo),
                  'new_status': status_new, 'staged_status': status_staged,
                  'first_result': first_result, 'second_result': second_result,
                  'full_status':full_status,'full_log':full_log,
                  'dot_staged':dot_staged,'second_files':['helloGit.py','notes.txt']}
        # L’abast del punt i les exclusions es comproven en un altre exemple,
        # separat del projecte que mostrem al vídeo.
        scope = base/'abast';scope.mkdir()
        git('init', '--initial-branch=main', cwd=scope)
        git('config', 'user.name', 'Demo', cwd=scope)
        git('config', 'user.email', 'demo@example.invalid', cwd=scope)
        (scope/'sub').mkdir()
        for relative in ['fora.txt','sub/modificat.txt','sub/eliminat.txt']:
            (scope/relative).write_text('Inicial\n')
        (scope/'.gitignore').write_text('/sub/ignorat.tmp\n')
        git('add', '.', cwd=scope);git('commit', '-m', 'Inicial', cwd=scope)
        (scope/'fora.txt').write_text('Canvi fora de la carpeta actual\n')
        (scope/'sub/modificat.txt').write_text('Modificat\n')
        (scope/'sub/nou.txt').write_text('Nou\n')
        (scope/'sub/eliminat.txt').unlink()
        (scope/'sub/ignorat.tmp').write_text('Ignorat\n')
        git('add', '.', cwd=scope/'sub')
        scoped = git('diff', '--cached', '--name-status', cwd=scope)
        assert scoped.splitlines() == ['D\tsub/eliminat.txt','M\tsub/modificat.txt','A\tsub/nou.txt']
        assert git('diff', '--name-only', cwd=scope) == 'fora.txt'
        assert git('check-ignore', 'sub/ignorat.tmp', cwd=scope) == 'sub/ignorat.tmp'
        report['dot_scope_verified'] = True
        report['dot_scope_staged'] = scoped
    (build/'exemple-verificat.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def draw_intro(d, scene, t, r):
    beats = scene['_timed_beats']
    beat = next((b for b in reversed(beats) if t >= b['at']), beats[0])
    view = beat['view']
    elapsed = max(0, t-beat['at'])
    effect = max(.2, beat.get('effect_at', beat['at']+1)-beat['at'])
    demo = scene['_demo']
    a, b = demo['first'], demo['second']

    def line(x, y, content, style='body', color=None):
        r.text(d, (x, y), content, style, color or r.WHITE)

    def card(x, y, w, h, label, lines=(), color=None, code=False):
        color = color or r.MINT
        r.panel(d, (x, y, x+w, y+h))
        line(x+24, y+20, label, 'label', color)
        for i, text in enumerate(lines):
            line(x+24, y+78+39*i, text, 'code' if code else 'body')

    def terminal(command, result=(), title='TERMINAL · ~/HelloGit · main', highlight=None):
        r.terminal(d, (64, 418, 1216, 574), title)
        r.command(d, 90, 472, command, 1)
        if highlight and highlight in command:
            x = 118 + d.textlength(command.split(highlight, 1)[0], font=r.F['code'])
            w = d.textlength(highlight, font=r.F['code'])
            d.line((x, 501, x+w, 501), fill=r.PURPLE, width=4)
        for i, output in enumerate(result):
            d.text((118, 530+24*i), output, font=r.F['tinycode'], fill=r.MINT, anchor='ls')

    def repositories(local=1, remote=0, transfer=False):
        for x, label, count, color in ((64, 'LOCAL · ORDINADOR', local, r.ORANGE),
                                       (734, 'REMOT · GITHUB', remote, r.PURPLE)):
            card(x, 230, 482, 179, label, color=color)
            if not count:
                line(x+24, 314, 'Encara sense commits', color=r.MUTED)
            else:
                if count == 2:
                    d.line((x+130, 325, x+330, 325), fill=r.BORDER, width=5)
                for j, value in enumerate((a, b)[:count]):
                    r.node(d, x+130+j*200, 325, value, color)
                line(x+24, 370, 'main', 'label', color)
        if transfer:
            r.arrow(d, (557, 322), (722, 322), r.MINT)
            q = r.ease((elapsed-effect)/1.4)
            if elapsed>effect and q < 1:
                r.node(d, 557+165*q, 322, None, r.MINT)

    def stages(which):
        values = [('TREBALL', 'helloGit.py', r.MINT),
                  ('PREPARACIÓ', 'Seleccionat' if which else 'Encara buit', r.PURPLE),
                  ('HISTORIAL LOCAL', 'Encara sense commits', r.ORANGE)]
        for i, (label, content, color) in enumerate(values):
            card(64+392*i, 235, 368, 168, label, [content], color=color)
            if i==0 or (i==1 and which):line(88+392*i,354,FIRST,'tinycode',color)
        if which:
            r.arrow(d, (399, 352), (471, 352), r.PURPLE)

    def syntax(command, label, explanation):
        r.terminal(d,(64,230,1216,389),'COMANDA · LLEGEIX-LA PER PARTS')
        r.command(d,90,300,command,1)
        selected=beat.get('highlight')
        if selected:
            x=118+d.textlength(command.split(selected,1)[0],font=r.F['code'])
            w=d.textlength(selected,font=r.F['code'])
            d.line((x,333,x+w,333),fill=r.PURPLE,width=5)
        card(64,416,1152,156,label,explanation,color=r.PURPLE)

    def second_files(prepared=False):
        for x, filename, state, content in (
                (64,'helloGit.py','MODIFICAT',SECOND),
                (666,'notes.txt','NOU',NOTES)):
            label = ('PREPARAT' if prepared else state)+' · '+filename
            card(x,230,550,177,label,[content],color=r.PURPLE if prepared else r.MINT,
                 code=filename.endswith('.py'))

    if view == 'second_notes':
        second_files()
        card(64,442,1152,130,'DESATS, ENCARA SENSE PREPARAR',
             ['El proper pas seleccionarà els dos fitxers.'],color=r.PURPLE)
        return
    if view in ('second_add_scope','second_add_files'):
        if view == 'second_add_scope':
            syntax('git add .','EL PUNT: CARPETA ACTUAL I SUBCARPETES',
                   ['Som a l’arrel: seleccionem els canvis de tot el projecte.'])
        else:
            syntax('git add .','ELS DOS CANVIS DEL NOSTRE EXEMPLE',
                   ['helloGit.py: modificat. notes.txt: nou.',
                    'Els fitxers nous ignorats queden fora.'])
        return

    if view in ('add_goal','add_execute'):
        stages(view=='add_execute' and elapsed>effect)
        if view=='add_goal':
            card(64,442,1152,130,'OBJECTIU',['Seleccionar el contingut que volem confirmar.'],color=r.PURPLE)
        else:terminal('git add helloGit.py',highlight='add')
        return
    if view in ('add_parts','add_file'):
        syntax('git add helloGit.py','NOM DEL FITXER' if view=='add_file' else 'PROGRAMA I ACCIÓ',
               ['helloGit.py és el fitxer que volem preparar.'] if view=='add_file' else
               ['git identifica el programa. add indica l’acció de preparar.'])
        return
    if view in ('commit_parts','commit_message','commit_text'):
        descriptions={
            'commit_parts':('ACCIÓ',['Crear una versió amb el contingut preparat.']),
            'commit_message':('OPCIÓ -m',['El text següent és el missatge del canvi.']),
            'commit_text':('MISSATGE ENTRE COMETES',['Una descripció que permet reconèixer la feina feta.'])}
        label,lines=descriptions[view]
        syntax('git commit -m "Afegeix la salutacio inicial"',label,lines)
        return
    if view=='commit_execute':
        repositories(1 if elapsed>effect else 0,0)
        terminal('git commit -m "Afegeix la salutacio inicial"',
                 ['Versió local creada: '+a] if elapsed>effect else [])
        return
    if view in ('push_parts','push_remote','push_branch','push_tracking'):
        descriptions={
            'push_parts':('ACCIÓ',['Enviar les versions confirmades al remot.']),
            'push_remote':('DESTINACIÓ',['origin és el nom del remot configurat per al projecte.']),
            'push_branch':('BRANCA',['main és la branca que estem publicant.']),
            'push_tracking':('SEGUIMENT',['-u desa la relació per als enviaments següents.'])}
        label,lines=descriptions[view];syntax('git push -u origin main',label,lines)
        return
    if view=='push_execute':
        repositories(1,1 if elapsed>effect+1.4 else 0,transfer=elapsed>effect)
        terminal('git push -u origin main',['Mateixa versió al local i al remot.'] if elapsed>effect+1.4 else [])
        return
    if view in ('status_full','status_full_result'):
        card(64,230,1152,177,'EDITOR · helloGit.py · DESAT',[FIRST],code=True)
        terminal('git status',['Untracked files: helloGit.py'] if view=='status_full_result' or elapsed>effect else [],
                 title='TERMINAL · EXTRACTE · UNTRACKED = FITXER NOU SENSE SEGUIR')
        return
    if view=='log_full':
        repositories(1,0)
        terminal('git log',['commit '+a+'…','Afegeix la salutacio inicial'],title='TERMINAL · EXTRACTE DE L’HISTORIAL')
        return

    if view == 'goal':
        for i, (title, sub, color) in enumerate((('Preparar', 'Triar el contingut', r.PURPLE),
              ('Confirmar', 'Desar una versió', r.ORANGE), ('Publicar', 'Compartir-la', r.MINT))):
            card(64+392*i, 263, 368, 218, f'0{i+1}', [title, sub], color=color)
        r.pill(d, 64, 528, 'UN EXEMPLE COMPLET, PAS A PAS')
    elif view == 'problem':
        card(64, 240, 550, 250, 'ABANS · FUNCIONA', ['salutacio = "Hola!"', 'print(salutacio)', '→ Hola!'], code=True)
        card(666, 240, 550, 250, 'DESPRÉS · ERROR', ['missatge = "Hola!"', 'print(salutacio)', 'NameError: salutacio'], color=r.ORANGE, code=True)
        d.line((688, 352, 1100, 352), fill=r.ORANGE, width=3)
        r.pill(d, 64, 530, 'L’HISTORIAL ENS AJUDA A INVESTIGAR EL CANVI')
    elif view in ('versions', 'versions_decision'):
        r.pill(d, 64, 218, 'EXEMPLE CONCEPTUAL D’HISTORIAL', r.PURPLE, '#312B47')
        d.line((210, 330, 1070, 330), fill=r.BORDER, width=5)
        for x, name, message in ((210, 'A', 'Versió inicial'), (640, 'B', 'Millora el missatge'), (1070, 'C', 'Afegeix una funció')):
            r.node(d, x, 330, name, r.ORANGE)
            r.text(d, (x, 392), message, 'body', r.WHITE, 'mt')
        if view == 'versions_decision':
            card(64, 452, 1152, 120, 'LA DECISIÓ ÉS NOSTRA', ['Desar al fitxer → preparar → confirmar. Després, revisar i provar.'])
        else:
            line(64, 500, 'Cada commit té una instantània, un identificador i un missatge.', 'body')
    elif view == 'local_remote':
        repositories(1, 0)
        r.pill(d, 64, 191, 'ESQUEMA DELS DOS REPOSITORIS', r.PURPLE, '#312B47')
        card(64, 444, 550, 120, 'GIT · LOCAL', ['Historial consultable sense connexió'], color=r.ORANGE)
        card(666, 444, 550, 120, 'GITHUB · INTERNET', ['Compartir i col·laborar'], color=r.PURPLE)
    elif view == 'setup':
        card(64, 232, 650, 335, 'PUNT DE PARTIDA', [
            '   Git i Python disponibles', '   Identitat i accés al remot configurats',
            '   Repositori buit ja clonat', '   Carpeta del projecte oberta'])
        for i in range(4):
            y=323+39*i
            d.line((90,y,95,y+5,104,y-6),fill=r.MINT,width=3)
        card(744, 232, 472, 335, 'LA DEMOSTRACIÓ COMENÇA AQUÍ', [
            'Carpeta: HelloGit', 'Branca: main', 'Remot: origin → GitHub', 'Commits: cap'], color=r.PURPLE)
    elif view in ('edit', 'run', 'status_new', 'second_edit'):
        second = view == 'second_edit'
        card(64, 230, 1152, 177, 'EDITOR · helloGit.py · DESAT', [SECOND if second else FIRST], code=True)
        if view == 'edit':
            card(64, 445, 1152, 125, 'CARPETA DE TREBALL', ['El fitxer està desat. Encara no hi ha cap commit.'])
        elif view == 'status_new':
            terminal('git status --short', [demo['new_status']+'   ← fitxer nou sense seguir'])
        else:
            terminal('python3 helloGit.py', [demo['second_result'] if second else demo['first_result']])
    elif view in ('stage', 'staged'):
        stages(view=='staged' or elapsed>effect)
        if view == 'stage':
            terminal('git add helloGit.py', title='TERMINAL · PREPARAR EL CONTINGUT ACTUAL', highlight='add')
        else:
            terminal('git status --short', [demo['staged_status']+'   ← fitxer nou preparat'])
    elif view == 'commit':
        repositories(1 if elapsed>effect else 0, 0)
        terminal('git commit -m "Afegeix la salutacio inicial"', ['Primer commit local: '+a] if elapsed>effect else [], highlight='-m')
    elif view == 'log':
        repositories(1, 0)
        terminal('git log --oneline', [demo['first_log']])
    elif view == 'clean':
        repositories(1, 0)
        terminal('git status --short', ['Sense sortida: no hi ha canvis pendents.'])
    elif view in ('push', 'published'):
        done = view == 'published'
        repositories(1, 1 if done or elapsed>effect+1.4 else 0, transfer=not done)
        terminal('git push -u origin main', ['-u: configura el seguiment   ·   origin: remot   ·   main: branca'], highlight='-u')
    elif view == 'second_stage':
        second_files(prepared=elapsed>effect)
        terminal('git add .', highlight='.')
    elif view in ('second_commit', 'second_push'):
        pushing = view == 'second_push'
        local=2 if pushing or elapsed>effect else 1
        repositories(local, 2 if pushing and elapsed>effect+1.4 else 1, transfer=pushing)
        terminal('git push' if pushing else 'git commit -m "'+SECOND_MESSAGE+'"',
                 ['Remot actualitzat: dos commits.'] if pushing and elapsed>effect+1.4 else
                 (['Historial local: dos commits.'] if local==2 else []))
    elif view.startswith('summary_'):
        selected = {'summary_add':0,'summary_commit':1,'summary_push':2}[view]
        for i,(title,cmd,sub,color) in enumerate((('PREPARAR','git add','Selecciona el contingut',r.PURPLE),
            ('CONFIRMAR','git commit','Desa una versió local',r.ORANGE),('PUBLICAR','git push','Comparteix els commits',r.MINT))):
            x=64+392*i
            card(x,252,368,250,title,[cmd,sub],color=color,code=False)
            if i==selected:d.rounded_rectangle((x-2,250,x+370,504),20,outline=color,width=4)
    elif view == 'exercise':
        card(64,235,1152,337,'AL TEU REPOSITORI DE PRÀCTIQUES',[
            '1. Canvia el missatge i prova el programa.',
            '2. Prepara el fitxer i confirma el canvi.',
            '3. Consulta l’historial: git log --oneline',
            '4. Explica el canvi abans de publicar-lo.'])
        r.pill(d,760,252,'PAUSA EL VÍDEO I PROVA-HO',r.PURPLE,'#312B47')
    else:
        raise ValueError(f'Visual de la introducció desconegut: {view}')
