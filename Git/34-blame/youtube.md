# YouTube · lliçó 34

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (58/100 caràcters)

```text
Blame: investiga l’origen d’una línia · Píndoles de Git 34
```

**Descripció**

```text
Investigar una línia amb [[git blame]] i confirmar la causa d’un error amb [[git show]].

Punt de partida: El programa ha deixat de funcionar i volem saber quin canvi ho ha provocat.

Ordres que surten al vídeo:
  python3 helloGit.py
  git blame helloGit.py
  git blame -L 3,3 helloGit.py
  git show 4cd6c24 -- helloGit.py
  git blame -L 2,2 helloGit.py
  git show b5e2fac -- helloGit.py

Practica-ho: En un fitxer de pràctiques, investiga dues línies relacionades. Revisa els commits que les van canviar i separa els canvis funcionals dels retocs de format.
Script per preparar el mateix punt de partida: Git/practiques/34-blame.sh

Capítols:
0:00 Capçalera i presentació
0:28 Una línia que falla té un context
0:43 $ python3 helloGit.py
1:03 $ git blame helloGit.py
1:32 $ git blame -L 3,3 helloGit.py
2:06 $ git show 4cd6c24 -- helloGit.py
2:32 $ git blame -L 2,2 helloGit.py
2:59 $ git show b5e2fac -- helloGit.py
3:25 Resum final
3:51 Pràctica final

Lliçó anterior: 33 · Cercar a l’historial: autoria, fitxers i text
Lliçó següent: 35 · Bisect: troba el primer commit que falla

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, blame  
**Llista:** Píndoles de Git, posició 35  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/34-blame.mp4`  
**Subtítols:** `34-blame/output/34-blame.ca.srt`  
**Miniatura:** `34-blame/output/portada.png`
