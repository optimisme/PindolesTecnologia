"""Escenes de stash, restore i revert: què es desa, què es conserva i què canvia."""
from lesson_visuals import code_card, commands

ORIGINAL='print("Hello Git!")'
EDITED='print("Hola, Anna!")'


def three_cards(r,d,items):
    for i,(title,sub,color) in enumerate(items):
        x=64+i*392
        r.panel(d,(x,230,x+368,393))
        r.text(d,(x+24,255),title,'h2',color)
        r.text(d,(x+24,323),sub,'body')


def work_and_stash(r,d,edited=False,stored=False,active='salutacio'):
    r.panel(d,(64,230,600,414))
    r.text(d,(88,250),f'TREBALL · {active}','label',r.MINT)
    r.text(d,(88,306),EDITED if edited else ORIGINAL,'code',r.MINT if edited else r.WHITE)
    if edited:
        r.text(d,(88,357),'notes.md · FITXER NOU','tinycode',r.ORANGE)
    else:
        r.text(d,(88,366),'Arbre de treball net','small',r.MUTED)
    r.panel(d,(700,230,1216,414))
    r.text(d,(724,250),'STASH · ENTRADA SEPARADA','label',r.PURPLE)
    if stored:
        r.text(d,(724,306),'helloGit.py + notes.md','code',r.PURPLE)
        r.text(d,(724,367),'Salutacio pendent','small',r.MUTED)
    else:
        r.text(d,(724,313),'Cap entrada pendent','body',r.MUTED)


def stash_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='t_hook':
        code_card(r,d,(64,240,760,486),'SALUTACIO · FEINA SENSE CONFIRMAR',[EDITED,'notes.md'],r.PURPLE)
        r.panel(d,(800,240,1216,486))
        r.text(d,(828,266),'UNA ALTRA TASCA','label',r.ORANGE)
        r.text(d,(828,335),'Cal tornar a main','body')
        r.text(d,(828,391),'La feina encara és pendent.','small',r.MUTED)
        r.pill(d,64,525,'APARCAR LA FEINA SENSE PERDRE-LA')
    elif sid=='t_status':
        code_card(r,d,(64,230,618,412),'helloGit.py · MODIFICAT',[EDITED],r.MINT)
        code_card(r,d,(666,230,1216,412),'notes.md · NO SEGUIT',['Provar la salutació'],r.ORANGE)
        commands(r,d,scene,p,'TERMINAL · FEINA PENDENT, SENSE PREPARAR')
        if p>.3:
            r.text(d,(790,493),' M helloGit.py','tinycode',r.MINT)
            r.text(d,(790,531),'?? notes.md','tinycode',r.ORANGE)
    elif sid=='t_push':
        done=p>.55
        work_and_stash(r,d,edited=not done,stored=done)
        r.arrow(d,(620,329),(679,329),r.PURPLE,4)
        if .2<p<.55:
            r.pill(d,470+250*r.ease((p-.2)/.35),416,'CANVIS',r.PURPLE,'#312B47')
        commands(r,d,scene,p,'TERMINAL · -u INCLOU ELS FITXERS NOUS NO SEGUITS')
    elif sid=='t_list':
        work_and_stash(r,d,stored=True)
        commands(r,d,scene,p,'TERMINAL · CONSULTAR LES ENTRADES DESADES')
        if p>.3:
            r.text(d,(520,507),'stash@{0}: On salutacio: Salutacio pendent','tinycode',r.PURPLE)
    elif sid=='t_main':
        work_and_stash(r,d,stored=True,active='main' if p>.35 else 'salutacio')
        commands(r,d,scene,p,'TERMINAL · main I salutacio CONTINUEN AL COMMIT B')
    elif sid=='t_back':
        work_and_stash(r,d,stored=True,active='salutacio' if p>.35 else 'main')
        commands(r,d,scene,p,'TERMINAL · TORNAR A LA BRANCA AMB L’ARBRE NET')
        if p>.6:
            r.text(d,(820,535),'Sense sortida: arbre net','small',r.MUTED)
    elif sid=='t_pop':
        done=p>.55
        work_and_stash(r,d,edited=done,stored=not done)
        r.arrow(d,(679,329),(620,329),r.MINT,4)
        if .2<p<.55:
            r.pill(d,720-250*r.ease((p-.2)/.35),416,'CANVIS',r.MINT)
        commands(r,d,scene,p,'TERMINAL · APLICACIÓ COMPATIBLE: L’ENTRADA S’ELIMINA')
    elif sid=='t_summary':
        three_cards(r,d,(('Desar','Canvis dins de l’stash',r.PURPLE),
                         ('Pausar','Atén una altra tasca',r.ORANGE),
                         ('Recuperar','Feina encara pendent',r.MINT)))
        commands(r,d,scene,p,'RESUM · PAUSAR LA FEINA SENSE FER UN COMMIT A LA BRANCA')
    else:
        raise ValueError(sid)


