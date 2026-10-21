"""Tags, cherry-pick i pull requests amb historials i interfícies esquemàtiques."""
from lesson_visuals import code_card, commands
from undo_visuals import ORIGINAL, EDITED


def tag_graph(r,d,p=1,tag=True,advanced=False,attach=False):
    end=900 if advanced else 490
    d.line((160,285,end,285),fill=r.BORDER,width=6)
    for x,name in ((160,'A'),(490,'B')):
        r.node(d,x,285,name,r.ORANGE)
    if advanced:
        r.node(d,900,285,'C',r.MINT)
    r.pill(d,(850 if advanced else 440),211,'main',r.ORANGE,'#3C2C2B')
    if tag:
        q=r.ease((p-.2)/.3) if attach else 1
        y=405-56*q
        r.pill(d,443,y,'v1.0',r.PURPLE,'#312B47')
        if q>.98:
            r.arrow(d,(455,349),(470,310),r.PURPLE,3)


def tag_remote(r,d,p):
    for x,title in ((64,'LOCAL'),(734,'ORIGIN · REMOT')):
        r.panel(d,(x,230,x+(554 if x==64 else 482),412))
        r.text(d,(x+24,249),title,'label',r.MUTED)
        xs=(x+80,x+235,x+390)
        advanced=x==64 or p>.38
        d.line((xs[0],320,xs[2] if advanced else xs[1],320),fill=r.BORDER,width=5)
        for j,cx in enumerate(xs):
            if j==2 and not advanced:continue
            r.node(d,cx,320,chr(65+j),r.MINT if j==2 else r.ORANGE)
        r.pill(d,(xs[2] if advanced else xs[1])-38,269,'main',r.ORANGE,'#3C2C2B')
        if x==64 or p>.72:
            r.pill(d,xs[1]+34,365,'v1.0',r.PURPLE,'#312B47')
    r.arrow(d,(632,320),(720,320),r.MINT,4)
    if .2<p<.38:
        r.node(d,580+200*r.ease((p-.2)/.18),320,None,r.MINT)
    if .51<p<.72:
        r.pill(d,565+220*r.ease((p-.51)/.21),368,'v1.0',r.PURPLE,'#312B47')


def tags_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='g_hook':
        tag_graph(r,d,p,attach=True)
        r.panel(d,(64,440,1216,574))
        r.text(d,(90,462),'La versió de l’entrega, identificada pel seu nom.','h2',r.PURPLE)
        r.text(d,(90,521),'Un punt concret de l’historial del projecte.','body',r.MUTED)
    elif sid=='g_before':
        code_card(r,d,(64,230,1216,411),'helloGit.py · main AL COMMIT B',[ORIGINAL],r.MINT)
        commands(r,d,scene,p,'TERMINAL · PROGRAMA PROVAT I CAP CANVI PENDENT')
        if p>.4:r.text(d,(800,501),'Hello Git!','code',r.MINT)
    elif sid=='g_create':
        tag_graph(r,d,p,attach=True)
        commands(r,d,scene,p,'TERMINAL · ETIQUETA ANOTADA AL COMMIT ACTUAL')
    elif sid=='g_list':
        r.terminal(d,(64,235,1216,574),'TERMINAL · CONSULTAR L’ETIQUETA I EL COMMIT · EXTRACTE')
        r.command(d,90,292,scene['commands'][0],p/.16)
        if p>.22:r.text(d,(118,338),'v1.0','code',r.PURPLE)
        if p>.32:r.command(d,90,389,scene['commands'][1],(p-.32)/.16)
        if p>.52:
            r.text(d,(118,436),'tag v1.0 · Primera entrega','code',r.PURPLE)
            r.text(d,(118,481),'commit b62d8e1 · B','code',r.ORANGE)
            r.text(d,(118,535),'Data, autor de l’etiqueta i canvi del commit…','small',r.MUTED)
    elif sid=='g_advance':
        tag_graph(r,d,advanced=p>.42)
        r.text(d,(650,382),EDITED,'code',r.MINT)
        commands(r,d,scene,p,'TERMINAL · DESPRÉS D’EDITAR I DESAR helloGit.py')
    elif sid=='g_read':
        code_card(r,d,(64,230,618,412),'EDITOR ACTUAL · COMMIT C',[EDITED],r.MINT)
        code_card(r,d,(666,230,1216,412),'SORTIDA DE SHOW · v1.0 · B',[ORIGINAL] if p>.3 else [],r.PURPLE)
        commands(r,d,scene,p,'TERMINAL · LLEGIR SENSE MODIFICAR EL FITXER ACTUAL')
    elif sid=='g_push':
        tag_remote(r,d,p)
        commands(r,d,scene,p,'TERMINAL · PUBLICAR LA BRANCA I L’ETIQUETA EXPLÍCITA')
    elif sid=='g_summary':
        tag_graph(r,d,advanced=True)
        for x,title,sub,color in ((64,'Crear','git tag -a v1.0 …',r.PURPLE),(456,'Consultar','git show v1.0',r.MINT),(848,'Publicar','git push origin v1.0',r.ORANGE)):
            r.panel(d,(x,440,x+368,574))
            r.text(d,(x+22,460),title,'h2',color)
            r.text(d,(x+22,525),sub,'tinycode',r.MUTED)
    else:raise ValueError(sid)


