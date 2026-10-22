# YouTube · lliçó 27

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (72/100 caràcters)

```text
Rebase interactiu: agrupa commits abans de publicar · Píndoles de Git 27
```

**Descripció**

```text
Agrupar tres commits relacionats que encara no hem publicat, conservant el contingut final.

Punt de partida: A la branca salutació hi ha tres commits petits sobre la mateixa millora: la salutació, una correcció de puntuació i unes notes. Encara no els hem publicat.

Ordres que surten al vídeo:
  git status --short
  git log -3 --oneline
  git rebase -i HEAD~3
  python3 helloGit.py
  git diff 0d33d2d HEAD

Practica-ho: En una branca local de pràctiques, agrupa tres commits relacionats. Guarda l’identificador de l’últim abans de començar i compara el contingut al final.
Script per preparar el mateix punt de partida: Git/practiques/27-rebase-interactiu.sh

Capítols:
0:00 Capçalera i presentació
0:37 Una millora explicada en tres commits
0:51 $ git status --short
1:12 $ git log -3 --oneline
1:41 $ git rebase -i HEAD~3
2:21 Triem les operacions
2:47 Escrivim el missatge conjunt
3:03 Un commit nou amb el mateix resultat
3:21 $ python3 helloGit.py
3:39 $ git diff 0d33d2d HEAD
4:13 Si l’operació s’atura
4:33 Resum final
4:56 Pràctica final

Lliçó anterior: 26 · Rebase: continua sobre una base nova
Lliçó següent: 28 · Cherry-pick: porta una correcció a una altra branca

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, rebase interactiu  
**Llista:** Píndoles de Git, posició 28  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/27-rebase-interactiu.mp4`  
**Subtítols:** `27-rebase-interactiu/output/27-rebase-interactiu.ca.srt`  
**Miniatura:** `27-rebase-interactiu/output/portada.png`
