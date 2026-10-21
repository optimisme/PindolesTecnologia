# YouTube · lliçó 13

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (68/100 caràcters)

```text
Fetch: consulta els canvis abans d’integrar-los · Píndoles de Git 13
```

**Descripció**

```text
Descarregar, revisar i integrar les novetats del servidor en tres passos separats.

Punt de partida: La nostra còpia és al dia de l’última vegada que vam consultar el servidor. Mentrestant, una altra persona hi ha publicat un commit nou.

Ordres que surten al vídeo:
  git status --short
  git fetch origin
  git log --oneline main..origin/main
  git diff main origin/main -- helloGit.py
  git merge --ff-only origin/main
  python3 helloGit.py

Practica-ho: Amb dos clons de pràctiques, publica una novetat des d’un i fes fetch a l’altre. Compara main i origin/main abans d’integrar.
Script per preparar el mateix punt de partida: Git/practiques/13-fetch.sh

Lliçó anterior: 12 · Pull i push: dues còpies al dia
Lliçó següent: 14 · Stash: aparca la feina pendent

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, fetch  
**Llista:** Píndoles de Git, posició 14  
**Idioma del vídeo i dels subtítols:** català  
**Subtítols:** `output/13-fetch.ca.srt`  
**Miniatura:** `output/portada.png`

> Encara no s’ha produït el vídeo: els capítols s’afegiran quan existeixi `output/produccio.json`.
