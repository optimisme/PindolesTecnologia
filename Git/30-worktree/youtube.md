# YouTube · lliçó 30

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (72/100 caràcters)

```text
Worktree: corregeix main sense interrompre la feina · Píndoles de Git 30
```

**Descripció**

```text
Fer una correcció en una segona carpeta de treball sense tocar la feina pendent de la primera.

Punt de partida: Som a la branca salutació, a mitja feina. Ens demanen una correcció ràpida a main i no volem tocar el que tenim a mig fer.

Ordres que surten al vídeo:
  git worktree add -b correccio ../projecte-correccio main
  git worktree list
  cd ../projecte-correccio
  python3 helloGit.py
  git add helloGit.py
  git commit -m "Corregeix la puntuacio"
  git switch main
  git merge --ff-only correccio
  git -C ../projecte status --short
  cd ../projecte
  git worktree remove ../projecte-correccio

Practica-ho: En un repositori de pràctiques, deixa una edició pendent i crea un worktree per a una correcció petita. Comprova l’estat de les dues carpetes abans de retirar l’auxiliar.
Script per preparar el mateix punt de partida: Git/practiques/30-worktree.sh

Lliçó anterior: 29 · Bisect: troba el primer commit que falla
Lliçó següent: 31 · Hooks: comprova la sintaxi abans del commit

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, worktree  
**Llista:** Píndoles de Git, posició 31  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/30-worktree.mp4`  
**Subtítols:** `30-worktree/output/30-worktree.ca.srt`  
**Miniatura:** `30-worktree/output/portada.png`

> Encara no s’ha produït el vídeo: els capítols s’afegiran quan existeixi `output/produccio.json`.
