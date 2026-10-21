# Lliçó 29 · Bisect: troba el primer commit que falla

**Sèrie:** Píndoles de Git · **Capçalera:** BISECT — Troba el primer commit que falla  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/29-bisect.sh`](../practiques/29-bisect.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-novena lliçó. *Bisect*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a localitzar el primer *commit* que falla amb una prova que es pugui repetir, i tancar la cerca. *(pausa 2.5 s)*

La primera entrega, l’etiqueta v u punt zero, funcionava. Després hi ha sis *commits* més i ara el programa falla. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Acotar l’error amb una prova

Sabem una versió que funciona i una que falla. *Bisect* tria versions intermèdies perquè les provem i cada resposta redueix a la meitat els *commits* sospitosos. La prova ha de ser sempre la mateixa. *(pausa 3 s)*

**Visual:** Graf de vuit commits; v1.0 a B amb FUNCIONA i H amb FALLA. Prova fixa python3 helloGit.py.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** No hi ha canvis pendents que es puguin barrejar amb les versions que anirem provant. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git bisect start`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git bisect start` | *git bisect start* comença la cerca. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La cerca està oberta i espera que indiquem els dos extrems. *(pausa 3.5 s)*

Sortida real:

```text
status: waiting for both 'good' and 'bad' commits
```

**Visual:** Indicador CERCA ACTIVA. main continua a H.

## Terminal · `git bisect bad`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git bisect bad` | Marquem la versió actual com la que falla. | 2.5 s |
| `bad` | Diu que la prova falla en el *commit* on som, el darrer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El darrer *commit* és l’extrem que falla. *(pausa 3.5 s)*

Sortida real:

```text
status: waiting for 'good' commit(s), 'bad' commit known
```

**Visual:** H amb l’etiqueta FALLA, a més del color.

## Terminal · `git bisect good v1.0`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git bisect good` | Indiquem la versió que sabem que funciona. | 2.5 s |
| `good` | Diu que aquesta versió supera la prova. | 2.5 s |
| `v1.0` | És l’etiqueta de la primera entrega. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *Git* ens porta a un *commit* del mig per provar-lo. La nostra branca no es mou; només canvia la versió dels fitxers. *(pausa 3.5 s)*

Sortida real:

```text
Bisecting: 2 revisions left to test after this (roughly 2 steps)
[ca4418ec8079784bde08356f36f75d92ab195db7] Comença les notes
```

**Visual:** HEAD es desplaça al commit triat; main quieta a H.

## HEAD separat

Durant la cerca, *HEAD* no segueix cap branca: apunta directament a un *commit*. *Git* en diu *HEAD* separat. És normal aquí, però no és el moment de fer *commits* nous. *(pausa 3 s)*

**Visual:** HEAD desenganxat de main i apuntant a E. Etiqueta HEAD SEPARAT.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Executem exactament la mateixa prova. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Falla amb un error de nom. Comuniquem aquest resultat a la cerca. *(pausa 3.5 s)*

Sortida real:

```text
Traceback (most recent call last):
  File "~/HelloGit/helloGit.py", line 2, in <module>
    print(salutacio)
          ^^^^^^^^^
NameError: name 'salutacio' is not defined
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git bisect bad`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git bisect bad` | Marquem aquesta versió com a fallida. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *Git* descarta els *commits* posteriors i ens porta a un *commit* anterior. *(pausa 3.5 s)*

Sortida real:

```text
Bisecting: 0 revisions left to test after this (roughly 1 step)
[81c386dd524947b697b1acc5415a03a8ec3c1f1d] Prepara la salutacio personalitzada
```

**Visual:** Els commits de E a H passen a DESCARTATS; HEAD es desplaça a D.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Repetim la prova. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Aquesta versió també falla. *(pausa 3.5 s)*

Sortida real:

```text
Traceback (most recent call last):
  File "~/HelloGit/helloGit.py", line 2, in <module>
    print(salutacio)
          ^^^^^^^^^
NameError: name 'salutacio' is not defined
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git bisect bad`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git bisect bad` | La marquem com a fallida. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només queda un *commit* per provar, l’anterior. *(pausa 3.5 s)*

Sortida real:

```text
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[1f8da74333e856834c233cfaec45d4f97355fe68] Afegeix un comentari
```

**Visual:** D marcat FALLA; HEAD es desplaça a C.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem aquesta versió de la mateixa manera. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara la salutació funciona. *(pausa 3.5 s)*

Sortida real:

```text
Hello Git!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git bisect good`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git bisect good` | Marquem el resultat correcte. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només queda un candidat, i *Git* l’anuncia com el primer *commit* que falla. Ja sabem quin canvi hem de revisar, però encara no l’hem arreglat. *(pausa 3.5 s)*

Sortida real:

```text
81c386dd524947b697b1acc5415a03a8ec3c1f1d is the first 'bad' commit
commit 81c386dd524947b697b1acc5415a03a8ec3c1f1d
Author: Anna Puig <anna@example.com>
Date:   Tue Oct 20 12:10:00 2026 +0200

    Prepara la salutacio personalitzada

 helloGit.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Ressaltar D com a RESULTAT a la sortida real. HEAD continua a C, l’últim commit provat.

## Terminal · `git show 81c386d -- helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | Revisem el canvi trobat. | 2.5 s |
| `81c386d` | És l’identificador que ha trobat la cerca. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El canvi fa servir una variable que no existeix. Consultar-lo no mou *HEAD*. *(pausa 3.5 s)*

Sortida real:

```text
commit 81c386dd524947b697b1acc5415a03a8ec3c1f1d
Author: Anna Puig <anna@example.com>
Date:   Tue Oct 20 12:10:00 2026 +0200

    Prepara la salutacio personalitzada

diff --git a/helloGit.py b/helloGit.py
index 0af3419..a0fe6bd 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1,2 +1,2 @@
 # Salutació del projecte
-print("Hello Git!")
+print(salutacio)
```

**Visual:** Diff real de D al costat del resultat de la prova.

## Terminal · `git bisect reset`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git bisect reset` | Tanquem la cerca. | 2.5 s |
| `reset` | Dins de *bisect*, *reset* acaba la sessió i torna a la branca d’abans. No té res a veure amb *git reset*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Tornem a *main*, al darrer *commit*. No s’ha creat cap *commit*; ara toca corregir l’error. *(pausa 3.5 s)*

Sortida real:

```text
Previous HEAD position was 1f8da74 Afegeix un comentari
Switched to branch 'main'
```

**Visual:** Desapareix CERCA ACTIVA; HEAD torna a unir-se a main a H.

## Resum final

Calen una prova repetible i dos extrems coneguts. *(pausa 2.5 s)*

Provem cada versió abans de dir si és bona o dolenta. *(pausa 2.5 s)*

*Bisect* troba el *commit*; després tanquem la cerca i el corregim. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un historial de pràctiques amb un error que es manté, marca un extrem que funciona i un que falla. Fes servir sempre la mateixa prova i acaba la cerca amb *git bisect reset*. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
