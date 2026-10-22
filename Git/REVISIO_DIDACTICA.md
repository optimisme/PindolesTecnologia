# Revisió didàctica de la sèrie

**21 d’octubre de 2026 · segona revisió.** S’han aplicat les recomanacions de l’auditoria:
reordenació, lliçons noves i dividides, correccions de contingut i exemples executats.
Després s’hi han afegit sis lliçons més. No s’ha generat cap àudio ni vídeo. La primera revisió (24 guions reescrits) és a
[arxiu/revisio-didactica-2026-10-20.md](arxiu/revisio-didactica-2026-10-20.md).

## Ordre nou

Primer el treball local bàsic, després branques, sincronització, desfer canvis, història
avançada i col·laboració:

| Bloc | Lliçons |
| --- | --- |
| Preparació | 0 Introducció · 1 Configuració · 2 Connectar amb GitHub |
| Treball local | 3 Primer commit · 4 Tres estats · 5 Esborrar i reanomenar · 6 Llegir l’historial · 7 Add interactiu · 8 Gitignore · 9 Finals de línia |
| Branques | 10 Branques · 11 Merge · 12 Conflictes |
| Sincronització | 13 Clone · 14 Pull i push · 15 Pull amb històries divergents · 16 Fetch · 17 Branques remotes |
| Desfer i recuperar | 18 Stash · 19 Restore · 20 Amend · 21 Reset · 22 Reflog · 23 Revert · 24 Quina ordre triar |
| Història | 25 Tags · 26 Rebase · 27 Rebase interactiu · 28 Cherry-pick |
| Col·laboració | 29–30 Pull requests · 31–32 Forks |
| Investigar i automatitzar | 33 Cercar a l’historial · 34 Blame · 35 Bisect · 36 Worktree · 37 Hooks |

Motius principals: els tres estats, l’add interactiu i el gitignore són treball local
bàsic i ara precedeixen les branques; fetch queda al costat de pull; amend s’agrupa amb
les eines per desfer; rebase passa després de dominar merge i conflictes.

## Lliçons noves

- **1 · Configuració inicial.** `git --version` (cal 2.23 o posterior per a `switch` i
  `restore`), nom i correu, branca inicial `main`, editor (`code --wait`) i llista de la
  configuració. Explica què fer en un ordinador compartit i que Git pot respondre en català.
- **2 · Connectar amb GitHub.** Autorització amb GitHub CLI (`gh auth login` i `status`),
  alternativa del gestor de credencials de Windows, repositori buit i primer clon.
- **6 · Llegir l’historial.** `log`, `log --oneline`, `HEAD` i `HEAD~1`, `show` i `diff`
  entre versions. Introdueix la notació que fan servir reset i rebase interactiu.

### Ampliació: sis lliçons més

- **5 · Esborrar i reanomenar fitxers.** `git rm`, `git mv`, la R i la D de l’estat breu, i
  l’error habitual d’esborrar des de l’explorador (la D a la segona columna).
- **9 · Finals de línia.** Diferència entre CRLF i LF, un fitxer que surt modificat sense
  canvis visibles, `.gitattributes` amb `* text=auto`, `git add --renormalize .` i
  `core.autocrlf` a Windows.
- **15 · Quan pull s’atura.** Continua l’error de `--ff-only`: integrar amb `pull --no-rebase`
  (fusió) o amb `pull --rebase`, i triar l’opció per defecte amb `pull.rebase`.
- **17 · Branques remotes.** `branch -vv`, `fetch --prune`, `branch -r`, `switch` a una
  branca que només és al servidor, i esborrar-ne una amb `push origin --delete`.
- **24 · Desfer canvis: quina ordre triar.** Repàs sense ordres noves: esquema de decisió
  entre restore, stash, amend, reset, reflog i revert, i la regla de no reescriure
  l’historial compartit.
- **33 · Cercar a l’historial.** `log --author`, `log -- fitxer`, `log --grep` i `log -S`.

