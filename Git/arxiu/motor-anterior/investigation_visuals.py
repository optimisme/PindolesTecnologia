"""Blame, bisect i amend: investigar l’historial i completar commits locals."""
from lesson_visuals import code_card, commands
from undo_visuals import three_cards

RED='#F17878'
BLAME_ROWS=(
 '^a31b2c4 (Demo 2026-10-19 10:00:00 +0200 1) # Programa de salutació',
 'b62d8e1 (Demo 2026-10-19 10:02:00 +0200 2) missatge = "Hola, Anna!"',
 'c95f4a7 (Demo 2026-10-19 10:04:00 +0200 3) print( salutacio )',
)


def diff(r,d,scene,p,lines,footnote=None):
    r.terminal(d,(64,235,1216,574),'TERMINAL · REVISAR EL COMMIT · HASH IL·LUSTRATIU')
    r.command(d,90,292,scene['commands'][0],p/.22)
    if p>.3:
        for i,(line,color) in enumerate(lines):r.text(d,(118,369+47*i),line,'code',color)
        if footnote:r.pill(d,90,527,footnote,r.PURPLE,'#312B47')


def blame_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='k_hook':
        code_card(r,d,(64,225,1216,412),'helloGit.py · main AL COMMIT C',[
            '1  # Programa de salutació',
            '2  missatge = "Hola, Anna!"',
            '3  print( salutacio )'],r.PURPLE)
        commands(r,d,scene,p,'TERMINAL · LA VARIABLE salutacio NO ESTÀ DEFINIDA')
        if p>.4:r.text(d,(695,507),"NameError: name 'salutacio' is not defined",'tinycode',RED)
    elif sid in ('k_blame','k_focus'):
        r.terminal(d,(64,235,1216,574),'TERMINAL · AUTORIA I DATES D’EXEMPLE')
        r.command(d,90,292,scene['commands'][0],p/.22)
        if p>.3:
            if sid=='k_blame':
                for i,line in enumerate(BLAME_ROWS):
                    if i==2:r.panel(d,(80,442,1198,483),fill='#312B47',outline=r.PURPLE,radius=10)
                    r.text(d,(90,357+47*i),line,'tinycode',r.PURPLE if i==2 else r.MUTED)
                r.text(d,(90,530),'Commit · autoria · data · número de línia · contingut','body',r.MUTED)
            else:
                r.panel(d,(80,371,1198,419),fill='#312B47',outline=r.PURPLE,radius=10)
                r.text(d,(90,384),BLAME_ROWS[2],'tinycode',r.PURPLE)
                r.pill(d,90,515,'c95f4a7 → COMMIT C',r.PURPLE,'#312B47')
    elif sid=='k_show':
        diff(r,d,scene,p,[('-print(salutacio)',r.ORANGE),('+print( salutacio )',r.MINT)],'C NOMÉS MODIFICA ELS ESPAIS')
    elif sid=='k_definition':
        code_card(r,d,(64,230,1216,411),'EDITOR · RELACIONAR DEFINICIÓ I ÚS',[
            '2  missatge = "Hola, Anna!"',
            '3  print( salutacio )'],r.PURPLE)
        r.pill(d,820,315,'NOMS DIFERENTS',r.ORANGE,'#3C2C2B')
        commands(r,d,scene,p,'TERMINAL · CONSULTAR LA LÍNIA DE LA DEFINICIÓ')
        if p>.4:r.text(d,(770,508),'b62d8e1 · línia 2 · commit B','tinycode',r.ORANGE)
    elif sid=='k_origin':
        diff(r,d,scene,p,[('-salutacio = "Hello Git!"',r.ORANGE),('+missatge = "Hola, Anna!"',r.MINT),(' print(salutacio)',r.MUTED)],'B CANVIA LA DEFINICIÓ PERÒ NO L’ÚS')
    elif sid=='k_context':
        d.line((160,285,900,285),fill=r.BORDER,width=6)
        for x,name,color in ((160,'A',r.MINT),(490,'B',RED),(900,'C',r.PURPLE)):r.node(d,x,285,name,color)
        r.pill(d,64,376,'A · funciona',r.MINT)
        r.pill(d,410,376,'B · introdueix l’error',r.ORANGE,'#3C2C2B')
        r.pill(d,900,376,'C · espais',r.PURPLE,'#312B47')
        commands(r,d,scene,p,'TERMINAL · HISTORIAL DEL FITXER · EXTRACTE')
        if p>.35:
            for i,line in enumerate(('c95f4a7 Ajusta espais','b62d8e1 Canvia variable','a31b2c4 Programa inicial')):
                r.text(d,(800,491+27*i),line,'tinycode',r.MUTED)
    elif sid=='k_summary':
        three_cards(r,d,(('Blame','Localitza el commit',r.PURPLE),('Show','Revisa el canvi',r.ORANGE),('Context','Relaciona les línies',r.MINT)))
        r.panel(d,(64,440,1216,574))
        r.text(d,(90,465),'Última modificació ≠ causa automàtica de l’error','h2',r.MINT)
        r.text(d,(90,526),'Consulta l’historial i comprova les dependències.','body',r.MUTED)
    else:raise ValueError(sid)


