# Forks i upstream: contribueix a un projecte

Veu: `ca-ES-EnricNeural` · Català · 97.0 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent amb dades inventades. El projecte original hello-git és a GitHub i accepta contribucions; l’autor de la proposta no hi publica directament. Es crea un fork propi amb main a B i es clona amb el directori explícit hello-git. Origin apunta al fork propi i upstream s’afegeix apuntant a l’original. URL-del-fork i URL-original són marcadors que cal substituir per les adreces reals. L’original rep després C, una actualització de README.md que no toca helloGit.py; el fork i main local continuen a B. Amb arbre net s’executen fetch upstream, merge --ff-only upstream/main i push origin main per sincronitzar local i fork a C. Després es crea salutacio, s’edita helloGit.py de print("Hello Git!") a print("Hola, Anna!"), es prova, es confirma D i es publica al fork amb push -u origin salutacio. La proposta de GitHub té base repository projecte/hello-git, base main, head fork alumne/hello-git, compare salutacio. No es fusiona la proposta. Les interfícies són esquemes i no es crea cap fork, PR ni publicació real; les proves usen dos remots bare locals temporals.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–7.21 s)

**Locució:** Vint-i-unena lliçó, Forks i upstream.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Original, fork i còpia local (7.2–17.7 s)

**Locució:** Vols contribuir a un projecte on no publiques directament. Pots crear un fork al teu compte, treballar-hi i proposar els canvis al projecte original.

**Animació:** Esquema de tres repositoris: còpia local, fork propi a GitHub i projecte original a GitHub.

## Una còpia del projecte al teu compte (17.7–29.0 s)

**Locució:** A GitHub, creem un fork del projecte. El fork és un altre repositori al nostre compte. Encara no tenim una còpia de treball a l’ordinador.

**Animació:** Interfície esquemàtica projecte/hello-git amb botó Fork. Apareix alumne/hello-git amb main B. Local encara buit.

## Origin apunta al nostre fork (29.0–38.9 s)

**Locució:** Clonem el fork al directori hello git i hi entrem. El remot origin queda configurat amb l’adreça del nostre repositori a GitHub.

**Animació:** Fork B es clona al repositori local B. S’etiqueta la connexió origin i es mostra el directori hello-git.

**Comandes en pantalla:**

```bash
git clone <URL-del-fork> hello-git
cd hello-git
```

## Afegim el remot upstream (38.9–49.2 s)

**Locució:** Afegim upstream amb l’adreça del projecte original i comprovem els remots. Origin és el fork propi; upstream és el nom que donem a l’original.

**Animació:** Dues connexions locals: origin al fork, upstream a l’original. Remote -v mostra adreces inventades amb fetch i push.

**Comandes en pantalla:**

```bash
git remote add upstream <URL-original>
git remote -v
```

## Incorporem les novetats de l’original (49.2–61.0 s)

**Locució:** L’original ha avançat a C. Amb l’arbre net, descarreguem d’upstream, avancem main sense divergències i publiquem main al nostre fork. Ara les tres còpies són a C.

**Animació:** Original main C, local i fork B. Fetch actualitza upstream/main; merge actualitza main local; push origin main actualitza només el fork.

**Comandes en pantalla:**

```bash
git fetch upstream
git merge --ff-only upstream/main
git push origin main
```

## Creem salutacio i editem el fitxer (61.0–73.8 s)

**Locució:** Creem salutacio des de main actualitzada. Editem el missatge en aquesta branca. La millora es podrà revisar per separat abans d’incorporar-la al projecte original.

**Animació:** Branca salutacio creada a C. Editor canvia helloGit.py a print("Hola, Anna!"). Main es conserva a C.

**Comandes en pantalla:**

```bash
git switch -c salutacio
```

## La nostra branca s’envia a origin (73.8–85.1 s)

**Locució:** Provem el programa, preparem el fitxer i fem commit. Després publiquem salutacio a origin: els commits van al nostre fork, mentre l’original continua intacte.

**Animació:** Terminal de quatre comandes. D avança salutacio local i viatja al fork. Original main continua a C.

**Comandes en pantalla:**

```bash
python3 helloGit.py
git add helloGit.py
git commit -m "Personalitza la salutacio"
git push -u origin salutacio
```

## La proposta travessa dos repositoris (85.1–97.0 s)

**Locució:** Obrim una pull request amb main de l’original com a destinació i salutacio del nostre fork com a origen. Publiquem al fork i proposem a l’original: aquesta és la connexió.

**Animació:** Interfície GitHub esquemàtica: base repository projecte/hello-git, base main; head fork alumne/hello-git, compare salutacio. Diff i proposta oberta, sense fusió.
