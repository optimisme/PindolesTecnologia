# Add interactiu: prepara només una part del fitxer

Veu: `ca-ES-EnricNeural` · Català · 101.8 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent amb main al commit B i sense canvis preparats. helloGit.py ja és seguit; conté saluda, doble, suma i comiat, i imprimeix saluda() i comiat(). Les funcions doble i suma no es modifiquen. S’edita només el retorn de saluda de Hello Git! a Hola, Anna!, i el de comiat de Fins aviat! a Adeu!. Les dues edicions estan prou separades perquè git add -p helloGit.py mostri dos blocs independents amb el context per defecte. Es respon y al primer bloc (salutació) i n al segon (comiat). L’índex conté només la salutació nova; l’arbre de treball conserva tots dos canvis. Després del commit C, l’índex i HEAD coincideixen amb la salutació nova i el comiat antic; el treball manté el comiat pendent. No hi ha altres fitxers modificats ni remots. Els exemples complets són a exemples/. Les lletres i els hashes de pantalla són il·lustratius.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–7.00 s)

**Locució:** Vint-i-tresena lliçó, Add interactiu.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## No tot ha d’entrar al mateix commit (7.0–19.5 s)

**Locució:** Has modificat la salutació i el comiat dins del mateix fitxer. Vols confirmar només la salutació. No cal preparar tot el fitxer: podem triar els blocs de canvi.

**Animació:** Dues targetes d’un mateix helloGit.py: saluda retorna Hola, Anna! i comiat retorna Adeu!. La preparació encara és buida.

## Identifiquem els dos blocs (19.5–29.2 s)

**Locució:** Amb diff revisem què hem editat. En aquest exemple, els dos canvis estan prou separats perquè Git els presenti com dos blocs independents.

**Animació:** Terminal mostra dos blocs: -Hello Git! +Hola, Anna! a saluda, i -Fins aviat! +Adeu! a comiat.

**Comandes en pantalla:**

```bash
git diff -- helloGit.py
```

## Responem y a la salutació (29.2–41.7 s)

**Locució:** Fem add amb l’opció pe sobre el fitxer. Git ensenya el primer bloc i pregunta si el volem preparar. Responem i grega, de yes, per acceptar la salutació.

**Animació:** Terminal git add -p helloGit.py, primer bloc de saluda i pregunta Stage this hunk. Es respon y; no és una ordre nova de shell.

**Comandes en pantalla:**

```bash
git add -p helloGit.py
```

## Responem n al comiat (41.7–53.1 s)

**Locució:** La mateixa sessió mostra el segon bloc. Responem ena per no preparar-lo. El canvi continua al fitxer de treball, però queda fora de la preparació.

**Animació:** Continuació de la mateixa sessió interactiva, bloc 2/2 de comiat. Es respon n a Stage this hunk. La sessió acaba sense descartar el canvi.

## Preparat i pendent són diferents (53.1–66.3 s)

**Locució:** Diff amb staged mostra només la salutació preparada. Diff sense aquesta opció mostra el comiat que continua pendent. Les dues consultes ens permeten comprovar la selecció.

**Animació:** Dues terminals: git diff --staged mostra la salutació, git diff mostra el comiat.

**Comandes en pantalla:**

```bash
git diff --staged
git diff
```

## El commit incorpora només la salutació (66.3–78.3 s)

**Locució:** Fem commit de la preparació. El nou commit C inclou la salutació, mentre el comiat queda pendent al fitxer. El commit no elimina aquesta edició local.

**Animació:** Tres zones: treball amb salutació i comiat nous; índex i commit C amb salutació nova i comiat antic.

**Comandes en pantalla:**

```bash
git commit -m "Personalitza la salutacio"
```

## El comiat continua sense preparar (78.3–89.7 s)

**Locució:** Revisem el commit i l’estat. Status encara mostra el fitxer modificat sense preparar. Diff confirma que el canvi pendent és només el comiat.

**Animació:** Terminal show --stat HEAD, status amb M a la segona columna i diff del comiat. La salutació ja és al commit.

**Comandes en pantalla:**

```bash
git show --stat HEAD
git status --short
git diff
```

## Una selecció concreta per a cada commit (89.7–101.8 s)

**Locució:** Revisa els blocs, tria què prepares i comprova el resultat abans de confirmar. Add interactiu ajuda a separar feines, conservant al fitxer els canvis que encara no vols incloure.

**Animació:** Tres targetes: revisar, triar y/n i comprovar. Nota final: salutació confirmada, comiat encara pendent.
