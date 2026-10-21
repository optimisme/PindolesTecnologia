"""Escenes dels episodis de branques, preparació i sincronització.

El renderitzador proporciona les primitives visuals per conservar el mateix estil.
"""


def code_card(r, d, box, label, lines, color=None):
    color = color or r.MINT
    x, y, right, bottom = box
    r.panel(d, box)
    r.text(d, (x+24, y+20), label, "label", color)
    d.line((x+1, y+58, right-1, y+58), fill=r.BORDER, width=1)
    for i,line in enumerate(lines):
        r.text(d, (x+24, y+82+i*35), line, "code", color)


def commands(r, d, scene, p, title="TERMINAL"):
    cmds = scene.get("commands", [])
    top = 420 if len(cmds) >= 3 else 450
    r.terminal(d, (64, top, 1216, 574), title)
    for i,cmd in enumerate(cmds):
        start = .06+i*.14
        if p >= start:
            r.command(d, 90, top+51+i*33, cmd, (p-start)/.15)


def branch_graph(r, d, p, advanced=False, active="salutacio"):
    d.line((180, 300, 430, 300), fill=r.BORDER, width=6)
    r.node(d, 180, 300, "a31b2c4")
    r.node(d, 430, 300, "b62d8e1")
    r.pill(d, 365, 231, "main", r.ORANGE, "#3C2C2B")
    if advanced:
        amount = r.ease((p-.1)/.25)
        endpoint = (430+370*amount, 300+60*amount)
        d.line((430, 300, *endpoint), fill=r.PURPLE, width=5)
        if amount > .95:
            r.node(d, 800, 360, "c95f4a7", r.PURPLE)
            r.pill(d, 740, 282, "salutacio", r.PURPLE, "#312B47")
    else:
        r.pill(d, 485, 231, "salutacio", r.PURPLE, "#312B47")
        r.arrow(d, (520, 268), (457, 293), r.PURPLE, 3)
    if active:
        r.pill(d, 940, 235, f"ACTIVA: {active}", r.MINT)


def branch_scene(r, d, scene, t, duration):
    sid, p = scene["id"], r.clamp(t/duration)
    if sid == "b_hook":
        code_card(r, d, (64,240,618,486), "MAIN · JA FUNCIONA", ['print("Hello Git!")'], r.ORANGE)
        code_card(r, d, (666,240,1216,486), "NOVA IDEA · PER PROVAR", [r.type_text('print("Hola, Anna!")', t/2)], r.PURPLE)
        r.arrow(d, (628,365), (652,365), r.MUTED, 3)
        if p > .45:
            r.pill(d, 64, 525, "UNA BRANCA PER PROVAR LA IDEA")
    elif sid in ("b_concept", "b_create"):
        branch_graph(r, d, p, active="salutacio" if sid == "b_create" and p > .35 else "main")
        if sid == "b_create":
            commands(r, d, scene, p, "TERMINAL · CREAR I SITUAR-SE A LA BRANCA")
            if p > .65:
                r.text(d, (890,535), "→ salutacio", "tinycode", r.PURPLE)
        else:
            r.text(d, (64,488), "Les dues branques comencen al mateix commit.", "h2")
            r.text(d, (64,540), "Crear una branca encara no duplica ni modifica el codi.", "body", r.MUTED)
    elif sid == "b_edit":
        code_card(r, d, (64,230,1216,409), "helloGit.py · BRANCA salutacio", [r.type_text('print("Hola, Anna!")', t/1.5)], r.PURPLE)
        r.pill(d, 780, 325, "main CONTINUA INTACTA", r.ORANGE, "#3C2C2B")
        commands(r, d, scene, p, "TERMINAL · CONFIRMAR EL CANVI A salutacio")
    elif sid == "b_graph":
        branch_graph(r, d, p, advanced=True)
        code_card(r, d, (64,447,618,574), "main · b62d8e1", ['print("Hello Git!")'], r.ORANGE)
        code_card(r, d, (666,447,1216,574), "salutacio · c95f4a7", ['print("Hola, Anna!")'], r.PURPLE)
    elif sid in ("b_main", "b_back"):
        current_main = (sid == "b_main") == (p > .35)
        name = "main" if current_main else "salutacio"
        line = 'print("Hello Git!")' if current_main else 'print("Hola, Anna!")'
        other_name = "salutacio" if current_main else "main"
        other_line = 'print("Hola, Anna!")' if current_main else 'print("Hello Git!")'
        code_card(r, d, (64,230,618,409), f"EDITOR · ACTIVA: {name}", [line], r.ORANGE if current_main else r.PURPLE)
        code_card(r, d, (666,230,1216,409), f"DESADA A {other_name}", [other_line], r.MUTED)
        commands(r, d, scene, p, "TERMINAL · CANVIAR DE BRANCA AMB LA FEINA CONFIRMADA")
    elif sid == "b_summary":
        for i,(title,sub,color) in enumerate((("Branca","Una línia de treball",r.PURPLE),
                                              ("Canvi","Prova la teva idea",r.MINT),
                                              ("Commit","Desa-la a la branca",r.ORANGE))):
            x=64+i*392
            r.panel(d, (x,230,x+368,393))
            r.text(d, (x+24,255), title, "h2", color)
            r.text(d, (x+24,323), sub, "body")
        commands(r, d, scene, p, "RESUM · PER INCORPORAR EL CANVI A main: MERGE")
    else:
        raise ValueError(f"Escena de branques desconeguda: {sid}")


