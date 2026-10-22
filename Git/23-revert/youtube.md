# YouTube · lliçó 23

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (54/100 caràcters)

```text
Revert: desfés un commit publicat · Píndoles de Git 23
```

**Descripció**

```text
Desfer l’efecte d’un commit ja publicat amb un commit nou que fa el canvi invers.

Punt de partida: L’últim commit ja és a GitHub i ha trencat el programa. Altres persones ja el poden tenir.

Ordres que surten al vídeo:
  python3 helloGit.py
  git status --short
  git log --oneline
  git show c1560a6 -- helloGit.py
  git revert --no-edit c1560a6
  git push

Practica-ho: En un repositori de pràctiques, desfés un commit amb git revert. Compara el graf abans i després i comprova que el commit original hi continua.
Script per preparar el mateix punt de partida: Git/practiques/23-revert.sh

Capítols:
0:00 Capçalera i presentació
0:33 Una correcció que també queda registrada
0:49 $ python3 helloGit.py
1:08 $ git status --short
1:27 $ git log --oneline
1:46 $ git show c1560a6 -- helloGit.py
2:15 $ git revert --no-edit c1560a6
2:52 $ python3 helloGit.py
3:08 $ git push
3:33 Revert desfà un commit concret
3:50 Resum final
4:12 Pràctica final

Lliçó anterior: 22 · Reflog: recupera un commit local
Lliçó següent: 24 · Desfer canvis: quina ordre triar

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, revert  
**Llista:** Píndoles de Git, posició 24  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/23-revert.mp4`  
**Subtítols:** `23-revert/output/23-revert.ca.srt`  
**Miniatura:** `23-revert/output/portada.png`