BIS_X={name:130+140*i for i,name in enumerate('ABCDEFGH')}


def bisect_graph(r,d,head='D',low='A',high='H',known=None,head_x=None,search=True):
    known=known or {'A':'good','H':'bad'}
    r.text(d,(64,215),f'TRAM DE CERCA: {low}–{high}' if search else 'RECERCA FINALITZADA · D IDENTIFICAT','label',r.MUTED)
    r.pill(d,1068,207,'main → H',r.ORANGE,'#3C2C2B')
    d.line((130,285,1110,285),fill=r.BORDER,width=6)
    if search:d.rounded_rectangle((BIS_X[low],243,BIS_X[high],250),radius=3,fill=r.PURPLE)
    for name,x in BIS_X.items():
        color={'good':r.MINT,'bad':RED}.get(known.get(name),r.MUTED)
        r.node(d,x,285,name,color)
    r.pill(d,88,365,'v1.0',r.PURPLE,'#312B47')
    x=BIS_X['H' if head=='main' else head] if head_x is None else head_x
    r.pill(d,x-48,365,f'HEAD: {head}',r.MINT)


def bisect_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='l_hook':
        bisect_graph(r,d,head='main')
        r.panel(d,(64,445,1216,574))
        r.text(d,(90,468),'A funcionava. H falla amb la mateixa prova.','h2',r.MINT)
        r.text(d,(90,528),"H: NameError: name 'salutacio' is not defined",'code',RED)
    elif sid=='l_bounds':
        for x,title,line,result,color in ((64,'A · v1.0 · BONA','print("Hello Git!")','→ Hello Git!',r.MINT),(666,'H · main · DOLENTA','print(salutacio)','→ NameError',RED)):
            code_card(r,d,(x,230,x+550,411),title,[line,result],color)
        commands(r,d,scene,p,'TERMINAL · COMENCEM AMB L’ARBRE NET')
        if p>.4:r.text(d,(710,506),'Sense sortida: no hi ha canvis','small',r.MUTED)
    elif sid=='l_start':
        bisect_graph(r,d,head='D' if p>.57 else 'main')
        commands(r,d,scene,p,'TERMINAL · BAD: L’ACTUAL H · GOOD: v1.0 A A')
        if p>.68:r.text(d,(720,537),'Git selecciona D per provar-lo','tinycode',r.PURPLE)
    elif sid=='l_bad':
        advanced=p>.6
        bisect_graph(r,d,head='C' if advanced else 'D',high='D' if advanced else 'H',known={'A':'good','H':'bad',**({'D':'bad'} if p>.38 else {})})
        commands(r,d,scene,p,'TERMINAL · EXECUTAR A D I COMUNICAR EL RESULTAT')
        if p>.33:r.text(d,(750,498),'NameError: salutacio','tinycode',RED)
        if advanced:r.text(d,(750,539),'Git selecciona C','tinycode',r.PURPLE)
    elif sid=='l_good':
        found=p>.58
        bisect_graph(r,d,head='C',low='C' if found else 'A',high='D',known={'A':'good','H':'bad','D':'bad',**({'C':'good'} if found else {})})
        if found:r.text(d,(64,410),'D · primer commit que falla','body',RED)
        commands(r,d,scene,p,'TERMINAL · EXECUTAR A C · HEAD ES QUEDA A C')
        if p>.32:r.text(d,(710,498),'Hello Git!','tinycode',r.MINT)
        if found:r.text(d,(710,538),"d04f7a2 is the first 'bad' commit",'tinycode',RED)
    elif sid=='l_inspect':
        diff(r,d,scene,p,[('-print("Hello Git!")',r.ORANGE),('+print(salutacio)',r.MINT)],'CONSULTA DE D · HEAD CONTINUA A C · main A H')
    elif sid=='l_reset':
        q=r.ease((p-.2)/.38)
        bisect_graph(r,d,head='main' if p>.58 else 'C',low='C',high='D',known={'A':'good','C':'good','D':'bad','H':'bad'},head_x=410+700*q,search=p<.6)
        if p>.6:r.text(d,(64,412),'Tornem a H · l’error continua pendent','body',RED)
        commands(r,d,scene,p,'TERMINAL · SORTIR DE LA CERCA I RECUPERAR EL PUNT DE PARTIDA')
    elif sid=='l_summary':
        three_cards(r,d,(('Prova','La mateixa a cada versió',r.PURPLE),('Good / bad','Classifica el resultat',r.MINT),('Primer error','Acota el commit',r.ORANGE)))
        r.panel(d,(64,441,1216,574))
        r.text(d,(90,465),'D identificat. La correcció encara és pendent.','h2',RED)
        r.text(d,(90,530),'En acabar la investigació: git bisect reset','code',r.MUTED)
    else:raise ValueError(sid)


