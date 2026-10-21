# Fetch: consulta els canvis abans d’integrar-los

Veu: `ca-ES-EnricNeural` · Català · 99.5 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent i lineal A–B–C. Main local i la referència local origin/main són a B, amb índex i arbre nets. Origin al servidor ja té main a C, un nou commit compatible d’una altra còpia. B conté print("Hello Git!"); C conté print("Hola, Anna!"). Main és la branca activa i segueix origin/main. Git fetch origin descarrega C i actualitza origin/main sense modificar main, índex ni treball. Main..origin/main llista C i git diff main origin/main -- helloGit.py compara els dos continguts. Només després git merge --ff-only origin/main avança main de B a C, perquè no hi ha divergències i l’arbre continua net. No es fa cap push. Els hashes són il·lustratius. Les comprovacions utilitzen un remot local temporal.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.50 s)

**Locució:** Vintena lliçó, Fetch.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Què ha canviat al remot? (6.5–18.2 s)

**Locució:** Una altra persona ha publicat un commit. Vols mirar què ha canviat abans d’incorporar-lo al teu projecte. Fetch permet descarregar-lo i revisar-lo primer.

**Animació:** Dues targetes amb B local i C al servidor. El fitxer local conserva Hello Git!; el servidor té Hola, Anna!.

## La referència local pot estar desactualitzada (18.2–29.5 s)

**Locució:** Partim de main a B i sense canvis pendents. Origin main també apunta a B: és una referència local de l’última consulta, no una vista en directe del servidor.

**Animació:** Servidor main C; local main B i origin/main B. Terminal mostra status net i log de la referència a B.

**Comandes en pantalla:**

```bash
git status --short
git log -1 --oneline origin/main
```

## Fetch actualitza origin/main (29.5–42.0 s)

**Locució:** Fem fetch d’origin. Git descarrega C i actualitza origin main. Main continua a B, i els fitxers i la preparació conserven el contingut que teníem.

**Animació:** C viatja del servidor al repositori local. Origin/main es mou a C; main i fitxers continuen a B.

**Comandes en pantalla:**

```bash
git fetch origin
```

## Quins commits encara no té main? (42.0–52.3 s)

**Locució:** Consultem els commits d’origin main que main encara no conté. En aquest exemple només apareix C. Ja podem decidir si volem revisar-ne el canvi.

**Animació:** Graf local A–B–C, main B i origin/main C. Log main..origin/main mostra c95f4a7 Canvia missatge.

**Comandes en pantalla:**

```bash
git log --oneline main..origin/main
```

## Revisem la diferència sense integrar-la (52.3–64.0 s)

**Locució:** Amb diff comparem el contingut de les dues versions. Aquí només canvia el missatge. Aquesta consulta tampoc modifica el nostre fitxer de treball.

**Animació:** Terminal diff de B a C: -print("Hello Git!"), +print("Hola, Anna!").

**Comandes en pantalla:**

```bash
git diff main origin/main -- helloGit.py
```

## Descarregat no vol dir incorporat (64.0–75.3 s)

**Locució:** El commit ja és al repositori local, però encara no forma part de main. Podem continuar revisant-lo. En aquest cas, decidim incorporar-lo.

**Animació:** Targeta main B fitxer Hello Git! i targeta origin/main C fitxer Hola, Anna!. Nota: cap canvi local després de les consultes.

## Ara sí: main avança a C (75.3–85.0 s)

**Locució:** Com que no hi ha divergències, podem avançar main amb un merge de tipus fast forward. Ara el fitxer s’actualitza i provem el programa.

**Animació:** Main es mou de B a C; origin/main es conserva a C. El programa mostra Hola, Anna!.

**Comandes en pantalla:**

```bash
git merge --ff-only origin/main
python3 helloGit.py
```

## Descarregar, revisar i integrar (85.0–99.5 s)

**Locució:** Fetch descarrega i actualitza les referències remotes locals. Després pots revisar i integrar. Pull fa una descàrrega i tot seguit intenta integrar-la: convé distingir aquests dos passos.

**Animació:** Tres targetes Fetch descarrega, Log i diff revisen, Merge integra. Es recorda que origin/main és una referència local.
