"""Reset, reflog i gitignore: punters, recuperació i selecció de fitxers."""
from lesson_visuals import code_card, commands
from undo_visuals import restore_zones, three_cards, ORIGINAL, EDITED


def graph(r,d,p=1,at_c=False,moving=False,recovered=False,y=280):
    d.line((160,y,900,y),fill=r.BORDER,width=6)
    for x,label in ((160,'A'),(470,'B'),(900,'C')):
        color=r.PURPLE if label=='C' and (at_c or recovered) else (r.MUTED if label=='C' else r.ORANGE)
        r.node(d,x,y,label,color)
    if not at_c and not recovered:
        d.line((500,y,870,y),fill=r.BG,width=7)
        for x in range(510,860,28):
            d.line((x,y,x+13,y),fill=r.BORDER,width=3)
    x=900 if at_c else (900-430*r.ease((p-.2)/.35) if moving else 470)
    r.pill(d,x-58,y-74,'main',r.ORANGE,'#3C2C2B')
    if recovered:
        r.pill(d,832,y-74,'recuperacio',r.PURPLE,'#312B47')
    elif not at_c:
        r.text(d,(970,y+45),'Fora de main','small',r.MUTED)
    r.pill(d,1040,y-15,'HEAD → main')


def compact_zones(r,d,versions,top=357):
    for i,(title,version,color) in enumerate(zip(('TREBALL','PREPARACIÓ','HEAD · main'),versions,(r.MINT,r.PURPLE,r.ORANGE))):
        x=64+i*392
        r.panel(d,(x,top,x+368,top+111))
        r.text(d,(x+20,top+14),title,'label',color)
        r.pill(d,x+284,top+8,f'V{version}',color,'#263247')
        r.text(d,(x+20,top+62),ORIGINAL if version==1 else EDITED,'tinycode',color)


def diff_terminal(r,d,scene,p,title):
    r.terminal(d,(64,235,1216,574),title)
    r.command(d,90,291,scene['commands'][0],p/.22)
    if p>.3:
        r.text(d,(118,370),'-'+ORIGINAL,'code',r.ORANGE)
        r.text(d,(118,416),'+'+EDITED,'code',r.MINT)
        r.text(d,(90,523),'c95f4a7 · identificador d’exemple','small',r.MUTED)


def reset_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='x_hook':
        graph(r,d,at_c=True)
        code_card(r,d,(64,407,760,574),'helloGit.py · COMMIT C',[EDITED],r.MINT)
        r.pill(d,820,440,'NOMÉS LOCAL',r.PURPLE,'#312B47')
        r.text(d,(820,509),'Encara no publicat','body',r.MUTED)
    elif sid=='x_before':
        restore_zones(r,d,(2,2,2))
        commands(r,d,scene,p,'TERMINAL · ARBRE NET · main A C')
        if p>.4:
            r.text(d,(710,504),'c95f4a7 Canvia missatge','tinycode',r.PURPLE)
            r.text(d,(710,537),'b62d8e1 Primer missatge','tinycode',r.MUTED)
    elif sid in ('x_soft','x_mixed'):
        done=p>.55
        graph(r,d,p,moving=True,y=280)
        v=(2,2 if sid=='x_soft' else (1 if done else 2),1 if done else 2)
        compact_zones(r,d,v,top=361)
        # Terminal lower in the frame; the compact zones end at 472.
        r.terminal(d,(64,489,1216,585),'TERMINAL · OPCIÓ INDEPENDENT DES DE C')
        r.command(d,90,538,scene['commands'][0],p/.24)
    elif sid=='x_softcheck':
        restore_zones(r,d,(2,2,1))
        commands(r,d,scene,p,'TERMINAL · CANVI PREPARAT RESPECTE DE B')
        if p>.4:
            r.text(d,(720,494),'M  helloGit.py','tinycode',r.PURPLE)
            r.text(d,(720,535),'+'+EDITED,'tinycode',r.MINT)
    elif sid=='x_restart':
        graph(r,d,at_c=True)
        compact_zones(r,d,(2,2,2),top=370)
        r.pill(d,64,522,'ALTERNATIVA INDEPENDENT · NO EXECUTAR DESPRÉS DE SOFT',r.PURPLE,'#312B47')
    elif sid=='x_compare':
        for x,title,versions,status,color in ((64,'SOFT',(2,2,1),'M  helloGit.py',r.PURPLE),(666,'MIXED',(2,1,1),' M helloGit.py',r.MINT)):
            r.panel(d,(x,230,x+550,574))
            r.text(d,(x+24,253),title,'h2',color)
            r.text(d,(x+24,307),'main → B · mateix punt de partida C','small',r.MUTED)
            for i,(name,v) in enumerate(zip(('Treball','Preparació','HEAD'),versions)):
                r.text(d,(x+26,352+i*43),name,'body')
                r.pill(d,x+380,346+i*43,f'V{v}',color,'#263247')
            r.text(d,(x+26,516),status,'code',color)
    elif sid=='x_summary':
        graph(r,d)
        r.panel(d,(64,421,1216,574))
        r.text(d,(90,442),'Main retrocedeix. El fitxer es conserva.','h2',r.MINT)
        r.text(d,(90,502),'C queda fora de main. El buscarem amb reflog.','body',r.MUTED)
        r.pill(d,950,533,'SEGÜENT: REFLOG',r.PURPLE,'#312B47')
    else:
        raise ValueError(sid)