def restore_zones(r,d,versions,direction=None,copy=None):
    for i,(title,version,color) in enumerate(zip(('TREBALL','PREPARACIÓ','ÚLTIM COMMIT'),versions,(r.MINT,r.PURPLE,r.ORANGE))):
        x=64+i*392
        r.panel(d,(x,238,x+368,411))
        r.text(d,(x+20,257),title,'label',color)
        r.pill(d,x+282,249,f'V{version}',color,'#263247')
        r.text(d,(x+20,318),ORIGINAL if version==1 else EDITED,'tinycode',color)
        r.text(d,(x+20,379),('Fitxer a l’editor','Còpia preparada','Contingut confirmat')[i],'small',r.MUTED)
    if direction=='unstage':
        r.arrow(d,(843,329),(830,329),r.ORANGE,3)
        r.text(d,(837,208),'restore --staged','small',r.ORANGE,'mt')
        if copy is not None:
            r.pill(d,1000-392*r.ease(copy),412,'V1',r.ORANGE,'#3C2C2B')
    elif direction=='work':
        r.arrow(d,(451,329),(438,329),r.PURPLE,3)
        r.text(d,(445,208),'restore','small',r.PURPLE,'mt')
        if copy is not None:
            r.pill(d,608-392*r.ease(copy),412,'V1',r.PURPLE,'#312B47')


def restore_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='u_hook':
        restore_zones(r,d,(2,2,1))
        r.panel(d,(64,454,1216,570))
        r.text(d,(90,475),'Desmarcar de preparació','h2',r.PURPLE)
        r.text(d,(90,530),'Conservar l’edició al fitxer.','body',r.MUTED)
    elif sid=='u_before':
        restore_zones(r,d,(2,2,1))
        commands(r,d,scene,p,'TERMINAL · M A LA PRIMERA COLUMNA: PREPARAT')
        if p>.35:
            r.text(d,(925,507),'M  helloGit.py','tinycode',r.PURPLE)
    elif sid=='u_unstage':
        restore_zones(r,d,(2,1 if p>.55 else 2,1),'unstage',(p-.2)/.35 if .2<p<.55 else None)
        commands(r,d,scene,p,'TERMINAL · RESTAURAR L’ÍNDEX DES DE HEAD')
        if p>.6:
            r.text(d,(800,507),'Treball: V2 conservada','small',r.MINT)
    elif sid=='u_diff':
        restore_zones(r,d,(2,1,1))
        commands(r,d,scene,p,'TERMINAL · M A LA SEGONA COLUMNA: SENSE PREPARAR')
        if p>.4:
            r.text(d,(550,507),' M helloGit.py','tinycode',r.MINT)
            r.text(d,(820,493),'-print("Hello Git!")','tinycode',r.ORANGE)
            r.text(d,(820,531),'+print("Hola, Anna!")','tinycode',r.MINT)
    elif sid=='u_decide':
        code_card(r,d,(64,240,618,486),'EDICIÓ LOCAL QUE DESCARTAREM',[EDITED],r.ORANGE)
        code_card(r,d,(666,240,1216,486),'PREPARACIÓ · V1 QUE ES CONSERVA',[ORIGINAL],r.PURPLE)
        r.pill(d,64,525,'AQUESTA EDICIÓ LOCAL ES DESCARTARÀ',r.ORANGE,'#3C2C2B')
    elif sid=='u_restore':
        restore_zones(r,d,(1 if p>.55 else 2,1,1),'work',(p-.2)/.35 if .2<p<.55 else None)
        commands(r,d,scene,p,'TERMINAL · RESTAURAR EL TREBALL DES DE LA PREPARACIÓ')
    elif sid=='u_check':
        restore_zones(r,d,(1,1,1))
        commands(r,d,scene,p,'TERMINAL · L’HISTORIAL NO HA CANVIAT')
        if p>.35:
            r.text(d,(680,507),'Sense sortida: no hi ha canvis pendents','small',r.MUTED)
    elif sid=='u_summary':
        for x,title,detail,color in ((64,'Desmarcar','Conserva l’edició del fitxer',r.PURPLE),
                                     (666,'Descartar l’edició','Copia des de la preparació',r.ORANGE)):
            r.panel(d,(x,230,x+550,409))
            r.text(d,(x+24,258),title,'h2',color)
            r.text(d,(x+24,334),detail,'body')
        commands(r,d,scene,p,'RESUM · DUES DESTINACIONS DIFERENTS PER A RESTORE')
    else:
        raise ValueError(sid)


def revert_graph(r,d,p,new=False,moving=False,published=False):
    points=((160,'A',r.ORANGE),(400,'B',r.ORANGE),(680,'C','#F17878'))
    d.line((160,300,680,300),fill=r.BORDER,width=6)
    for x,label,color in points:
        r.node(d,x,300,label,color)
    amount=r.ease((p-.2)/.35) if moving else int(new)
    if amount>0:
        d.line((680,300,680+310*amount,300),fill=r.MINT,width=5)
    ready=amount>.98
    if ready:
        r.node(d,990,300,'D',r.MINT)
    r.pill(d,945 if ready else 635,228,'main',r.ORANGE,'#3C2C2B')
    r.pill(d,925 if published else 615,378,'origin/main',r.PURPLE,'#312B47')


