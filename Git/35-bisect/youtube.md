# YouTube · lliçó 35

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (61/100 caràcters)

```text
Bisect: troba el primer commit que falla · Píndoles de Git 35
```

**Descripció**

```text
Localitzar el primer commit que falla amb una prova que es pugui repetir, i tancar la cerca.

Punt de partida: La primera entrega, l’etiqueta v u punt zero, funcionava. Després hi ha sis commits més i ara el programa falla.

Ordres que surten al vídeo:
  git status --short
  git bisect start
  git bisect bad
  git bisect good v1.0
  python3 helloGit.py
  git bisect good
  git show 0188213 -- helloGit.py
  git bisect reset

Practica-ho: En un historial de pràctiques amb un error que es manté, marca un extrem que funciona i un que falla. Fes servir sempre la mateixa prova i acaba la cerca amb git bisect reset.
Script per preparar el mateix punt de partida: Git/practiques/35-bisect.sh

Capítols:
0:00 Capçalera i presentació
0:32 Acotar l’error amb una prova
0:52 $ git status --short
1:10 $ git bisect start
1:28 $ git bisect bad
1:52 $ git bisect good v1.0
2:24 HEAD separat
2:45 $ python3 helloGit.py
3:03 $ git bisect bad
3:23 $ python3 helloGit.py
3:37 $ git bisect bad
3:53 $ python3 helloGit.py
4:08 $ git bisect good
4:32 $ git show 0188213 -- helloGit.py
4:56 $ git bisect reset
5:30 Resum final
5:53 Pràctica final

Lliçó anterior: 34 · Blame: investiga l’origen d’una línia
Lliçó següent: 36 · Worktree: corregeix main sense interrompre la feina

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, bisect  
**Llista:** Píndoles de Git, posició 36  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/35-bisect.mp4`  
**Subtítols:** `35-bisect/output/35-bisect.ca.srt`  
**Miniatura:** `35-bisect/output/portada.png`