VERSIONS = {
    1: ['print("Hello Git!")'],
    2: ['print("Hola, Anna!")'],
    3: ['print("Hola, Anna!")', 'print("Fins aviat!")'],
}


def zones(r, d, versions, notes=None):
    notes = notes or ("Fitxer a l'editor", "Còpia per al pròxim commit", "Últim commit")
    for i,(title,color,version,note) in enumerate(zip(("TREBALL","PREPARACIÓ","HISTORIAL"),
                                                     (r.MINT,r.PURPLE,r.ORANGE),versions,notes)):
        x=64+i*392
        r.panel(d, (x,238,x+368,411))
        r.text(d, (x+20,257), title, "label", color)
        r.pill(d, x+282, 249, f"V{version}", color, "#263247")
        for j,line in enumerate(VERSIONS[version]):
            r.text(d, (x+20,305+j*29), line, "tinycode", color)
        r.text(d, (x+20,379), note, "small", r.MUTED)
    r.arrow(d, (438,328), (451,328), r.PURPLE, 3)
    r.arrow(d, (830,328), (843,328), r.ORANGE, 3)
    r.text(d, (445,208), "git add", "small", r.PURPLE, "mt")
    r.text(d, (837,208), "git commit", "small", r.ORANGE, "mt")


def state_scene(r, d, scene, t, duration):
    sid, p = scene["id"], r.clamp(t/duration)
    if sid == "s_hook":
        code_card(r, d, (64,240,618,487), "JA PREPARAT AMB ADD · V2", VERSIONS[2], r.PURPLE)
        code_card(r, d, (666,240,1216,487), "EDITAT DESPRÉS · V3", VERSIONS[3], r.MINT)
        if p > .4:
            r.pill(d, 64,525,"LA SEGONA LÍNIA TAMBÉ ENTRARÀ AL COMMIT?",r.ORANGE,"#3C2C2B")
    elif sid == "s_spaces":
        zones(r, d, (1,1,1))
        for i,(title,sub,color) in enumerate((("Desar","Modifica el fitxer",r.MINT),
                                             ("Add","Copia a preparació",r.PURPLE),
                                             ("Commit","Guarda a l'historial",r.ORANGE))):
            x=64+i*392
            r.panel(d,(x,451,x+368,563))
            r.text(d,(x+22,469),title,"h2",color)
            r.text(d,(x+22,520),sub,"body")
    elif sid == "s_edit":
        zones(r,d,(2,1,1))
        r.terminal(d,(64,436,1216,574),"TERMINAL · CANVIS PENDENTS DE PREPARAR")
        r.command(d,90,484,scene["commands"][0],p/.22)
        if p > .3:
            r.text(d,(580,489),'-print("Hello Git!")',"tinycode",r.ORANGE)
            r.text(d,(580,525),'+print("Hola, Anna!")',"tinycode",r.MINT)
    elif sid == "s_add":
        zones(r,d,(2,2 if p>.42 else 1,1))
        if .2 < p < .42:
            r.pill(d, 230+392*r.ease((p-.2)/.22), 410,"V2",r.PURPLE,"#312B47")
        commands(r,d,scene,p,"TERMINAL · PREPARAR UNA VERSIÓ CONCRETA")
    elif sid == "s_again":
        zones(r,d,(3 if p>.25 else 2,2,1))
        r.panel(d,(64,451,1216,563))
        r.text(d,(90,475),"Una edició nova no actualitza la preparació.","body")
        r.text(d,(90,523),'S’ha afegit: print("Fins aviat!")',"tinycode",r.MINT)
        r.pill(d,865,487,"CAL TORNAR A FER ADD",r.PURPLE,"#312B47")
    elif sid == "s_compare":
        r.pill(d,64,214,"git status --short: MM helloGit.py",r.ORANGE,"#3C2C2B")
        r.text(d,(650,220),"Preparats + pendents al mateix fitxer", "body",r.MUTED)
        for x,label,cmd in ((64,"CANVIS PENDENTS","git diff"),(650,"CANVIS PREPARATS","git diff --staged")):
            r.terminal(d,(x,270,x+550,574),label)
            r.command(d,x+26,328,cmd,p/.22)
            if p > .3:
                if x==64:
                    r.text(d,(x+26,393),'+print("Fins aviat!")',"tinycode",r.MINT)
                    r.text(d,(x+26,515),"Treball V3 vs preparació V2", "small",r.MUTED)
                else:
                    r.text(d,(x+26,382),'-print("Hello Git!")',"tinycode",r.ORANGE)
                    r.text(d,(x+26,417),'+print("Hola, Anna!")',"tinycode",r.MINT)
                    r.text(d,(x+26,515),"Preparació V2 vs últim commit V1", "small",r.MUTED)
    elif sid == "s_commit":
        zones(r,d,(3,2,2 if p>.35 else 1),("Línia nova pendent","Igual que l'últim commit" if p>.35 else "Canvi preparat","Confirmat: sense el comiat" if p>.35 else "Últim commit"))
        commands(r,d,scene,p,"TERMINAL · COMMIT DE LA VERSIÓ PREPARADA")
        if p>.6:
            r.text(d,(900,535)," M helloGit.py","tinycode",r.ORANGE)
    elif sid == "s_summary":
        zones(r,d,(3,3 if p>.32 else 2,3 if p>.62 else 2))
        commands(r,d,scene,p,"TERMINAL · INCLOURE TAMBÉ EL COMIAT")
    else:
        raise ValueError(f"Escena d'estats desconeguda: {sid}")


