# Lliçó 23 · Revert: desfés un commit publicat

**Sèrie:** Píndoles de Git · **Capçalera:** REVERT — Desfés un commit publicat  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/23-revert.sh`](../practiques/23-revert.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-tresena lliçó. *Revert*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a desfer l’efecte d’un *commit* ja publicat amb un *commit* nou que fa el canvi invers. *(pausa 2.5 s)*

L’últim *commit* ja és a *GitHub* i ha trencat el programa. Altres persones ja el poden tenir. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Una correcció que també queda registrada

Com que el *commit* ja és compartit, no el traurem de l’historial. Crearem un *commit* nou que en desfaci l’efecte, i així ningú perd la història que ja té. *(pausa 3 s)*

**Visual:** Graf A, B i C al local i al remot. C es manté visible durant tota la demostració.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El programa falla amb un error de nom, perquè fa servir una variable que no existeix. *(pausa 3.5 s)*

Sortida real:

```text
Traceback (most recent call last):
  File "~/HelloGit/helloGit.py", line 2, in <module>
    print(salutacio)
          ^^^^^^^^^
NameError: name 'salutacio' is not defined
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** No tenim edicions pendents, així la correcció no es barrejarà amb altres feines. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git log --oneline`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Busquem el *commit* a l’historial. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El primer de la llista és el que ha trencat el programa. En copiem l’identificador. *(pausa 3.5 s)*

Sortida real:

```text
c1560a6 Personalitza la salutacio
1a6c8de Afegeix una exclamacio
a97b48b Afegeix la salutacio inicial
```

**Visual:** Ressaltar la primera línia de la sortida real amb l’etiqueta COPIA EL TEU IDENTIFICADOR.

## Terminal · `git show c1560a6 -- helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | Revisem el canvi abans de desfer-lo. | 2.5 s |
| `c1560a6` | És el *commit* que hem identificat. | 2.5 s |
| `helloGit.py` | Mirem només el programa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* va substituir la salutació que funcionava per una variable sense definir. *(pausa 3.5 s)*

Sortida real:

```text
commit c1560a6778332a4f53b66b53ac456798a538fc8f
Author: Ermessenda Carcassona <ermessenda@example.com>
Date:   Tue Oct 20 12:08:00 2026 +0200

    Personalitza la salutacio

diff --git a/helloGit.py b/helloGit.py
index 52662af..343c51c 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1,2 @@
-print("Hello Git!")
+missatge = "Hola, Ermessenda!"
+print(salutacio)
```

**Visual:** Diff real amb l’abans i el després del mateix fitxer.

## Terminal · `git revert --no-edit c1560a6`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git revert` | *git revert* crea un *commit* nou amb el canvi invers del que indiquem. | 2.5 s |
| `--no-edit` | Accepta el missatge automàtic sense obrir l’editor. | 2.5 s |
| `c1560a6` | És el *commit* que volem desfer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Apareix un *commit* nou després de l’erroni. El *commit* erroni continua a l’historial i el nou en desfà l’efecte. *(pausa 3.5 s)*

Sortida real:

```text
[main e5d817c] Revert "Personalitza la salutacio"
 Date: Tue Oct 20 13:10:00 2026 +0200
 1 file changed, 1 insertion(+), 2 deletions(-)
```

**Visual:** Afegir D amb C com a pare. No moure main enrere ni esborrar C.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació torna a funcionar. *(pausa 3.5 s)*

Sortida real:

```text
Hello Git!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git push`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | Amb *git push* enviem els *commits* de la branca al remot. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El remot rep el *commit* nou amb un enviament normal. Les altres còpies podran descarregar la correcció. *(pausa 3.5 s)*

Sortida real:

```text
To ~/origin.git
   c1560a6..e5d817c  main -> main
```

**Visual:** Conservar el mateix identificador al local i al remot. La fletxa envia commits; no envia edicions sense confirmar.

## Revert desfà un commit concret

*git revert* no torna tot el projecte a una data anterior: desfà només el *commit* que li indiquem. Els *commits* posteriors que no hi tinguin relació es conserven. *(pausa 3 s)*

**Visual:** Panell amb C, un commit posterior que només toca notes.md i el commit invers de C. Les notes es conserven.

## Resum final

*git revert* crea un *commit* nou amb el canvi invers. *(pausa 2.5 s)*

El *commit* original continua a l’historial i la branca avança. *(pausa 2.5 s)*

És la manera de desfer canvis que ja hem compartit. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques, desfés un *commit* amb *git revert*. Compara el graf abans i després i comprova que el *commit* original hi continua. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
