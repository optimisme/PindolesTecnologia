"""Preparació per blocs, worktrees i un hook que comprova l’índex."""
from pathlib import Path
from lesson_visuals import code_card, commands
from undo_visuals import three_cards, ORIGINAL, EDITED

RED='#F17878'
CORRECTION='print("Hello, Git!")'
BAD='print("Hola, Anna!"'
HOOK_LINES=(Path(__file__).parent/'25-hooks/exemples/pre-commit').read_text().splitlines()


def patch(r,d,scene,p,kind='saluda',first=False):
    r.terminal(d,(64,235,1216,574),'TERMINAL · ADD INTERACTIU · BLOC 1/2' if first else 'TERMINAL · CONTINUACIÓ DE LA MATEIXA SESSIÓ · BLOC 2/2')
    if first:r.command(d,90,292,scene['commands'][0],p/.2)
    else:r.text(d,(90,292),'Segon bloc · comiat()','label',r.ORANGE)
    if p>.25:
        old,new=('Hello Git!','Hola, Anna!') if first else ('Fins aviat!','Adeu!')
        r.text(d,(118,367),f'-    return "{old}"','code',r.ORANGE)
        r.text(d,(118,413),f'+    return "{new}"','code',r.MINT)
        r.text(d,(90,502),'Stage this hunk [y,n,...]?','code',r.MUTED)
    if p>.55:
        r.text(d,(520,502),'y' if first else 'n','code',r.MINT if first else r.ORANGE)
        r.pill(d,780,514,'PREPARAT' if first else 'QUEDA PENDENT',r.MINT if first else r.ORANGE,'#1E3A35' if first else '#3C2C2B')


def selected_zones(r,d,committed=True):
    for i,(title,lines,color) in enumerate((('TREBALL',('Salutació nova','Comiat nou · pendent'),r.MINT),('PREPARACIÓ',('Salutació nova','Comiat antic'),r.PURPLE),('COMMIT C' if committed else 'HEAD · B',('Salutació nova' if committed else 'Salutació antiga','Comiat antic'),r.ORANGE))):
        x=64+392*i;r.panel(d,(x,235,x+368,411))
        r.text(d,(x+20,255),title,'label',color)
        for j,line in enumerate(lines):r.text(d,(x+20,313+j*44),line,'body',color)


