"""Fetch, forks i rebase interactiu: descàrrega, connexions i historial local."""
from lesson_visuals import code_card, commands
from undo_visuals import three_cards, ORIGINAL, EDITED


def fetch_graph(r,d,p=1,fetched=False,moving=False,integrated=False,integrating=False):
    r.panel(d,(64,230,618,435));r.panel(d,(666,230,1216,435))
    r.text(d,(88,248),'ORIGIN · SERVIDOR','label',r.PURPLE)
    r.text(d,(690,248),'REPOSITORI LOCAL','label',r.MINT)
    r.pill(d,443,267,'main',r.PURPLE,'#312B47')
    d.line((150,330,490,330),fill=r.BORDER,width=5)
    for x,name in ((150,'A'),(320,'B'),(490,'C')):r.node(d,x,330,name,r.PURPLE)
    ready=fetched or (moving and p>.54)
    r.text(d,(710,330),'…','h2',r.MUTED,'mm')
    d.line((734,330,774,330),fill=r.BORDER,width=5)
    if ready:d.line((800,330,1080,330),fill=r.BORDER,width=5)
    r.node(d,800,330,'B',r.ORANGE)
    if ready:r.node(d,1080,330,'C',r.PURPLE)
    q=r.ease((p-.22)/.35) if integrating else int(integrated)
    r.pill(d,750+280*q,267,'main',r.ORANGE,'#3C2C2B')
    x=1000 if ready else 735
    r.pill(d,x,397,'origin/main',r.PURPLE,'#312B47')
    r.text(d,(1015,248),'Fitxers: C' if q>.98 else 'Fitxers: B','small',r.MUTED)
    if moving:
        r.arrow(d,(632,330),(651,330),r.MINT,4)
        if .2<p<.54:r.node(d,490+590*r.ease((p-.2)/.34),330,None,r.PURPLE)


def fetch_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid in ('p_hook','p_decide'):
        code_card(r,d,(64,240,618,486),'MAIN LOCAL · B',[ORIGINAL],r.ORANGE)
        code_card(r,d,(666,240,1216,486),'ORIGIN · SERVIDOR · C' if sid=='p_hook' else 'origin/main · C DESCARREGAT',[EDITED],r.PURPLE)
        r.pill(d,64,531,'REVISAR ABANS D’INCORPORAR' if sid=='p_hook' else 'MAIN I EL FITXER LOCAL ENCARA SÓN A B',r.MINT)
    elif sid=='p_before':
        fetch_graph(r,d)
        commands(r,d,scene,p,'TERMINAL · STATUS SENSE SORTIDA · REFERÈNCIA LOCAL ANTIGA')
        if p>.38:r.text(d,(775,535),'b62d8e1 Primer missatge','tinycode',r.MUTED)
    elif sid=='p_fetch':
        fetch_graph(r,d,p,moving=True)
        commands(r,d,scene,p,'TERMINAL · DESCARREGAR SENSE INTEGRAR A main')
    elif sid=='p_log':
        fetch_graph(r,d,fetched=True)
        commands(r,d,scene,p,'TERMINAL · COMMITS D’origin/main QUE main NO CONTÉ')
        if p>.38:r.text(d,(750,536),'c95f4a7 Canvia missatge','tinycode',r.PURPLE)
    elif sid=='p_diff':
        r.terminal(d,(64,235,1216,574),'TERMINAL · COMPARAR ELS CONTINGUTS DE B I C')
        r.command(d,90,292,scene['commands'][0],p/.22)
        if p>.32:
            r.text(d,(118,376),'-'+ORIGINAL,'code',r.ORANGE)
            r.text(d,(118,424),'+'+EDITED,'code',r.MINT)
            r.pill(d,90,524,'EL FITXER LOCAL CONTINUA A B',r.ORANGE,'#3C2C2B')
    elif sid=='p_merge':
        fetch_graph(r,d,p,fetched=True,integrating=True)
        commands(r,d,scene,p,'TERMINAL · ARBRE NET I SENSE DIVERGÈNCIES')
        if p>.62:r.text(d,(820,536),'Hola, Anna!','tinycode',r.MINT)
    elif sid=='p_summary':
        three_cards(r,d,(('Fetch','Descarrega',r.PURPLE),('Log i diff','Permeten revisar',r.ORANGE),('Merge','Integra a la branca',r.MINT)))
        r.panel(d,(64,441,1216,574))
        r.text(d,(90,466),'origin/main és una referència local.','h2',r.PURPLE)
        r.text(d,(90,527),'Pull descarrega i tot seguit intenta integrar.','body',r.MUTED)
    else:raise ValueError(sid)


