# De classe a casa: clone, pull i push

Veu: `ca-ES-EnricNeural` · Català · 84.8 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Repositori HelloGit amb branca main i remot origin configurats. Treball en sèrie, sense divergències i amb arbres de treball nets abans de pull. <URL-del-repositori> és un marcador que cal substituir per l'adreça pròpia. Els identificadors són il·lustratius.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.83 s)

**Locució:** Quarta lliçó, Sincronització.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## A casa encara tens el codi d'ahir (6.8–17.7 s)

**Locució:** A classe has acabat la pràctica. A casa obres el projecte i encara hi ha el codi d'ahir. Falta sincronitzar els dos ordinadors.

**Animació:** L'ordinador de classe mostra el commit B i el de casa el commit A. GitHub encara té A.

## GitHub és el punt de trobada (17.7–27.3 s)

**Locució:** Cada ordinador té el seu propi repositori local. GitHub és el punt de trobada: els commits només hi arriben quan els enviem.

**Animació:** Tres nodes: classe, GitHub i casa. S'assenyalen els dos repositoris locals i el repositori remot.

## Primer: commit i push (27.3–36.1 s)

**Locució:** A classe, desem el canvi amb add i commit. Després, git push envia aquest commit al repositori de GitHub.

**Animació:** El commit B apareix a classe després del commit i es copia a GitHub amb push. Casa encara té A.

**Comandes en pantalla:**

```bash
git add helloGit.py
git commit -m "Practica de classe"
git push
```

## Encara no tens el projecte? Clone. (36.1–46.0 s)

**Locució:** Si a casa encara no tenim el projecte, fem git clone amb l'adreça del repositori. Es crea una carpeta amb els fitxers i l'historial.

**Animació:** Camí alternatiu per a un ordinador sense repositori: una carpeta buida rep els commits A i B des de GitHub. La terminal inclou cd HelloGit.

**Comandes en pantalla:**

```bash
git clone <URL-del-repositori> HelloGit
cd HelloGit
```

## Ja tens el projecte? Pull. (46.0–55.0 s)

**Locució:** Si ja el teníem clonat, no cal tornar-lo a clonar. Entrem a la carpeta i fem git pull per integrar els commits nous.

**Animació:** Alternativa a clone: casa parteix d'A i incorpora B des de GitHub. La terminal executa pull dins de HelloGit.

**Comandes en pantalla:**

```bash
cd HelloGit
git pull
```

## Ara casa envia el següent canvi (55.0–63.3 s)

**Locució:** Ara el codi de casa ja està actualitzat. Hi fem un altre canvi, el confirmem i l'enviem amb git push.

**Animació:** Es crea C a casa i després viatja a GitHub. Classe continua a B fins que faci pull.

**Comandes en pantalla:**

```bash
git add helloGit.py
git commit -m "Millora des de casa"
git push
```

## Recupera el que has fet a casa (63.3–73.2 s)

**Locució:** Quan tornem a classe, git pull descarrega i integra el commit de casa. Abans de començar, comprovem que no tenim canvis locals pendents.

**Animació:** Git status --short sense sortida confirma un arbre net. Pull porta C des de GitHub a classe. Els tres repositoris queden sincronitzats.

**Comandes en pantalla:**

```bash
git status --short
git pull
```

## Actualitza. Treballa. Comparteix. (73.2–84.8 s)

**Locució:** La rutina és senzilla: actualitzar, treballar, fer commit i enviar. Clone és per obtenir el projecte; pull per actualitzar-lo; push per compartir els commits.

**Animació:** Tres targetes resumeixen clone, pull i push amb fletxes i una rutina de treball en quatre passos.

**Comandes en pantalla:**

```bash
git clone <URL-del-repositori> HelloGit
git pull
git push
```
