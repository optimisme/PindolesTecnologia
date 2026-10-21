# Bisect: troba el primer commit que falla

Veu: `ca-ES-EnricNeural` · Català · 103.5 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent amb vuit commits lineals A–H. Main és a H amb arbre net. El fitxer notes.md canvia a cada commit. A, B i C executen print("Hello Git!"); D substitueix la línia per print(salutacio), sense definir la variable, i l’error es conserva a E, F, G i H. L’etiqueta v1.0 és a A, una versió ja provada com a bona amb python3 helloGit.py. H falla amb la mateixa prova. No hi ha errors intermitents ni versions impossibles de provar. Amb aquesta història, la seqüència de Git comprovada és: start, bad (H), good v1.0 (A), checkout temporal D; prova D i bad; checkout temporal C; prova C i good; resultat D primer bad. Quan es troba D, HEAD continua a C fins al bisect reset, que retorna a main H. Main no es mou durant la investigació. D es representa amb d04f7a2 i la resta de hashes són il·lustratius. La recerca no crea commits ni arregla el programa.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.71 s)

**Locució:** Divuitena lliçó, Bisect.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Quin commit va introduir l’error? (6.7–19.5 s)

**Locució:** A l’última entrega el programa funcionava. Ara, a main, falla. Hi ha diversos commits entremig: podem trobar el primer que va introduir l’error sense provar-los tots.

**Animació:** Graf de vuit commits A–H. v1.0 a A correcte, main H amb NameError. D encara no està identificat visualment.

## Una versió bona i una de dolenta (19.5–33.6 s)

**Locució:** Necessitem una prova que puguem repetir. Aquí executem el programa. Sabem que ve u punt zero, a A, funciona i H falla. Comencem sense canvis locals pendents.

**Animació:** Dues targetes A v1.0 sortida Hello Git! i H main NameError. Terminal status sense sortida.

**Comandes en pantalla:**

```bash
git status --short
```

## Git proposa una versió intermèdia (33.6–47.3 s)

**Locució:** Iniciem bisect, marquem l’actual com a dolenta i indiquem l’etiqueta bona. Git selecciona D per provar-lo. Main continua a H; només canviem temporalment la versió de treball.

**Animació:** Comandes start, bad, good v1.0. HEAD passa d’H a D en estat separat; main no es mou.

**Comandes en pantalla:**

```bash
git bisect start
git bisect bad
git bisect good v1.0
```

## D falla. Reduïm el tram. (47.3–57.3 s)

**Locució:** Executem la mateixa prova a D. Falla, i ho indiquem amb bad. Ara l’error ja existia a D: podem centrar-nos en el tram entre A i D. Git ens situa a C.

**Animació:** Prova a D mostra NameError. D es marca bad; Git proposa C. Interval actiu A–D, main H.

**Comandes en pantalla:**

```bash
python3 helloGit.py
git bisect bad
```

## C funciona. El primer que falla és D. (57.3–69.5 s)

**Locució:** Provem C i funciona. Ho marquem com a bo. C i D són consecutius: Git ja pot identificar D com el primer commit dolent dins del tram investigat.

**Animació:** Prova a C mostra Hello Git!. Good fixa C com a extrem bo; resultat d04f7a2 is the first bad commit. HEAD continua a C i main H.

**Comandes en pantalla:**

```bash
python3 helloGit.py
git bisect good
```

## Mirem què va canviar a D (69.5–81.4 s)

**Locució:** Amb show revisem el commit trobat. Aquí substituïa el missatge per una variable no definida. Ja tenim un canvi concret per investigar i corregir.

**Animació:** Diff de D: -print("Hello Git!"), +print(salutacio). Consulta explícita del hash sense canviar HEAD.

**Comandes en pantalla:**

```bash
git show d04f7a2 -- helloGit.py
```

## Tornem a main amb bisect reset (81.4–92.2 s)

**Locució:** Quan acabem, fem bisect reset per tornar al punt de partida. Main continua a H. La investigació no ha creat commits ni ha corregit encara l’error.

**Animació:** HEAD torna de C a main H. No apareix cap commit nou. H conserva el programa que falla.

**Comandes en pantalla:**

```bash
git bisect reset
```

## Provar, classificar i reduir el tram (92.2–103.5 s)

**Locució:** Amb una prova repetible, bisect redueix el tram fins a trobar el primer commit que falla. Cal provar cada versió de la mateixa manera i sortir de la cerca quan acabem.

**Animació:** Tres targetes prova repetible, good o bad, primer commit que falla. Nota: D identificat; correcció encara pendent.