def add_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='a_hook':
        code_card(r,d,(64,235,618,486),'helloGit.py · CANVI DE SALUTACIÓ',['def saluda():','    return "Hola, Anna!"'],r.PURPLE)
        code_card(r,d,(666,235,1216,486),'MATEIX FITXER · CANVI DE COMIAT',['def comiat():','    return "Adeu!"'],r.ORANGE)
        r.pill(d,64,532,'VOLEM CONFIRMAR NOMÉS LA SALUTACIÓ',r.MINT)
    elif sid=='a_diff':
        r.terminal(d,(64,235,1216,574),'TERMINAL · DOS BLOCS SEPARATS · EXTRACTE DEL DIFF')
        r.command(d,90,292,scene['commands'][0],p/.2)
        if p>.3:
            lines=(('saluda() · bloc 1',r.PURPLE),('-    return "Hello Git!"',r.ORANGE),('+    return "Hola, Anna!"',r.MINT),('comiat() · bloc 2',r.PURPLE),('-    return "Fins aviat!"',r.ORANGE),('+    return "Adeu!"',r.MINT))
            for i,(line,color) in enumerate(lines):r.text(d,(118,345+i*32),line,'tinycode',color)
    elif sid=='a_yes':patch(r,d,scene,p,first=True)
    elif sid=='a_no':patch(r,d,scene,p,first=False)
    elif sid=='a_compare':
        for x,title,cmd,old,new,color in ((64,'PREPARACIÓ · SALUTACIÓ',scene['commands'][0],'Hello Git!','Hola, Anna!',r.PURPLE),(666,'PENDENT · COMIAT',scene['commands'][1],'Fins aviat!','Adeu!',r.ORANGE)):
            r.terminal(d,(x,235,x+550,574),title)
            r.command(d,x+26,301,cmd,p/.22)
            if p>.3:
                r.text(d,(x+26,381),f'-return "{old}"','code',r.ORANGE)
                r.text(d,(x+26,425),f'+return "{new}"','code',r.MINT)
                r.pill(d,x+26,516,'ENTRARÀ AL COMMIT' if x==64 else 'ES CONSERVA AL FITXER',color,'#312B47' if x==64 else '#3C2C2B')
    elif sid=='a_commit':
        selected_zones(r,d,committed=p>.55)
        commands(r,d,scene,p,'TERMINAL · EL COMMIT COPIA LA PREPARACIÓ')
        if p>.62:r.text(d,(750,508),'Commit C · salutació confirmada','tinycode',r.MINT)
    elif sid=='a_check':
        selected_zones(r,d)
        commands(r,d,scene,p,'TERMINAL · COMIAT MODIFICAT SENSE PREPARAR')
        if p>.4:
            for i,line in enumerate(('helloGit.py | 2 +-',' M helloGit.py','+return "Adeu!"')):r.text(d,(830,474+i*33),line,'tinycode',r.MINT if i==2 else r.MUTED)
    elif sid=='a_summary':
        three_cards(r,d,(('Revisar','Blocs de canvi',r.PURPLE),('Triar y / n','Prepara el que toca',r.ORANGE),('Comprovar','Diff abans del commit',r.MINT)))
        r.panel(d,(64,441,1216,574));r.text(d,(90,466),'Salutació confirmada. Comiat encara pendent.','h2',r.MINT)
        r.text(d,(90,529),'L’edició que no prepares continua al fitxer.','body',r.MUTED)
    else:raise ValueError(sid)


def two_worktrees(r,d,added=True,right_branch='correccio',right_d=False,removed=False):
    r.text(d,(640,208),'HISTORIAL I BRANQUES COMPARTITS','label',r.MUTED,'mm')
    r.panel(d,(64,235,618,411));r.panel(d,(666,235,1216,411))
    r.text(d,(88,254),'projecte · salutacio','label',r.PURPLE)
    r.text(d,(88,307),EDITED,'code',r.PURPLE)
    r.text(d,(88,359),' M helloGit.py','tinycode',r.ORANGE)
    r.pill(d,426,350,'Índex B',r.PURPLE,'#312B47')
    if removed:
        r.text(d,(690,254),'WORKTREE AUXILIAR RETIRAT','label',r.MUTED)
        r.text(d,(690,307),'main i correccio → D','code',r.MINT)
        r.text(d,(690,378),'Les branques i el commit D es conserven.','small',r.MUTED)
    else:
        r.text(d,(690,254),'projecte-correccio · '+right_branch if added else 'main · PUNT DE PARTIDA','label',r.MINT)
        r.text(d,(690,307),CORRECTION if right_d else ORIGINAL,'code',r.MINT)
        r.text(d,(690,359),'Arbre net · índex '+('D' if right_d else 'B') if added else 'Encara sense worktree auxiliar','small',r.MUTED)
        r.text(d,(690,388),'Commit '+('D' if right_d else 'B'),'small',r.MUTED)


