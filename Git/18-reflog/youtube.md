# YouTube · lliçó 18

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (53/100 caràcters)

```text
Reflog: recupera un commit local · Píndoles de Git 18
```

**Descripció**

```text
Trobar un commit al [[reflog]] i tornar-hi a donar accés amb una branca, sense perdre els canvis preparats.

Punt de partida: Continuem on ho vam deixar amb reset soft. La branca ha tornat enrere i el commit de la salutació ja no apareix a l’historial de main.

Ordres que surten al vídeo:
  git log --oneline
  git reflog
  git show 11b767c -- helloGit.py
  git branch recuperacio 11b767c
  git log --oneline --decorate --all
  git status --short

Practica-ho: Després d’un reset soft de pràctiques, troba el commit al reflog, revisa’l i crea-hi una branca de recuperació sense canviar de branca.
Script per preparar el mateix punt de partida: Git/practiques/18-reflog.sh

Lliçó anterior: 17 · Reset: torna enrere un commit local
Lliçó següent: 19 · Revert: desfés un commit publicat

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, reflog  
**Llista:** Píndoles de Git, posició 19  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/18-reflog.mp4`  
**Subtítols:** `18-reflog/output/18-reflog.ca.srt`  
**Miniatura:** `18-reflog/output/portada.png`

> Encara no s’ha produït el vídeo: els capítols s’afegiran quan existeixi `output/produccio.json`.
