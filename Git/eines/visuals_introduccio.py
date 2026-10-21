"""Vistes fetes a mida de la lliçó 0 (introducció): sense terminal ni passos de comandes."""


def draw_general(d, scene, t, r):
    beats=scene['_timed_beats']
    beat=next((b for b in reversed(beats) if t>=b['at']),beats[0])
    view=beat['view']

    def card(x,y,w,h,label,lines=(),color=None):
        color=color or r.MINT
        r.panel(d,(x,y,x+w,y+h))
        r.text(d,(x+24,y+21),label,'label',color)
        for i,line in enumerate(lines):r.text(d,(x+24,y+80+i*40),line,'body')

    def website(x,title,new=False):
        card(x,240,550,285,title,color=r.PURPLE if new else r.MINT)
        d.rounded_rectangle((x+25,305,x+525,357),8,fill='#253449')
        r.text(d,(x+43,319),'Inici    Projectes    Contacte' if new else 'Inici    Contacte','body')
        d.rounded_rectangle((x+25,383,x+250,487),8,fill='#203B42')
        d.rounded_rectangle((x+272,383,x+525,487),8,fill='#312B47')
        if new:d.line((x+125,351,x+235,351),fill=r.PURPLE,width=4)

    def history():
        r.panel(d,(64,236,1216,475))
        r.text(d,(88,257),'REPOSITORI · HISTORIAL DEL PROJECTE','label',r.ORANGE)
        d.line((220,342,1060,342),fill=r.BORDER,width=6)
        for x,name,label,color in ((220,'A','Versió inicial',r.ORANGE),
                (640,'B','Afegeix el menú',r.PURPLE),(1060,'C','Corregeix un error',r.MINT)):
            r.node(d,x,342,name,color)
            r.text(d,(x,411),label,'body',r.WHITE,'mt')

    if view=='project':
        website(64,'PRIMERA VERSIÓ');website(666,'DESPRÉS D’UN CANVI',True)
        r.pill(d,64,541,'EL PROJECTE EVOLUCIONA')
    elif view=='copies':
        for i,(name,note,color) in enumerate((('projecte_final','Primera còpia',r.ORANGE),
              ('projecte_final2','Una altra còpia',r.PURPLE),('projecte_definitiu','Un altre canvi',r.MINT))):
            x=64+i*392
            d.rounded_rectangle((x+24,247,x+150,281),8,fill=color)
            card(x,269,368,219,name,[note],color)
        r.text(d,(64,532),'Els noms de carpetes no expliquen tota la història.','h2')
    elif view in ('history','records'):
        history()
        if view=='records':
            r.pill(d,64,521,'COMMIT = REGISTRE D’UNA VERSIÓ',r.PURPLE,'#312B47')
            r.text(d,(668,526),'Identificador i missatge del canvi','body',r.MUTED)
        else:r.text(d,(64,527),'Versions relacionades dins del mateix historial.','h2')
    elif view=='compare':
        website(64,'VERSIÓ A');website(666,'VERSIÓ B',True)
        r.arrow(d,(628,390),(652,390),r.PURPLE)
        r.pill(d,64,541,'LA COMPARACIÓ FA VISIBLE EL CANVI')
    elif view=='local':
        card(64,235,550,288,'ORDINADOR · GIT',['Fitxers del projecte','Historial de versions'],r.ORANGE)
        card(666,235,550,288,'CONNEXIÓ A INTERNET',['No cal per registrar versions','ni per consultar l’historial.'],r.PURPLE)
        r.pill(d,64,540,'EL REPOSITORI LOCAL CONSERVA LA INFORMACIÓ')
    elif view in ('remote','team'):
        for i,(label,lines,color) in enumerate((('ORDINADOR A',['Còpia de treball','Historial local'],r.ORANGE),
              ('GITHUB · REMOT',['Repositori compartit','Versions publicades'],r.PURPLE),
              ('ORDINADOR B',['Còpia de treball','Historial local'],r.MINT))):
            card(64+i*392,240,368,245,label,lines,color)
        r.arrow(d,(437,355),(450,355),r.PURPLE);r.arrow(d,(829,355),(842,355),r.MINT)
        r.text(d,(64,528),'Compartir versions i integrar la feina de l’equip.' if view=='team' else
               'Git i GitHub tenen funcions diferents.','h2')
    elif view=='intentional':
        for i,(label,note,color) in enumerate((('EDITOR','Escrivim el canvi',r.MINT),
              ('FITXER DESAT','El canvi és al disc',r.PURPLE),('HISTORIAL','Registrem una versió',r.ORANGE))):
            card(64+i*392,250,368,235,label,[note],color)
        r.arrow(d,(437,355),(450,355),r.PURPLE);r.arrow(d,(829,355),(842,355),r.ORANGE)
        r.pill(d,64,535,'DESAR AL FITXER I REGISTRAR UNA VERSIÓ SÓN ACCIONS DIFERENTS')
    elif view=='review':
        card(64,245,550,250,'REGISTRAR',['Conservem un estat','i un missatge del canvi.'],r.ORANGE)
        card(666,245,550,250,'REVISAR I PROVAR',['Comprovem el contingut','i el resultat del programa.'],r.MINT)
        r.text(d,(64,539),'Una versió registrada també pot contenir errors.','h2')
    elif view in ('summary','next'):
        for i,(label,note,color) in enumerate((('Registrar','Conservar versions',r.ORANGE),
              ('Comparar','Entendre els canvis',r.PURPLE),('Col·laborar','Coordinar la feina',r.MINT))):
            card(64+i*392,257,368,234,label,[note],color)
        r.pill(d,64,537,'LLIÇÓ 1 · CONFIGURACIÓ INICIAL' if view=='next' else 'TRES IDEES PER COMENÇAR')
    else:raise ValueError(f'Visual general desconegut: {view}')
