# Píndoles de Git

Lliçons curtes de Git en català, amb locució sintètica, animacions generades amb codi
i muntatge amb FFmpeg. El contingut de cada lliçó és a `NN-nom/llico.yaml`; tota la
resta (guions, sortides reals, scripts de pràctica i fitxes de YouTube) es genera i es
comprova a partir d’aquí.

## Estat

- **32 lliçons**, numerades del 0 al 31. L’ordre és a [serie.yaml](serie.yaml).
- Tots els guions estan revisats i compilats: [GUIONS.md](GUIONS.md) n’indica escenes,
  passos, paraules i durada estimada (de 2½ a 5½ minuts, uns 158 minuts en total).
- Totes les ordres de les lliçons pràctiques s’han executat en repositoris temporals i
  les afirmacions del guió s’han comprovat ([eines/repeticio.py](eines/repeticio.py)).
  Les sortides i els identificadors que es veuran a la pantalla són els reals.
- **Cap vídeo de la nova numeració està produït encara.** Els vídeos anteriors (amb la
  numeració antiga) són a [arxiu/produccio-anterior](arxiu/produccio-anterior/).
  Les lliçons 0 i 3 conserven la caché de veu aprovada: només caldrà sintetitzar de nou
  la presentació («Tercera lliçó…») i la frase final de la lliçó 0.

| Lliçó | Tema | Guió | Pràctica | YouTube |
| ---: | --- | --- | --- | --- |
| 0 | Introducció a Git | [guió](00-introduccio/guio.md) | — | [fitxa](00-introduccio/youtube.md) |
| 1 | Configuració inicial *(nova)* | [guió](01-configuracio/guio.md) | — | [fitxa](01-configuracio/youtube.md) |
| 2 | Connectar amb GitHub *(nova)* | [guió](02-github/guio.md) | [script](practiques/02-github.sh) | [fitxa](02-github/youtube.md) |
| 3 | El primer commit | [guió](03-primer-commit/guio.md) | [script](practiques/03-primer-commit.sh) | [fitxa](03-primer-commit/youtube.md) |
| 4 | Els tres estats | [guió](04-tres-estats/guio.md) | [script](practiques/04-tres-estats.sh) | [fitxa](04-tres-estats/youtube.md) |
| 5 | Llegir l’historial *(nova)* | [guió](05-historial/guio.md) | [script](practiques/05-historial.sh) | [fitxa](05-historial/youtube.md) |
| 6 | Add interactiu | [guió](06-add-interactiu/guio.md) | [script](practiques/06-add-interactiu.sh) | [fitxa](06-add-interactiu/youtube.md) |
| 7 | Gitignore | [guió](07-gitignore/guio.md) | [script](practiques/07-gitignore.sh) | [fitxa](07-gitignore/youtube.md) |
| 8 | Branques | [guió](08-branques/guio.md) | [script](practiques/08-branques.sh) | [fitxa](08-branques/youtube.md) |
| 9 | Merge | [guió](09-merge/guio.md) | [script](practiques/09-merge.sh) | [fitxa](09-merge/youtube.md) |
| 10 | Conflictes | [guió](10-conflictes/guio.md) | [script](practiques/10-conflictes.sh) | [fitxa](10-conflictes/youtube.md) |
| 11 | Clone *(dividida)* | [guió](11-clone/guio.md) | [script](practiques/11-clone.sh) | [fitxa](11-clone/youtube.md) |
| 12 | Pull i push *(dividida)* | [guió](12-pull-push/guio.md) | [script](practiques/12-pull-push.sh) | [fitxa](12-pull-push/youtube.md) |
| 13 | Fetch | [guió](13-fetch/guio.md) | [script](practiques/13-fetch.sh) | [fitxa](13-fetch/youtube.md) |
| 14 | Stash | [guió](14-stash/guio.md) | [script](practiques/14-stash.sh) | [fitxa](14-stash/youtube.md) |
| 15 | Restore | [guió](15-restore/guio.md) | [script](practiques/15-restore.sh) | [fitxa](15-restore/youtube.md) |
| 16 | Amend | [guió](16-amend/guio.md) | [script](practiques/16-amend.sh) | [fitxa](16-amend/youtube.md) |
| 17 | Reset | [guió](17-reset/guio.md) | [script](practiques/17-reset.sh) | [fitxa](17-reset/youtube.md) |
| 18 | Reflog | [guió](18-reflog/guio.md) | [script](practiques/18-reflog.sh) | [fitxa](18-reflog/youtube.md) |
| 19 | Revert | [guió](19-revert/guio.md) | [script](practiques/19-revert.sh) | [fitxa](19-revert/youtube.md) |
| 20 | Tags | [guió](20-tags/guio.md) | [script](practiques/20-tags.sh) | [fitxa](20-tags/youtube.md) |
| 21 | Rebase | [guió](21-rebase/guio.md) | [script](practiques/21-rebase.sh) | [fitxa](21-rebase/youtube.md) |
| 22 | Rebase interactiu | [guió](22-rebase-interactiu/guio.md) | [script](practiques/22-rebase-interactiu.sh) | [fitxa](22-rebase-interactiu/youtube.md) |
| 23 | Cherry-pick | [guió](23-cherry-pick/guio.md) | [script](practiques/23-cherry-pick.sh) | [fitxa](23-cherry-pick/youtube.md) |
| 24 | Pull request: proposar *(dividida)* | [guió](24-pull-request-obrir/guio.md) | [script](practiques/24-pull-request-obrir.sh) | [fitxa](24-pull-request-obrir/youtube.md) |
| 25 | Pull request: revisar i integrar *(dividida)* | [guió](25-pull-request-revisar/guio.md) | [script](practiques/25-pull-request-revisar.sh) | [fitxa](25-pull-request-revisar/youtube.md) |
| 26 | Forks i upstream *(dividida)* | [guió](26-forks-upstream/guio.md) | [script](practiques/26-forks-upstream.sh) | [fitxa](26-forks-upstream/youtube.md) |
| 27 | Contribuir des d’un fork *(dividida)* | [guió](27-forks-contribuir/guio.md) | [script](practiques/27-forks-contribuir.sh) | [fitxa](27-forks-contribuir/youtube.md) |
| 28 | Blame | [guió](28-blame/guio.md) | [script](practiques/28-blame.sh) | [fitxa](28-blame/youtube.md) |
| 29 | Bisect | [guió](29-bisect/guio.md) | [script](practiques/29-bisect.sh) | [fitxa](29-bisect/youtube.md) |
| 30 | Worktree | [guió](30-worktree/guio.md) | [script](practiques/30-worktree.sh) | [fitxa](30-worktree/youtube.md) |
| 31 | Hooks | [guió](31-hooks/guio.md) | [script](practiques/31-hooks.sh) | [fitxa](31-hooks/youtube.md) |

