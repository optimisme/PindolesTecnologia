# Lliçó 5 · Esborrar i reanomenar fitxers

**Sèrie:** Píndoles de Git · **Capçalera:** ESBORRAR I REANOMENAR — Treure i canviar de nom fitxers seguits  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/05-fitxers.sh`](../practiques/05-fitxers.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Cinquena lliçó. Esborrar i reanomenar fitxers.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a esborrar i reanomenar fitxers que *Git* ja segueix, i confirmar aquests canvis com qualsevol altre. *(pausa 2.5 s)*

El projecte té el programa, un fitxer de notes i un fitxer de proves que ja no necessitem. Tot està confirmat i no hi ha canvis pendents. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Esborrar també és un canvi

Si un fitxer ja és a l’historial, esborrar-lo o canviar-li el nom també són canvis. Els preparem i els confirmem com una edició qualsevol. *(pausa 3 s)*

**Visual:** Explorador amb helloGit.py, notes.txt i prova.py, tots tres marcats SEGUIT.

## Terminal · `git rm prova.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git rm` | *git rm* esborra un fitxer seguit. | 2.5 s |
| `prova.py` | És el fitxer que ja no necessitem. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El fitxer desapareix de la carpeta i l’eliminació queda preparada per al proper *commit*. *(pausa 3.5 s)*

Sortida real:

```text
rm 'prova.py'
```

**Visual:** prova.py desapareix de l’explorador i apareix al panell PREPARACIÓ amb una D.

## Terminal · `git mv notes.txt notes.md`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git mv` | *git mv* canvia el nom d’un fitxer seguit. | 2.5 s |
| `notes.txt` | És el nom actual. | 2.5 s |
| `notes.md` | És el nom nou. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El fitxer ja té el nom nou i el canvi de nom també queda preparat. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** notes.txt es transforma en notes.md; al panell PREPARACIÓ apareix una R amb el nom antic i el nou.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La erra indica un canvi de nom, amb el nom antic i el nou. La de indica el fitxer esborrat. Tots dos canvis estan preparats. *(pausa 3.5 s)*

Sortida real:

```text
R  notes.txt -> notes.md
D  prova.py
```

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git commit -m "Ordena els fitxers del projecte"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Ordena els fitxers del projecte. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* guarda l’eliminació i el canvi de nom. Les versions antigues continuen a l’historial. *(pausa 3.5 s)*

Sortida real:

```text
[main 55f09bf] Ordena els fitxers del projecte
 2 files changed, 1 deletion(-)
 rename notes.txt => notes.md (100%)
 delete mode 100644 prova.py
```

**Visual:** Crear el node nou només en executar.

## Un error habitual, esborrar des de l’explorador

> **Un error habitual.** Parteix del seu propi punt; no s’encadena amb el camí principal.

Un altre cas. Si esborrem el fitxer des de l’explorador o des de l’editor, *Git* veu que falta, però l’eliminació encara no està preparada. *(pausa 3 s)*

**Visual:** Separador UN ERROR HABITUAL. prova.py s’envia a la paperera des de l’explorador.

## Terminal · `git status --short`

> **Un error habitual.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La de és a la segona columna. El fitxer falta a la carpeta, però el proper *commit* encara el conservaria. *(pausa 3.5 s)*

Sortida real:

```text
 D prova.py
```

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git add prova.py`

> **Un error habitual.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Preparar el fitxer que falta prepara la seva eliminació. Ara la de és a la primera columna, com abans. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Resum final

*git rm* esborra el fitxer i en prepara l’eliminació. *(pausa 2.5 s)*

*git mv* canvia el nom i el deixa preparat. *(pausa 2.5 s)*

Si esborrem des de l’explorador, després cal preparar l’eliminació. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques, esborra un fitxer seguit i canvia el nom d’un altre. Revisa l’estat breu abans de confirmar els dos canvis. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
