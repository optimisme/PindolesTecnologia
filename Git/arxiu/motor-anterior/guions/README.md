# Guions revisats · lliçons 2–25

Els 24 guions estan reescrits amb explicacions per passos, comandes desglossades, pauses i cap pregunta.
Aquesta revisió només modifica documents. Les locucions i els vídeos existents es conserven.
Cada carpeta té `guio-revisat.md` per llegir i `guio-revisat.json` amb els passos i idiomes explícits.
Els `episodi.json` i `guio.md` publicats es mantenen vinculats als mitjans actuals.
La futura producció haurà d’adaptar els visuals a aquests passos i obtenir els temps reals del nou àudio.

| Lliçó | Guió revisat | Escenes | Passos | Paraules |
| --- | --- | ---: | ---: | ---: |
| 02-branques | [Llegir](../02-branques/guio-revisat.md) | 14 | 40 | 506 |
| 03-estats | [Llegir](../03-estats/guio-revisat.md) | 14 | 41 | 508 |
| 04-sincronitzacio | [Llegir](../04-sincronitzacio/guio-revisat.md) | 22 | 65 | 733 |
| 05-merge | [Llegir](../05-merge/guio-revisat.md) | 10 | 29 | 350 |
| 06-conflictes | [Llegir](../06-conflictes/guio-revisat.md) | 13 | 35 | 456 |
| 07-rebase | [Llegir](../07-rebase/guio-revisat.md) | 14 | 40 | 472 |
| 08-stash | [Llegir](../08-stash/guio-revisat.md) | 13 | 38 | 467 |
| 09-restore | [Llegir](../09-restore/guio-revisat.md) | 10 | 27 | 351 |
| 10-revert | [Llegir](../10-revert/guio-revisat.md) | 11 | 33 | 379 |
| 11-reset | [Llegir](../11-reset/guio-revisat.md) | 10 | 24 | 336 |
| 12-reflog | [Llegir](../12-reflog/guio-revisat.md) | 11 | 34 | 398 |
| 13-gitignore | [Llegir](../13-gitignore/guio-revisat.md) | 12 | 36 | 496 |
| 14-tags | [Llegir](../14-tags/guio-revisat.md) | 14 | 49 | 527 |
| 15-cherry-pick | [Llegir](../15-cherry-pick/guio-revisat.md) | 15 | 49 | 513 |
| 16-pull-requests | [Llegir](../16-pull-requests/guio-revisat.md) | 20 | 64 | 719 |
| 17-blame | [Llegir](../17-blame/guio-revisat.md) | 10 | 31 | 343 |
| 18-bisect | [Llegir](../18-bisect/guio-revisat.md) | 14 | 44 | 454 |
| 19-amend | [Llegir](../19-amend/guio-revisat.md) | 11 | 37 | 424 |
| 20-fetch | [Llegir](../20-fetch/guio-revisat.md) | 10 | 35 | 361 |
| 21-forks | [Llegir](../21-forks/guio-revisat.md) | 20 | 67 | 687 |
| 22-rebase-interactiu | [Llegir](../22-rebase-interactiu/guio-revisat.md) | 17 | 52 | 588 |
| 23-add-interactiu | [Llegir](../23-add-interactiu/guio-revisat.md) | 13 | 41 | 455 |
| 24-worktree | [Llegir](../24-worktree/guio-revisat.md) | 16 | 58 | 596 |
| 25-hooks | [Llegir](../25-hooks/guio-revisat.md) | 15 | 39 | 549 |

## Edició i comprovació

`contingut.py` conté el text editorial i les instruccions de cada lliçó.
Des de la carpeta `vids`, `python3 guions/compila.py` actualitza només els guions revisats.
No carrega credencials, no contacta cap sintetitzador i no modifica les carpetes audio o output.
Per validar els idiomes, les opcions, els subtítols i els 748 arxius conservats: `.venv/bin/python guions/verifica.py`.