def publish_revert(r,d,p):
    for x,title in ((64,'LOCAL · main'),(734,'GITHUB · origin/main')):
        r.panel(d,(x,230,x+(554 if x==64 else 482),429))
        r.text(d,(x+24,250),title,'label',r.ORANGE if x==64 else r.PURPLE)
    d.line((130,335,520,335),fill=r.BORDER,width=5)
    for x,label in ((130,'A'),(260,'B'),(390,'C'),(520,'D')):
        r.node(d,x,335,label,r.MINT if label=='D' else ('#F17878' if label=='C' else r.ORANGE))
    r.text(d,(790,335),'…','h2',r.MUTED)
    d.line((835,335,950,335),fill=r.BORDER,width=5)
    r.node(d,950,335,'C','#F17878')
    r.arrow(d,(632,335),(720,335),r.MINT,4)
    if .22<p<.6:
        r.node(d,520+550*r.ease((p-.22)/.38),335,None,r.MINT)
    elif p>=.6:
        d.line((950,335,1080,335),fill=r.MINT,width=5)
        r.node(d,1080,335,'D',r.MINT)


def revert_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='w_hook':
        code_card(r,d,(64,240,618,486),'helloGit.py · COMMIT C',['print(salutacio)'],'#F17878')
        r.text(d,(88,409),'NameError: salutacio','tinycode','#F17878')
        r.panel(d,(666,240,1216,486))
        r.text(d,(690,262),'GITHUB · COMMIT C','label',r.PURPLE)
        r.node(d,940,336,'C','#F17878')
        r.text(d,(690,425),'Ja compartit amb altres persones','body')
        r.pill(d,64,525,'OBJECTIU: CONSERVAR L’HISTORIAL COMPARTIT')
    elif sid=='w_find':
        revert_graph(r,d,p)
        commands(r,d,scene,p,'TERMINAL · ARBRE NET I IDENTIFICADOR DEL COMMIT')
        if p>.35:
            for i,line in enumerate(('c95f4a7 Canvia missatge','b62d8e1 Primer missatge','a31b2c4 Inici del projecte')):
                r.text(d,(680,491+i*27),line,'tinycode','#F17878' if i==0 else r.MUTED)
    elif sid=='w_show':
        r.terminal(d,(64,240,1216,574),'TERMINAL · REVISAR EL CANVI ABANS DE REVERTIR-LO')
        r.command(d,90,306,scene['commands'][0],p/.24)
        if p>.35:
            r.text(d,(118,385),'-print("Hello Git!")','code',r.ORANGE)
            r.text(d,(118,429),'+print(salutacio)','code',r.MINT)
            r.pill(d,90,513,'LA VARIABLE salutacio NO ESTÀ DEFINIDA',r.ORANGE,'#3C2C2B')
    elif sid=='w_revert':
        revert_graph(r,d,p,moving=True)
        commands(r,d,scene,p,'TERMINAL · --no-edit ACCEPTA EL MISSATGE AUTOMÀTIC')
        if p>.62:
            r.text(d,(650,507),'[main d04f7a2] Revert "Canvia missatge"','tinycode',r.MINT)
    elif sid=='w_history':
        revert_graph(r,d,p,new=True)
        r.panel(d,(64,454,1216,570))
        r.text(d,(90,475),'El commit C es conserva.','h2')
        r.text(d,(90,530),'D en reverteix l’efecte. L’historial continua avançant.','body',r.MUTED)
    elif sid=='w_check':
        code_card(r,d,(64,230,1216,409),'helloGit.py · RESULTAT DEL COMMIT D',[ORIGINAL],r.MINT)
        commands(r,d,scene,p,'TERMINAL · PROVAR EL PROGRAMA I COMPROVAR L’ESTAT')
        if p>.4:
            r.text(d,(850,501),'Hello Git!','code',r.MINT)
            r.text(d,(850,545),'Arbre de treball net','small',r.MUTED)
    elif sid=='w_push':
        publish_revert(r,d,p)
        commands(r,d,scene,p,'TERMINAL · PUBLICAR EL COMMIT D AMB UN PUSH NORMAL')
    elif sid=='w_summary':
        three_cards(r,d,(('C continua','Historial conservat',r.PURPLE),
                         ('D reverteix','Un commit nou',r.MINT),
                         ('Push comparteix','Correcció publicada',r.ORANGE)))
        commands(r,d,scene,p,'RESUM · REVISAR, REVERTIR I PUBLICAR')
    else:
        raise ValueError(sid)


def draw_undo(d,scene,t,duration,r):
    if scene['id'].startswith('t_'):
        stash_scene(r,d,scene,t,duration)
    elif scene['id'].startswith('u_'):
        restore_scene(r,d,scene,t,duration)
    elif scene['id'].startswith('w_'):
        revert_scene(r,d,scene,t,duration)
    else:
        raise ValueError(scene['id'])