def fork_network(r,d,counts=(2,2,2),local=True,connected=True,compact=False,flow='push',local_note=None):
    top,bottom,y=(218,380,318) if compact else (235,411,330)
    xs=(64,480,896)
    for i,(x,title,count) in enumerate(zip(xs,('LOCAL','GITHUB · FORK PROPI','GITHUB · ORIGINAL'),counts)):
        color=r.PURPLE if i==1 else r.ORANGE if i==2 else r.MINT
        r.panel(d,(x,top,x+320,bottom))
        r.text(d,(x+19,top+18),title,'label',color)
        if i==0 and not local:
            r.text(d,(x+19,top+76),'Encara sense còpia','body',r.MUTED)
            continue
        main='C' if count>=3 else 'B'
        note=local_note if i==0 and local_note else f'main {main}'+(' · salutacio D' if count==4 else '')
        r.text(d,(x+19,top+51),note,'small',r.MUTED)
        points=[x+50+70*j for j in range(count)]
        d.line((points[0],y,points[-1],y),fill=r.BORDER,width=4)
        for j,cx in enumerate(points):r.node(d,cx,y,chr(65+j),r.PURPLE if j==3 else color)
    r.arrow(d,(466,y) if flow=='clone' else (397,y),(397,y) if flow=='clone' else (466,y),r.PURPLE,3)
    r.text(d,(431,y-48),'origin','small',r.PURPLE,'mt')
    if connected:
        d.line((224,top,224,207,1056,207,1056,top),fill=r.ORANGE,width=3)
        r.arrow(d,(224,top-12),(224,top),r.ORANGE,3)
        r.pill(d,568,189,'upstream',r.ORANGE,'#3C2C2B')


def window(r,d,title,project='exemple / hello-git'):
    r.panel(d,(64,218,1216,583),fill='#111B2C')
    for i,color in enumerate(('#F17878','#EEC36E',r.MINT)):d.ellipse((84+i*20,235,93+i*20,244),fill=color)
    r.text(d,(178,232),'GITHUB · ESQUEMA DIDÀCTIC','label',r.MUTED)
    r.text(d,(1188,232),project,'small',r.MUTED,'rt')
    d.line((65,262,1215,262),fill=r.BORDER,width=1)
    r.text(d,(90,280),title,'h2')


