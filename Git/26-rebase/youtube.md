# YouTube · lliçó 26

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (57/100 caràcters)

```text
Rebase: continua sobre una base nova · Píndoles de Git 26
```

**Descripció**

```text
Tornar a aplicar els commits propis sobre una base actualitzada i veure per què canvien d’identificador.

Punt de partida: La nostra branca salutació té dos commits propis, encara no publicats. Mentrestant, main ha avançat amb un commit nou en un altre fitxer.

Ordres que surten al vídeo:
  git switch salutacio
  git rebase main
  git log --oneline --graph --all
  python3 helloGit.py
  git add helloGit.py
  git rebase --continue
  git rebase --abort

Practica-ho: En una branca local de pràctiques amb canvis compatibles, torna a aplicar la teva feina sobre main. Compara el graf i prova el resultat.
Script per preparar el mateix punt de partida: Git/practiques/26-rebase.sh

Capítols:
0:00 Capçalera i presentació
0:37 Una base que ha avançat
0:52 $ git switch salutacio
1:21 $ git rebase main
1:56 Seguim un canvi concret
2:14 $ git log --oneline --graph --all
2:44 Comparació amb merge
3:05 Si apareix un conflicte
3:19 $ python3 helloGit.py
3:34 $ git add helloGit.py
3:50 $ git rebase --continue
4:21 Alternativa, abandonar el rebase
4:57 Resum final
5:23 Pràctica final

Lliçó anterior: 25 · Tags: identifica una entrega del projecte
Lliçó següent: 27 · Rebase interactiu: agrupa commits abans de publicar

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, rebase  
**Llista:** Píndoles de Git, posició 27  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/26-rebase.mp4`  
**Subtítols:** `26-rebase/output/26-rebase.ca.srt`  
**Miniatura:** `26-rebase/output/portada.png`