def amend_graph(r,d,p=1,amended=False,moving=False):
    done=amended or (moving and p>.58)
    d.line((160,300,480,300,900,260),fill=r.BORDER,width=6)
    if done:d.line((480,300,900,365),fill=r.MINT,width=5)
    r.node(d,160,300,'A',r.ORANGE);r.node(d,480,300,'B',r.ORANGE)
    r.node(d,900,260,'C',r.MUTED if done else r.PURPLE)
    if done:
        r.node(d,900,365,'C′',r.MINT)
        r.text(d,(1020,298),'C queda fora de main','small',r.MUTED)
    q=r.ease((p-.22)/.36) if moving else int(amended)
    r.pill(d,1040,247+105*q,'main',r.ORANGE,'#3C2C2B')
    if .22<p<.58 and moving:r.pill(d,600+250*r.ease((p-.22)/.36),392,'notes.md',r.MINT)


def amend_scene(r,d,scene,t,duration):
    sid,p=scene['id'],r.clamp(t/duration)
    if sid=='o_hook':
        for x,title,lines,color in ((64,'COMMIT C · NOMÉS LOCAL',['helloGit.py confirmat'],r.PURPLE),(666,'FORA DEL COMMIT',['notes.md · fitxer nou'],r.ORANGE)):
            code_card(r,d,(x,240,x+550,480),title,lines,color)
        r.pill(d,64,531,'ÚLTIM COMMIT PROPI · ENCARA NO PUBLICAT',r.PURPLE,'#312B47')
    elif sid=='o_before':
        code_card(r,d,(64,230,618,411),'C · JA CONFIRMAT',['print("Hola, Anna!")'],r.PURPLE)
        code_card(r,d,(666,230,1216,411),'notes.md · ENCARA NO SEGUIT',['Exemple de salutació'],r.ORANGE)
        commands(r,d,scene,p,'TERMINAL · L’ÍNDEX NO TÉ ALTRES CANVIS PENDENTS')
        if p>.38:
            r.text(d,(770,499),'?? notes.md','tinycode',r.ORANGE)
            r.text(d,(770,537),'c95f4a7 Millora la salutacio','tinycode',r.PURPLE)
    elif sid=='o_add':
        code_card(r,d,(64,230,618,411),'FITXER LOCAL',['notes.md','Exemple de salutació'],r.MINT)
        code_card(r,d,(666,230,1216,411),'PREPARACIÓ',['notes.md · afegit'] if p>.4 else ['Cap canvi preparat'],r.PURPLE)
        commands(r,d,scene,p,'TERMINAL · PREPARAR NOMÉS EL FITXER QUE FALTAVA')
        if p>.5:r.text(d,(730,508),'notes.md | 1 +','tinycode',r.MINT)
    elif sid=='o_amend':
        amend_graph(r,d,p,moving=True)
        commands(r,d,scene,p,'TERMINAL · --no-edit CONSERVA EL MISSATGE')
        if p>.65:r.text(d,(760,508),'C′ · notes.md inclòs','tinycode',r.MINT)
    elif sid=='o_graph':
        amend_graph(r,d,amended=True)
        r.panel(d,(64,464,1216,574))
        r.text(d,(90,486),'Mateix pare B. Identificador nou.','h2',r.MINT)
        r.text(d,(90,538),'C′ substitueix C a main; no és un fill de C.','body',r.MUTED)
    elif sid=='o_check':
        r.terminal(d,(64,235,1216,574),'TERMINAL · C′ INCLOU ELS CANVIS RESPECTE DE B · EXTRACTE')
        r.command(d,90,292,scene['commands'][0],p/.18)
        if p>.26:
            for i,line in enumerate(('commit e18a3b6 · C′ · Millora la salutacio','helloGit.py | 2 +-','notes.md    | 1 +')):
                r.text(d,(118,351+37*i),line,'tinycode',r.MINT if i else r.PURPLE)
        if p>.48:r.command(d,90,482,scene['commands'][1],(p-.48)/.16)
        if p>.68:r.text(d,(650,530),'Sense sortida: arbre net','small',r.MUTED)
    elif sid=='o_message':
        for x,title,line,note,color in ((64,'ABANS · C','Millora la salutacio','Índex sense canvis respecte de C',r.PURPLE),(666,'DESPRÉS · C*','Personalitza el missatge','Arbre igual · pare B · hash nou',r.MINT)):
            code_card(r,d,(x,230,x+550,411),title,[line],color)
            r.text(d,(x+24,371),note,'small',r.MUTED)
        commands(r,d,scene,p,'TERMINAL · ALTERNATIVA INDEPENDENT DES DE C · NOMÉS MISSATGE')
    elif sid=='o_summary':
        three_cards(r,d,(('Preparar','Només allò que falta',r.PURPLE),('Revisar','Comprova l’índex',r.ORANGE),('Substituir','Un commit complet',r.MINT)))
        r.panel(d,(64,441,1216,574))
        r.text(d,(90,465),'Últim commit propi, encara no publicat.','h2',r.MINT)
        r.text(d,(90,529),'Amend reescriu el commit i en canvia l’identificador.','body',r.MUTED)
    else:raise ValueError(sid)


def draw_investigation(d,scene,t,duration,r):
    {'k':blame_scene,'l':bisect_scene,'o':amend_scene}[scene['id'][0]](r,d,scene,t,duration)