def worktree_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='d_hook':
        two_worktrees(r,d,added=False)
        r.panel(d,(64,454,1216,574));r.text(d,(90,476),'Preparar una correcció sense aparcar la feina.','h2',r.MINT)
        r.text(d,(90,536),'salutacio és l’activa · main no està oberta en cap worktree','body',r.MUTED)
    elif sid=='d_add':
        two_worktrees(r,d,added=p>.5)
        commands(r,d,scene,p,'TERMINAL · PROJECTE ORIGINAL · CREAR LA BRANCA correccio')
    elif sid=='d_list':
        two_worktrees(r,d)
        commands(r,d,scene,p,'TERMINAL · LLISTA DE CARPETES I BRANQUES · EXTRACTE')
        if p>.36:
            r.text(d,(770,496),'…/projecte [salutacio]','tinycode',r.PURPLE)
            r.text(d,(770,537),'…/projecte-correccio [correccio]','tinycode',r.MINT)
    elif sid=='d_fix':
        code_card(r,d,(64,230,1216,397),'EDITOR · PROJECTE-CORRECCIO · DESAR EL RETOC',[CORRECTION],r.MINT)
        r.pill(d,854,311,'ACTIVA: correccio',r.PURPLE,'#312B47')
        commands(r,d,scene,p,'TERMINAL · PROVAR, PREPARAR I CONFIRMAR EL COMMIT D')
        if p>.4:r.text(d,(840,475),'Hello, Git!','tinycode',r.MINT)
        if p>.66:r.text(d,(840,539),'Commit D creat','tinycode',r.MINT)
    elif sid=='d_merge':
        two_worktrees(r,d,right_branch='main' if p>.33 else 'correccio',right_d=p<.33 or p>.6)
        commands(r,d,scene,p,'TERMINAL · main NO ESTAVA ACTIVA EN CAP ALTRE WORKTREE')
    elif sid=='d_independent':
        two_worktrees(r,d,right_branch='main',right_d=True)
        commands(r,d,scene,p,'TERMINAL · ARA SOM A projecte-correccio · main D')
        if p>.4:
            r.text(d,(830,497),'Auxiliar: arbre net','small',r.MUTED)
            r.text(d,(830,538),' M helloGit.py','tinycode',r.ORANGE)
    elif sid=='d_return':
        two_worktrees(r,d,right_branch='main',right_d=True)
        commands(r,d,scene,p,'TERMINAL · TORNAR A projecte · salutacio B')
        if p>.4:
            r.text(d,(810,493),'-'+ORIGINAL,'tinycode',r.ORANGE)
            r.text(d,(810,535),'+'+EDITED,'tinycode',r.MINT)
    elif sid=='d_remove':
        two_worktrees(r,d,right_branch='main',right_d=True,removed=p>.44)
        commands(r,d,scene,p,'TERMINAL · RETIRAR EL WORKTREE AUXILIAR NET, DES DE FORA')
        if p>.6:
            r.text(d,(840,503),'…/projecte [salutacio]','tinycode',r.PURPLE)
            r.text(d,(840,541),'d04f7a2 Corregeix la puntuacio','tinycode',r.MINT)
    elif sid=='d_summary':
        three_cards(r,d,(('Fitxers','Una carpeta per feina',r.PURPLE),('Preparació','Índex separat',r.ORANGE),('Historial','Branques compartides',r.MINT)))
        r.panel(d,(64,441,1216,574));r.text(d,(90,466),'Main corregit. Feina de salutacio conservada.','h2',r.MINT)
        r.text(d,(90,530),'Retirar la carpeta auxiliar no elimina la correcció.','body',r.MUTED)
    else:raise ValueError(sid)


def hook_zones(r,d,work_bad=False,index_bad=False,created=False):
    for i,(title,line,color,note) in enumerate((('TREBALL',BAD if work_bad else EDITED,RED if work_bad else r.MINT,'Fitxer a l’editor'),('PREPARACIÓ',BAD if index_bad else EDITED,RED if index_bad else r.PURPLE,'Versió que revisa el hook'),('HEAD · C' if created else 'HEAD · B',EDITED if created else ORIGINAL,r.MINT if created else r.ORANGE,'Commit creat' if created else 'Encara sense commit nou'))):
        x=64+392*i;r.panel(d,(x,235,x+368,411))
        r.text(d,(x+20,256),title,'label',color);r.text(d,(x+20,315),line,'tinycode',color);r.text(d,(x+20,378),note,'small',r.MUTED)


