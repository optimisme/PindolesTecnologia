# YouTube · lliçó 31

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (62/100 caràcters)

```text
Forks i upstream: una còpia pròpia al dia · Píndoles de Git 31
```

**Descripció**

```text
Relacionar el projecte original, el [[fork]] i el clon local, i mantenir el [[fork]] al dia amb l’original.

Punt de partida: Volem contribuir a un projecte d’una altra persona, on no tenim permís per publicar.

Ordres que surten al vídeo:
  git clone <URL-del-fork> HelloGit
  cd HelloGit
  git remote add upstream <URL-original>
  git remote -v
  git fetch upstream
  git merge --ff-only upstream/main
  git push origin main

Practica-ho: Fes un fork d’un projecte de pràctiques, clona’l i afegeix-hi el remot upstream. Comprova les dues adreces abans de continuar.
Script per preparar el mateix punt de partida: Git/practiques/31-forks-upstream.sh

Capítols:
0:00 Capçalera i presentació
0:32 Tres repositoris
0:50 Creem el fork
1:05 $ git clone <URL-del-fork> HelloGit
1:35 $ cd HelloGit
1:49 $ git remote add upstream <URL-original>
2:35 $ git remote -v
2:57 L’original avança
3:13 $ git fetch upstream
3:43 $ git merge --ff-only upstream/main
4:13 $ git push origin main
4:44 Resum final
5:14 Pràctica final

Lliçó anterior: 30 · Pull request: revisa, actualitza i integra
Lliçó següent: 32 · Forks: contribueix al projecte original

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, forks  
**Llista:** Píndoles de Git, posició 32  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/31-forks-upstream.mp4`  
**Subtítols:** `31-forks-upstream/output/31-forks-upstream.ca.srt`  
**Miniatura:** `31-forks-upstream/output/portada.png`
