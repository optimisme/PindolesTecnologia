# YouTube · lliçó 16

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (68/100 caràcters)

```text
Fetch: consulta els canvis abans d’integrar-los · Píndoles de Git 16
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
Script per preparar el mateix punt de partida: Git/practiques/16-fetch.sh

Capítols:
0:00 Capçalera i presentació
0:30 Una referència que no s’actualitza sola
0:49 $ git status --short
1:08 $ git fetch origin
1:40 $ git log --oneline main..origin/main
2:14 $ git diff main origin/main -- helloGit.py
2:44 $ git merge --ff-only origin/main
3:14 $ python3 helloGit.py
3:33 Resum final
4:02 Pràctica final

Lliçó anterior: 15 · Quan pull s’atura: històries divergents
Lliçó següent: 17 · Branques remotes: consultar, seguir i esborrar

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, fetch  
**Llista:** Píndoles de Git, posició 17  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/16-fetch.mp4`  
**Subtítols:** `16-fetch/output/16-fetch.ca.srt`  
**Miniatura:** `16-fetch/output/portada.png`
