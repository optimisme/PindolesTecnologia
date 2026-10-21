# Lliçó 4 · Desar, preparar i confirmar: els tres estats

**Sèrie:** Píndoles de Git · **Capçalera:** ELS TRES ESTATS — Desar, preparar i confirmar  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/04-tres-estats.sh`](../practiques/04-tres-estats.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Quarta lliçó. Els tres estats.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a distingir el treball, la preparació i l’historial, també quan editem després de preparar. *(pausa 2.5 s)*

El programa ja està confirmat amb la salutació original i no tenim cap canvi pendent. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Tres zones del mateix projecte

Desar a l’editor modifica la carpeta de treball. Preparar selecciona un contingut concret. Confirmar enregistra aquesta selecció a l’historial. Són tres accions diferents. *(pausa 3 s)*

**Visual:** Tres panells persistents, TREBALL, PREPARACIÓ i ÚLTIM COMMIT, tots amb la salutació ORIGINAL.

## Editem el treball

Canviem la salutació i desem. El treball ja té la salutació nova, però la preparació i l’últim *commit* encara tenen l’original. *(pausa 3 s)*

**Visual:** TREBALL passa a SALUTACIÓ NOVA; els altres dos panells es queden amb l’ORIGINAL.

## Terminal · `git diff`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | *git diff* compara el treball amb la preparació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Hi veiem el canvi que encara no hem preparat. La línia amb el signe menys és l’anterior, i la del signe més, la nova. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 52662af..55b21a2 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1 @@
-print("Hello Git!")
+print("Hola, Anna!")
```

**Visual:** Fletxa PREPARACIÓ → TREBALL sobre la sortida real; llegenda textual per als signes menys i més.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Amb *git add* preparem el contingut que volem confirmar. | 2.5 s |
| `helloGit.py` | El nom indica el fitxer que preparem. Hi entra el contingut tal com està desat ara. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara el treball i la preparació tenen la salutació nova. La preparació és una còpia d’aquest moment; no segueix les edicions que farem després. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació.

## Terminal · `git diff --staged`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Ara comparem la preparació amb l’últim *commit*. | 2.5 s |
| `--staged` | Doble guionet *staged* tria aquesta altra comparació, la del contingut preparat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació nova està preparada per entrar al proper *commit*. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 52662af..55b21a2 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1 @@
-print("Hello Git!")
+print("Hola, Anna!")
```

**Visual:** Fletxa ÚLTIM COMMIT → PREPARACIÓ sobre la sortida real.

## Desem una altra edició

Afegim una línia de comiat i desem. El treball té la salutació i el comiat, però la preparació continua tenint només la salutació nova. *(pausa 3 s)*

**Visual:** TREBALL passa a SALUTACIÓ AMB COMIAT; PREPARACIÓ es queda amb la SALUTACIÓ NOVA; ÚLTIM COMMIT, ORIGINAL.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat amb *git status*. Aquesta consulta no modifica el projecte. | 2.5 s |
| `--short` | Doble guionet *short* demana la forma breu. La primera columna compara la preparació amb l’últim *commit*; la segona, el treball amb la preparació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Apareixen dues emes al mateix fitxer. La primera vol dir que hi ha canvis preparats; la segona, que el treball té canvis que encara no hem preparat. *(pausa 3.5 s)*

Sortida real:

```text
MM helloGit.py
```

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra.

## Terminal · `git diff`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Revisem què queda fora de la preparació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només hi surt el comiat. La salutació ja no és pendent, perquè ja és a la preparació. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 55b21a2..56f43b6 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1,2 @@
 print("Hola, Anna!")
+print("Fins aviat!")
```

**Visual:** Ressaltar només la línia del comiat a TREBALL.

## Terminal · `git commit -m "Canvia la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Amb *git commit* enregistrem el contingut preparat en una versió local. | 2.5 s |
| `-m` | El guionet ema indica que a continuació escrivim el missatge del canvi. | 2.5 s |
| `"Canvia la salutacio"` | El text entre cometes descriu la feina: Canvia la salutació. Les cometes mantenen el missatge com un sol argument. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** L’historial guarda la salutació nova. El comiat continua al treball, sense confirmar: el *commit* no l’ha esborrat. *(pausa 3.5 s)*

Sortida real:

```text
[main 6e2e114] Canvia la salutacio
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara sí, seleccionem també el comiat. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Afegeix un comiat"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Afegeix un comiat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Les tres zones tornen a coincidir. La salutació i el comiat han quedat en dos *commits* diferents. *(pausa 3.5 s)*

Sortida real:

```text
[main 1dbce39] Afegeix un comiat
 1 file changed, 1 insertion(+)
```

**Visual:** Crear el node nou només en executar.

## Resum final

Desar canvia el treball. *(pausa 2.5 s)*

*git add* copia a la preparació el contingut d’aquell moment. *(pausa 2.5 s)*

*git commit* enregistra la preparació i deixa la resta d’edicions pendents. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Edita, prepara i torna a editar el mateix fitxer. Compara les dues ordres *diff* abans de confirmar per saber exactament què entrarà al *commit*. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
