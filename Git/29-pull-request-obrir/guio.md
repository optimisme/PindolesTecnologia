# Lliçó 29 · Pull request: proposa un canvi a l’equip

**Sèrie:** Píndoles de Git · **Capçalera:** PULL REQUEST — Proposa un canvi a l’equip  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/29-pull-request-obrir.sh`](../practiques/29-pull-request-obrir.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-novena lliçó. *Pull requests*, primera part.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a publicar una branca i obrir una proposta perquè l’equip la revisi abans d’integrar-la. *(pausa 2.5 s)*

Treballem en equip en un repositori compartit de *GitHub*. La nostra còpia de *main* és al dia i no tenim canvis pendents. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Una proposta abans d’integrar

Una *pull request* és una proposta per incorporar els *commits* d’una branca a una altra. És l’espai on l’equip revisa i comenta els canvis abans d’integrar-los. *(pausa 3 s)*

**Visual:** Esquema main / salutacio / PROPOSTA. main no es mou.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Comencem sense canvis pendents. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git switch -c salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* seleccionem la branca on treballarem. | 2.5 s |
| `-c` | El guionet ce crea una branca nova i hi canvia. | 2.5 s |
| `salutacio` | És el nom de la branca nova. Comença al *commit* actual. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Treballarem en una branca pròpia perquè es pugui revisar per separat. *(pausa 3.5 s)*

Sortida real:

```text
Switched to a new branch 'salutacio'
```

**Visual:** Afegir l’etiqueta nova al commit actual sense crear cap node i moure-hi l’indicador de branca activa.

## Fem el canvi

Personalitzem la salutació i la provem abans de confirmar-la. *(pausa 3 s)*

**Visual:** Editor amb print("Hola, Ermessenda").

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Surt la salutació personalitzada, encara sense exclamació. Aquesta és la primera versió de la proposta. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Ermessenda
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El canvi queda preparat. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Personalitza la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Personalitza la salutació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* és a la branca salutació, al nostre ordinador. *main* continua on era. *(pausa 3.5 s)*

Sortida real:

```text
[salutacio be18fc3] Personalitza la salutacio
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Crear el node nou només en executar.

## Terminal · `git push -u origin salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | Amb *git push* publiquem la branca al remot. | 2.5 s |
| `-u` | El guionet u desa la relació de seguiment; els enviaments següents podran ser només *git push*. | 2.5 s |
| `origin` | *origin* és el nom del remot on publiquem. | 2.5 s |
| `salutacio` | És el nom de la branca que publiquem. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La branca ja és al remot i es pot comparar amb *main*. Encara no l’hem integrada. *(pausa 3.5 s)*

Sortida real:

```text
branch 'salutacio' set up to track 'origin/salutacio'.
To ~/origin.git
 * [new branch]      salutacio -> salutacio
```

**Visual:** La branca apareix al remot amb el mateix commit que al local.

## Triem destinació i origen

A la web de *GitHub* obrim una proposta nova. La destinació, que *GitHub* anomena *base*, és *main*. L’origen, que anomena *compare*, és la branca salutació. *(pausa 3.5 s)*

Escrivim un títol i expliquem el canvi i com l’hem provat. Revisem la llista de canvis abans de crear la proposta. *(pausa 3.5 s)*

**Visual:** Esquema del formulari, base main i compare salutacio. Subratllar primer la destinació i després l’origen. Text d’exemple, Personalitza la salutació. Prova, python3 helloGit.py.

## La proposta queda oberta

La proposta ja és visible per a l’equip, amb el *commit* i les diferències. Ara toca esperar la revisió; encara no s’ha integrat res a *main*. *(pausa 3 s)*

**Visual:** Esquema de la pull request oberta amb l’estat OBERTA, el commit C i la pestanya de canvis.

## Resum final

La *pull request* es crea a partir d’una branca publicada. *(pausa 2.5 s)*

La destinació és *main* i l’origen, la branca amb el canvi. *(pausa 2.5 s)*

Proposar no és integrar; primer ve la revisió. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques compartit, publica una branca amb un canvi petit i obre una proposta cap a *main* amb una descripció de com l’has provat. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
