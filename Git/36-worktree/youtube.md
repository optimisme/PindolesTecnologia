# YouTube · lliçó 36

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (72/100 caràcters)

```text
Worktree: corregeix main sense interrompre la feina · Píndoles de Git 36
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
Script per preparar el mateix punt de partida: Git/practiques/36-worktree.sh

Capítols:
0:00 Capçalera i presentació
0:31 Dues carpetes, preparacions separades
0:46 $ git worktree add -b correccio ../projecte-correccio main
1:32 $ git worktree list
1:52 $ cd ../projecte-correccio
2:16 Fem només la correcció
2:45 $ git add helloGit.py
3:02 $ git commit -m "Corregeix la puntuacio"
3:24 $ git switch main
3:57 $ git merge --ff-only correccio
4:24 $ git -C ../projecte status --short
4:55 $ cd ../projecte
5:13 $ git worktree remove ../projecte-correccio
5:43 Resum final
6:08 Pràctica final

Lliçó anterior: 35 · Bisect: troba el primer commit que falla
Lliçó següent: 37 · Hooks: comprova la sintaxi abans del commit

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, worktree  
**Llista:** Píndoles de Git, posició 37  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/36-worktree.mp4`  
**Subtítols:** `36-worktree/output/36-worktree.ca.srt`  
**Miniatura:** `36-worktree/output/portada.png`
