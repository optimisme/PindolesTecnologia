"""Gràfics de merge, conflictes i rebase, amb lletres de commit didàctiques."""
from lesson_visuals import code_card, commands


def ff_graph(r,d,p,merged=False,moving=False):
    d.line((180,310,900,310),fill=r.BORDER,width=6)
    for x,label,color in ((180,'A',r.ORANGE),(480,'B',r.ORANGE),(900,'C',r.PURPLE)):
        r.node(d,x,310,label,color)
    amount=r.ease((p-.25)/.35) if moving else int(merged)
    r.pill(d,435+420*amount,228,'main',r.ORANGE,'#3C2C2B')
    r.pill(d,842,380,'salutacio',r.PURPLE,'#312B47')
    if moving and amount==1:
        r.pill(d,64,390,'FAST-FORWARD',r.MINT)


def merge_graph(r,d,p,merged=False):
    a,b,main,feature,merge=(130,315),(340,315),(620,265),(620,365),(1010,315)
    for start,end,color in ((a,b,r.BORDER),(b,main,r.ORANGE),(b,feature,r.PURPLE)):
        d.line((*start,*end),fill=color,width=5)
    for point,label,color in ((a,'A',r.ORANGE),(b,'B',r.ORANGE),(main,'D',r.ORANGE),(feature,'C',r.PURPLE)):
        r.node(d,*point,label,color)
    r.pill(d,650,379,'salutacio',r.PURPLE,'#312B47')
    if merged:
        amount=r.ease((p-.12)/.35)
        for start in (main,feature):
            end=(start[0]+(merge[0]-start[0])*amount,start[1]+(merge[1]-start[1])*amount)
            d.line((*start,*end),fill=r.MINT,width=5)
        if amount>.98:
            r.node(d,*merge,'M',r.MINT)
            r.pill(d,965,242,'main',r.ORANGE,'#3C2C2B')
        else:
            r.pill(d,572,202,'main',r.ORANGE,'#3C2C2B')
    else:
        r.pill(d,572,202,'main',r.ORANGE,'#3C2C2B')


def three_cards(r,d,items):
    for i,(title,sub,color) in enumerate(items):
        x=64+i*392
        r.panel(d,(x,230,x+368,393))
        r.text(d,(x+24,255),title,'h2',color)
        r.text(d,(x+24,323),sub,'body')


def merge_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='m_hook':
        code_card(r,d,(64,240,618,486),'MAIN · VERSIÓ ACTUAL',['print("Hello Git!")'],r.ORANGE)
        code_card(r,d,(666,240,1216,486),'SALUTACIO · PROVA CONFIRMADA',['print("Hola, Anna!")'],r.PURPLE)
        r.arrow(d,(652,366),(628,366),r.MINT,3)
        if p>.45:
            r.pill(d,64,525,'OBJECTIU: INCORPORAR LA PROVA A main')
    elif sid=='m_before':
        ff_graph(r,d,p)
        r.text(d,(64,490),'B és un avantpassat de C.','h2')
        r.text(d,(64,542),'Main no ha avançat pel seu compte.','body',r.MUTED)
    elif sid=='m_target':
        ff_graph(r,d,p)
        commands(r,d,scene,p,'TERMINAL · EL DESTÍ DE LA FUSIÓ ÉS main')
        if p>.65:
            r.text(d,(940,535),'→ main','tinycode',r.ORANGE)
    elif sid=='m_merge':
        ff_graph(r,d,p,moving=True)
        commands(r,d,scene,p,'TERMINAL · INTEGRAR salutacio A main')
        if p>.62:
            r.text(d,(840,507),'Fast-forward','tinycode',r.MINT)
    elif sid=='m_ff':
        ff_graph(r,d,p,merged=True)
        r.text(d,(64,489),'Fast-forward: main avança fins a C.','h2')
        r.text(d,(64,541),'Mateixos commits. Cap node nou de merge.','body',r.MUTED)
    elif sid=='m_check':
        code_card(r,d,(64,230,1216,409),'helloGit.py · ACTIVA: main',['print("Hola, Anna!")'],r.ORANGE)
        commands(r,d,scene,p,'TERMINAL · HISTORIAL DE main')
        if p>.35:
            for i,line in enumerate(('c95f4a7 Personalitza salutacio','b62d8e1 Primer missatge','a31b2c4 Inici del projecte')):
                r.text(d,(650,493+i*26),line,'tinycode',r.MUTED)
    elif sid=='m_diverged':
        merge_graph(r,d,p,merged=True)
        r.pill(d,64,482,'EXEMPLE ALTERNATIU: M TÉ DOS PARES, D I C',r.MINT)
        r.text(d,(64,538),'La fusió conserva els dos camins.','body',r.MUTED)
    elif sid=='m_summary':
        three_cards(r,d,(('Destí: main','Escull la branca activa',r.ORANGE),
                         ('Merge','Integra la funcionalitat',r.MINT),
                         ('Origen intacte','La branca es conserva',r.PURPLE)))
        commands(r,d,scene,p,'RESUM · CANVIAR AL DESTÍ I INTEGRAR')
    else:
        raise ValueError(sid)


