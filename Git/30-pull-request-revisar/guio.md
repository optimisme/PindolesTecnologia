# Lliçó 30 · Pull request: revisa, actualitza i integra

**Sèrie:** Píndoles de Git · **Capçalera:** PULL REQUEST — Revisa, actualitza i integra  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/30-pull-request-revisar.sh`](../practiques/30-pull-request-revisar.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Trentena lliçó. *Pull requests*, segona part.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a respondre a una revisió, actualitzar la mateixa proposta i portar el resultat integrat al nostre *main*. *(pausa 2.5 s)*

Tenim una proposta oberta amb la salutació personalitzada. Una companya l’està revisant. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## La revisió demana un canvi

La revisora proposa acabar la salutació amb una exclamació. Fem el canvi a la mateixa branca, desem i el provem. *(pausa 3 s)*

**Visual:** Comentari d’exemple a la pull request i editor amb print("Hola, Ermessenda!").

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació ja acaba amb exclamació. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Ermessenda!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La millora demanada queda preparada. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Completa la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Completa la salutació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* nou completa la branca de la proposta. *(pausa 3.5 s)*

Sortida real:

```text
[salutacio 3d6d969] Completa la salutacio
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Crear el node nou només en executar.

## Terminal · `git push`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | Amb *git push* enviem els *commits* de la branca al remot. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La mateixa *pull request* mostra ara el *commit* nou. No cal obrir-ne una altra: la proposta segueix la branca. *(pausa 3.5 s)*

Sortida real:

```text
To ~/origin.git
   401cc38..3d6d969  salutacio -> salutacio
```

**Visual:** Conservar el mateix identificador al local i al remot. La fletxa envia commits; no envia edicions sense confirmar.

## Integrem la proposta

La revisora aprova la versió actualitzada. Una persona amb permís la fusiona amb el botó de fusió; en aquest exemple, es crea un *commit* de *merge* a *main* del remot. *(pausa 3 s)*

**Visual:** Esquema amb l’aprovació i el botó Merge pull request, opció Create a merge commit. Graf del remot amb M i dos pares. Cap acció sobre un servei real.

## Terminal · `git switch main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `main` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El nostre *main* local encara no té la fusió que s’ha fet al remot. *(pausa 3.5 s)*

Sortida real:

```text
Your branch is up to date with 'origin/main'.
Switched to branch 'main'
```

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució.

## Terminal · `git pull --ff-only`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git pull` | Actualitzem la còpia local de *main*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* local arriba al *commit* de fusió, que té com a pares l’antic *main* i l’últim *commit* de la proposta. *(pausa 3.5 s)*

Sortida real:

```text
Updating 1a6c8de..f52a630
Fast-forward
 helloGit.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
From ~/origin
   1a6c8de..f52a630  main       -> origin/main
```

**Visual:** El mateix M al remot i al local.

## Terminal · `git branch -d salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git branch` | La branca de la proposta ja està integrada; l’esborrem del nostre ordinador. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** L’etiqueta local desapareix i els *commits* continuen a *main*. A *GitHub*, la branca del remot s’esborra amb el botó que apareix després de fusionar. *(pausa 3.5 s)*

Sortida real:

```text
Deleted branch salutacio (was 3d6d969).
```

**Visual:** Retirar l’etiqueta local salutacio; botó Delete branch a l’esquema de la web.

## Resum final

Un *push* a la mateixa branca actualitza la proposta oberta. *(pausa 2.5 s)*

La integració es fa després de la revisió, a la web. *(pausa 2.5 s)*

Després, actualitzem el nostre *main* i esborrem la branca integrada. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Amb una persona col·laboradora, demana un canvi petit en una proposta, actualitza-la amb un *commit* nou, integra-la i porta el resultat al teu *main*. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