def pick_graph(r,d,p=1,applied=False,moving=False,active='main'):
    points=((130,280,'A'),(400,280,'B'),(680,355,'C'),(980,355,'D'))
    d.line((130,280,400,280),fill=r.BORDER,width=6)
    d.line((400,280,680,355,980,355),fill=r.PURPLE,width=5)
    done=applied or (moving and p>.58)
    if done:
        d.line((400,280,980,255),fill=r.MINT,width=5)
    for x,y,name in points:r.node(d,x,y,name,r.PURPLE if name in ('C','D') else r.ORANGE)
    if done:
        r.node(d,980,255,'E',r.MINT)
    r.pill(d,930 if done else 350,190 if done else 210,'main',r.ORANGE,'#3C2C2B')
    r.pill(d,920,412,'salutacio',r.PURPLE,'#312B47')
    r.pill(d,64,214,f'ACTIVA: {active}')
    r.text(d,(620,424),'C · notes.md','small',r.MUTED)
    if moving and .22<p<.58:
        q=r.ease((p-.22)/.36)
        r.pill(d,1040,351-100*q,'CANVI',r.MINT)
    if done:r.text(d,(1070,302),'D ≠ E','code',r.MINT)


def cherry_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='h_hook':
        pick_graph(r,d,active='salutacio')
        code_card(r,d,(64,455,618,581),'C · FUNCIONALITAT PENDENT',['notes.md'],r.PURPLE)
        code_card(r,d,(666,455,1216,581),'D · CORRECCIÓ INDEPENDENT',[ORIGINAL],r.MINT)
    elif sid=='h_log':
        pick_graph(r,d,active='salutacio')
        commands(r,d,scene,p,'TERMINAL · CONSULTAR L’HISTORIAL DE LA BRANCA D’ORIGEN')
        if p>.35:
            for i,(line,color) in enumerate((('d04f7a2 Corregeix missatge',r.MINT),('c95f4a7 Notes de la prova',r.PURPLE),('b62d8e1 Missatge inicial',r.MUTED))):
                r.text(d,(780,492+27*i),line,'tinycode',color)
    elif sid=='h_show':
        r.terminal(d,(64,235,1216,574),'TERMINAL · CANVI DE D · HASH IL·LUSTRATIU')
        r.command(d,90,294,scene['commands'][0],p/.23)
        if p>.33:
            r.text(d,(118,374),'-print(salutacio)','code',r.ORANGE)
            r.text(d,(118,420),'+'+ORIGINAL,'code',r.MINT)
            r.pill(d,90,519,'notes.md NO FORMA PART D’AQUEST CANVI',r.PURPLE,'#312B47')
    elif sid=='h_switch':
        pick_graph(r,d,active='main' if p>.38 else 'salutacio')
        commands(r,d,scene,p,'TERMINAL · STATUS SENSE SORTIDA: ARBRE NET')
    elif sid=='h_apply':
        pick_graph(r,d,p,moving=True)
        commands(r,d,scene,p,'TERMINAL · REAPLICAR EL CANVI SOBRE LA BRANCA ACTUAL')
    elif sid=='h_check':
        code_card(r,d,(64,230,618,412),'MAIN · COMMIT E · HASH NOU',[ORIGINAL,'notes.md no hi és'],r.MINT)
        code_card(r,d,(666,230,1216,412),'SALUTACIO · HISTORIAL CONSERVAT',['C: notes.md','D: correcció'],r.PURPLE)
        commands(r,d,scene,p,'TERMINAL · PROVAR I CONSULTAR EL NOU COMMIT')
        if p>.4:
            r.text(d,(770,495),'Hello Git!','tinycode',r.MINT)
            r.text(d,(770,534),'e18a3b6 Corregeix missatge','tinycode',r.MINT)
    elif sid=='h_conflict':
        r.pill(d,64,218,'CAS CONDICIONAL · SI HI HA UN CONFLICTE',r.ORANGE,'#3C2C2B')
        for x,title in ((64,'OPCIÓ A · RESOLDRE I CONTINUAR'),(666,'OPCIÓ B · AVORTAR')):
            r.terminal(d,(x,280,x+550,574),title)
        r.text(d,(90,341),'Edita i resol el fitxer.','body',r.MUTED)
        for i,cmd in enumerate(scene['commands'][:2]):
            if p>.12+i*.15:r.command(d,90,414+i*60,cmd,(p-.12-i*.15)/.15)
        r.command(d,692,414,scene['commands'][2],p/.22)
        r.text(d,(692,508),'Torna al punt de partida.','body',r.MUTED)
    elif sid=='h_summary':
        pick_graph(r,d,applied=True)
        r.panel(d,(64,455,1216,574))
        r.text(d,(90,476),'D continua a salutacio. E aplica el canvi a main.','h2',r.MINT)
        r.text(d,(90,534),'Revisa les dependències i prova el resultat.','body',r.MUTED)
    else:raise ValueError(sid)