def conflict_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='c_hook':
        code_card(r,d,(64,240,618,486),'MAIN · LÍNIA 1',['print("Hola, classe!")'],r.ORANGE)
        code_card(r,d,(666,240,1216,486),'SALUTACIO · LÍNIA 1',['print("Hola, Anna!")'],r.PURPLE)
        if p>.4:
            r.pill(d,64,525,'GIT NECESSITA UNA DECISIÓ SOBRE EL CONTINGUT',r.ORANGE,'#3C2C2B')
    elif sid=='c_before':
        merge_graph(r,d,p)
        code_card(r,d,(64,447,618,574),'main · COMMIT D',['print("Hola, classe!")'],r.ORANGE)
        code_card(r,d,(666,447,1216,574),'salutacio · COMMIT C',['print("Hola, Anna!")'],r.PURPLE)
    elif sid=='c_stop':
        merge_graph(r,d,p)
        r.pill(d,64,213,'FUSIÓ ATURADA · ENCARA NO HI HA M',r.ORANGE,'#3C2C2B')
        commands(r,d,scene,p,'TERMINAL · INTENTAR LA FUSIÓ DES DE main')
        if p>.35:
            r.text(d,(650,507),'CONFLICT (content): helloGit.py','tinycode',r.ORANGE)
    elif sid=='c_markers':
        r.terminal(d,(64,241,440,574),'TERMINAL · ESTAT')
        r.command(d,90,315,scene['commands'][0],p/.25)
        if p>.3:
            r.text(d,(118,382),'UU helloGit.py','tinycode',r.ORANGE)
            r.text(d,(90,463),'UU = pendent de resoldre','small',r.MUTED)
        r.panel(d,(464,241,1216,574))
        r.text(d,(488,262),'helloGit.py · CONTINGUT EN CONFLICTE','label',r.MUTED)
        lines=(('<<<<<<< HEAD',r.ORANGE),('print("Hola, classe!")',r.ORANGE),
               ('=======',r.MUTED),('print("Hola, Anna!")',r.PURPLE),('>>>>>>> salutacio',r.PURPLE))
        for i,(line,color) in enumerate(lines):
            r.text(d,(488,321+i*41),line,'code',color)
    elif sid=='c_edit':
        code_card(r,d,(64,230,1216,409),'helloGit.py · RESULTAT ESCOLLIT',['print("Hola, grup!")'],r.MINT)
        r.pill(d,835,325,'SENSE MARCADORS',r.MINT)
        commands(r,d,scene,p,'TERMINAL · COMPROVAR QUE FUNCIONA')
        if p>.4:
            r.text(d,(835,507),'Hola, grup!','code',r.MINT)
    elif sid=='c_add':
        code_card(r,d,(64,230,618,409),'RESOLUCIÓ REVISADA',['print("Hola, grup!")'],r.MINT)
        r.panel(d,(650,230,1216,409))
        r.text(d,(674,250),'PREPARACIÓ','label',r.PURPLE)
        r.text(d,(674,306),'Resolt i preparat' if p>.3 else 'Pendent de preparar','h2',r.PURPLE)
        r.text(d,(674,367),'Fusió pendent de commit','body',r.MUTED)
        commands(r,d,scene,p,'TERMINAL · MARCAR LA RESOLUCIÓ COM A PREPARADA')
        if p>.6:
            r.text(d,(920,535),'M  helloGit.py','tinycode',r.PURPLE)
    elif sid=='c_commit':
        merge_graph(r,d,p,merged=True)
        commands(r,d,scene,p,'TERMINAL · FINALITZAR LA FUSIÓ AMB UN COMMIT')
    elif sid=='c_summary':
        three_cards(r,d,(('Revisar','Decideix el text final',r.PURPLE),
                         ('Provar','Comprova el resultat',r.MINT),
                         ('Confirmar','Add i commit',r.ORANGE)))
        commands(r,d,scene,p,'RESUM · PROVAR, PREPARAR I CONFIRMAR')
    else:
        raise ValueError(sid)


def rebase_graph(r,d,p,mode='before'):
    base,main,old1,old2,new1,new2=(170,285),(430,285),(430,375),(690,375),(700,285),(970,285)
    d.line((*base,*main),fill=r.ORANGE,width=5)
    r.node(d,*base,'B',r.ORANGE)
    r.node(d,*main,'D',r.ORANGE)
    r.pill(d,383,212,'main',r.ORANGE,'#3C2C2B')
    if mode in ('before','replay'):
        dim=mode=='replay' and p>.65
        color=r.BORDER if dim else r.PURPLE
        d.line((*base,*old1,*old2),fill=color,width=5)
        r.node(d,*old1,'C',color)
        r.node(d,*old2,'E',color)
        if not dim:
            r.pill(d,760,375,'salutacio',r.PURPLE,'#312B47')
    if mode in ('after','replay'):
        progress=1 if mode=='after' else r.ease((p-.15)/.23)
        endpoint=(main[0]+(new1[0]-main[0])*progress,285)
        d.line((*main,*endpoint),fill=r.PURPLE,width=5)
        if progress>.98:
            r.node(d,*new1,'C′',r.PURPLE)
        progress=1 if mode=='after' else r.ease((p-.4)/.23)
        if progress>0:
            d.line((*new1,new1[0]+(new2[0]-new1[0])*progress,285),fill=r.PURPLE,width=5)
        if progress>.98:
            r.node(d,*new2,'E′',r.PURPLE)
        if mode=='after' or p>.65:
            r.pill(d,914,212,'salutacio',r.PURPLE,'#312B47')
    if mode=='after':
        r.text(d,(640,393),'B → D → C′ → E′','code',r.MUTED,'mt')


