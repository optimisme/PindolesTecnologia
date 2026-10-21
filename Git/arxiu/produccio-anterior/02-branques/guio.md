# Branques: prova una idea sense tocar main

Veu: `ca-ES-EnricNeural` · Català · 89.2 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Repositori HelloGit a main, amb un commit de helloGit.py que conté print("Hello Git!"). Arbre de treball net. Identificadors de commit il·lustratius.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.67 s)

**Locució:** Segona lliçó, Branques.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Prova el canvi sense tocar main (6.7–16.3 s)

**Locució:** Vols afegir una salutació personalitzada, però el programa actual ja funciona. Com la proves sense canviar la versió de main?

**Animació:** L'editor mostra la salutació original i una targeta presenta la proposta Hola, Anna!, encara pendent de provar.

## Un mateix passat. Dos camins. (16.3–25.6 s)

**Locució:** Una branca és una línia de treball amb el seu propi historial. Al principi comparteix els mateixos commits que la branca d'origen.

**Animació:** Dues etiquetes de branca apunten inicialment al mateix commit; es destaca l'historial compartit.

## Creem la branca salutacio (25.6–35.1 s)

**Locució:** Creem la branca salutació amb git switch i l'opció de crear. Ara hi estem treballant; main continua al mateix commit.

**Animació:** La terminal crea salutacio. Les dues branques apunten al mateix commit i l'etiqueta activa passa de main a salutacio.

**Comandes en pantalla:**

```bash
git switch -c salutacio
git branch --show-current
```

## El canvi es desa a salutacio (35.1–43.8 s)

**Locució:** Canviem el missatge del fitxer. Després, git add prepara el canvi i git commit el desa a la branca salutació.

**Animació:** El fitxer passa de Hello Git! a Hola, Anna! i la terminal prepara i confirma el canvi.

**Comandes en pantalla:**

```bash
git add helloGit.py
git commit -m "Personalitza salutacio"
```

## Main conserva la seva versió (43.8–56.5 s)

**Locució:** El nou commit només fa avançar salutació. Main encara apunta a la versió anterior. Les dues branques comparteixen el passat, però ara tenen finals diferents.

**Animació:** Només salutacio avança fins al commit nou. Main es queda al commit original; no s'inventa cap commit extra a main.

## El codi original continua aquí (56.5–68.0 s)

**Locució:** Tornem a main amb git switch main. El fitxer torna a mostrar el missatge original. El commit de salutació continua desat a la seva branca.

**Animació:** La terminal canvia a main, l'etiqueta activa es mou i l'editor torna a print("Hello Git!").

**Comandes en pantalla:**

```bash
git switch main
```

## La feina nova també hi continua (68.0–78.0 s)

**Locució:** Si tornem a salutació, reapareix el missatge nou. Canviar de branca actualitza els fitxers per mostrar la versió de la branca seleccionada.

**Animació:** En tornar a salutacio, reapareix print("Hola, Anna!"). Les dues branques es conserven.

**Comandes en pantalla:**

```bash
git switch salutacio
```

## Crea. Prova. Confirma. (78.0–89.2 s)

**Locució:** Crear una branca, provar el canvi i fer commit. Main conserva la seva versió. Per incorporar-hi la funcionalitat, farem servir merge.

**Animació:** Resum dels passos i dels dos missatges. Merge queda presentat com a concepte per a un episodi posterior, sense executar-lo.

**Comandes en pantalla:**

```bash
git switch -c salutacio
git add helloGit.py
git commit -m "Personalitza salutacio"
```
