"""Vistes fetes a mida de la lliçó 0 (introducció): sense terminal ni passos de comandes."""

# Tres columnes amb espai suficient per a una fletxa entre targetes.
COLUMNS = [(64, 404), (470, 810), (876, 1216)]


def draw_general(d, scene, t, r):
    beats=scene['_timed_beats']
    beat=next((b for b in reversed(beats) if t>=b['at']),beats[0])
    view=beat['view']

    def card(x,y,w,h,label,lines=(),color=None,title=None):
        color=color or r.MINT
        r.panel(d,(x,y,x+w,y+h))
        r.text(d,(x+24,y+20),label,'label',color)
        top=y+60
        if title:
            r.text(d,(x+24,top),title,'h2',color)
            top+=56
        for i,line in enumerate(lines):r.text(d,(x+24,top+i*38),line,'body')

    def arrows(y,colors):
        for (_,right),(left,_),color in zip(COLUMNS,COLUMNS[1:],colors):
            r.arrow(d,(right+12,y),(left-12,y),color)

    def website(x,title,new=False):
        card(x,240,550,285,title,color=r.PURPLE if new else r.MINT)
        d.rounded_rectangle((x+25,300,x+525,352),8,fill='#253449')
        menu='Inici    Projectes    Contacte' if new else 'Inici    Contacte'
        r.text(d,(x+43,313),menu,'body')
        if new:
            # Subratllat mesurat sobre el text, no amb posicions fixes.
            left=x+43+d.textlength('Inici    ',font=r.F['body'])
            right=left+d.textlength('Projectes',font=r.F['body'])
            d.line((left,346,right,346),fill=r.PURPLE,width=4)
        d.rounded_rectangle((x+25,372,x+262,500),8,fill='#203B42')
        d.rounded_rectangle((x+282,372,x+525,500),8,fill='#312B47')
        r.text(d,(x+41,386),'Benvinguda','label',r.MINT)
        for i,line in enumerate(('Hola! Som la','classe de 1r.')):
            r.text(d,(x+41,418+i*26),line,'small',r.WHITE)
        if new:
            r.text(d,(x+298,386),'Projectes','label',r.PURPLE)
            for i,line in enumerate(('Web de la classe','Joc de preguntes')):
                r.text(d,(x+298,418+i*26),'· '+line,'small',r.WHITE)
        else:
            r.text(d,(x+298,386),'Contacte','label',r.PURPLE)
            r.text(d,(x+298,418),'Escriu-nos!','small',r.WHITE)

    def history():
        r.panel(d,(64,236,1216,475))
        r.text(d,(88,257),'REPOSITORI · HISTORIAL DEL PROJECTE','label',r.ORANGE)
        d.line((220,350,1060,350),fill=r.BORDER,width=6)
        for x,name,label,color in ((220,'A','Versió inicial',r.ORANGE),
                (640,'B','Afegeix el menú',r.PURPLE),(1060,'C','Corregeix un error',r.MINT)):
            r.node(d,x,350,None,color,scale=1.2)
            r.text(d,(x,350),name,'h2',r.BG,'mm')
            r.text(d,(x,405),label,'body',r.WHITE,'mt')

    if view=='project':
        website(64,'PRIMERA VERSIÓ');website(666,'DESPRÉS D’UN CANVI',True)
        r.pill(d,64,545,'EL PROJECTE EVOLUCIONA')
    elif view=='copies':
        for i,(name,note,color) in enumerate((('projecte_final','Primera còpia',r.ORANGE),
              ('projecte_final2','Una altra còpia',r.PURPLE),('projecte_definitiu','Un altre canvi',r.MINT))):
            left,right=COLUMNS[i]
            d.rounded_rectangle((left+24,247,left+150,281),8,fill=color)
            card(left,269,right-left,219,name,[note],color)
        r.text(d,(64,532),'Els noms de carpetes no expliquen tota la història.','h2')
    elif view in ('history','records'):
        history()
        if view=='records':
            r.pill(d,64,521,'COMMIT = REGISTRE D’UNA VERSIÓ',r.PURPLE,'#312B47')
            r.text(d,(500,526),'Identificador i missatge del canvi','body',r.MUTED)
        else:r.text(d,(64,527),'Versions relacionades dins del mateix historial.','h2')
    elif view=='compare':
        website(64,'VERSIÓ A');website(666,'VERSIÓ B',True)
        r.arrow(d,(624,436),(656,436),r.PURPLE)
        r.pill(d,64,545,'LA COMPARACIÓ FA VISIBLE EL CANVI')
    elif view=='local':
        card(64,235,550,288,'ORDINADOR · GIT',['Fitxers del projecte','Historial de versions'],r.ORANGE)
        card(666,235,550,288,'CONNEXIÓ A INTERNET',['No cal per registrar versions','ni per consultar l’historial.'],r.PURPLE)
        r.pill(d,64,540,'EL REPOSITORI LOCAL CONSERVA LA INFORMACIÓ')
    elif view in ('remote','team'):
        for (left,right),(label,lines,color) in zip(COLUMNS,(('ORDINADOR A',['Còpia de treball','Historial local'],r.ORANGE),
              ('GITHUB · REMOT',['Repositori compartit','Versions publicades'],r.PURPLE),
              ('ORDINADOR B',['Còpia de treball','Historial local'],r.MINT))):
            card(left,240,right-left,245,label,lines,color)
        arrows(362,(r.PURPLE,r.MINT))
        r.text(d,(64,528),'Compartir versions i integrar la feina de l’equip.' if view=='team' else
               'Git i GitHub tenen funcions diferents.','h2')
    elif view=='intentional':
        for (left,right),(label,note,color) in zip(COLUMNS,(('EDITOR','Escrivim el canvi',r.MINT),
              ('FITXER DESAT','El canvi és al disc',r.PURPLE),('HISTORIAL','Registrem una versió',r.ORANGE))):
            card(left,250,right-left,235,label,[note],color)
        arrows(367,(r.PURPLE,r.ORANGE))
        r.pill(d,64,535,'DESAR AL FITXER I REGISTRAR UNA VERSIÓ SÓN ACCIONS DIFERENTS')
    elif view=='review':
        card(64,245,550,250,'REGISTRAR',['Conservem un estat','i un missatge del canvi.'],r.ORANGE)
        card(666,245,550,250,'REVISAR I PROVAR',['Comprovem el contingut','i el resultat del programa.'],r.MINT)
        r.text(d,(64,539),'Una versió registrada també pot contenir errors.','h2')
    elif view in ('summary','next'):
        for i,((left,right),(title,note,color)) in enumerate(zip(COLUMNS,(('Registrar','Conservar versions',r.ORANGE),
              ('Comparar','Entendre els canvis',r.PURPLE),('Col·laborar','Coordinar la feina',r.MINT)))):
            card(left,257,right-left,234,f'0{i+1}',[note],color,title=title)
        r.pill(d,64,537,'LLIÇÓ 1 · CONFIGURACIÓ INICIAL' if view=='next' else 'TRES IDEES PER COMENÇAR')
    else:raise ValueError(f'Visual general desconegut: {view}')
