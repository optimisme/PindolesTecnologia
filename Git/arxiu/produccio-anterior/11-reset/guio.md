# Reset: torna enrere un commit local

Veu: `ca-ES-EnricNeural` · Català · 94.7 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Main apunta a C, un commit propi encara no publicat. Arbre i índex nets. B conté print("Hello Git!"), C conté print("Hola, Anna!"). A, B, C i els hashes són il·lustratius. Es comparen dues alternatives independents que parteixen de C: soft i mixed. No s’executen seguides. HEAD segueix main; el reset mou main a B i C queda fora de la línia de main, sense esborrar immediatament l’objecte. No hi ha altres edicions pendents.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.62 s)

**Locució:** Onzena lliçó, Reset.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Vull continuar editant aquest canvi (6.6–17.8 s)

**Locució:** Has fet un commit, però encara hi vols treballar. És teu i no l’has publicat. Amb reset podem fer retrocedir la branca i conservar el canvi al fitxer.

**Animació:** Graf A–B–C, main a C. C conté el missatge Hola, Anna! i es marca com a només local.

## Main és a C. Tot està confirmat. (17.8–27.6 s)

**Locució:** Partim d’un directori net. Main és al commit C. El treball, la preparació i l’últim commit contenen la mateixa versió del fitxer.

**Animació:** Zones treball V2, preparació V2 i HEAD V2. Terminal status net i log C–B–A.

**Comandes en pantalla:**

```bash
git status --short
git log --oneline
```

## Soft mou la branca a B (27.6–38.9 s)

**Locució:** Fem reset amb soft i HEAD, titlla, u: el commit anterior. Main retrocedeix a B, però el fitxer i la preparació conserven el contingut de C.

**Animació:** Main passa de C a B; C queda atenuat. Zones V2 V2 V1.

**Comandes en pantalla:**

```bash
git reset --soft HEAD~1
```

## El canvi continua preparat (38.9–49.2 s)

**Locució:** Status mostra el canvi preparat. Diff amb staged el compara amb B. Podem continuar editant, tornar a preparar el fitxer i fer un altre commit.

**Animació:** M a la primera columna. Diff staged mostra la substitució del missatge. No s’executa cap altre reset.

**Comandes en pantalla:**

```bash
git status --short
git diff --staged
```

## Tornem al punt de partida C (49.2–60.9 s)

**Locució:** Ara comparem una alternativa. Imaginem de nou el punt de partida: main a C i tot net. Aquesta opció no s’executa després de l’anterior.

**Animació:** Cartell ALTERNATIVA INDEPENDENT. Graf main C i les tres zones V2. Sense comandes per reconstruir el cas.

## Mixed deixa el canvi sense preparar (60.9–71.0 s)

**Locució:** Amb mixed, main també retrocedeix a B. La preparació passa al contingut de B, però el fitxer conserva el canvi. Ara queda pendent de preparar.

**Animació:** Graf main B; C atenuat; zones treball V2, preparació V1, HEAD V1.

**Comandes en pantalla:**

```bash
git reset --mixed HEAD~1
```

## El fitxer es conserva en tots dos casos (71.0–82.0 s)

**Locució:** Soft deixa el canvi preparat. Mixed el deixa sense preparar. En tots dos casos main apunta a B i el fitxer manté el missatge nou.

**Animació:** Dues targetes independents SOFT V2/V2/V1 i MIXED V2/V1/V1. Estat M en columna 1 o 2 respectivament.

## Un pas enrere per continuar treballant (82.0–94.7 s)

**Locució:** Aquí hem reescrit una branca local encara no publicada. C ja no surt a la seva línia, però pot continuar al repositori. A la pròxima lliçó el recuperarem amb reflog.

**Animació:** Main B i C atenuat amb etiqueta Fora de main. Enllaç visual cap a la lliçó RE FLOG. No es mostra hard ni force push.
