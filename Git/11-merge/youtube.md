# YouTube · lliçó 11

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (50/100 caràcters)

```text
Merge: porta les idees a main · Píndoles de Git 11
```

**Descripció**

```text
Integrar dues branques a [[main]] i distingir l’avançament directe de la fusió amb dos pares.

Punt de partida: Continuem amb les dues idees de la lliçó anterior: una branca saluda per nom i l’altra afegeix un comiat. Totes dues estan confirmades i provades, i main encara té la versió original.

Ordres que surten al vídeo:
  git switch main
  git branch --show-current
  git merge --ff-only salutacio
  git merge --ff-only comiat
  git merge comiat
  python3 helloGit.py
  git branch -d salutacio comiat

Practica-ho: En un repositori de pràctiques, crea dues branques des de main amb canvis en línies diferents. Integra la primera amb avançament directe i la segona amb una fusió. Executa el programa i esborra les dues branques.
Script per preparar el mateix punt de partida: Git/practiques/11-merge.sh

Capítols:
0:00 Capçalera i presentació
0:37 Origen i destinació
0:54 $ git switch main
1:25 $ git branch --show-current
1:50 $ git merge --ff-only salutacio
2:42 $ git merge --ff-only comiat
3:07 $ git merge comiat
3:46 $ python3 helloGit.py
4:11 $ git branch -d salutacio comiat
4:56 Resum final
5:22 Pràctica final

Lliçó anterior: 10 · Branques: prova idees sense tocar main
Lliçó següent: 12 · Conflictes: dues edicions, una decisió

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, merge  
**Llista:** Píndoles de Git, posició 12  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/11-merge.mp4`  
**Subtítols:** `11-merge/output/11-merge.ca.srt`  
**Miniatura:** `11-merge/output/portada.png`
