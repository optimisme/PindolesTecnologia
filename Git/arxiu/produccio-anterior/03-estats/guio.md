# Desar, preparar i fer commit: els tres estats

Veu: `ca-ES-EnricNeural` · Català · 82.2 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Fitxer helloGit.py ja seguit per Git i confirmat amb print("Hello Git!"). Sense canvis pendents. Les etiquetes V1, V2 i V3 representen continguts del mateix fitxer, no fitxers duplicats.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.75 s)

**Locució:** Tercera lliçó, Els tres estats.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Has editat després de git add? (6.8–16.9 s)

**Locució:** Has desat el fitxer i has fet git add. Després hi escrius una altra línia. Si ara fas commit, hi entrarà també aquesta última línia?

**Animació:** Dues còpies conceptuals del mateix fitxer: la versió preparada i una edició posterior amb una segona línia.

## Desar és només el primer pas (16.9–26.8 s)

**Locució:** Tres espais: carpeta de treball, preparació i historial. Desar a l'editor només modifica el primer; encara no crea cap commit.

**Animació:** Tres zones amb una còpia V1 del fitxer i una fletxa per a add i una altra per a commit.

## El canvi és al fitxer de treball (26.8–34.9 s)

**Locució:** El fitxer ja té un commit. Canviem el missatge: git diff mostra els canvis que encara no hem preparat.

**Animació:** La carpeta de treball passa a V2. Preparació i historial continuen a V1. La terminal mostra el diff del missatge.

**Comandes en pantalla:**

```bash
git diff
```

## Add copia l'estat d'ara (34.9–43.7 s)

**Locució:** Git add copia l'estat actual a la preparació. Git diff amb l'opció staged mostra què entrarà al pròxim commit.

**Animació:** Una còpia V2 viatja a la preparació, mentre que V2 també continua al directori de treball i l'historial encara és V1.

**Comandes en pantalla:**

```bash
git add helloGit.py
git diff --staged
```

## La preparació no canvia sola (43.7–53.4 s)

**Locució:** Després d'add, afegim una segona línia. Aquesta edició queda a la carpeta de treball; la preparació conserva l'estat anterior.

**Animació:** V3 conté un comiat nou. La preparació conserva V2 i l'historial V1. Es remarca que add no és un vincle viu amb el fitxer.

## Dos diffs. Dues comparacions. (53.4–63.3 s)

**Locució:** Git status mostra canvis preparats i pendents al mateix fitxer. Git diff mostra els pendents; l'opció staged, els preparats.

**Animació:** Dos terminals mostren git diff amb la línia nova i git diff --staged amb el canvi de salutació. MM indica canvis als dos llocs.

**Comandes en pantalla:**

```bash
git status --short
git diff
git diff --staged
```

## Es confirma el que has preparat (63.3–72.5 s)

**Locució:** Si fem commit ara, guardem només el que havíem preparat. L'última línia continua al fitxer, però encara no és a l'historial.

**Animació:** L'historial avança a V2. Preparació i historial coincideixen; el fitxer de treball encara és V3 i té un canvi pendent.

**Comandes en pantalla:**

```bash
git commit -m "Canvia salutacio"
git status --short
```

## Desar. Preparar. Confirmar. (72.5–82.2 s)

**Locució:** Per incloure-la, repetim git add i fem un altre commit. Recorda: desar modifica, add prepara i commit guarda a l'historial.

**Animació:** V3 es copia a la preparació i després es confirma. Les tres zones acaben amb el mateix contingut, sense canvis pendents.

**Comandes en pantalla:**

```bash
git add helloGit.py
git commit -m "Afegeix comiat"
```