def network(r,d,versions,transfer=None,p=1):
    xs=(64,480,896)
    for i,(x,name,count) in enumerate(zip(xs,("CLASSE","GITHUB","CASA"),versions)):
        color=r.PURPLE if i==1 else r.MINT
        r.panel(d,(x,230,x+320,411))
        r.text(d,(x+22,249),name,"label",color)
        r.text(d,(x+22,285),"Remot · main" if i==1 else ("Local · main" if count else "Cap repositori"),"body")
        if count:
            if count>1:
                d.line((x+60,346,x+60+(count-1)*90,346),fill=r.BORDER,width=5)
            for j in range(count):
                r.node(d,x+60+j*90,346,chr(65+j),color)
    for a,b in ((0,1),(1,2)):
        left,right=xs[a]+332,xs[b]-14
        r.arrow(d,(left,346),(right,346),r.BORDER,3)
    if transfer:
        source,target,label=transfer
        amount=r.ease((p-.33)/.31)
        if .33 < p < .69:
            x=xs[source]+160+(xs[target]-xs[source])*amount
            r.pill(d,x-24,329,label,r.MINT)
        if target>source:
            left,right=xs[source]+332,xs[target]-14
        else:
            left,right=xs[source]-14,xs[target]+332
        r.arrow(d,(left,346),(right,346),r.MINT,4)