def pr_shell(r,d,title):
    r.panel(d,(64,218,1216,583),fill='#111B2C')
    for i,color in enumerate(('#F17878','#EEC36E',r.MINT)):
        d.ellipse((84+20*i,235,93+20*i,244),fill=color)
    r.text(d,(178,232),'GITHUB · ESQUEMA DIDÀCTIC','label',r.MUTED)
    r.text(d,(1188,232),'exemple / hello-git','small',r.MUTED,'rt')
    d.line((65,262,1215,262),fill=r.BORDER,width=1)
    r.text(d,(90,279),title,'h2')


def pr_graph(r,d,p=1,local=False):
    points=((180,280,'B'),(470,340,'C'),(760,340,'D'),(1080,280,'M'))
    d.line((180,280,470,340,760,340,1080,280),fill=r.PURPLE,width=5)
    d.line((180,280,1080,280),fill=r.MINT,width=5)
    for x,y,name in points:r.node(d,x,y,name,r.MINT if name=='M' else r.PURPLE if name in ('C','D') else r.ORANGE)
    if local:
        x=180+900*r.ease((p-.22)/.4)
        r.pill(d,x-42,207,'main',r.ORANGE,'#3C2C2B')
        r.pill(d,1003,358,'origin/main',r.MINT)
        r.pill(d,700,412,'salutacio',r.PURPLE,'#312B47')


