# Amend: completa l’últim commit local

Veu: `ca-ES-EnricNeural` · Català · 94.7 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent amb main a C, últim commit propi encara no publicat. A conté README.md, B afegeix helloGit.py amb print("Hello Git!"), C modifica helloGit.py a print("Hola, Anna!") amb el missatge Millora la salutacio. notes.md existeix localment amb una línia de documentació però és un fitxer nou no seguit que es va oblidar. No hi ha altres canvis locals ni preparats. S’afegeix només notes.md, es revisa la preparació i s’executa commit --amend --no-edit per crear C′, amb pare B, missatge i autoria de C conservats, i el fitxer afegit. C ja no pertany a la línia de main, però no s’esborra immediatament l’objecte. L’alternativa final de només missatge parteix independentment de C, amb l’índex sense canvis respecte a C; no continua després de l’amend anterior. Es mostra --amend -m per crear C* amb el mateix arbre i pare B, i un missatge diferent. No hi ha remots ni publicació. Els hashes i les lletres són il·lustratius.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.54 s)

**Locució:** Dinovena lliçó, Amend.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Aquest fitxer havia d’entrar al commit (6.5–17.5 s)

**Locució:** Has fet l’últim commit, però t’has deixat un fitxer. Encara no l’has publicat. Amb amend podem substituir aquell commit per un de complet.

**Animació:** Main a C amb helloGit.py confirmat. Notes.md és nou i queda fora del commit. C marcat només local.

## C està confirmat. notes.md encara no. (17.5–29.4 s)

**Locució:** Comprovem l’estat i l’últim commit. El fitxer de notes continua sense seguir. En aquest exemple, la resta està confirmada i no hi ha altres canvis preparats.

**Animació:** Status mostra ?? notes.md i log C Millora la salutacio.

**Comandes en pantalla:**

```bash
git status --short
git log -1 --oneline
```

## Seleccionem què volem incorporar (29.4–40.3 s)

**Locució:** Fem add només del fitxer oblidat i revisem els canvis preparats. Amend incorporarà el contingut de la preparació: cal assegurar-nos que sigui el que volem.

**Animació:** Notes.md passa de nou a preparat. Diff staged stat mostra un fitxer i una línia afegida.

**Comandes en pantalla:**

```bash
git add notes.md
git diff --staged --stat
```

## Amend crea una versió nova de C (40.3–52.3 s)

**Locució:** Fem commit amb amend i no edit. Git crea un commit nou que inclou el fitxer preparat i conserva el missatge anterior. Main passa a apuntar a C prima.

**Animació:** C s’atenua i apareix C′ des del mateix pare B. Notes.md queda inclòs. --no-edit conserva Millora la salutacio.

**Comandes en pantalla:**

```bash
git commit --amend --no-edit
```

## C prima té el mateix pare B (52.3–60.6 s)

**Locució:** No hem afegit un commit després de C. L’hem substituït a la branca per C prima, amb un identificador diferent i el mateix pare B.

**Animació:** Comparació A–B–C antiga i A–B–C′ actual. No hi ha una aresta de C a C′. C queda fora de la línia actual de main.

## El commit ja inclou el fitxer (60.6–70.5 s)

**Locució:** Revisem l’últim commit i l’estat. Ara el commit conté també el fitxer de notes, conserva el missatge i ja no tenim canvis pendents.

**Animació:** Show stat de C′ inclou helloGit.py i notes.md respecte de B. Status sense sortida.

**Comandes en pantalla:**

```bash
git show --stat HEAD
git status --short
```

## També podem corregir el missatge (70.5–82.2 s)

**Locució:** En un cas independent, sense canvis preparats, amend amb l’opció ema permet corregir només el missatge. També crea un identificador nou, però el contingut queda igual.

**Animació:** Alternativa des de C amb índex igual a C. C* manté l’arbre i el pare B, amb missatge nou. No es continua després de C′.

**Comandes en pantalla:**

```bash
git commit --amend -m "Personalitza el missatge"
```

## Un retoc abans de publicar (82.2–94.7 s)

**Locució:** Prepara només allò que falta, revisa-ho i completa l’últim commit. En aquesta lliçó hem treballat amb un commit propi encara no publicat, perquè amend reescriu aquest punt de l’historial.

**Animació:** Tres targetes preparar, revisar, substituir. Recordatori commit propi local, missatge conservat amb --no-edit, identificador nou.
