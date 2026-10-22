# Lliçó 12 · Conflictes: dues edicions, una decisió

**Sèrie:** Píndoles de Git · **Capçalera:** CONFLICTES — Dues edicions, una decisió  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/12-conflictes.sh`](../practiques/12-conflictes.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Dotzena lliçó. Conflictes.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a llegir un conflicte de fusió, decidir el resultat i confirmar la resolució. *(pausa 2.5 s)*

Som a *main*. Des d’una mateixa versió, *main* i la branca salutació han canviat la mateixa línia de manera diferent. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Dues propostes incompatibles

Les dues branques han canviat la mateixa línia de manera diferent. *Git* no pot triar per nosaltres: necessita una decisió sobre el contingut. *(pausa 3 s)*

**Visual:** Les dues línies, una sota l’altra, amb el nom de la branca de cada una.

## Terminal · `git merge salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git merge` | Intentem integrar salutació a la branca activa. | 2.5 s |
| `salutacio` | És la branca que entra. La destinació continua sent *main*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La fusió s’atura i avisa d’un conflicte. Encara no s’ha creat el *commit* que uneix les dues històries. *(pausa 3.5 s)*

Sortida real:

```text
Auto-merging helloGit.py
CONFLICT (content): Merge conflict in helloGit.py
Automatic merge failed; fix conflicts and then commit the result.
```

**Visual:** Sortida real amb la paraula CONFLICT ressaltada; el graf no té cap node nou.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Dues us majúscules indiquen un fitxer amb un conflicte sense resoldre. Mirem-ne el contingut. *(pausa 3.5 s)*

Sortida real:

```text
UU helloGit.py
```

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Llegim els marcadors

*Git* ha escrit les dues versions al fitxer, entre marcadors. La primera és la de la branca actual, assenyalada com a *HEAD*, que aquí és *main*. *(pausa 3.5 s)*

La línia d’iguals separa les dues propostes, i el darrer marcador tanca la versió que entra, la de salutació. Els marcadors no són codi del programa. *(pausa 3.5 s)*

**Visual:** Editor amb el contingut real del fitxer en conflicte. Subratllar un marcador cada vegada.

## Escrivim el resultat acordat

Decidim escriure Hola, grup! Esborrem tots els marcadors i deixem una sola instrucció vàlida. La resolució pot combinar les idees; no cal quedar-se amb una de les dues propostes sencera. *(pausa 3 s)*

**Visual:** Animar l’edició fins a print("Hola, grup!"). No preparar el fitxer abans de mostrar aquesta decisió.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació final funciona. Encara falta preparar-la i acabar la fusió. *(pausa 3.5 s)*

Sortida real:

```text
Hola, grup!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Preparar el fitxer indica a *Git* que el conflicte està resolt. No comprova que el programa sigui correcte; per això l’hem provat abans. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Resol el conflicte de la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Resol el conflicte de la salutació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara sí, es crea el *commit* de fusió, amb dos pares i el contingut que hem decidit. *(pausa 3.5 s)*

Sortida real:

```text
[main 935ebbd] Resol el conflicte de la salutacio
```

**Visual:** Crear el node nou només en executar.

## Alternativa, abandonar la fusió

> **Alternativa.** Parteix del seu propi punt; no s’encadena amb el camí principal.

En un cas alternatiu, podem abandonar una fusió que encara no hem acabat. Tornem al moment del conflicte, abans de preparar res. *(pausa 3 s)*

**Visual:** Separador ALTERNATIVA. Recuperar l’estat amb el conflicte, no el resultat ja confirmat.

## Terminal · `git merge --abort`

> **Alternativa.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git merge` | Cancel·lem la fusió pendent. | 2.5 s |
| `--abort` | Doble guionet *abort* abandona l’operació i torna a l’estat d’abans d’intentar-la. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El fitxer recupera la versió de *main* i no queda cap fusió pendent. Aquest camí només té sentit abans de crear el *commit*. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Desapareixen els marcadors i l’indicador de fusió pendent; cap node nou.

## Resum final

Un conflicte vol dir que cal una decisió sobre el contingut. *(pausa 2.5 s)*

Editem, provem i preparem la resolució abans de confirmar-la. *(pausa 2.5 s)*

El *commit* acaba la fusió; avortar és l’alternativa abans d’acabar-la. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Crea dues salutacions incompatibles en dues branques d’un repositori de pràctiques. Resol el conflicte amb una tercera salutació, prova el programa i completa la fusió. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
