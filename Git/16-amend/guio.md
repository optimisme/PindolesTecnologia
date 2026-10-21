# Lliçó 16 · Amend: completa l’últim commit local

**Sèrie:** Píndoles de Git · **Capçalera:** AMEND — Completa l’últim commit local  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/16-amend.sh`](../practiques/16-amend.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Setzena lliçó. *Amend*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a afegir un fitxer oblidat a l’últim *commit* encara no publicat i entendre per què canvia l’identificador. *(pausa 2.5 s)*

Acabem de confirmar la salutació personalitzada, però hem oblidat les notes que l’expliquen. Encara no hem publicat res. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Completar abans de publicar

Doble guionet *amend* crea un *commit* nou que substitueix l’últim de la branca, amb el contingut que haguem preparat. Com que encara no l’hem publicat, ningú més el té. *(pausa 3 s)*

**Visual:** Graf A, B i C, amb l’etiqueta NO PUBLICAT a C. notes.md NOU al treball.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només hi ha les notes noves. Comprovem que no hi ha res més abans de substituir el *commit*. *(pausa 3.5 s)*

Sortida real:

```text
?? notes.md
```

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git add notes.md`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Les notes queden preparades. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git diff --staged --stat`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Revisem el resum del que hem preparat. | 2.5 s |
| `--stat` | Doble guionet *stat* mostra només la llista de fitxers i quantes línies canvien. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només hi surten les notes. No afegirem cap altra feina per accident. *(pausa 3.5 s)*

Sortida real:

```text
 notes.md | 1 +
 1 file changed, 1 insertion(+)
```

**Visual:** Sortida real amb notes.md ressaltat.

## Terminal · `git commit --amend --no-edit`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Substituïm l’últim *commit* amb *git commit*. | 2.5 s |
| `--amend` | Crea un *commit* nou amb el mateix pare que l’anterior i hi afegeix el contingut preparat. | 2.5 s |
| `--no-edit` | Conserva el missatge anterior sense obrir l’editor. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* apunta a un *commit* nou, amb el mateix pare i un identificador diferent. El missatge i l’autoria es conserven, i les notes ja hi són. *(pausa 3.5 s)*

Sortida real:

```text
[main 970cb92] Personalitza la salutacio
 Date: Tue Oct 20 12:07:00 2026 +0200
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 notes.md
```

**Visual:** Atenuar C fora de la línia de main i crear C′ des de B. No dibuixar C′ com a fill de C.

## Terminal · `git show --stat HEAD`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | Comprovem el *commit* resultant. | 2.5 s |
| `HEAD` | Assenyala el *commit* actual, el que acabem de crear. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El mateix missatge inclou ara la salutació i les notes. *(pausa 3.5 s)*

Sortida real:

```text
commit 970cb92b28f371b87aa46b917799ef03c2300547
Author: Anna Puig <anna@example.com>
Date:   Tue Oct 20 12:07:00 2026 +0200

    Personalitza la salutacio

 helloGit.py | 2 +-
 notes.md    | 1 +
 2 files changed, 2 insertions(+), 1 deletion(-)
```

**Visual:** Sortida real amb el missatge i la llista de fitxers; main a C′.

## Un altre cas, canviar només el missatge

> **Un altre cas.** Parteix del seu propi punt; no s’encadena amb el camí principal.

En un cas diferent, tornem al *commit* original sense res preparat. També podem substituir-lo només per corregir el missatge. *(pausa 3 s)*

**Visual:** Separador UN ALTRE CAS. C amb la preparació igual que C, sense les notes.

## Terminal · `git commit --amend -m "Personalitza la salutacio per a l'Anna"`

> **Un altre cas.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Escrivim el missatge nou per a l’últim *commit*. | 2.5 s |
| `-m` | Introdueix el missatge nou. | 2.5 s |
| `"Personalitza la salutacio per a l'Anna"` | És el text nou. Com que no hem preparat res, el contingut no canvia. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Es crea un altre identificador, amb el mateix contingut i el mateix pare. *(pausa 3.5 s)*

Sortida real:

```text
[main 75273ed] Personalitza la salutacio per a l'Anna
 Date: Tue Oct 20 12:07:00 2026 +0200
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Comparació CONTINGUT IGUAL / MISSATGE DIFERENT / IDENTIFICADOR DIFERENT.

## Resum final

Doble guionet *amend* substitueix l’últim *commit*; no hi afegeix un fill. *(pausa 2.5 s)*

Abans de fer-ho, revisem què hem preparat. *(pausa 2.5 s)*

Només ho fem amb l’últim *commit* propi, encara no publicat. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques, sense publicar, afegeix un fitxer oblidat a l’últim *commit*. Compara el pare, el missatge, els fitxers i l’identificador abans i després. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