def forks_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='q_hook':
        fork_network(r,d)
        r.panel(d,(64,451,1216,574))
        r.text(d,(90,471),'Origin: el fork propi. Upstream: l’original.','h2')
        r.text(d,(90,532),'Connexions configurades al repositori local.','body',r.MUTED)
    elif sid=='q_fork':
        for x,title,color in ((64,'projecte / hello-git',r.ORANGE),(738,'alumne / hello-git',r.PURPLE)):
            r.panel(d,(x,242,x+478,486))
            if x==738 and p<.4:continue
            r.text(d,(x+25,267),'GITHUB · ORIGINAL' if x==64 else 'GITHUB · FORK PROPI','label',color)
            r.text(d,(x+25,326),title,'h2',color)
            r.text(d,(x+25,421),'main → B','body',r.MUTED)
        r.arrow(d,(560,365),(720,365),r.MINT,4)
        r.text(d,(640,307),'Fork','h2',r.MINT,'mt')
        r.pill(d,64,531,'ENCARA NO HI HA CÒPIA LOCAL',r.ORANGE,'#3C2C2B')
    elif sid=='q_clone':
        fork_network(r,d,local=p>.46,connected=False,flow='clone')
        commands(r,d,scene,p,'TERMINAL · SUBSTITUEIX <URL-del-fork> PER L’ADREÇA PRÒPIA')
    elif sid=='q_upstream':
        fork_network(r,d,connected=p>.32)
        r.terminal(d,(64,450,1216,585),'TERMINAL · origin: FORK · upstream: ORIGINAL')
        for i,cmd in enumerate(scene['commands']):
            start=.04+.19*i
            if p>=start:r.command(d,90,498+i*34,cmd,(p-start)/.16)
        if p>.5:
            for i,line in enumerate(('origin   <URL-del-fork> (fetch)','origin   <URL-del-fork> (push)','upstream <URL-original> (fetch)','upstream <URL-original> (push)')):
                r.text(d,(760,491+i*24),line,'tinycode',r.PURPLE if i<2 else r.ORANGE)
    elif sid=='q_sync':
        # La zona superior reserva espai per als tres passos de terminal.
        count_local=3 if p>.47 else 2;count_fork=3 if p>.7 else 2
        note='main B · upstream/main C' if .25<p<.47 else None
        fork_network(r,d,(count_local,count_fork,3),local_note=note)
        commands(r,d,scene,p,'TERMINAL · ARBRE NET · main LOCAL I FORK SENSE DIVERGÈNCIES')
    elif sid=='q_branch':
        code_card(r,d,(64,230,1216,411),'EDITOR · DESPRÉS DE CREAR LA BRANCA salutacio',[
            r.type_text(EDITED,(p-.3)/.3)],r.PURPLE)
        r.pill(d,840,309,'main CONTINUA A C',r.ORANGE,'#3C2C2B')
        commands(r,d,scene,p,'TERMINAL · CREAR LA BRANCA ABANS D’EDITAR I DESAR EL FITXER')
    elif sid=='q_publish':
        fork_network(r,d,(4 if p>.48 else 3,4 if p>.76 else 3,3),compact=True)
        r.terminal(d,(64,400,1216,585),'TERMINAL · PROVAR, CONFIRMAR I PUBLICAR AL FORK')
        for i,cmd in enumerate(scene['commands']):
            start=.04+.18*i
            if p>=start:r.command(d,90,447+33*i,cmd,(p-start)/.14)
    elif sid=='q_pr':
        window(r,d,'Personalitza la salutacio','projecte / hello-git')
        r.text(d,(90,332),'DESTINACIÓ · BASE REPOSITORY','label',r.ORANGE)
        r.text(d,(666,332),'ORIGEN · HEAD FORK','label',r.PURPLE)
        r.pill(d,90,365,'projecte/hello-git · main',r.ORANGE,'#3C2C2B')
        r.pill(d,666,365,'alumne/hello-git · salutacio',r.PURPLE,'#312B47')
        r.arrow(d,(640,381),(424,381),r.MINT,4)
        r.text(d,(90,428),'Canvi: personalitza el missatge.','body')
        r.text(d,(90,478),'-'+ORIGINAL,'code',r.ORANGE)
        r.text(d,(90,522),'+'+EDITED,'code',r.MINT)
        if p>.4:r.pill(d,880,467,'Create pull request',r.MINT)
        if p>.68:r.pill(d,880,523,'Open · revisió pendent',r.PURPLE,'#312B47')
    else:raise ValueError(sid)


def squash_graph(r,d,result=False):
    d.line((140,300,390,300,620,250,850,250,1080,250),fill=r.BORDER if result else r.PURPLE,width=5)
    if result:d.line((390,300,1060,400),fill=r.MINT,width=5)
    r.node(d,140,300,'A',r.ORANGE);r.node(d,390,300,'B',r.ORANGE)
    for x,name in ((620,'C'),(850,'D'),(1080,'E')):r.node(d,x,250,name,r.MUTED if result else r.PURPLE)
    r.pill(d,340,230,'main',r.ORANGE,'#3C2C2B')
    if result:
        r.node(d,1060,400,'S',r.MINT)
        r.pill(d,890,384,'salutacio',r.PURPLE,'#312B47')
        r.text(d,(760,315),'C, D i E: línia antiga','small',r.MUTED)
    else:r.pill(d,1015,185,'salutacio',r.PURPLE,'#312B47')


