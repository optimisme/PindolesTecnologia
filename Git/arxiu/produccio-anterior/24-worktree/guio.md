# Worktree: prepara una correcció sense interrompre la feina

Veu: `ca-ES-EnricNeural` · Català · 104.2 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent en un repositori principal anomenat projecte. Main i salutacio apunten inicialment a B, però la branca activa a projecte és salutacio, que té helloGit.py editat sense preparar a print("Hola, Anna!"). L’índex i B contenen print("Hello Git!"). Main no està activa en cap altre worktree. Es crea correccio des de main amb git worktree add -b correccio ../projecte-correccio main, conservant el treball de salutacio. La carpeta nova és neta i té índex propi. Després de git worktree list, es fa cd ../projecte-correccio. Allí es canvia només la puntuació a print("Hello, Git!"), es prova i es confirma D a correccio. Es fa git switch main en aquesta carpeta i git merge --ff-only correccio, que avança main a D. La carpeta original continua a salutacio B amb el treball Hola, Anna! intacte. Es comprova l’estat dels dos directoris, es torna amb cd ../projecte i es retira la carpeta auxiliar neta amb git worktree remove sense --force. Main i correccio es conserven a D; només desapareix el worktree auxiliar. No es publica res. No es força una mateixa branca a estar activa en dues carpetes. Totes les proves i les retirades de carpetes es fan en directoris temporals.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.88 s)

**Locució:** Vint-i-quatrena lliçó, Worktree.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## La feina pendent pot quedar on és (6.9–17.0 s)

**Locució:** Tens feina pendent a salutacio i necessites corregir main. Amb worktree podem obrir una altra carpeta sense interrompre aquesta edició.

**Animació:** Carpeta projecte, branca salutacio i edició local Hola, Anna!. Main és a B amb Hello Git!, sense canvis.

## Creem correccio des de main (17.0–27.3 s)

**Locució:** Creem un worktree amb correccio, que parteix de main. La carpeta nova té fitxers i preparació propis; la feina pendent es queda a l’original.

**Animació:** S’afegeix projecte-correccio amb correccio a B i arbre net. Projecte conserva el canvi local.

**Comandes en pantalla:**

```bash
git worktree add -b correccio ../projecte-correccio main
```

## Entrem a la carpeta de la correcció (27.3–37.5 s)

**Locució:** Worktree list mostra carpetes i branques actives. Entrem a projecte correccio: hi tenim la versió de partida de main, amb el treball net.

**Animació:** Terminal list: projecte [salutacio], projecte-correccio [correccio]. Cd entra a la segona carpeta i l’editor mostra Hello Git!.

**Comandes en pantalla:**

```bash
git worktree list
cd ../projecte-correccio
```

## La correcció té el seu propi commit (37.5–47.3 s)

**Locució:** Afegim una coma al missatge, provem el programa i confirmem el retoc a correccio. Els canvis de salutacio queden fora d’aquest commit.

**Animació:** Editor de projecte-correccio mostra print("Hello, Git!"). Commit D a correccio, fill de B.

**Comandes en pantalla:**

```bash
python3 helloGit.py
git add helloGit.py
git commit -m "Corregeix la puntuacio"
```

## Main avança dins del segon worktree (47.3–58.6 s)

**Locució:** Canviem a main en aquesta carpeta: no està activa en cap altra. Un merge de tipus fast forward incorpora correccio, conservant la feina pendent de salutacio.

**Animació:** El segon worktree passa a main D. El primer continua a salutacio B, amb fitxer local Hola, Anna! i índex B.

**Comandes en pantalla:**

```bash
git switch main
git merge --ff-only correccio
```

## Un directori net i un amb feina pendent (58.6–70.0 s)

**Locució:** La carpeta de main és neta; la de salutacio manté la modificació pendent. Compartim historial i branques, però cada carpeta té el seu índex i fitxers.

**Animació:** Terminal status net al worktree auxiliar; git -C ../projecte status mostra M a la segona columna a l’original.

**Comandes en pantalla:**

```bash
git status --short
git -C ../projecte status --short
```

## La nostra edició continua intacta (70.0–79.3 s)

**Locució:** Tornem a projecte i revisem el canvi local: continua intacte. Main ja té la correcció i nosaltres seguim a salutacio.

**Animació:** Cd a projecte. Diff de Hello Git! a Hola, Anna! encara pendent. Main i correccio són a D, salutacio a B.

**Comandes en pantalla:**

```bash
cd ../projecte
git diff -- helloGit.py
```

## Retirem el worktree net (79.3–90.8 s)

**Locució:** Des de fora, retirem la carpeta auxiliar amb worktree remove. Ha d’estar neta. Les branques i el commit de la correcció es conserven al repositori.

**Animació:** La carpeta projecte-correccio es retira sense --force. List només mostra projecte [salutacio]. Log de main encara mostra D.

**Comandes en pantalla:**

```bash
git worktree remove ../projecte-correccio
git worktree list
git log -1 --oneline main
```

## Dues carpetes, un historial compartit (90.8–104.2 s)

**Locució:** Dues carpetes, amb fitxers i preparació separats, comparteixen l’historial. Hem corregit main sense interrompre salutacio. Retirar el worktree auxiliar conserva la correcció.

**Animació:** Tres targetes: fitxers separats, índex propi i historial compartit. La correcció es conserva després de retirar el worktree.