def hooks_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='h25_hook':
        code_card(r,d,(64,240,618,486),'EDITOR · FALTA UN PARÈNTESI',[BAD],RED)
        r.panel(d,(666,240,1216,486));r.text(d,(690,269),'OBJECTIU DEL CONTROL','label',r.PURPLE)
        r.text(d,(690,338),'Comprovar la sintaxi','h2',r.MINT);r.text(d,(690,412),'Abans de crear el commit','body',r.MUTED)
        r.pill(d,64,532,'HOOK LOCAL · PRE-COMMIT',r.PURPLE,'#312B47')
    elif sid=='h25_script':
        r.terminal(d,(64,230,1216,574),'EDITOR · .git/hooks/pre-commit · PYTHON')
        for i,line in enumerate(HOOK_LINES):
            r.text(d,(88,290+32*i),str(i+1),'tinycode',r.MUTED)
            r.text(d,(130,290+32*i),line,'code',r.MINT if i in (0,6) else r.PURPLE)
        r.pill(d,90,529,'git show :helloGit.py → CONTINGUT DE L’ÍNDEX',r.MINT)
    elif sid=='h25_enable':
        code_card(r,d,(64,240,760,412),'FITXER LOCAL',['.git/hooks/pre-commit'],r.PURPLE)
        r.panel(d,(800,240,1216,412));r.text(d,(824,266),'EXECUCIÓ','label',r.MUTED)
        r.pill(d,824,329,'PERMESA' if p>.5 else 'PENDENT',r.MINT if p>.5 else r.ORANGE)
        commands(r,d,scene,p,'TERMINAL · DIRECTORI DE HOOKS PER DEFECTE EN AQUEST EXEMPLE')
    elif sid=='h25_fail':
        hook_zones(r,d,work_bad=True,index_bad=True)
        commands(r,d,scene,p,'TERMINAL · L’ERROR DEL HOOK ATURA EL COMMIT')
        if p>.6:
            r.text(d,(810,495),"SyntaxError: '(' was never closed",'tinycode',RED)
            r.text(d,(810,538),'main continua a B','tinycode',r.ORANGE)
    elif sid=='h25_index':
        hook_zones(r,d,index_bad=True)
        commands(r,d,scene,p,'TERMINAL · FITXER CORREGIT, PERÒ ENCARA SENSE TORNAR A FER ADD')
        if p>.45:
            r.text(d,(810,494),'Índex encara incorrecte','tinycode',RED)
            r.text(d,(810,535),"SyntaxError: '(' was never closed",'tinycode',RED)
    elif sid=='h25_pass':
        hook_zones(r,d,index_bad=p<.3,created=p>.62)
        commands(r,d,scene,p,'TERMINAL · ADD ACTUALITZA LA VERSIÓ QUE REVISARÀ EL HOOK')
        if p>.67:r.text(d,(850,535),'Commit C creat','tinycode',r.MINT)
    elif sid=='h25_local':
        code_card(r,d,(64,235,618,411),'LOCAL · NO VERSIONAT',['.git/hooks/pre-commit'],r.PURPLE)
        code_card(r,d,(666,235,1216,411),'VERSIONAT · COMMIT C',['helloGit.py'],r.MINT)
        commands(r,d,scene,p,'TERMINAL · COMPROVACIÓ DE SINTAXI, SENSE EXECUTAR EL PROGRAMA')
        if p>.4:r.text(d,(740,507),'Sense sortida: arbre net','small',r.MUTED)
    elif sid=='h25_summary':
        three_cards(r,d,(('Índex','La versió preparada',r.PURPLE),('Sintaxi','Comprova abans',r.ORANGE),('Commit','Només si passa',r.MINT)))
        r.panel(d,(64,441,1216,574));r.text(d,(90,466),'El hook és una comprovació local.','h2',r.MINT)
        r.text(d,(90,529),'Per compartir-lo: distribuir i configurar l’script.','body',r.MUTED)
    else:raise ValueError(sid)


def draw_workflow(d,scene,t,duration,r):
    {'a':add_scene,'d':worktree_scene,'h25':hooks_scene}[scene['id'].split('_')[0]](r,d,scene,t,duration)
