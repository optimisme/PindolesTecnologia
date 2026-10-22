# Lliçó 36 · Worktree: corregeix main sense interrompre la feina

**Sèrie:** Píndoles de Git · **Capçalera:** WORKTREE — Dues carpetes, un historial compartit  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/36-worktree.sh`](../practiques/36-worktree.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Trenta-sisena lliçó. *Worktree*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a fer una correcció en una segona carpeta de treball sense tocar la feina pendent de la primera. *(pausa 2.5 s)*

Som a la branca salutació, a mitja feina. Ens demanen una correcció ràpida a *main* i no volem tocar el que tenim a mig fer. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Dues carpetes, preparacions separades

Un *worktree* és una segona carpeta de treball connectada al mateix repositori. Té els seus fitxers, la seva preparació i la seva branca activa. *(pausa 3 s)*

**Visual:** Dos espais, ORIGINAL a salutacio amb un canvi pendent i AUXILIAR encara inexistent.

## Terminal · `git worktree add -b correccio ../projecte-correccio main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git worktree add` | *git worktree add* crea la carpeta nova. | 2.5 s |
| `-b` | El guionet be crea una branca nova per a aquesta carpeta. | 2.5 s |
| `correccio` | És el nom de la branca de la correcció. | 2.5 s |
| `../projecte-correccio` | És el camí de la carpeta nova, al costat de l’original. | 2.5 s |
| `main` | És el punt de partida; la correcció comença a la versió de *main*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La carpeta auxiliar comença neta, a la branca correcció. L’original conserva l’edició pendent. *(pausa 3.5 s)*

Sortida real:

```text
HEAD is now at 0d6725b Afegeix una exclamacio
Preparing worktree (new branch 'correccio')
```

**Visual:** Crear la segona carpeta; el text de l’editor original no es mou.

## Terminal · `git worktree list`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git worktree list` | Consultem les carpetes connectades. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Cada línia mostra una carpeta i la seva branca activa. Encara treballem des de l’original. *(pausa 3.5 s)*

Sortida real:

```text
~/projecte           0d6725b [salutacio]
~/projecte-correccio 0d6725b [correccio]
```

**Visual:** Dues files amb camí i branca a la sortida real; indicador AQUÍ SOM a l’original.

## Terminal · `cd ../projecte-correccio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `cd` | Entrem a la carpeta auxiliar. | 2.5 s |
| `../projecte-correccio` | Els dos punts pugen a la carpeta superior i, des d’allà, entrem a la nova. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La terminal és a la carpeta de la correcció, que no té canvis pendents. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** AQUÍ SOM passa a l’auxiliar; l’editor original continua de referència.

## Fem només la correcció

Afegim una coma a la salutació original, desem i provem el programa en aquesta carpeta. *(pausa 3 s)*

**Visual:** Editor auxiliar amb print("Hello, Git!"). L’original continua amb print("Hola, Ermessenda!") sense confirmar.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Surt la salutació amb coma. La feina de l’altra carpeta continua al seu lloc. *(pausa 3.5 s)*

Sortida real:

```text
Hello, Git!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La correcció queda preparada només a la carpeta auxiliar. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Corregeix la puntuacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Corregeix la puntuació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* de la correcció no inclou la feina pendent de la salutació. *(pausa 3.5 s)*

Sortida real:

```text
[correccio 2a38650] Corregeix la puntuacio
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Crear el node nou només en executar.

## Terminal · `git switch main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `main` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Canviem a *main* dins de la carpeta auxiliar. Es pot fer perquè *main* no és activa a cap altra carpeta. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'main'
```

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució.

## Terminal · `git merge --ff-only correccio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git merge` | Incorporem la correcció a *main*. | 2.5 s |
| `correccio` | És la branca que acabem de confirmar. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* avança fins a la correcció. L’original continua a salutació amb l’edició pendent intacta. *(pausa 3.5 s)*

Sortida real:

```text
Updating 0d6725b..2a38650
Fast-forward
 helloGit.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** main i correccio a D; salutacio a B; dues preparacions separades.

## Terminal · `git -C ../projecte status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git -C ../projecte status` | Consultem la carpeta original sense sortir de l’auxiliar. | 2.5 s |
| `-C` | El guionet ce majúscula indica la carpeta on *Git* ha d’executar l’ordre. | 2.5 s |
| `../projecte` | És la carpeta original. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** L’original continua amb la salutació modificada i sense preparar. *(pausa 3.5 s)*

Sortida real:

```text
 M helloGit.py
```

**Visual:** Consulta identificada com ORIGINAL, diferenciada de l’estat de l’auxiliar.

## Terminal · `cd ../projecte`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `cd` | Tornem a la carpeta original. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Tornem a la feina de la salutació. La correcció ja és a *main*. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Ruta original i editor amb la feina pendent intacta.

## Terminal · `git worktree remove ../projecte-correccio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git worktree remove` | Retirem la carpeta auxiliar. | 2.5 s |
| `remove` | Esborra la carpeta. Només ho fa si no té canvis pendents, com en aquest cas. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La carpeta auxiliar desapareix. *main*, la branca correcció i el *commit* es conserven. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Retirar només la icona de la carpeta, sense esborrar etiquetes ni nodes del graf.

## Resum final

Les carpetes d’un *worktree* comparteixen historial i branques. *(pausa 2.5 s)*

Cada carpeta té treball, preparació i branca activa propis. *(pausa 2.5 s)*

Retirar una carpeta neta conserva els *commits* i les branques. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques, deixa una edició pendent i crea un *worktree* per a una correcció petita. Comprova l’estat de les dues carpetes abans de retirar l’auxiliar. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