def compare_graphs(r,d):
    r.text(d,(64,208),'MATEIXA BRANCA ACTIVA: salutacio','label',r.MUTED)
    for x,title in ((64,'git merge main'),(650,'git rebase main')):
        r.panel(d,(x,246,x+550,574))
        r.text(d,(x+24,265),title,'code',r.MINT)
    # Merge de main dins de salutacio: main queda a D; M té pares E i D.
    points={'B':(124,385),'D':(264,335),'C':(264,435),'E':(404,435),'M':(534,385)}
    for a,b in (('B','D'),('B','C'),('C','E'),('D','M'),('E','M')):
        d.line((*points[a],*points[b]),fill=r.BORDER,width=4)
    for label,point in points.items():
        r.node(d,*point,label,r.ORANGE if label=='D' else r.PURPLE)
    r.text(d,(264,311),'main','small',r.ORANGE,'mb')
    r.text(d,(534,347),'salutacio','small',r.PURPLE,'mb')
    r.text(d,(88,534),'Conserva C i E. Afegeix M.','small',r.MUTED)
    # Rebase de la mateixa branca: commits C′ i E′ nous, main encara a D.
    points2=((710,'B'),(850,'D'),(990,'C′'),(1130,'E′'))
    d.line((710,385,1130,385),fill=r.BORDER,width=4)
    for x,label in points2:
        r.node(d,x,385,label,r.ORANGE if label=='D' else r.PURPLE)
    r.text(d,(850,347),'main','small',r.ORANGE,'mb')
    r.text(d,(1130,347),'salutacio','small',r.PURPLE,'mb')
    r.text(d,(674,534),'C′ i E′ són commits nous.','small',r.MUTED)


def rebase_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid in ('r_hook','r_before'):
        rebase_graph(r,d,p)
        r.panel(d,(64,454,1216,570))
        if sid=='r_hook':
            r.text(d,(90,474),'Main incorpora D. La teva feina parteix de B.','h2')
            r.text(d,(90,530),'Volem continuar sobre la versió actualitzada.','body',r.MUTED)
        else:
            r.text(d,(90,474),'Un commit nou a main. Dos de propis a salutacio.','body')
            r.pill(d,90,519,'BRANCA LOCAL · ENCARA NO PUBLICADA',r.PURPLE,'#312B47')
    elif sid=='r_command':
        rebase_graph(r,d,p)
        commands(r,d,scene,p,'TERMINAL · ACTUALITZAR LA BASE DE salutacio')
    elif sid=='r_replay':
        rebase_graph(r,d,p,'replay')
        r.panel(d,(64,454,1216,574))
        for x,title,old,new in ((90,'PRIMER CANVI','c95f4a7','f12c3d4'),(650,'SEGON CANVI','e56a9b3','f98b1a6')):
            r.text(d,(x,470),title,'label',r.PURPLE)
            r.text(d,(x,518),f'{old} → {new}','code')
    elif sid=='r_after':
        rebase_graph(r,d,p,'after')
        commands(r,d,scene,p,'TERMINAL · REVISAR L’HISTORIAL RESULTANT')
    elif sid=='r_compare':
        compare_graphs(r,d)
    elif sid=='r_conflict':
        three_cards(r,d,(('Resoldre','Edita el fitxer',r.ORANGE),
                         ('Preparar','Git add',r.PURPLE),
                         ('Continuar','Rebase --continue',r.MINT)))
        commands(r,d,scene,p,'NOMÉS SI S’ATURA: RESOLDRE, PREPARAR I CONTINUAR')
    elif sid=='r_summary':
        rebase_graph(r,d,p,'after')
        r.panel(d,(64,454,1216,570))
        r.text(d,(90,474),'Branca pròpia, encara no compartida.','h2',r.PURPLE)
        r.text(d,(90,530),'Integrar la funcionalitat a main continua pendent.','body',r.MUTED)
    else:
        raise ValueError(sid)


def draw_integration(d,scene,t,duration,r):
    if scene['id'].startswith('m_'):
        merge_scene(r,d,scene,t,duration)
    elif scene['id'].startswith('c_'):
        conflict_scene(r,d,scene,t,duration)
    elif scene['id'].startswith('r_'):
        rebase_scene(r,d,scene,t,duration)
    else:
        raise ValueError(scene['id'])
