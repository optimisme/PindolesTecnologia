# Revisió didàctica de la sèrie

**21 d’octubre de 2026 · segona revisió.** S’han aplicat les recomanacions de l’auditoria:
reordenació, lliçons noves i dividides, correccions de contingut i exemples executats.
No s’ha generat cap àudio ni vídeo. La primera revisió (24 guions reescrits) és a
[arxiu/revisio-didactica-2026-10-20.md](arxiu/revisio-didactica-2026-10-20.md).

## Ordre nou

Primer el treball local bàsic, després branques, sincronització, desfer canvis, història
avançada i col·laboració:

| Bloc | Lliçons |
| --- | --- |
| Preparació | 0 Introducció · 1 Configuració *(nova)* · 2 Connectar amb GitHub *(nova)* |
| Treball local | 3 Primer commit · 4 Tres estats · 5 Llegir l’historial *(nova)* · 6 Add interactiu · 7 Gitignore |
| Branques | 8 Branques · 9 Merge · 10 Conflictes |
| Sincronització | 11 Clone · 12 Pull i push · 13 Fetch |
| Desfer i recuperar | 14 Stash · 15 Restore · 16 Amend · 17 Reset · 18 Reflog · 19 Revert |
| Història | 20 Tags · 21 Rebase · 22 Rebase interactiu · 23 Cherry-pick |
| Col·laboració | 24–25 Pull requests · 26–27 Forks |
| Investigar i automatitzar | 28 Blame · 29 Bisect · 30 Worktree · 31 Hooks |

Motius principals: els tres estats, l’add interactiu i el gitignore són treball local
bàsic i ara precedeixen les branques; fetch queda al costat de pull; amend s’agrupa amb
les eines per desfer; rebase passa després de dominar merge i conflictes.

## Lliçons noves

- **1 · Configuració inicial.** `git --version` (cal 2.23 o posterior per a `switch` i
  `restore`), nom i correu, branca inicial `main`, editor (`code --wait`) i llista de la
  configuració. Explica què fer en un ordinador compartit i que Git pot respondre en català.
- **2 · Connectar amb GitHub.** Autorització amb GitHub CLI (`gh auth login` i `status`),
  alternativa del gestor de credencials de Windows, repositori buit i primer clon.
- **5 · Llegir l’historial.** `log`, `log --oneline`, `HEAD` i `HEAD~1`, `show` i `diff`
  entre versions. Introdueix la notació que fan servir reset i rebase interactiu.

## Lliçons dividides

Les tres més llargues (més de 700 paraules) s’han dividit perquè cada vídeo tingui un
sol objectiu: Sincronització → Clone (11) i Pull i push (12); Pull requests → proposar (24)
i revisar i integrar (25); Forks → fork i upstream (26) i contribuir (27).

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
  (al commit B, a Tags i a Bisect); autoria `Anna Puig`.
- **Pràctica reproduïble.** Cada lliçó pràctica té `practiques/NN-nom.sh`, que crea el mateix
  punt de partida del vídeo amb remots locals.

## Correccions de contingut

- **Merge:** després de l’avançament directe, s’esborra la branca integrada amb `branch -d`.
- **Conflictes:** el contingut dels marcadors es comprova exactament; l’alternativa
  `merge --abort` s’executa des d’un conflicte real.
- **Gitignore:** la carpeta `__pycache__/` apareix de debò perquè el programa importa un
  mòdul; el registre nou el genera el programa. `git ls-files` mostra que la regla no retira
  el fitxer ja seguit.
- **Pull i push:** nou cas d’error habitual, `pull --ff-only` quan les dues còpies han divergit.
- **Restore:** l’alternativa de tres versions s’executa i es comprova.
- **Reflog:** `--decorate` explícit, perquè sense terminal Git no mostra els noms de branca.
- **Bisect:** seqüència real de proves (E, D i C), explicació de `HEAD` separat i `v1.0` a B.
- **Hooks:** el control mostra un missatge clar amb la línia de l’error en lloc d’una traça
  de Python, i s’explica `--no-verify`.
- **Add interactiu:** «Adéu!» amb accent; s’explica l’opció de dividir un bloc.
- **Pull requests:** després d’integrar, `pull --ff-only` i esborrar la branca local i remota.

## Comprovació

Totes les lliçons pràctiques s’executen amb `eines/repeticio.py`: 303 etapes, amb les
afirmacions de cada guió comprovades (branques, pares, contingut, estat, sortides).
Els 30 scripts de pràctica s’executen i es comparen amb la repetició. Les mateixes
comprovacions corren a GitHub Actions a cada canvi.
