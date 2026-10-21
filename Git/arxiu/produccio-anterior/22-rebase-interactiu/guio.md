# Rebase interactiu: agrupa commits abans de publicar

Veu: `ca-ES-EnricNeural` · Català · 116.9 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent amb historial lineal A–B–C–D–E. Main apunta a B i salutacio és l’activa a E. Només C, D i E són propis i encara no publicats. B conté README.md i helloGit.py amb print("Hello Git!"). C canvia el missatge a print("Hola, Anna"), D afegeix l’exclamació i E afegeix notes.md amb documentació de la mateixa feina. Índex i treball nets. HEAD~3 és B. Rebase -i HEAD~3 obre la llista C, D, E de més antic a més recent: pick C, squash D, squash E. Es desen i tanquen l’editor de la llista i el del missatge conjunt, amb el missatge Personalitza la salutacio. El resultat S té pare B, arbre idèntic a E i identificador nou. Main continua a B i salutacio passa a S; els objectes antics no s’eliminen immediatament però C, D, E surten de la línia de salutacio. E es representa amb e18a3b6, i els altres hashes són il·lustratius. Es comprova el programa i git diff e18a3b6 HEAD -- no mostra diferències. El cas de conflicte és una alternativa condicional independent: add i continue, o abort. No hi ha remots ni publicació forçada.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–7.25 s)

**Locució:** Vint-i-dosena lliçó, Rebase interactiu.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Tres commits per una mateixa millora (7.2–20.5 s)

**Locució:** Has fet una millora en tres commits: el canvi inicial, un retoc i la documentació. Encara no els has publicat. Podem agrupar-los en un commit que expliqui la feina completa.

**Animació:** Main a B, salutacio C–D–E. Tres missatges relacionats i etiqueta només locals.

## Els tres últims commits són nostres (20.5–32.5 s)

**Locució:** Comprovem l’estat, els tres últims commits i el programa. Treballem a salutacio amb l’arbre net. Només reescriurem aquests tres commits encara no publicats.

**Animació:** Terminal status net, log E Documenta salutacio, D Afegeix exclamacio, C Personalitza salutacio. Sortida Hola, Anna!.

**Comandes en pantalla:**

```bash
git status --short
git log -3 --oneline
python3 helloGit.py
```

## HEAD titlla tres ens porta a B (32.5–43.5 s)

**Locució:** Fem rebase interactiu des de tres commits enrere. Aquest punt és B. Git obre un editor amb la llista dels commits que hi ha després: C, D i E.

**Animació:** Graf destaca base B i interval C–D–E. Terminal git rebase -i HEAD~3. La branca main queda a B.

**Comandes en pantalla:**

```bash
git rebase -i HEAD~3
```

## Pick al primer. Squash als altres dos. (43.5–56.6 s)

**Locució:** La llista va del més antic al més recent. Deixem pick al primer i canviem els altres dos a squash. Així els unim al primer. Desem i tanquem l’editor.

**Animació:** Editor de text, no terminal: pick c95f4a7 Personalitza salutacio; squash d04f7a2 Afegeix exclamacio; squash e18a3b6 Documenta salutacio. No es canvia l’ordre.

## Un missatge que expliqui la feina (56.6–69.5 s)

**Locució:** Git ens demana el missatge del commit conjunt. El deixem com Personalitza la salutació, amb una descripció coherent de la millora. Desem i tanquem perquè l’operació acabi.

**Animació:** Editor del missatge conjunt. Es mostra Personalitza la salutacio, sense ordres de shell. Es confirma desar i tancar.

## Un commit nou amb el mateix resultat (69.5–81.5 s)

**Locució:** Salutacio ara apunta al commit S, amb pare B. Els tres commits antics queden fora d’aquesta línia. Main continua a B, i els fitxers conserven el resultat final d’E.

**Animació:** Graf A–B–S amb main B i salutacio S. C–D–E es mostren atenuats en una línia antiga, sense cap aresta d’E a S.

## Historial nou. Mateixos fitxers finals. (81.5–91.4 s)

**Locució:** Revisem el commit, provem el programa i comparem amb l’antic E. El programa funciona i diff no mostra canvis: hem agrupat l’historial conservant el contingut final.

**Animació:** Log mostra S, programa Hola, Anna!, diff entre hash il·lustratiu d’E i HEAD sense sortida.

**Comandes en pantalla:**

```bash
git log -1 --oneline
python3 helloGit.py
git diff e18a3b6 HEAD --
```

## Resoldre i continuar, o avortar (91.4–103.4 s)

**Locució:** Si apareix un conflicte, el resolem al fitxer, fem add i continuem el rebase. O podem avortar per tornar al punt de partida. Són dues alternatives.

**Animació:** Dues terminals separades: opció resoldre amb add i rebase --continue; opció independent rebase --abort.

**Comandes en pantalla:**

```bash
git add helloGit.py
git rebase --continue
git rebase --abort
```

## Agrupa, explica i comprova (103.4–116.9 s)

**Locució:** Agrupa només commits relacionats, escriu un missatge clar i comprova el resultat. Aquí hem reescrit feina pròpia encara no publicada: els identificadors canvien, però el contingut final es conserva.

**Animació:** Tres targetes agrupar, explicar i provar. Recordatori: commits propis locals; base B i main no es mouen.
