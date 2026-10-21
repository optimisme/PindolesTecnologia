# Gitignore: tria què entra al repositori

Veu: `ca-ES-EnricNeural` · Català · 96.3 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Repositori de prova independent. helloGit.py i app.log ja estan seguits; app.log té una edició local sense preparar i el seu índex encara coincideix amb HEAD. debug.log i __pycache__/helloGit.pyc són nous no seguits; .gitignore encara no existeix. S’afegeixen els patrons *.log i __pycache__/. Check-ignore es prova amb debug.log, no amb el log ja seguit. Rm --cached retira app.log de l’índex, conserva el fitxer local i prepara la seva eliminació del repositori. Es confirma la regla i l’eliminació en un commit local. Cap fitxer d’aquest exemple es modifica al repositori real.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.62 s)

**Locució:** Tretzena lliçó, Git ignore.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## El codi, els logs i la memòria cau (6.6–16.2 s)

**Locució:** Has executat el programa i status s’omple de fitxers generats. Volem versionar el codi, però deixar fora els logs i la memòria cau.

**Animació:** Targetes helloGit.py seguit, app.log seguit i modificat, debug.log nou, __pycache__/ nou.

**Comandes en pantalla:**

```bash
git status --short
```

## Un patró per línia a .gitignore (16.2–28.8 s)

**Locució:** Creem un fitxer anomenat punt git ignore. Una línia amb asterisc punt log ignora els noms acabats en punt log. La regla de memòria cau ignora aquesta carpeta.

**Animació:** Editor .gitignore amb *.log i __pycache__/, filtre rep els fitxers nous.

## Els fitxers nous deixen de fer soroll (28.8–40.5 s)

**Locució:** Tornem a status. El log nou i la memòria cau ja no apareixen. El fitxer de regles sí: també l’hem de versionar perquè es comparteixi amb el projecte.

**Animació:** Terminal M app.log i ?? .gitignore. debug.log i __pycache__ apareixen a una zona ignorada.

**Comandes en pantalla:**

```bash
git status --short
```

## Quin patró està ignorant el fitxer? (40.5–50.1 s)

**Locució:** Check ignore, amb l’opció ve, ens diu quina regla ignora debug punt log. Si un fitxer no apareix, això ens ajuda a saber per què.

**Animació:** Terminal mostra .gitignore:1:*.log debug.log. Etiquetes fitxer de regles, línia i patró.

**Comandes en pantalla:**

```bash
git check-ignore -v debug.log
```

## App.log continua apareixent (50.1–60.5 s)

**Locució:** App punt log encara surt modificat perquè Git ja el seguia. Afegir una regla no deixa de seguir automàticament un fitxer que ja era al repositori.

**Animació:** Dues targetes debug.log nou ignorat i app.log ja seguit. Status conserva M app.log.

## Cached conserva el fitxer local (60.5–71.2 s)

**Locució:** Si volem deixar de versionar aquest log, fem git rm amb cached. El fitxer es conserva al disc, però preparem la seva eliminació del repositori.

**Animació:** App.log passa fora de l’índex i continua al disc. Terminal status D primera columna.

**Comandes en pantalla:**

```bash
git rm --cached app.log
git status --short
```

## Compartim la regla amb el projecte (71.2–83.4 s)

**Locució:** Preparem punt git ignore i fem commit. Aquest commit desa les regles i retira el log dels fitxers versionats. La nostra còpia local del log continua existint.

**Animació:** Índex .gitignore A i app.log D es confirma. Disc conserva app.log.

**Comandes en pantalla:**

```bash
git add .gitignore
git commit -m "Ignora fitxers generats"
```

## Codi versionat. Fitxers generats fora. (83.4–96.3 s)

**Locució:** Les regles filtren els fitxers no seguits. Si Git ja els seguia, cal una decisió separada per retirar-los. Així status torna a mostrar els canvis que ens interessen.

**Animació:** Targetes codi versionat, regles compartides, fitxers generats locals. Status final sense canvis.

**Comandes en pantalla:**

```bash
git status --short
```
