# Lliçó 25 · Tags: identifica una entrega del projecte

**Sèrie:** Píndoles de Git · **Capçalera:** TAGS — Identifica una entrega del projecte  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/25-tags.sh`](../practiques/25-tags.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-cinquena lliçó. *Tags*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a marcar una entrega amb una etiqueta anotada i publicar-la. *(pausa 2.5 s)*

Hem acabat la primera entrega del projecte. Està confirmada, publicada i provada. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Un nom per a una entrega

El projecte continuarà canviant, però volem poder tornar a aquesta entrega. Una etiqueta posa un nom fix a un *commit* concret. *(pausa 3 s)*

**Visual:** Graf A i B; main a B. Targeta ENTREGA amb el programa provat.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La versió que entregarem funciona. *(pausa 3.5 s)*

Sortida real:

```text
Hello Git!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** No hi ha canvis pendents. L’etiqueta assenyalarà el *commit*; una edició sense confirmar no hi entraria. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git tag -a v1.0 -m "Primera entrega"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git tag` | Creem l’etiqueta amb *git tag*. | 2.5 s |
| `-a` | El guionet a crea una etiqueta anotada, amb autoria, data i missatge propis. | 2.5 s |
| `v1.0` | És el nom de l’entrega, versió u punt zero. | 2.5 s |
| `-m` | El guionet ema introdueix el missatge de l’etiqueta. | 2.5 s |
| `"Primera entrega"` | Descriu què representa aquest punt del projecte. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** L’etiqueta apunta al *commit* actual. No afegeix cap *commit* a la història de *main*. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Etiqueta v1.0 al costat de B, sense cap node nou.

## Terminal · `git show v1.0`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | Revisem l’etiqueta creada. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Primer surten les dades de l’etiqueta i, després, el *commit* al qual apunta. *(pausa 3.5 s)*

Sortida real:

```text
tag v1.0
Tagger: Ermessenda Carcassona <ermessenda@example.com>
Date:   Tue Oct 20 12:49:00 2026 +0200

Primera entrega

commit 1a6c8de2ce87682a0cd3cba96119e48fa7ac847c
Author: Ermessenda Carcassona <ermessenda@example.com>
Date:   Tue Oct 20 12:06:00 2026 +0200

    Afegeix una exclamacio

diff --git a/helloGit.py b/helloGit.py
index 078d6bf..52662af 100644
--- a/helloGit.py
+++ b/helloGit.py
```

**Visual:** Separar a la sortida real DADES DE L’ETIQUETA i COMMIT ASSOCIAT.

## Continuem treballant

Després de l’entrega, canviem la salutació, la preparem i la confirmem. La branca avançarà; l’etiqueta, no. *(pausa 3 s)*

**Visual:** Editor amb print("Hola, Ermessenda!") abans de preparar i confirmar.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació nova queda preparada. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Canvia la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Canvia la salutació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* avança. L’etiqueta de la versió u punt zero continua assenyalant l’entrega. *(pausa 3.5 s)*

Sortida real:

```text
[main 36d091d] Canvia la salutacio
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Crear el node nou només en executar.

## Terminal · `git show v1.0:helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | Llegim el fitxer tal com era a l’entrega, sense canviar el treball. | 2.5 s |
| `v1.0:helloGit.py` | Abans dels dos punts, la versió; després, el fitxer dins d’aquella versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Surt la salutació de l’entrega. L’editor continua amb la salutació nova. *(pausa 3.5 s)*

Sortida real:

```text
print("Hello Git!")
```

**Visual:** Dos panells, CONSULTA DE V1.0 i FITXER ACTUAL. Cap fletxa que sobreescrigui el treball.

## Terminal · `git push`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | Amb *git push* enviem els *commits* de la branca al remot. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El remot rep el *commit* nou. Les etiquetes no s’envien amb un *push* normal. *(pausa 3.5 s)*

Sortida real:

```text
To ~/origin.git
   1a6c8de..36d091d  main -> main
```

**Visual:** Conservar el mateix identificador al local i al remot. La fletxa envia commits; no envia edicions sense confirmar.

## Terminal · `git push origin v1.0`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | Publiquem l’etiqueta explícitament. | 2.5 s |
| `origin` | És el remot del projecte. | 2.5 s |
| `v1.0` | Indiquem l’etiqueta que enviem, en lloc d’una branca. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El remot també coneix l’entrega pel seu nom. Això no crea per si sol una publicació de tipus *Release* a *GitHub*. *(pausa 3.5 s)*

Sortida real:

```text
To ~/origin.git
 * [new tag]         v1.0 -> v1.0
```

**Visual:** main a C i v1.0 a B, tant al local com al remot.

## Resum final

Una branca avança; una etiqueta queda fixa al *commit* de l’entrega. *(pausa 2.5 s)*

L’etiqueta anotada té dades pròpies i no afegeix cap *commit*. *(pausa 2.5 s)*

Les etiquetes es publiquen explícitament. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Marca una versió provada d’un repositori de pràctiques amb una etiqueta anotada. Fes un *commit* posterior i llegeix el fitxer de l’etiqueta sense canviar l’editor. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