def sync_scene(r,d,scene,t,duration):
    sid,p=scene["id"],r.clamp(t/duration)
    if sid in ("n_hook","n_copies"):
        network(r,d,(2,1,1))
        r.panel(d,(64,451,1216,563))
        r.text(d,(90,474),"A classe: commit B. A casa: commit A." if sid=="n_hook" else "Dos repositoris locals. Un remot compartit.","h2")
        r.text(d,(90,528),"Els commits no viatgen sols." if sid=="n_hook" else "Cada ordinador conserva la seva pròpia còpia i el seu historial.","body",r.MUTED)
    elif sid=="n_push":
        network(r,d,(2 if p>.2 else 1,2 if p>.66 else 1,1),(0,1,"B"),p)
        commands(r,d,scene,p,"CLASSE · CONFIRMAR I ENVIAR")
    elif sid=="n_clone":
        network(r,d,(2,2,2 if p>.66 else 0),(1,2,"A + B"),p)
        commands(r,d,scene,p,"CASA · OPCIÓ A: ENCARA NO HI HA REPOSITORI")
    elif sid=="n_pull":
        network(r,d,(2,2,2 if p>.66 else 1),(1,2,"B"),p)
        commands(r,d,scene,p,"CASA · OPCIÓ B: EL REPOSITORI JA ESTAVA CLONAT")
    elif sid=="n_home":
        network(r,d,(2,3 if p>.66 else 2,3 if p>.2 else 2),(2,1,"C"),p)
        commands(r,d,scene,p,"CASA · NOU CANVI, COMMIT I PUSH")
    elif sid=="n_class":
        network(r,d,(3 if p>.66 else 2,3,3),(1,0,"C"),p)
        commands(r,d,scene,p,"CLASSE · COMPROVAR L'ESTAT I ACTUALITZAR")
        if p>.25:
            r.text(d,(700,505),"Status sense sortida: arbre net", "small",r.MUTED)
    elif sid=="n_summary":
        for i,(title,sub,color) in enumerate((("Clone","Obtenir el projecte",r.PURPLE),
                                             ("Pull","Integrar els nous commits",r.ORANGE),
                                             ("Push","Enviar els teus commits",r.MINT))):
            x=64+i*392
            r.panel(d,(x,230,x+368,393))
            r.text(d,(x+24,255),title,"h2",color)
            r.text(d,(x+24,323),sub,"body")
        commands(r,d,scene,p,"RESUM · ACTUALITZAR → TREBALLAR → COMMIT → PUSH")
    else:
        raise ValueError(f"Escena de sincronització desconeguda: {sid}")


def draw_lesson(d,scene,t,duration,r):
    if scene["id"].startswith("b_"):
        branch_scene(r,d,scene,t,duration)
    elif scene["id"].startswith("s_"):
        state_scene(r,d,scene,t,duration)
    elif scene["id"].startswith("n_"):
        sync_scene(r,d,scene,t,duration)
    elif scene['id'].startswith(('m_','c_','r_')):
        from integration_visuals import draw_integration
        draw_integration(d,scene,t,duration,r)
    elif scene['id'].startswith(('t_','u_','w_')):
        from undo_visuals import draw_undo
        draw_undo(d,scene,t,duration,r)
    elif scene['id'].startswith(('x_','y_','z_')):
        from recovery_visuals import draw_recovery
        draw_recovery(d,scene,t,duration,r)
    elif scene['id'].startswith(('g_','h_','j_')):
        from collaboration_visuals import draw_collaboration
        draw_collaboration(d,scene,t,duration,r)
    elif scene['id'].startswith(('k_','l_','o_')):
        from investigation_visuals import draw_investigation
        draw_investigation(d,scene,t,duration,r)
    elif scene['id'].startswith(('p_','q_','v_')):
        from advanced_visuals import draw_advanced
        draw_advanced(d,scene,t,duration,r)
    elif scene['id'].startswith(('a_','d_','h25_')):
        from workflow_visuals import draw_workflow
        draw_workflow(d,scene,t,duration,r)
    else:
        raise ValueError(f"Escena desconeguda: {scene['id']}")
