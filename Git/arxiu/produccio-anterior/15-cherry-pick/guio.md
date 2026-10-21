# Cherry-pick: porta una correcció a una altra branca

Veu: `ca-ES-EnricNeural` · Català · 95.8 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent amb arbre net. A–B a main; salutacio parteix de B i conté C i D. B té print(salutacio), sense definir salutacio, a helloGit.py. C afegeix notes.md d’una funcionalitat inacabada i no toca helloGit.py. D corregeix només helloGit.py a print("Hello Git!"). D es representa com d04f7a2 i C com c95f4a7, hashes il·lustratius. Main continua a B i no conté notes.md. El canvi de D no depèn de C i s’aplica netament a main. Cherry-pick sense --ff crea E, un commit nou amb pare B, mentre D té pare C. No hi ha publicació. El cas de conflicte és una alternativa condicional explicada al final.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.50 s)

**Locució:** Quinzena lliçó, Cherry pick.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Només vull aquest commit (6.5–18.0 s)

**Locució:** A la branca de proves hi ha una funcionalitat a mig fer i una correcció útil. Volem portar només la correcció a main. Aquí entra cherry pick.

**Animació:** Graf A–B, salutacio C–D. C etiquetat Funcionalitat pendent, D Correcció. Main a B.

## C és la prova. D corregeix l’error. (18.0–30.4 s)

**Locució:** Amb log consultem els commits de salutacio. C afegeix unes notes de la prova. D corregeix el programa. Copiem l’identificador de D.

**Animació:** Log de salutacio mostra D d04f7a2 Corregeix missatge, C c95f4a7 Notes de la prova i B.

**Comandes en pantalla:**

```bash
git log --oneline salutacio
```

## La correcció és independent (30.4–41.9 s)

**Locució:** Revisem D amb show. Només canvia el missatge que fallava. En aquest exemple no depèn de la funcionalitat anterior i es pot aplicar a main.

**Animació:** Terminal diff entre print(salutacio) i print("Hello Git!"); notes.md queda fora del canvi de D.

**Comandes en pantalla:**

```bash
git show d04f7a2 -- helloGit.py
```

## Ens situem a main amb l’arbre net (41.9–50.7 s)

**Locució:** Comprovem que no hi hagi canvis pendents i anem a main. Cherry pick aplicarà el canvi a la branca on ens trobem.

**Animació:** Punter ACTIVA passa de salutacio a main. Main B encara executa print(salutacio).

**Comandes en pantalla:**

```bash
git status --short
git switch main
```

## D es reaplica com un commit nou (50.7–62.0 s)

**Locució:** Executem cherry pick amb l’identificador de D. Git reaplica el seu canvi i crea E sobre main. D continua a salutacio, amb el seu historial original.

**Animació:** El canvi de D viatja a main; apareix E fill de B. D i E amb colors iguals però identificadors diferents.

**Comandes en pantalla:**

```bash
git cherry-pick d04f7a2
```

## Main funciona sense la prova pendent (62.0–73.5 s)

**Locució:** Provem el programa i revisem l’últim commit. E té un identificador nou. El fitxer de notes de C no ha entrat a main: només hem aplicat la correcció.

**Animació:** Sortida Hello Git!, log main E i B. Notes.md només existeix a salutacio.

**Comandes en pantalla:**

```bash
python3 helloGit.py
git log -1 --oneline
```

## Pot caldre resoldre un conflicte (73.5–84.6 s)

**Locució:** Si hi ha un conflicte, Git s’atura. Resolem el fitxer, el preparem i continuem. O podem avortar l’operació per tornar al punt de partida.

**Animació:** Cas condicional independent. Dues terminals alternatives: resoldre amb add i continue, o abort. No es mostren com una seqüència única.

**Comandes en pantalla:**

```bash
git add helloGit.py
git cherry-pick --continue
git cherry-pick --abort
```

## Seleccionar, revisar i reaplicar (84.6–95.8 s)

**Locució:** Cherry pick ens permet portar un canvi concret a una altra branca. Revisa’n les dependències, tria la destinació i comprova el resultat abans de compartir-lo.

**Animació:** Graf final main E i salutacio D. C queda només a salutacio. Targetes Selecciona D, Reaplica a main, Prova E.
