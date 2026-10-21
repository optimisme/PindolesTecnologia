# YouTube · lliçó 29

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (61/100 caràcters)

```text
Bisect: troba el primer commit que falla · Píndoles de Git 29
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
  git show 81c386d -- helloGit.py
  git bisect reset

Practica-ho: En un historial de pràctiques amb un error que es manté, marca un extrem que funciona i un que falla. Fes servir sempre la mateixa prova i acaba la cerca amb git bisect reset.
Script per preparar el mateix punt de partida: Git/practiques/29-bisect.sh

Lliçó anterior: 28 · Blame: investiga l’origen d’una línia
Lliçó següent: 30 · Worktree: corregeix main sense interrompre la feina

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, bisect  
**Llista:** Píndoles de Git, posició 30  
**Idioma del vídeo i dels subtítols:** català  
**Subtítols:** `output/29-bisect.ca.srt`  
**Miniatura:** `output/portada.png`

> Encara no s’ha produït el vídeo: els capítols s’afegiran quan existeixi `output/produccio.json`.
