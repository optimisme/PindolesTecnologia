# Blame: investiga l’origen d’una línia

Veu: `ca-ES-EnricNeural` · Català · 94.8 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent amb historial lineal A–B–C, main a C i arbre net. A conté tres línies a helloGit.py: # Programa de salutació; salutacio = "Hello Git!"; print(salutacio). B canvia només la línia 2 a missatge = "Hola, Anna!", i introdueix NameError a la línia 3. C només canvia la línia 3 a print( salutacio ), un canvi d’espais. Blame sense -w atribueix la línia 3 a C, però la regressió es va introduir a B. Els hashes a31b2c4, b62d8e1 i c95f4a7 són il·lustratius, igual que l’autor Demo i les dates. No hi ha canvis sense confirmar ni publicació. Les comandes només consulten l’historial; la prova del programa falla deliberadament.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.58 s)

**Locució:** Dissetena lliçó, Blame.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Quan va canviar aquesta línia? (6.6–18.7 s)

**Locució:** El programa falla en imprimir una variable. Volem entendre d’on surt aquella línia i quins canvis l’envolten. Blame ens ajuda a començar la investigació.

**Animació:** Editor amb tres línies: missatge definit a la 2 i print( salutacio ) a la 3. NameError en executar.

**Comandes en pantalla:**

```bash
python3 helloGit.py
```

## Cada línia té un commit associat (18.7–29.1 s)

**Locució:** Git blame mostra el commit que va modificar per últim cada línia, amb informació d’autoria i data. Aquí, la línia que falla apunta a C.

**Animació:** Terminal amb blame: línia 1 A, línia 2 B, línia 3 C. Es ressalten el hash i el número de línia.

**Comandes en pantalla:**

```bash
git blame helloGit.py
```

## Ens centrem en la línia tres (29.1–38.9 s)

**Locució:** Amb l’opció ela i el rang tres, tres, consultem només aquella línia. Copiem l’identificador de C per revisar el canvi que va fer.

**Animació:** Terminal blame -L 3,3 i la línia 3 de C. Es remarca c95f4a7, identificador il·lustratiu.

**Comandes en pantalla:**

```bash
git blame -L 3,3 helloGit.py
```

## C només hi havia afegit espais (38.9–50.5 s)

**Locució:** Show ens ensenya la diferència de C. Només hi va afegir espais: la variable ja era incorrecta abans. L’última modificació no és necessàriament l’origen de l’error.

**Animació:** Diff de C: -print(salutacio), +print( salutacio ). Etiqueta CANVI DE FORMAT.

**Comandes en pantalla:**

```bash
git show c95f4a7 -- helloGit.py
```

## On es defineix aquesta variable? (50.5–62.4 s)

**Locució:** Mirem la línia anterior. Ara defineix missatge, però després imprimim salutacio. Consultem aquesta altra línia amb blame: ens porta al commit B.

**Animació:** Editor connecta missatge de línia 2 amb salutacio de línia 3. Terminal blame -L 2,2 atribueix la definició a B.

**Comandes en pantalla:**

```bash
git blame -L 2,2 helloGit.py
```

## B va canviar el nom de la variable (62.4–72.9 s)

**Locució:** Show confirma que B havia canviat el nom de la variable sense actualitzar la línia que l’utilitza. Aquí tenim el canvi que va introduir l’error.

**Animació:** Diff de B: -salutacio = "Hello Git!", +missatge = "Hola, Anna!"; print(salutacio) es manté com a context.

**Comandes en pantalla:**

```bash
git show b62d8e1 -- helloGit.py
```

## Una línia sola no explica tot el canvi (72.9–83.2 s)

**Locució:** Podem consultar també l’historial del fitxer. Blame ens orienta cap a un commit; show i el context ens permeten entendre què va passar realment.

**Animació:** Graf A correcte, B introdueix l’error i C modifica el format. Log del fitxer mostra C, B i A.

**Comandes en pantalla:**

```bash
git log --oneline -- helloGit.py
```

## Línia, commit i context (83.2–94.8 s)

**Locució:** Comença per la línia, revisa el commit i segueix les seves dependències. Blame és una eina per comprendre l’historial, no una prova automàtica de la causa d’un error.

**Animació:** Tres targetes: Blame localitza, Show explica, Context completa. La consulta no modifica els fitxers.
