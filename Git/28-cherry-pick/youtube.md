# YouTube · lliçó 28

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (72/100 caràcters)

```text
Cherry-pick: porta una correcció a una altra branca · Píndoles de Git 28
```

**Descripció**

```text
Aplicar a [[main]] només una correcció d’una altra branca, sense portar-hi la resta de la feina.

Punt de partida: main té una errada a la salutació. A la branca salutació, entre altres feines encara pendents, ja hi ha un commit que la corregeix.

Ordres que surten al vídeo:
  git log --oneline salutacio
  git show 2e324d3 -- helloGit.py
  git status --short
  git switch main
  git cherry-pick 2e324d3
  python3 helloGit.py
  git add helloGit.py
  git cherry-pick --continue
  git cherry-pick --abort

Practica-ho: En un repositori de pràctiques, crea en una branca una correcció independent d’una altra feina. Porta només la correcció a main i comprova els fitxers de les dues branques.
Script per preparar el mateix punt de partida: Git/practiques/28-cherry-pick.sh

Capítols:
0:00 Capçalera i presentació
0:34 Una correcció dins d’una altra feina
0:51 $ git log --oneline salutacio
1:15 $ git show 2e324d3 -- helloGit.py
1:39 $ git status --short
1:57 $ git switch main
2:26 $ git cherry-pick 2e324d3
3:00 $ python3 helloGit.py
3:20 Si l’aplicació s’atura
3:34 $ python3 helloGit.py
3:49 $ git add helloGit.py
4:05 $ git cherry-pick --continue
4:33 Alternativa, abandonar
5:03 Resum final
5:28 Pràctica final

Lliçó anterior: 27 · Rebase interactiu: agrupa commits abans de publicar
Lliçó següent: 29 · Pull request: proposa un canvi a l’equip

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, cherry-pick  
**Llista:** Píndoles de Git, posició 29  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/28-cherry-pick.mp4`  
**Subtítols:** `28-cherry-pick/output/28-cherry-pick.ca.srt`  
**Miniatura:** `28-cherry-pick/output/portada.png`