def interactive_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='v_hook':
        three_cards(r,d,(('C','Canvi inicial',r.PURPLE),('D','Retoc del missatge',r.PURPLE),('E','Documentació',r.PURPLE)))
        r.panel(d,(64,440,1216,574))
        r.text(d,(90,465),'Una mateixa millora, tres commits locals.','h2',r.MINT)
        r.text(d,(90,527),'Encara no s’han publicat. Els podem agrupar.','body',r.MUTED)
    elif sid=='v_before':
        squash_graph(r,d)
        r.text(d,(64,377),'→ Hola, Anna!','code',r.MINT)
        commands(r,d,scene,p,'TERMINAL · salutacio ACTIVA · ARBRE NET · COMMITS LOCALS')
        if p>.4:
            for i,line in enumerate(('e18a3b6 Documenta salutacio','d04f7a2 Afegeix exclamacio','c95f4a7 Personalitza salutacio')):
                r.text(d,(800,488+27*i),line,'tinycode',r.PURPLE)
    elif sid=='v_start':
        squash_graph(r,d)
        r.pill(d,64,380,'BASE: B · REESCRIUREM C, D I E',r.MINT)
        commands(r,d,scene,p,'TERMINAL · HEAD~3 ÉS EL PARE DELS TRES COMMITS')
    elif sid=='v_todo':
        r.terminal(d,(64,228,1216,585),'EDITOR DEL REBASE · MÉS ANTIC PRIMER · DESAR I TANCAR')
        for i,(hid,msg) in enumerate((('c95f4a7','Personalitza salutacio'),('d04f7a2','Afegeix exclamacio'),('e18a3b6','Documenta salutacio'))):
            action='pick' if i==0 or p<.3 else 'squash'
            r.text(d,(90,312+55*i),action,'code',r.MINT if action=='pick' else r.ORANGE)
            r.text(d,(210,312+55*i),hid+' '+msg,'code',r.PURPLE)
        r.pill(d,90,521,'DESAR I TANCAR L’EDITOR',r.MINT)
        r.text(d,(680,529),'Squash uneix amb l’anterior.','body',r.MUTED)
    elif sid=='v_message':
        r.terminal(d,(64,228,1216,585),'EDITOR DEL MISSATGE · COMMIT CONJUNT')
        r.text(d,(90,313),r.type_text('Personalitza la salutacio',p/.35),'code',r.MINT)
        if p>.35:r.text(d,(90,404),'Afegeix el missatge i la documentacio.','code',r.MUTED)
        if p>.6:r.pill(d,90,521,'DESAR I TANCAR PER ACABAR',r.MINT)
    elif sid=='v_result':
        squash_graph(r,d,result=p>.36)
        r.panel(d,(64,485,1216,574))
        r.text(d,(90,501),'S té pare B i el mateix contingut final que E.','h2',r.MINT)
        r.text(d,(90,547),'main continua a B · salutacio apunta a S','small',r.MUTED)
    elif sid=='v_verify':
        code_card(r,d,(64,230,1216,397),'RESULTAT FINAL · helloGit.py I notes.md',[
            EDITED,'notes.md: Exemple de salutació'],r.MINT)
        commands(r,d,scene,p,'TERMINAL · COMPARAR AMB L’ANTIC E · HASH IL·LUSTRATIU')
        if p>.4:
            r.text(d,(750,475),'f27c8d0 Personalitza la salutacio','tinycode',r.PURPLE)
            r.text(d,(750,512),'Hola, Anna!','tinycode',r.MINT)
            r.text(d,(750,549),'Diff sense sortida: mateix contingut','small',r.MUTED)
    elif sid=='v_conflict':
        r.pill(d,64,218,'CAS CONDICIONAL · SI APAREIX UN CONFLICTE',r.ORANGE,'#3C2C2B')
        for x,title in ((64,'OPCIÓ A · RESOLDRE I CONTINUAR'),(666,'OPCIÓ B · AVORTAR')):r.terminal(d,(x,280,x+550,574),title)
        r.text(d,(90,340),'Resol el conflicte al fitxer.','body',r.MUTED)
        for i,cmd in enumerate(scene['commands'][:2]):
            if p>.12+i*.16:r.command(d,90,414+i*60,cmd,(p-.12-i*.16)/.15)
        r.command(d,692,414,scene['commands'][2],p/.22)
        r.text(d,(692,508),'Torna al punt de partida.','body',r.MUTED)
    elif sid=='v_summary':
        three_cards(r,d,(('Agrupar','Commits relacionats',r.PURPLE),('Explicar','Un missatge clar',r.ORANGE),('Provar','Mateix resultat final',r.MINT)))
        r.panel(d,(64,441,1216,574))
        r.text(d,(90,465),'Feina pròpia, encara no publicada.','h2',r.MINT)
        r.text(d,(90,528),'Identificador nou · base B i main es conserven','body',r.MUTED)
    else:raise ValueError(sid)


def draw_advanced(d,scene,t,duration,r):
    {'p':fetch_scene,'q':forks_scene,'v':interactive_scene}[scene['id'][0]](r,d,scene,t,duration)
