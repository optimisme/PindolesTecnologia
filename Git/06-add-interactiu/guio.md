# Lliçó 6 · Add interactiu: prepara només una part del fitxer

**Sèrie:** Píndoles de Git · **Capçalera:** ADD INTERACTIU — Prepara només una part del fitxer  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/06-add-interactiu.sh`](../practiques/06-add-interactiu.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Sisena lliçó. *Add* interactiu.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a preparar només una part d’un fitxer i deixar l’altra edició pendent al treball. *(pausa 2.5 s)*

El programa té una funció de salutació i una de comiat, separades per altres funcions. Ja està confirmat i no tenim canvis pendents. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Dues edicions, dos canvis separables

Mostrem el programa complet abans d’editar-lo. La salutació és a dalt i el comiat, a baix. *(pausa 3 s)*

Canviem la salutació per Hola, Anna! i el comiat per Adéu! Volem confirmar ara només la salutació i deixar el comiat per a més endavant. *(pausa 3 s)*

**Visual:** Editor amb el codi complet de exemples/helloGit-abans.py; després, l’editat de exemples/helloGit-editat.py amb les dues funcions modificades ressaltades per torns i les funcions del mig sense canvis.

## Terminal · `git diff -- helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Revisem els canvis abans de seleccionar-los. | 2.5 s |
| `--` | Els dos guionets separen les opcions del nom del fitxer. | 2.5 s |
| `helloGit.py` | Consultem els canvis d’aquest fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El primer bloc canvia la salutació i el segon, el comiat. Cada bloc comença amb una línia de dues arrobes. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 7c2367f..65a3480 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1,5 +1,5 @@
 def saluda():
-    return "Hello Git!"
+    return "Hola, Anna!"
 
 
 def doble(valor):
@@ -11,7 +11,7 @@ def suma(a, b):
 
 
 def comiat():
-    return "Fins aviat!"
```

**Visual:** Sortida real amb els dos blocs numerats BLOC 1 i BLOC 2.

## Terminal · `git add -p helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Entrem a la preparació interactiva. | 2.5 s |
| `-p` | El guionet pe permet triar els blocs de canvi un per un. | 2.5 s |
| `helloGit.py` | Limitem la selecció a aquest fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *Git* mostra el primer bloc i espera una resposta. Ara no escrivim cap ordre nova: responem a la pregunta que ha fet. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 7c2367f..65a3480 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1,5 +1,5 @@
 def saluda():
-    return "Hello Git!"
+    return "Hola, Anna!"
 
 
 def doble(valor):
(1/2) Stage this hunk [y,n,q,a,d,k,K,j,J,g,/,e,p,P,?]? @@ -11,7 +11,7 @@ def suma(a, b):
 
 
 def comiat():
-    return "Fins aviat!"
```

**Visual:** Terminal en mode INTERACTIU amb el primer bloc de la salutació i la llista d’opcions. La sortida real completa inclou també el segon bloc; mostrar-la per parts.

## Resposta interactiva · `y`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `y` | Responem i grega, de *yes*, per preparar el primer bloc. | 2.5 s |
| execució | Introduïm la resposta. | 1.5 s |

**Resultat:** La salutació passa a la preparació, i la mateixa sessió ens mostra el segon bloc. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Moure només el bloc de la salutació del treball a la preparació.

## Resposta interactiva · `n`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `n` | Responem ena per deixar fora el segon bloc. | 2.5 s |
| execució | Introduïm la resposta. | 1.5 s |

**Resultat:** El comiat es queda al treball. Com que no hi ha més blocs, tornem a la terminal normal. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** El comiat es queda al panell TREBALL. Torna a aparèixer el símbol habitual de la terminal.

## Terminal · `git diff --staged`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Comprovem què hem preparat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només hi ha la salutació nova. Aquesta és la selecció que entrarà al *commit*. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 7c2367f..4b75474 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1,5 +1,5 @@
 def saluda():
-    return "Hello Git!"
+    return "Hola, Anna!"
 
 
 def doble(valor):
```

**Visual:** Fletxa ÚLTIM COMMIT → PREPARACIÓ; el comiat antic continua igual a totes dues zones.

## Terminal · `git diff`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Comprovem què queda pendent. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només hi surt el comiat nou. La salutació ja coincideix entre el treball i la preparació. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 4b75474..65a3480 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -11,7 +11,7 @@ def suma(a, b):
 
 
 def comiat():
-    return "Fins aviat!"
+    return "Adéu!"
 
 
 print(saluda())
```

**Visual:** Fletxa PREPARACIÓ → TREBALL; ressaltar el comiat sense preparar.

## Terminal · `git commit -m "Personalitza la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Amb *git commit* enregistrem el contingut preparat en una versió local. | 2.5 s |
| `-m` | El guionet ema indica que a continuació escrivim el missatge del canvi. | 2.5 s |
| `"Personalitza la salutacio"` | El text entre cometes descriu la feina: Personalitza la salutació. Les cometes mantenen el missatge com un sol argument. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* guarda la salutació. L’edició del comiat continua al treball; el *commit* no l’ha esborrat. *(pausa 3.5 s)*

Sortida real:

```text
[main edb255f] Personalitza la salutacio
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar.

## El bloc és la unitat de selecció

Aquí les dues edicions eren prou lluny per formar dos blocs. Si *Git* les ajunta en un de sol, el bloc es pot dividir amb l’opció essa de la mateixa llista. *(pausa 3 s)*

**Visual:** Comparació DOS BLOCS SEPARATS / UN BLOC CONJUNT. En el bloc conjunt, la llista de respostes de mostra inclou la s de dividir.

## Resum final

Amb el guionet pe, *git add* permet preparar blocs concrets d’un fitxer. *(pausa 2.5 s)*

Les respostes i grega i ena pertanyen a la sessió interactiva, no a la terminal. *(pausa 2.5 s)*

El *commit* guarda la selecció i deixa la resta d’edicions al treball. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un fitxer de pràctiques amb dues edicions separades, prepara un bloc i deixa’n l’altre. Compara els dos diffs abans de confirmar. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
