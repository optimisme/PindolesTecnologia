# Lliçó 9 · Finals de línia: Windows, macOS i Linux

**Sèrie:** Píndoles de Git · **Capçalera:** FINALS DE LÍNIA — Windows, macOS i Linux al mateix projecte  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/09-finals-linia.sh`](../practiques/09-finals-linia.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Novena lliçó. Finals de línia.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a evitar que un projecte compartit entre Windows, macOS i Linux sembli canviat a totes les línies. *(pausa 2.5 s)*

Un mateix projecte es fa servir en ordinadors amb Windows i amb macOS. El programa ja està confirmat i no hi ha canvis pendents. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Dos caràcters invisibles

Cada línia d’un fitxer de text acaba amb un caràcter invisible. A Windows sovint en són dos, retorn de carro i salt de línia; a macOS i Linux, només el salt de línia. *(pausa 3 s)*

**Visual:** El mateix fitxer amb els finals visibles, CRLF a la versió de Windows i LF a la de macOS i Linux.

## Un editor que desa amb un altre final

Una companya obre el fitxer a Windows, no canvia cap paraula i el desa. El seu editor ha posat els finals de línia de Windows. *(pausa 3 s)*

**Visual:** Editor amb l’indicador CRLF a la barra inferior; el text és idèntic.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El fitxer surt modificat, encara que el text que veiem és exactament el mateix. *(pausa 3.5 s)*

Sortida real:

```text
 M helloGit.py
```

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git diff`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Mirem què hi ha canviat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Totes les línies surten esborrades i tornades a afegir. En un projecte real, això amaga els canvis de veritat i provoca conflictes sense sentit. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 097ee02..cc8a4bb 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1,2 +1,2 @@
-print("Hello Git!")
-print("Fins aviat!")
+print("Hello Git!")
+print("Fins aviat!")
```

**Visual:** Sortida real amb totes les línies en vermell i en verd; ressaltar el final invisible que ha canviat.

## Una regla per a tot el projecte

Creem el fitxer punt *gitattributes* a l’arrel del projecte amb la línia que veus. Indica a *Git* que detecti els fitxers de text i en guardi sempre els finals de macOS i Linux a l’historial. *(pausa 3 s)*

En treure els fitxers a cada ordinador, *Git* pot fer servir els finals propis del sistema. Com el punt *gitignore*, aquest fitxer es confirma perquè tothom faci servir la mateixa regla. *(pausa 3 s)*

**Visual:** Editor .gitattributes amb la línia literal * text=auto. Ressaltar l’asterisc i després text=auto.

## Terminal · `git add --renormalize .`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Apliquem la regla als fitxers que ja seguíem. | 2.5 s |
| `--renormalize` | Torna a preparar els fitxers seguits aplicant-hi les regles de finals de línia. | 2.5 s |
| `.` | El punt vol dir tota la carpeta del projecte. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El programa ja no surt modificat: un cop normalitzat, el seu contingut és el mateix que hi havia a l’historial. Només queda preparat el fitxer de regles. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** helloGit.py deixa de sortir com a modificat; .gitattributes apareix a PREPARACIÓ.

## Terminal · `git add .gitattributes`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El fitxer de regles queda preparat. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Normalitza els finals de linia"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Normalitza els finals de linia. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La regla ja forma part del projecte. A partir d’ara, cada ordinador treballa amb els seus finals sense canviar l’historial. *(pausa 3.5 s)*

Sortida real:

```text
[main 4adeea8] Normalitza els finals de linia
 1 file changed, 1 insertion(+)
 create mode 100644 .gitattributes
```

**Visual:** Crear el node nou només en executar.

## A Windows, també la configuració global

Als ordinadors amb Windows, a més, és habitual activar *core.autocrlf* amb *git config*. Si el projecte ja té la regla, la regla té prioritat i el resultat és el mateix per a tothom. *(pausa 3 s)*

**Visual:** Terminal de Windows amb git config --global core.autocrlf true, marcada NOMÉS A WINDOWS. Al costat, .gitattributes marcat PRIORITAT DEL PROJECTE.

## Resum final

Windows i els altres sistemes acaben les línies de manera diferent. *(pausa 2.5 s)*

Punt *gitattributes* amb asterisc *text=auto* guarda finals uniformes a l’historial. *(pausa 2.5 s)*

El fitxer de regles es confirma perquè s’apliqui a tots els ordinadors. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques, afegeix el fitxer de regles de finals de línia, aplica’l als fitxers que ja segueixes i confirma’l. Comprova que l’estat queda net. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