def reflog_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='y_hook':
        graph(r,d)
        compact_zones(r,d,(2,2,1),top=390)
        r.pill(d,64,535,'DESPRÉS DE RESET --soft · CANVIS ENCARA PREPARATS',r.PURPLE,'#312B47')
    elif sid=='y_log':
        graph(r,d)
        commands(r,d,scene,p,'TERMINAL · NOMÉS L’HISTORIAL ACCESSIBLE DES DE main')
        if p>.35:
            r.text(d,(680,499),'b62d8e1 Primer missatge','tinycode',r.ORANGE)
            r.text(d,(680,538),'a31b2c4 Inici del projecte','tinycode',r.MUTED)
    elif sid=='y_reflog':
        r.terminal(d,(64,235,1216,574),'TERMINAL · MOVIMENTS LOCALS DE HEAD')
        r.command(d,90,292,scene['commands'][0],p/.22)
        if p>.3:
            r.text(d,(90,367),'b62d8e1 HEAD@{0}: reset: moving to HEAD~1','code',r.ORANGE)
            r.panel(d,(80,410,1198,460),fill='#312B47',outline=r.PURPLE,radius=10)
            r.text(d,(90,421),'c95f4a7 HEAD@{1}: commit: Canvia missatge','code',r.PURPLE)
            r.text(d,(90,526),'Copiem c95f4a7 · hash d’exemple','body',r.MUTED)
    elif sid=='y_show':
        diff_terminal(r,d,scene,p,'TERMINAL · ÉS EL COMMIT QUE BUSQUEM?')
    elif sid=='y_branch':
        graph(r,d,recovered=p>.45)
        r.text(d,(64,409),'Branca activa: main · B','body',r.MINT)
        commands(r,d,scene,p,'TERMINAL · CREAR UNA REFERÈNCIA SENSE CANVIAR DE BRANCA')
    elif sid=='y_all':
        r.terminal(d,(64,235,1216,574),'TERMINAL · INCLOURE TOTES LES BRANQUES')
        r.command(d,90,292,scene['commands'][0],p/.22)
        if p>.3:
            for i,(line,color) in enumerate((('c95f4a7 (recuperacio) Canvia missatge',r.PURPLE),('b62d8e1 (HEAD -> main) Primer missatge',r.ORANGE),('a31b2c4 Inici del projecte',r.MUTED))):
                r.text(d,(90,371+i*48),line,'code',color)
    elif sid=='y_pending':
        restore_zones(r,d,(2,2,1))
        commands(r,d,scene,p,'TERMINAL · M A LA PRIMERA COLUMNA: CANVIS PREPARATS')
        if p>.35:
            r.text(d,(650,507),'M  helloGit.py','code',r.PURPLE)
            r.pill(d,930,521,'recuperacio → C',r.PURPLE,'#312B47')
    elif sid=='y_summary':
        three_cards(r,d,(('Reflog','Troba el commit local',r.ORANGE),('Show','Revisa el canvi',r.PURPLE),('Branch','Crea una referència',r.MINT)))
        r.panel(d,(64,438,1216,574))
        r.text(d,(90,462),'Les entrades són locals i poden caducar.','body',r.MUTED)
        r.text(d,(90,518),'No recupera qualsevol edició sense commit.','body',r.ORANGE)
    else:
        raise ValueError(sid)


