# Rebase: continua sobre una base nova

Veu: `ca-ES-EnricNeural` · Català · 89.8 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Branca salutacio pròpia i no publicada, amb dos commits C i E sobre B. Main ha avançat a D amb un canvi en un altre fitxer; l'exemple principal no té conflictes. Les dues branques són locals i l'arbre de treball és net. C′ i E′ són commits nous amb identificadors nous, no els commits originals moguts. Les lletres són didàctiques. La resolució de conflictes es mostra com a cas condicional separat.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.67 s)

**Locució:** Setena lliçó, Rebase.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## La teva base s'ha quedat enrere (6.7–19.2 s)

**Locució:** Mentre treballaves en una branca, main ha incorporat millores. Vols continuar la funcionalitat sobre aquesta versió actualitzada. Aquí és on entra rebase.

**Animació:** Es destaquen D a main i els dos commits propis C i E, encara basats en B.

## Una base comuna. Dos camins. (19.2–28.6 s)

**Locució:** Main té un commit nou i salutació, dos de propis. Comparteixen la base, però ara els seus historials divergeixen.

**Animació:** Graf B–D a dalt i B–C–E a sota. Main apunta a D i salutacio a E; la branca no s'ha publicat.

## Rebase actua sobre salutacio (28.6–37.6 s)

**Locució:** Ens situem a salutació i fem git rebase main. La branca activa rebrà una nova base; main no es modifica.

**Animació:** La terminal selecciona salutacio i inicia rebase main. El punter main continua fix a D.

**Comandes en pantalla:**

```bash
git switch salutacio
git rebase main
```

## Els canvis es reapliquen (37.6–47.6 s)

**Locució:** Git reaplica els dos canvis sobre l'últim commit de main. Es creen commits nous, amb pares i identificadors diferents dels originals.

**Animació:** C′ i E′ apareixen successivament després de D. C i E es mostren atenuats com a originals, no es desplacen físicament. Salutacio avança al final quan acaba.

## Main es queda. Salutacio avança. (47.6–56.7 s)

**Locució:** Ara els nostres commits queden darrere del nou commit de main. Main es manté al seu lloc; salutació avança.

**Animació:** Línia B–D–C′–E′ amb main a D i salutacio a E′. El terminal mostra el graf de l'historial.

**Comandes en pantalla:**

```bash
git log --oneline --graph --all
```

## Dos resultats d'historial diferents (56.7–68.1 s)

**Locució:** Amb merge, un commit pot unir els dos camins. Amb rebase, reconstruïm els nostres commits sobre l'altre camí. Són dos historials diferents.

**Animació:** Comparació des del mateix estat inicial i amb salutacio activa: git merge main conserva D i C–E i afegeix M a salutacio amb pares E i D; git rebase main deixa B–D–C′–E′. Main continua a D en les dues alternatives.

## Resol, prepara i continua (68.1–78.8 s)

**Locució:** Si apareix un conflicte, el resolem, fem git add i continuem amb git rebase i l'opció continue. L'exemple principal té canvis compatibles.

**Animació:** Cas condicional etiquetat. Tres passos: resoldre el fitxer, preparar-lo i git rebase --continue. No es fa un git commit manual de merge.

**Comandes en pantalla:**

```bash
git add helloGit.py
git rebase --continue
```

## Una base nova per continuar (78.8–89.8 s)

**Locució:** Fes rebase en una branca pròpia encara no compartida: reescriu els seus commits. Per portar després la funcionalitat a main, encara l'hauràs d'integrar.

**Animació:** Main continua a D i salutacio a E′. Es remarquen la branca local, els identificadors nous i que la integració a main encara és pendent.