Correspondència amb la numeració anterior: 0→0, 1→3, 2→8, 3→4, 4→11 i 12, 5→9, 6→10,
7→21, 8→14, 9→15, 10→19, 11→17, 12→18, 13→7, 14→20, 15→23, 16→24 i 25, 17→28, 18→29,
19→16, 20→13, 21→26 i 27, 22→22, 23→6, 24→30, 25→31. El detall i els motius són a
[REVISIO_DIDACTICA.md](REVISIO_DIDACTICA.md).

## Carpetes

```text
serie.yaml            Ordre de les lliçons, veu, termes anglesos, plantilles d’ordres
NN-nom/llico.yaml     Contingut editable de la lliçó (únic fitxer que s’edita a mà)
NN-nom/execucio.json  Generat: sortides reals i estat de cada pas de l’exemple
NN-nom/guio.json      Generat: entrada del muntatge (escenes, passos, idiomes, pauses)
NN-nom/guio.md        Generat: guió per llegir i revisar
NN-nom/youtube.md     Generat: títol, descripció, capítols i etiquetes
NN-nom/exemples/      Fitxers complets que la lliçó mostra (quan n’hi ha)
NN-nom/output/        Produït: subtítols, narració, portada i informes de la lliçó
output/               Produït: els vídeos finals de la sèrie (NN-nom.mp4)
practiques/NN-nom.sh  Generat: crea el punt de partida del vídeo per practicar
eines/                Repetició, escenes, scripts de pràctica, render i vistes fetes a mida
capcalera/, veu/      Decisions aprovades de capçalera i veu
arxiu/                Producció anterior, motor anterior i proves descartades
```

## Ordres

Des de l’arrel del projecte, amb l’entorn de `README.md` preparat:

```bash
.venv/bin/python Git/eines/repeticio.py Git          # executa i comprova els exemples
.venv/bin/python -m motor.guions Git                 # compila i revisa els guions
.venv/bin/python Git/eines/practiques.py Git         # scripts de pràctica
.venv/bin/python Git/eines/practiques.py Git --prova # els executa i els compara amb la repetició
.venv/bin/python -m motor.youtube Git                # fitxes de YouTube
.venv/bin/python Git/eines/escenes.py Git 08-branques # imatges fixes de revisió dels visuals
.venv/bin/python -m unittest discover -s motor/proves -t .
```

Per produir un vídeo (genera àudio i vídeo, necessita `.env`):

```bash
.venv/bin/python Git/eines/render.py Git/08-branques --audio-only
.venv/bin/python Git/eines/render.py Git/08-branques
```

El vídeo final queda a [output/](output/README.md) amb el nom de la lliçó
(`output/08-branques.mp4`); la resta de fitxers produïts, a `08-branques/output/`.
El render s’atura si el guió o la repetició no estan al dia. Després de produir,
`python -m motor.youtube Git` afegeix els capítols reals a la fitxa.

Per canviar l’ordre de la sèrie: editar `llicons` a `serie.yaml`, executar
`python -m motor.serie Git --renumera` i tornar a executar les ordres anteriors.

