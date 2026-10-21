# Merge: portem la prova a main

Veu: `ca-ES-EnricNeural` · Català · 86.0 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Repositori local net amb main al commit B i salutacio al commit C, descendent directe de B. A main, helloGit.py mostra Hello Git!; a salutacio, Hola, Anna!. Inicialment som a salutacio. Exemple amb el comportament habitual fast-forward de Git. A, B, C, D i M són noms didàctics de commits; els hashes de mostra són il·lustratius.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.50 s)

**Locució:** Cinquena lliçó, Merge.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Portem la salutació a main (6.5–15.5 s)

**Locució:** La salutació nova funciona a la seva branca. Ara volem incorporar-la a main perquè formi part de la versió principal.

**Animació:** Dos editors mostren main amb Hello Git! i salutacio amb Hola, Anna!. La nova funcionalitat està preparada per integrar-la.

## Main encara és al commit anterior (15.5–26.8 s)

**Locució:** Main continua al commit anterior. Salutació té un commit més. No hem canviat main mentre treballàvem en aquesta funcionalitat.

**Animació:** Historial lineal A–B–C: main apunta a B i salutacio a C. No s'inventa cap commit divergent.

## La branca activa rebrà els canvis (26.8–35.2 s)

**Locució:** Primer tornem a main amb git switch. Aquesta és la branca que rebrà els canvis; comprovem que és l'activa.

**Animació:** La terminal canvia a main i git branch --show-current en confirma el nom. Els dos punters encara són a B i C.

**Comandes en pantalla:**

```bash
git switch main
git branch --show-current
```

## Git pot avançar directament (35.2–44.6 s)

**Locució:** Fem git merge salutació. Com que main és un avantpassat de salutació, Git pot avançar directament fins al seu commit.

**Animació:** La terminal executa merge i l'etiqueta main es desplaça de B fins a C. No apareix cap node nou.

**Comandes en pantalla:**

```bash
git merge salutacio
```

## Dos noms. El mateix commit. (44.6–55.7 s)

**Locució:** Aquest avançament s'anomena fast forward. Main i salutació apunten al mateix commit. No s'ha creat cap commit nou per fer la unió.

**Animació:** Main i salutacio apunten a C. Una etiqueta remarca que el nombre de commits és el mateix que abans de fer merge.

## Main ja incorpora el canvi (55.7–64.6 s)

**Locució:** El fitxer de main ja mostra la salutació personalitzada. Amb git log veiem que el canvi forma part del seu historial.

**Animació:** L'editor de main mostra Hola, Anna!. La terminal consulta l'historial de main.

**Comandes en pantalla:**

```bash
git log --oneline main
```

## Quan els historials divergeixen (64.6–73.6 s)

**Locució:** Si main també hagués avançat, els historials podrien divergir. Git podria crear un commit de merge amb dos pares.

**Animació:** Exemple alternatiu clarament etiquetat: B té dos descendents, D a main i C a salutacio. Un commit M amb pares D i C integra canvis compatibles.

## Canvia al destí. Integra. Revisa. (73.6–86.0 s)

**Locució:** Merge integra canvis a la branca activa. En el nostre exemple main avança i salutació es conserva. Si les edicions xoquen, caldrà resoldre un conflicte.

**Animació:** Resum del flux a main. La branca d'origen continua existint; els conflictes es presenten com a tema de la lliçó següent.

**Comandes en pantalla:**

```bash
git switch main
git merge salutacio
```
