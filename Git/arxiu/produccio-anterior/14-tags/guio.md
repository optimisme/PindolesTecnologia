# Tags: identifica una versió del projecte

Veu: `ca-ES-EnricNeural` · Català · 99.1 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent, main a B i arbre net. Origin/main també apunta a B i main té upstream configurat. B conté print("Hello Git!") a helloGit.py. No existeix v1.0. Es crea una etiqueta anotada amb -a i missatge -m. Després s’edita el fitxer a print("Hola, Anna!") i es confirma C, fill de B. L’etiqueta continua referint-se a B. Es publica primer main amb git push i després explícitament v1.0. No es crea cap Release de GitHub. Els grafs i hashes són didàctics; les proves fan servir un remot local temporal.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.50 s)

**Locució:** Catorzena lliçó, Tags.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Aquesta és la versió 1.0 (6.5–19.6 s)

**Locució:** Avui entregues una versió que funciona. Demà continuaràs canviant el projecte. Com identifiques exactament el punt de l’entrega? Amb una etiqueta, o tag.

**Animació:** Graf A–B, B ressaltat amb un marcador v1.0 que apareix sobre el commit.

## El commit B és el de l’entrega (19.6–31.8 s)

**Locució:** Partim de main al commit B, sense canvis pendents. Provem el programa. L’etiqueta assenyalarà aquest commit; les edicions sense confirmar no hi entrarien.

**Animació:** Fitxer de B, sortida Hello Git! i estat net.

**Comandes en pantalla:**

```bash
python3 helloGit.py
git status --short
```

## Creem una etiqueta anotada (31.8–43.2 s)

**Locució:** Creem ve u punt zero amb tag, l’opció a i un missatge. És una etiqueta anotada: afegeix informació sobre l’entrega sense crear un commit nou.

**Animació:** Animació etiqueta v1.0 lligada a B. El graf conserva A i B sense nous nodes.

**Comandes en pantalla:**

```bash
git tag -a v1.0 -m "Primera entrega"
```

## Podem trobar i revisar l’entrega (43.2–55.1 s)

**Locució:** Tag amb list mostra les etiquetes. Show permet consultar-ne la informació i el commit associat. Ja tenim un nom fàcil de recordar per aquesta entrega.

**Animació:** Terminal mostra v1.0, etiqueta anotada i commit b62d8e1.

**Comandes en pantalla:**

```bash
git tag --list
git show v1.0
```

## Main avança. V1.0 es queda a B. (55.1–64.8 s)

**Locució:** Ara canviem el missatge i fem un altre commit. Main avança a C. L’etiqueta continua a B: seguir treballant a la branca no la mou.

**Animació:** Editor a Hola, Anna!; C apareix amb main mentre v1.0 es conserva a B.

**Comandes en pantalla:**

```bash
git add helloGit.py
git commit -m "Canvia missatge"
```

## Què contenia la versió 1.0? (64.8–74.6 s)

**Locució:** Amb show i el nom de l’etiqueta podem llegir aquell fitxer tal com era a l’entrega. El nostre fitxer actual continua amb el missatge nou.

**Animació:** Dues targetes editor C amb Hola, Anna! i sortida de git show v1.0:helloGit.py amb Hello Git!.

**Comandes en pantalla:**

```bash
git show v1.0:helloGit.py
```

## Publiquem main i després v1.0 (74.6–86.4 s)

**Locució:** Publiquem els commits amb push. Després enviem explícitament l’etiqueta a origin. Així el remot també podrà identificar l’entrega pel mateix nom.

**Animació:** Main C viatja al remot; després v1.0 apareix també a B del remot. Dues accions consecutives.

**Comandes en pantalla:**

```bash
git push
git push origin v1.0
```

## Un nom per tornar a una entrega (86.4–99.1 s)

**Locució:** Una branca avança amb els commits. Una etiqueta identifica un punt concret de l’historial. Crea-la al commit correcte i publica-la quan vulguis compartir aquella versió.

**Animació:** Graf A–B–C amb main C i v1.0 B, repetit al remot; resum crear, consultar, publicar.