def pr_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='j_hook':
        for i,(title,detail,color) in enumerate((('Branca','Proposa el canvi',r.PURPLE),('Revisió','Acorda el resultat',r.ORANGE),('Main','Integra la feina',r.MINT))):
            x=64+i*392
            r.panel(d,(x,247,x+368,461))
            r.text(d,(x+25,276),title,'h2',color)
            r.text(d,(x+25,376),detail,'body')
            if i<2:r.arrow(d,(x+374,347),(x+386,347),r.MUTED,3)
        r.pill(d,64,524,'PULL REQUEST · PROPOSTA DE CANVI A GITHUB',r.PURPLE,'#312B47')
    elif sid=='j_branch':
        d.line((200,300,650,300),fill=r.BORDER,width=6)
        r.node(d,200,300,'A');r.node(d,650,300,'B')
        r.pill(d,600,230,'main',r.ORANGE,'#3C2C2B')
        if p>.38:r.pill(d,730,230,'salutacio',r.PURPLE,'#312B47')
        r.pill(d,64,373,'ACTIVA: salutacio' if p>.38 else 'ACTIVA: main')
        commands(r,d,scene,p,'TERMINAL · CREAR LA BRANCA DES DE main ACTUALITZADA')
    elif sid=='j_commit':
        code_card(r,d,(64,225,1216,397),'EDITOR · salutacio · DESAR ABANS DE CONFIRMAR',['print("Hola, Anna")'],r.PURPLE)
        r.text(d,(820,311),'→ Hola, Anna','code',r.MINT)
        commands(r,d,scene,p,'TERMINAL · PROVAR I CREAR EL COMMIT C')
    elif sid=='j_push':
        for x,title in ((64,'LOCAL · salutacio'),(734,'ORIGIN · salutacio')):
            r.panel(d,(x,235,x+(554 if x==64 else 482),412))
            r.text(d,(x+22,255),title,'label',r.PURPLE)
            d.line((x+100,330,x+280,330),fill=r.BORDER,width=5)
            r.node(d,x+100,330,'B',r.ORANGE)
            if x==64 or p>.55:r.node(d,x+280,330,'C',r.PURPLE)
            r.text(d,(x+325,331),'main → B','small',r.MUTED)
        r.arrow(d,(632,330),(720,330),r.PURPLE,4)
        if .23<p<.55:r.node(d,580+230*r.ease((p-.23)/.32),330,None,r.PURPLE)
        commands(r,d,scene,p,'TERMINAL · PUBLICAR salutacio, AMB SEGUIMENT REMOT')
    elif sid=='j_open':
        pr_shell(r,d,'Millora la salutacio')
        r.pill(d,90,331,'base: main',r.ORANGE,'#3C2C2B')
        r.pill(d,400,331,'compare: salutacio',r.PURPLE,'#312B47')
        r.arrow(d,(380,348),(255,348),r.MUTED,3)
        r.panel(d,(90,386,765,560))
        r.text(d,(110,405),'Què: personalitza el missatge.','body')
        r.text(d,(110,446),'Prova: python3 helloGit.py','tinycode',r.MUTED)
        r.text(d,(110,487),'-'+ORIGINAL,'tinycode',r.ORANGE)
        r.text(d,(110,523),'+print("Hola, Anna")','tinycode',r.MINT)
        if p>.35:r.pill(d,820,435,'Create pull request',r.MINT)
    elif sid=='j_review':
        pr_shell(r,d,'Millora la salutacio · #1')
        r.text(d,(90,340),'Conversation      Files changed','label',r.MUTED)
        r.panel(d,(90,386,790,560))
        r.text(d,(112,408),'helloGit.py','label',r.MUTED)
        r.text(d,(112,456),'-'+ORIGINAL,'code',r.ORANGE)
        r.text(d,(112,502),'+print("Hola, Anna")','code',r.MINT)
        if p>.24:
            r.panel(d,(814,386,1190,560),outline=r.ORANGE)
            r.text(d,(837,402),'REVISIÓ · UNA ALTRA PERSONA','label',r.ORANGE)
            r.text(d,(837,442),'Afegeix una exclamació','body')
            r.text(d,(837,476),'al final del missatge.','body')
            r.pill(d,837,518,'Changes requested',r.ORANGE,'#3C2C2B')
    elif sid=='j_update':
        code_card(r,d,(64,218,1216,385),'EDITOR · MATEIXA BRANCA salutacio',['print("Hola, Anna!")'],r.MINT)
        if p>.65:r.pill(d,720,333,'PR #1 · 2 commits · pendent de revisió',r.PURPLE,'#312B47')
        r.terminal(d,(64,400,1216,585),'TERMINAL · PROVAR, CONFIRMAR I ACTUALITZAR LA MATEIXA PR')
        for i,cmd in enumerate(scene['commands']):
            start=.04+.17*i
            if p>=start:r.command(d,90,447+33*i,cmd,(p-start)/.13)
    elif sid=='j_merge':
        pr_shell(r,d,'Millora la salutacio · #1')
        r.pill(d,90,330,'Revisió aprovada · requisits complerts',r.MINT)
        r.text(d,(90,385),'Mètode: Create a merge commit','body',r.MUTED)
        if p<.57:
            r.pill(d,90,466,'Confirm merge',r.MINT)
            r.text(d,(90,532),'Acció d’una persona amb permís per fusionar.','body',r.MUTED)
        else:
            r.pill(d,1030,330,'Merged',r.PURPLE,'#312B47')
            d.line((180,444,470,504,760,504,1080,444),fill=r.PURPLE,width=5)
            d.line((180,444,1080,444),fill=r.MINT,width=5)
            for x,y,name in ((180,444,'B'),(470,504,'C'),(760,504,'D'),(1080,444,'M')):
                r.node(d,x,y,name,r.MINT if name=='M' else r.PURPLE if name in ('C','D') else r.ORANGE)
            r.text(d,(1080,538),'main','label',r.MINT,'mt')
    elif sid=='j_pull':
        pr_graph(r,d,p,local=True)
        commands(r,d,scene,p,'TERMINAL · main LOCAL SENSE DIVERGÈNCIES NI CANVIS PENDENTS')
    else:raise ValueError(sid)


def draw_collaboration(d,scene,t,duration,r):
    {'g':tags_scene,'h':cherry_scene,'j':pr_scene}[scene['id'][0]](r,d,scene,t,duration)
