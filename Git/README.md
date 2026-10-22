# Píndoles de Git

Lliçons curtes de Git en català, amb locució sintètica, animacions generades amb codi
i muntatge amb FFmpeg. El contingut de cada lliçó és a `NN-nom/llico.yaml`; tota la
resta (guions, sortides reals, scripts de pràctica i fitxes de YouTube) es genera i es
comprova a partir d’aquí.

## Estat

- **38 lliçons**, numerades del 0 al 37. L’ordre és a [serie.yaml](serie.yaml).
- Tots els guions estan revisats i compilats: [GUIONS.md](GUIONS.md) n’indica escenes,
  passos, paraules i durada estimada (de 3 a 6½ minuts, uns 184 minuts en total).
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
| 4 | Desar, preparar i confirmar | [guió](04-tres-estats/guio.md) | [script](practiques/04-tres-estats.sh) | [fitxa](04-tres-estats/youtube.md) |
| 5 | Esborrar i reanomenar fitxers *(nova)* | [guió](05-fitxers/guio.md) | [script](practiques/05-fitxers.sh) | [fitxa](05-fitxers/youtube.md) |
| 6 | Llegir l’historial *(nova)* | [guió](06-historial/guio.md) | [script](practiques/06-historial.sh) | [fitxa](06-historial/youtube.md) |
| 7 | Add interactiu | [guió](07-add-interactiu/guio.md) | [script](practiques/07-add-interactiu.sh) | [fitxa](07-add-interactiu/youtube.md) |
| 8 | Gitignore | [guió](08-gitignore/guio.md) | [script](practiques/08-gitignore.sh) | [fitxa](08-gitignore/youtube.md) |
| 9 | Finals de línia *(nova)* | [guió](09-finals-linia/guio.md) | [script](practiques/09-finals-linia.sh) | [fitxa](09-finals-linia/youtube.md) |
| 10 | Branques | [guió](10-branques/guio.md) | [script](practiques/10-branques.sh) | [fitxa](10-branques/youtube.md) |
| 11 | Merge | [guió](11-merge/guio.md) | [script](practiques/11-merge.sh) | [fitxa](11-merge/youtube.md) |
| 12 | Conflictes | [guió](12-conflictes/guio.md) | [script](practiques/12-conflictes.sh) | [fitxa](12-conflictes/youtube.md) |
| 13 | Clone *(dividida)* | [guió](13-clone/guio.md) | [script](practiques/13-clone.sh) | [fitxa](13-clone/youtube.md) |
| 14 | Pull i push *(dividida)* | [guió](14-pull-push/guio.md) | [script](practiques/14-pull-push.sh) | [fitxa](14-pull-push/youtube.md) |
| 15 | Quan pull s’atura *(nova)* | [guió](15-pull-divergent/guio.md) | [script](practiques/15-pull-divergent.sh) | [fitxa](15-pull-divergent/youtube.md) |
| 16 | Fetch | [guió](16-fetch/guio.md) | [script](practiques/16-fetch.sh) | [fitxa](16-fetch/youtube.md) |
| 17 | Branques remotes *(nova)* | [guió](17-branques-remotes/guio.md) | [script](practiques/17-branques-remotes.sh) | [fitxa](17-branques-remotes/youtube.md) |
| 18 | Stash | [guió](18-stash/guio.md) | [script](practiques/18-stash.sh) | [fitxa](18-stash/youtube.md) |
| 19 | Restore | [guió](19-restore/guio.md) | [script](practiques/19-restore.sh) | [fitxa](19-restore/youtube.md) |
| 20 | Amend | [guió](20-amend/guio.md) | [script](practiques/20-amend.sh) | [fitxa](20-amend/youtube.md) |
| 21 | Reset | [guió](21-reset/guio.md) | [script](practiques/21-reset.sh) | [fitxa](21-reset/youtube.md) |
| 22 | Reflog | [guió](22-reflog/guio.md) | [script](practiques/22-reflog.sh) | [fitxa](22-reflog/youtube.md) |
| 23 | Revert | [guió](23-revert/guio.md) | [script](practiques/23-revert.sh) | [fitxa](23-revert/youtube.md) |
| 24 | Desfer canvis *(nova)* | [guió](24-desfer/guio.md) | — | [fitxa](24-desfer/youtube.md) |
| 25 | Tags | [guió](25-tags/guio.md) | [script](practiques/25-tags.sh) | [fitxa](25-tags/youtube.md) |
| 26 | Rebase | [guió](26-rebase/guio.md) | [script](practiques/26-rebase.sh) | [fitxa](26-rebase/youtube.md) |
| 27 | Rebase interactiu | [guió](27-rebase-interactiu/guio.md) | [script](practiques/27-rebase-interactiu.sh) | [fitxa](27-rebase-interactiu/youtube.md) |
| 28 | Cherry-pick | [guió](28-cherry-pick/guio.md) | [script](practiques/28-cherry-pick.sh) | [fitxa](28-cherry-pick/youtube.md) |
| 29 | Pull request *(dividida)* | [guió](29-pull-request-obrir/guio.md) | [script](practiques/29-pull-request-obrir.sh) | [fitxa](29-pull-request-obrir/youtube.md) |
| 30 | Pull request *(dividida)* | [guió](30-pull-request-revisar/guio.md) | [script](practiques/30-pull-request-revisar.sh) | [fitxa](30-pull-request-revisar/youtube.md) |
| 31 | Forks i upstream *(dividida)* | [guió](31-forks-upstream/guio.md) | [script](practiques/31-forks-upstream.sh) | [fitxa](31-forks-upstream/youtube.md) |
| 32 | Forks *(dividida)* | [guió](32-forks-contribuir/guio.md) | [script](practiques/32-forks-contribuir.sh) | [fitxa](32-forks-contribuir/youtube.md) |
| 33 | Cercar a l’historial *(nova)* | [guió](33-cercar-historial/guio.md) | [script](practiques/33-cercar-historial.sh) | [fitxa](33-cercar-historial/youtube.md) |
| 34 | Blame | [guió](34-blame/guio.md) | [script](practiques/34-blame.sh) | [fitxa](34-blame/youtube.md) |
| 35 | Bisect | [guió](35-bisect/guio.md) | [script](practiques/35-bisect.sh) | [fitxa](35-bisect/youtube.md) |
| 36 | Worktree | [guió](36-worktree/guio.md) | [script](practiques/36-worktree.sh) | [fitxa](36-worktree/youtube.md) |
| 37 | Hooks | [guió](37-hooks/guio.md) | [script](practiques/37-hooks.sh) | [fitxa](37-hooks/youtube.md) |

Correspondència amb la numeració dels vídeos anteriors: 0→0, 1→3, 2→10, 3→4, 4→13 i 14,
5→11, 6→12, 7→26, 8→18, 9→19, 10→23, 11→21, 12→22, 13→8, 14→25, 15→28, 16→29 i 30,
17→34, 18→35, 19→20, 20→16, 21→31 i 32, 22→27, 23→7, 24→36, 25→37. El detall i els motius són a
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
.venv/bin/python Git/eines/escenes.py Git 10-branques # imatges fixes de revisió dels visuals
.venv/bin/python Git/eines/revisa_visuals.py Git     # textos fora de lloc, superposats o tallats
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
- **Exemples coherents:** carpeta `HelloGit`, autoria `Ermessenda Carcassona`, `v1.0` com a primera
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