## Lliçons dividides

Les tres més llargues (més de 700 paraules) s’han dividit perquè cada vídeo tingui un
sol objectiu: Sincronització → Clone (13) i Pull i push (14); Pull requests → proposar (29)
i revisar i integrar (30); Forks → fork i upstream (31) i contribuir (32).

## Correccions aplicades a totes les lliçons

- **Punt de partida parlat.** El text tècnic d’`inici` ja no es llegeix: cada lliçó té una
  frase pensada per a l’alumnat (`inici_parlat`).
- **Idioma de la veu.** Ara el compilador marca automàticament els termes anglesos i falla
  si algun queda en català (abans: «Cherry pick», «Pull requests», «Git ignore», «fork»,
  «diff», «show» o «log»).
- **Res il·legible en veu alta.** Cap hash, V1/V2/V3, «C prima», intervals de lletres ni
  noms de carpetes amb guions baixos a la locució; el compilador ho comprova.
- **Identificadors reals.** Els hashes de pantalla surten de la repetició i són coherents
  dins de cada lliçó (abans es repetien `c95f4a7` i `d04f7a2` en lliçons diferents).
- **Menys repeticions.** Les opcions ja explicades a la sèrie es fan servir amb plantilles
  breus (`status-breu`, `add-breu`, `commit-breu`).
- **Editor.** Les lliçons que obren un editor (merge divergent, rebase, cherry-pick i rebase
  interactiu) parteixen de l’editor configurat a la lliçó 1 i expliquen que cal desar i tancar.
- **Coherència.** Carpeta `HelloGit` a totes les lliçons; `v1.0` és sempre la primera entrega
  (al commit B, a Tags i a Bisect); autoria `Ermessenda Carcassona`.
- **Pràctica reproduïble.** Cada lliçó pràctica té `practiques/NN-nom.sh`, que crea el mateix
  punt de partida del vídeo amb remots locals.

## Correccions de contingut

- **Branques i merge:** la lliçó 10 crea dues branques des de `main` (salutació i comiat, en línies
  diferents) i en compara les tres versions; la 11 integra la primera amb avançament directe, mostra
  que `--ff-only` s’atura amb la segona i la fusiona amb un commit de dos pares. Després s’esborren
  les dues branques amb `branch -d`.
- **Conflictes:** el contingut dels marcadors es comprova exactament; l’alternativa
  `merge --abort` s’executa des d’un conflicte real.
- **Gitignore:** la carpeta `__pycache__/` apareix de debò perquè el programa importa un
  mòdul; el registre nou el genera el programa. `git ls-files` mostra que la regla no retira
  el fitxer ja seguit. També cobreix els secrets (`.env`), `status --ignored`, on s’aplica cada
  patró, les excepcions amb `!` (i la trampa de la carpeta ignorada), què passa a l’equip i a
  l’historial en deixar de seguir un fitxer i les regles personals.
- **Pull i push:** nou cas d’error habitual, `pull --ff-only` quan les dues còpies han divergit.
- **Restore:** l’alternativa de tres versions s’executa i es comprova.
- **Reflog:** `--decorate` explícit, perquè sense terminal Git no mostra els noms de branca.
- **Bisect:** seqüència real de proves (E, D i C), explicació de `HEAD` separat i `v1.0` a B.
- **Hooks:** el control mostra un missatge clar amb la línia de l’error en lloc d’una traça
  de Python, i s’explica `--no-verify`.
- **Add interactiu:** «Adéu!» amb accent; s’explica l’opció de dividir un bloc.
- **Pull requests:** després d’integrar, `pull --ff-only` i esborrar la branca local i remota.

## Comprovació

Totes les lliçons s’executen amb `eines/repeticio.py`: 349 etapes, amb les
afirmacions de cada guió comprovades (branques, pares, contingut, estat, sortides).
Els 35 scripts de pràctica s’executen i es comparen amb la repetició. Les mateixes
comprovacions corren a GitHub Actions a cada canvi.
