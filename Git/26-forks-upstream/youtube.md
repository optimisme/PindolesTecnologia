# YouTube · lliçó 26

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (62/100 caràcters)

```text
Forks i upstream: una còpia pròpia al dia · Píndoles de Git 26
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
Script per preparar el mateix punt de partida: Git/practiques/26-forks-upstream.sh

Lliçó anterior: 25 · Pull request: revisa, actualitza i integra
Lliçó següent: 27 · Forks: contribueix al projecte original

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, forks  
**Llista:** Píndoles de Git, posició 27  
**Idioma del vídeo i dels subtítols:** català  
**Subtítols:** `output/26-forks-upstream.ca.srt`  
**Miniatura:** `output/portada.png`

> Encara no s’ha produït el vídeo: els capítols s’afegiran quan existeixi `output/produccio.json`.