def files(r,d,filtered=False,removed=False,top=237):
    for i,(name,sub,color) in enumerate((('helloGit.py','Codi · seguit',r.MINT),('app.log','Local · ignorat' if removed else 'Ja seguit · modificat',r.MUTED if removed else r.ORANGE),('debug.log','Nou · ignorat' if filtered else 'Nou · no seguit',r.MUTED if filtered else r.PURPLE),('__pycache__/','Nou · ignorat' if filtered else 'Nou · no seguit',r.MUTED if filtered else r.PURPLE))):
        x=64+i*294
        r.panel(d,(x,top,x+270,top+158))
        r.text(d,(x+18,top+24),name,'code',color)
        r.text(d,(x+18,top+102),sub,'small',color)


def ignore_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='z_hook':
        files(r,d)
        commands(r,d,scene,p,'TERMINAL · app.log JA ESTAVA SEGUIT')
        if p>.35:
            for i,line in enumerate((' M app.log','?? debug.log','?? __pycache__/')):
                r.text(d,(760,490+i*27),line,'tinycode',r.ORANGE if i==0 else r.PURPLE)
    elif sid=='z_rules':
        code_card(r,d,(64,235,618,574),'.gitignore · FITXER NOU',['*.log','__pycache__/'],r.PURPLE)
        r.panel(d,(666,235,1216,574))
        r.text(d,(690,260),'FILTRAR FITXERS NO SEGUITS','label',r.MINT)
        for i,name in enumerate(('debug.log','__pycache__/')):
            r.pill(d,705,345+i*77,name,r.MUTED,'#263247')
            r.text(d,(970,353+i*77),'IGNORAT','label',r.MUTED)
    elif sid=='z_status':
        files(r,d,filtered=True)
        commands(r,d,scene,p,'TERMINAL · LES REGLES TAMBÉ S’HAN DE VERSIONAR')
        if p>.35:
            r.text(d,(760,495),' M app.log','tinycode',r.ORANGE)
            r.text(d,(760,537),'?? .gitignore','tinycode',r.PURPLE)
    elif sid=='z_check':
        r.terminal(d,(64,235,1216,574),'TERMINAL · ORIGEN DEL PATRÓ QUE S’APLICA')
        r.command(d,90,294,scene['commands'][0],p/.22)
        if p>.35:
            r.text(d,(90,383),'.gitignore:1:*.log    debug.log','code',r.PURPLE)
            for i,(a,b) in enumerate((('Fitxer de regles','.gitignore'),('Número de línia','1'),('Patró que coincideix','*.log'))):
                x=90+i*370
                r.text(d,(x,470),a,'label',r.MUTED)
                r.text(d,(x,517),b,'code',r.MINT)
    elif sid=='z_tracked':
        for x,name,sub,color in ((64,'debug.log','Nou: el patró l’ignora',r.MUTED),(666,'app.log','Ja seguit: continua a Git',r.ORANGE)):
            code_card(r,d,(x,235,x+550,490),name,[sub],color)
        r.pill(d,64,532,'IGNORAR NO RETIRA FITXERS JA SEGUITS',r.ORANGE,'#3C2C2B')
    elif sid=='z_untrack':
        for x,title,lines,color in ((64,'DISC LOCAL',['app.log','El fitxer continua existint'],r.MINT),(666,'PREPARACIÓ',['D  app.log','Retirada preparada'],r.ORANGE)):
            code_card(r,d,(x,235,x+550,410),title,lines if p>.45 or x==64 else ['app.log · seguit'],color)
        commands(r,d,scene,p,'TERMINAL · --cached RETIRA DE L’ÍNDEX')
        if p>.55:
            r.text(d,(800,537),'D  app.log','tinycode',r.ORANGE)
    elif sid=='z_commit':
        for x,title,lines,color in ((64,'CANVIS AL COMMIT',['A  .gitignore','D  app.log'],r.PURPLE),(666,'DISC LOCAL',['app.log es conserva','Logs i cau ignorats'],r.MINT)):
            code_card(r,d,(x,235,x+550,410),title,lines,color)
        commands(r,d,scene,p,'TERMINAL · CONFIRMAR REGLES I RETIRADA DEL LOG')
    elif sid=='z_summary':
        three_cards(r,d,(('Codi','Fitxers versionats',r.MINT),('Regles','Compartides amb Git',r.PURPLE),('Generats','Fora del seguiment',r.MUTED)))
        commands(r,d,scene,p,'TERMINAL · REPOSITORI NET DESPRÉS DEL COMMIT')
        if p>.4:
            r.text(d,(650,505),'Sense sortida: cap canvi pendent','body',r.MUTED)
    else:
        raise ValueError(sid)


def draw_recovery(d,scene,t,duration,r):
    dispatch={'x':reset_scene,'y':reflog_scene,'z':ignore_scene}
    dispatch[scene['id'][0]](r,d,scene,t,duration)
