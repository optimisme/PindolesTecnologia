# Pull requests: revisa i integra una feina en equip

Veu: `ca-ES-EnricNeural` · Català · 111.0 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Projecte independent ja clonat de GitHub. Main local i origin/main són a B, arbre net i main amb upstream. Es té permís per publicar branques al mateix repositori i hi ha una altra persona que revisa la proposta. La branca salutacio encara no existeix. B té print("Hello Git!"). C canvia el fitxer a print("Hola, Anna") i D hi afegeix l’exclamació: print("Hola, Anna!"). Les dues edicions es fan explícitament abans de les comandes. GitHub té habilitada l’opció Create a merge commit. Es representa una revisió seguida d’una nova aprovació després de D, sense conflictes i amb els requisits de fusió complerts; una persona amb permís crea M, pares B i D, a main remot. No es força la branca main ni es modifica localment fins al pull --ff-only final. La interfície de GitHub és un esquema docent amb dades inventades; no es crea, comenta, revisa ni fusiona cap PR real. Les proves executen només l’equivalent Git en un remot local temporal.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.62 s)

**Locució:** Setzena lliçó, Pull requests.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Una proposta abans d’integrar el canvi (6.6–18.4 s)

**Locució:** La teva branca funciona. Abans d’incorporar-la a main, una altra persona pot revisar-la. A GitHub ho fem amb una pull request: una proposta de canvi.

**Animació:** Tres targetes branca, revisió i main, unides amb fletxes.

## Main està al dia. Creem salutacio. (18.4–29.9 s)

**Locució:** Partim de main actualitzada i sense canvis pendents. Creem salutacio. Farem la millora en aquesta branca perquè es pugui revisar abans d’integrar-la.

**Animació:** Graf B amb main; apareix salutacio i passa a ser activa.

**Comandes en pantalla:**

```bash
git status --short
git switch -c salutacio
```

## Preparem el primer canvi (29.9–41.8 s)

**Locució:** Canviem el missatge del fitxer, executem el programa i confirmem la millora. Encara és un commit local a salutacio. Main continua al punt de partida.

**Animació:** Editor print("Hola, Anna") i sortida Hola, Anna. Commit C en salutacio.

**Comandes en pantalla:**

```bash
python3 helloGit.py
git add helloGit.py
git commit -m "Millora la salutacio"
```

## GitHub ja pot comparar els commits (41.8–53.4 s)

**Locució:** Enviem salutacio a origin. L’opció u deixa configurat el seguiment de la branca remota. Publicar-la encara no incorpora el canvi a main.

**Animació:** C viatja al remot; origin/salutacio a C i origin/main encara B.

**Comandes en pantalla:**

```bash
git push -u origin salutacio
```

## Base: main. Compare: salutacio. (53.4–63.9 s)

**Locució:** Obrim una pull request amb main com a destinació i salutacio com a origen. Expliquem què canvia i com ho hem provat, i revisem la diferència.

**Animació:** Interfície esquemàtica amb base main, compare salutacio, títol, descripció, prova i diff. Botó Create pull request.

## Una petició de millora (63.9–74.7 s)

**Locució:** Una altra persona revisa el codi i demana afegir una exclamació. La revisió ens ajuda a acordar el resultat abans de fusionar la proposta.

**Animació:** Interfície esquemàtica Files changed, comentari Afegeix una exclamació al final, estat Changes requested.

## Un push actualitza la mateixa proposta (74.7–86.5 s)

**Locució:** Editem el missatge, el tornem a provar i fem un nou commit. Amb push a la mateixa branca, la pull request incorpora el canvi. No cal obrir-ne una altra.

**Animació:** Editor final print("Hola, Anna!"). Terminal de quatre comandes. PR passa d’un a dos commits i a pendent de nova revisió.

**Comandes en pantalla:**

```bash
python3 helloGit.py
git add helloGit.py
git commit -m "Completa la salutacio"
git push
```

## La feina revisada entra a main (86.5–98.0 s)

**Locució:** Després de revisar l’actualització i complir els requisits, una persona amb permís pot fusionar. Aquí triem crear un commit de merge, que incorpora la branca a main.

**Animació:** Aprovació de D i requisits complerts. Opció Create a merge commit, confirmació, estat Merged. Graf remot B–M i C–D–M; M té pares B i D.

## Ara la millora també és al nostre main (98.0–111.0 s)

**Locució:** Finalment tornem a main i fem pull. La còpia local incorpora la fusió. Branca, proposta, revisió i integració: un recorregut complet per treballar en equip.

**Animació:** Main local B avança fins al merge M remot. Fitxer final Hola, Anna!; arbre net. Pull --ff-only és possible perquè main local no ha divergit.

**Comandes en pantalla:**

```bash
git switch main
git pull --ff-only
```
