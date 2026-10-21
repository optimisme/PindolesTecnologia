# Lliçó 15 · Restore: desmarca o descarta un canvi local

**Sèrie:** Píndoles de Git · **Capçalera:** RESTORE — Desmarca o descarta un canvi local  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/15-restore.sh`](../practiques/15-restore.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Quinzena lliçó. *Restore*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a desfer la preparació d’un canvi o descartar una edició, sabent d’on es copia cada contingut. *(pausa 2.5 s)*

Hem canviat la salutació i l’hem preparada, però encara no l’hem confirmada. L’últim *commit* té la salutació original. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Dues destinacions diferents

Podem desfer canvis a la preparació o al treball. Abans d’executar *git restore*, decidim quina zona volem restaurar i d’on en copiarem el contingut. *(pausa 3 s)*

**Visual:** Tres panells, TREBALL i PREPARACIÓ amb la SALUTACIÓ NOVA, ÚLTIM COMMIT amb l’ORIGINAL.

## Terminal · `git restore --staged helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git restore` | Primer desfem la preparació, però conservem l’edició del fitxer. | 2.5 s |
| `--staged` | Doble guionet *staged* tria la preparació com a destinació. Hi copia el contingut de l’últim *commit*. | 2.5 s |
| `helloGit.py` | Només afecta aquest fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La preparació torna a l’original i el treball conserva la salutació nova. Només hem desfet la selecció; l’edició continua al fitxer. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Fletxa ÚLTIM COMMIT → PREPARACIÓ. Cap fletxa cap al treball.

## Terminal · `git diff`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Llegim el canvi que continua al fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació nova encara és al treball. Després de revisar-la, decidim que aquest canvi concret no el volem conservar. *(pausa 3.5 s)*

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

**Visual:** Sortida real. Mostrar la decisió DESCARTAR AQUESTA EDICIÓ abans de l’ordre següent.

## Terminal · `git restore helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git restore` | Ara restaurem el fitxer de treball. | 2.5 s |
| `helloGit.py` | Sense doble guionet *staged*, la destinació és el treball i el contingut surt de la preparació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El treball torna a l’original, perquè la preparació ja era l’original. L’edició s’ha descartat i no es pot recuperar amb *Git*, perquè mai no l’havíem confirmada. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Fletxa PREPARACIÓ → TREBALL. Retirar la salutació nova sense insinuar que s’ha guardat enlloc.

## Un altre cas, tres versions

> **Un altre cas.** Parteix del seu propi punt; no s’encadena amb el camí principal.

En un cas diferent, la preparació té la salutació nova i el treball té una tercera versió, amb una benvinguda. Restaurar el treball hi copia el que hi ha a la preparació, no l’últim *commit*. *(pausa 3 s)*

**Visual:** Separador UN ALTRE CAS. ÚLTIM COMMIT · original / PREPARACIÓ · salutació nova / TREBALL · amb benvinguda.

## Terminal · `git restore helloGit.py`

> **Un altre cas.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git restore` | Restaurem el treball en aquest altre cas. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El fitxer recupera la salutació nova, que és la que hi havia a la preparació. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Fletxa PREPARACIÓ → TREBALL amb la salutació nova.

## Resum final

Amb doble guionet *staged*, desfem la preparació i conservem l’edició. *(pausa 2.5 s)*

Sense aquesta opció, restaurem el treball a partir de la preparació. *(pausa 2.5 s)*

Abans de descartar una edició, la revisem; un canvi mai confirmat no es pot recuperar. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un fitxer de pràctiques, prepara una edició i desfés la preparació conservant el fitxer. Revisa-la amb *git diff* abans de decidir si la tornes a preparar o la descartes. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