## Guia d’estil

Guia acordada per a totes les lliçons. El compilador en comprova automàticament les
parts marcades amb ✔︎.

### Capçalera i presentació

- Capçalera comuna de **4 segons** amb música, número, títol i subtítol. Generador:
  [motor/capcalera.py](../motor/capcalera.py); títols a cada `llico.yaml` (`capcalera`).
- Després de la música, la veu anuncia el número i el títol: «Vuitena lliçó. Branques.» ✔︎

### Veu i idiomes

- Veu **en-US-AndrewMultilingualNeural** amb SSML explícit: català **+5%**, anglès **+0%**,
  pausa de **500 ms** en cada canvi d’idioma. Configuració aprovada a [veu/andrew](veu/andrew/README.md).
- Els termes de `termes_angles` (i el text entre `[[ ]]`) es llegeixen en anglès; el
  compilador falla si algun queda dins d’un fragment català. ✔︎
- Els identificadors escrits sense accent (`salutacio`) es pronuncien en català. ✔︎
- No es llegeixen en veu alta hashes, rutes, `~`, `__`, intervals de lletres ni noms com
  V1/V2: la pantalla mostra el detall i la veu en diu el sentit. ✔︎

### Guies visuals

- Mostrar el problema i el punt de partida: carpeta, branca activa, fitxers i estat.
- Comanda completa visible; subratllat progressiu de l’acció, cada paràmetre i el valor;
  execució després de l’explicació i resultat amb pausa pròpia.
- Les sortides de la terminal són les reals de la repetició. Quan contenen rutes locals de
  la prova o depenen d’un servei extern, es marquen com a «sortida de mostra». ✔︎
- Fer servir text o símbols a més del color. Els subtítols no tapen la zona de treball.

### Explicar les ordres

- Cada opció s’explica la primera vegada que apareix a la sèrie; després es pot fer
  servir la versió breu de la plantilla (`status-breu`, `commit-breu`...). ✔︎
- `-m` s’explica abans del missatge entre cometes. ✔︎

### Pauses

- Una idea per pas; pauses de 1,5 a 4 segons sense locució, ampliables per llegir. ✔︎
- Les lliçons no fan preguntes. ✔︎

### Resum i pràctica

- Tres idees finals i una acció de pràctica. ✔︎ L’script `practiques/NN-nom.sh` crea el
  mateix punt de partida del vídeo i s’enllaça a la descripció de YouTube.

### Criteris complementaris

- **Claredat abans que durada**, però cada vídeo amb un sol objectiu: les lliçons llargues
  s’han dividit en dues.
- **Vídeos autònoms:** la locució explica el punt de partida i no remet a materials externs. ✔︎
- **Error habitual amb explicació** quan ajuda: per exemple, `pull --ff-only` amb històries
  divergents o el hook que revisa la preparació i no l’editor.
- **Exemples coherents:** carpeta `HelloGit`, autoria `Anna Puig`, `v1.0` com a primera
  entrega i identificadors reals per lliçó.

## Fonts del contingut

- [Pro Git: enregistrar canvis](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository),
  [branques](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell),
  [remots](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes),
  [etiquetes](https://git-scm.com/book/en/v2/Git-Basics-Tagging) i
  [configuració inicial](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
- Referència de Git: [config](https://git-scm.com/docs/git-config), [log](https://git-scm.com/docs/git-log),
  [show](https://git-scm.com/docs/git-show), [diff](https://git-scm.com/docs/git-diff),
  [add](https://git-scm.com/docs/git-add), [merge](https://git-scm.com/docs/git-merge),
  [rebase](https://git-scm.com/docs/git-rebase), [stash](https://git-scm.com/docs/git-stash),
  [restore](https://git-scm.com/docs/git-restore), [revert](https://git-scm.com/docs/git-revert),
  [reset](https://git-scm.com/docs/git-reset), [reflog](https://git-scm.com/docs/git-reflog),
  [gitignore](https://git-scm.com/docs/gitignore), [check-ignore](https://git-scm.com/docs/git-check-ignore),
  [rm](https://git-scm.com/docs/git-rm), [tag](https://git-scm.com/docs/git-tag),
  [cherry-pick](https://git-scm.com/docs/git-cherry-pick), [blame](https://git-scm.com/docs/git-blame),
  [bisect](https://git-scm.com/docs/git-bisect), [commit](https://git-scm.com/docs/git-commit),
  [fetch](https://git-scm.com/docs/git-fetch), [pull](https://git-scm.com/docs/git-pull),
  [worktree](https://git-scm.com/docs/git-worktree), [hooks](https://git-scm.com/docs/githooks)
- GitHub: [GitHub CLI](https://cli.github.com/manual/gh_auth_login),
  [crear un fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo),
  [configurar upstream](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-repository-for-a-fork),
  [pull request des d’un fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork),
  [crear](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) i
  [fusionar una pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request)
- Python: [compile](https://docs.python.org/3/library/functions.html#compile)
