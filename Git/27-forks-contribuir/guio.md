# Lliçó 27 · Forks: contribueix al projecte original

**Sèrie:** Píndoles de Git · **Capçalera:** CONTRIBUIR DES D’UN FORK — Proposa un canvi a l’original  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/27-forks-contribuir.sh`](../practiques/27-forks-contribuir.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-setena lliçó. *Forks*, contribuir a l’original.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a preparar una contribució al nostre *fork* i proposar-la al projecte original amb una *pull request*. *(pausa 2.5 s)*

El nostre *fork* i la còpia local estan al dia amb l’original. Ara hi farem una contribució. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Una branca per a la contribució

Cada contribució va en una branca pròpia, creada a partir del *main* actualitzat. Així el nostre *main* es pot continuar posant al dia amb l’original. *(pausa 3 s)*

**Visual:** Tres caixes, ORIGINAL, FORK i LOCAL, totes a C.

## Terminal · `git switch -c salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* seleccionem la branca on treballarem. | 2.5 s |
| `-c` | El guionet ce crea una branca nova i hi canvia. | 2.5 s |
| `salutacio` | És el nom de la branca nova. Comença al *commit* actual. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La branca de la contribució comença a la versió actualitzada. *(pausa 3.5 s)*

Sortida real:

```text
Switched to a new branch 'salutacio'
```

**Visual:** Afegir l’etiqueta nova al commit actual sense crear cap node i moure-hi l’indicador de branca activa.

## Fem la contribució

Personalitzem la salutació i la provem. *(pausa 3 s)*

**Visual:** Editor amb print("Hola, Anna!").

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació nova funciona a la branca de la contribució. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Anna!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La contribució queda preparada. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Personalitza la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Personalitza la salutació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* és a la branca local salutació. L’original no en sap res. *(pausa 3.5 s)*

Sortida real:

```text
[salutacio 53a1c5c] Personalitza la salutacio
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

**Resultat:** La branca de la contribució ja és al nostre *fork*. A l’original no hi hem publicat res. *(pausa 3.5 s)*

Sortida real:

```text
branch 'salutacio' set up to track 'origin/salutacio'.
To ~/fork.git
 * [new branch]      salutacio -> salutacio
```

**Visual:** La branca apareix al remot amb el mateix commit que al local.

## Proposem el canvi a l’original

A la web de *GitHub* obrim una *pull request*. La destinació és *main* del projecte original; l’origen és la branca salutació del nostre *fork*. *(pausa 3.5 s)*

Expliquem la millora i com l’hem provada. Ara la revisió depèn de les persones que mantenen l’original. *(pausa 3.5 s)*

**Visual:** Formulari amb repositori i branca a tots dos costats, base repository original · main i head repository fork · salutacio. No representar cap fusió ni aprovació.

## Mentre esperem la revisió

Si ens demanen canvis, fem nous *commits* a la mateixa branca i els enviem al *fork*: la proposta s’actualitza sola. El nostre *main* el continuem posant al dia amb *upstream*. *(pausa 3 s)*

**Visual:** Cicle COMMIT → PUSH AL FORK → PROPOSTA ACTUALITZADA; a part, FETCH UPSTREAM → MERGE → PUSH ORIGIN MAIN.

## Resum final

Cada contribució va en una branca pròpia. *(pausa 2.5 s)*

Publiquem la branca al nostre *fork*, mai a l’original. *(pausa 2.5 s)*

La *pull request* va del nostre *fork* cap al *main* de l’original. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Des del *fork* de pràctiques, crea una branca amb un canvi petit, publica-la al *fork* i obre una proposta cap a l’original amb una descripció clara. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
