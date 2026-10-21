# Stash: aparca la feina pendent

Veu: `ca-ES-EnricNeural` · Català · 77.8 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Branca salutacio creada des de main al mateix commit B. HelloGit.py està seguit i confirmat amb print("Hello Git!"); ara té l'edició no preparada print("Hola, Anna!"). Notes.md és un fitxer nou no seguit i no ignorat. No hi ha canvis preparats a l'índex. Les comandes usen helloGit.py i notes.md en minúscula. No es modifica main durant l'exemple. Stash crea una entrada separada; no afegeix cap commit a la branca. Les lletres són didàctiques.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.58 s)

**Locució:** Vuitena lliçó, Stash.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## La feina encara no està acabada (6.6–15.5 s)

**Locució:** Tens una salutació a mig fer i et demanen arreglar un error a main. Com aparques aquesta feina sense perdre-la?

**Animació:** Un editor mostra el missatge pendent i notes.md. Apareix una petició per atendre main, sense modificar encara la branca.

## Un fitxer modificat i un de nou (15.5–23.4 s)

**Locució:** Hi ha un fitxer modificat i un de nou. Git status els mostra com a feina pendent de commit.

**Animació:** La terminal mostra M a la segona columna per a helloGit.py i ?? per a notes.md. Encara no hi ha canvis preparats.

**Comandes en pantalla:**

```bash
git status --short
```

## Stash aparta els canvis (23.4–32.7 s)

**Locució:** Fem git stash push amb l'opció u. Guardem els canvis i els fitxers nous no seguits; el directori de treball queda net.

**Animació:** Els dos canvis es copien a una entrada separada. HelloGit.py torna al contingut confirmat i notes.md desapareix del directori de treball.

**Comandes en pantalla:**

```bash
git stash push -u -m "Salutacio pendent"
```

## La feina queda a l'stash (32.7–41.6 s)

**Locució:** L'entrada conserva la feina i un missatge per reconèixer-la. Git stash list mostra les entrades que tenim desades.

**Animació:** El calaix de stash conté helloGit.py i notes.md. La terminal mostra stash@{0}: On salutacio: Salutacio pendent.

**Comandes en pantalla:**

```bash
git stash list
```

## Ara podem canviar a main (41.6–50.5 s)

**Locució:** Ara canviem a main per atendre l'altra tasca. La feina continua a l'stash, sense afegir cap commit a salutació.

**Animació:** La branca activa passa a main, que mostra el missatge original. L'entrada d'stash queda visible i el commit de salutacio no es mou.

**Comandes en pantalla:**

```bash
git switch main
```

## Recuperem la branca de treball (50.5–58.8 s)

**Locució:** Quan acabem, tornem a salutació. Comprovem que el directori de treball és net abans de recuperar els canvis.

**Animació:** Tornem a salutacio. Git status --short no produeix cap línia. L'entrada d'stash encara hi és.

**Comandes en pantalla:**

```bash
git switch salutacio
git status --short
```

## La feina torna a l'editor (58.8–67.9 s)

**Locució:** Amb git stash pop recuperem el fitxer modificat i el fitxer nou. Si s'apliquen bé, aquesta entrada s'elimina de la llista.

**Animació:** Els canvis tornen del calaix al directori de treball. El missatge personalitzat i notes.md reapareixen. L'aplicació és compatible i l'entrada es retira.

**Comandes en pantalla:**

```bash
git stash pop
git stash list
```

## Aparca. Canvia de tasca. Recupera. (67.9–77.8 s)

**Locució:** La feina torna a estar pendent de commit. Stash serveix per fer una pausa; després la podem continuar i confirmar quan estigui llesta.

**Animació:** Resum dels tres passos. La feina recuperada continua sense confirmar, i els punters de main i salutacio es conserven al commit B.

**Comandes en pantalla:**

```bash
git stash push -u
git stash list
git stash pop
```
