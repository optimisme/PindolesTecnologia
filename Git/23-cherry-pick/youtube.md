# YouTube · lliçó 23

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (72/100 caràcters)

```text
Cherry-pick: porta una correcció a una altra branca · Píndoles de Git 23
```

**Descripció**

```text
Aplicar a [[main]] només una correcció d’una altra branca, sense portar-hi la resta de la feina.

Punt de partida: main té una errada a la salutació. A la branca salutació, entre altres feines encara pendents, ja hi ha un commit que la corregeix.

Ordres que surten al vídeo:
  git log --oneline salutacio
  git show efabf94 -- helloGit.py
  git status --short
  git switch main
  git cherry-pick efabf94
  python3 helloGit.py
  git add helloGit.py
  git cherry-pick --continue
  git cherry-pick --abort

Practica-ho: En un repositori de pràctiques, crea en una branca una correcció independent d’una altra feina. Porta només la correcció a main i comprova els fitxers de les dues branques.
Script per preparar el mateix punt de partida: Git/practiques/23-cherry-pick.sh

Lliçó anterior: 22 · Rebase interactiu: agrupa commits abans de publicar
Lliçó següent: 24 · Pull request: proposa un canvi a l’equip

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, cherry-pick  
**Llista:** Píndoles de Git, posició 24  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/23-cherry-pick.mp4`  
**Subtítols:** `23-cherry-pick/output/23-cherry-pick.ca.srt`  
**Miniatura:** `23-cherry-pick/output/portada.png`

> Encara no s’ha produït el vídeo: els capítols s’afegiran quan existeixi `output/produccio.json`.
