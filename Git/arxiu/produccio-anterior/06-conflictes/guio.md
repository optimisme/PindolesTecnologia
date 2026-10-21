# Conflictes: dues edicions, una decisió

Veu: `ca-ES-EnricNeural` · Català · 84.7 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Arbre de treball net a main. Des d'una mateixa base B amb print("Hello Git!"), main ha creat D amb print("Hola, classe!") i salutacio ha creat C amb print("Hola, Anna!"). Les dues branques modifiquen la mateixa línia. Marcadors de conflicte del format merge habitual. Les lletres representen commits il·lustratius.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.75 s)

**Locució:** Sisena lliçó, Conflictes.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Quin missatge s'ha de quedar? (6.8–18.0 s)

**Locució:** Dues branques han canviat la mateixa línia de manera diferent. En fer merge, quin missatge s'ha de quedar? Git necessita que decidim el resultat.

**Animació:** Dos editors mostren Hola, classe! i Hola, Anna! amb la mateixa línia ressaltada.

## La mateixa línia, dos canvis (18.0–27.5 s)

**Locució:** Les dues branques parteixen del mateix missatge. A main l'hem canviat per Hola, classe; a salutació, per Hola, Anna.

**Animació:** El graf B–D i B–C connecta les dues edicions al mateix ancestre. S'etiqueten main i salutacio.

## Merge s'atura per decidir (27.5–38.8 s)

**Locució:** Des de main, executem git merge salutació. La fusió s'atura amb un conflicte. Encara no s'ha creat el commit que uneix els canvis.

**Animació:** La terminal indica CONFLICT (content). El graf continua amb D i C separats; encara no hi ha cap commit M.

**Comandes en pantalla:**

```bash
git merge salutacio
```

## Git assenyala les dues versions (38.8–48.2 s)

**Locució:** Git status identifica el fitxer pendent. Dins del fitxer, els marcadors separen la versió de main i la de salutació.

**Animació:** Un terminal mostra UU helloGit.py. L'editor conté tots els marcadors: <<<<<<< HEAD, ======= i >>>>>>> salutacio.

**Comandes en pantalla:**

```bash
git status --short
```

## El resultat el decidim nosaltres (48.2–57.2 s)

**Locució:** Editem el fitxer i triem el text final: Hola, grup. Eliminem tots els marcadors i comprovem que el programa funciona.

**Animació:** El fitxer queda amb print("Hola, grup!"), sense marcadors. Python l'executa i mostra Hola, grup!.

**Comandes en pantalla:**

```bash
python3 helloGit.py
```

## Add prepara la resolució (57.2–65.3 s)

**Locució:** Ara git add marca el conflicte com a resolt. Preparar el fitxer no crea encara el commit de merge.

**Animació:** El fitxer resolt s'afegeix a l'índex. Status passa d'UU a M preparat. La fusió continua pendent de commit.

**Comandes en pantalla:**

```bash
git add helloGit.py
git status --short
```

## Ara sí: un commit amb dos pares (65.3–74.0 s)

**Locució:** Amb git commit, acabem la fusió. El nou commit connecta els dos historials i conserva el contingut que hem revisat.

**Animació:** Apareix M amb pares D i C; main avança a M i salutacio continua a C. El text final és Hola, grup!.

**Comandes en pantalla:**

```bash
git commit -m "Resol conflicte"
```

## Revisa. Resol. Prova. Confirma. (74.0–84.7 s)

**Locució:** Per resoldre un conflicte, revisa les dues propostes, escriu el resultat correcte, prova'l i confirma'l. Main ja incorpora la teva decisió.

**Animació:** Resum: revisar les propostes, eliminar els marcadors, provar el codi, add i commit.

**Comandes en pantalla:**

```bash
python3 helloGit.py
git add helloGit.py
git commit -m "Resol conflicte"
```
