# Revert: desfés un commit publicat

Veu: `ca-ES-EnricNeural` · Català · 84.8 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Main és al commit ordinari C, ja publicat a origin/main, amb el directori de treball net. B tenia print("Hello Git!") i l'últim commit C ho ha substituït per print(salutacio), sense definir la variable. No hi ha commits posteriors ni conflictes. C es mostra com c95f4a7: és un hash il·lustratiu i s'ha de substituir per l'identificador real de git log. A, B, C i D són etiquetes didàctiques. L'exemple usa --no-edit per acceptar el missatge automàtic del revert. La publicació es representa visualment; les comprovacions usen un remot local temporal.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.58 s)

**Locució:** Desena lliçó, Revert.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## El commit ja és a GitHub (6.6–16.8 s)

**Locució:** Has publicat un commit i ara el programa falla. Altres persones ja el tenen. Com desfem el canvi conservant l'historial?

**Animació:** El graf A–B–C és compartit entre main, GitHub i un company. El fitxer executa print(salutacio) i produeix NameError.

## Busquem quin canvi ha fallat (16.8–24.9 s)

**Locució:** Partim d'un directori net. Amb git log busquem el commit que introdueix l'error i en copiem l'identificador.

**Animació:** Status confirma que no hi ha canvis locals. Log mostra c95f4a7 com a últim commit amb l'error.

**Comandes en pantalla:**

```bash
git status --short
git log --oneline
```

## Comprovem què va introduir (24.9–34.3 s)

**Locució:** Git show permet revisar què va canviar. Aquí, el commit substitueix el missatge correcte per una variable que no existeix.

**Animació:** La terminal mostra un diff amb -print("Hello Git!") i +print(salutacio). S'associa el canvi al commit C.

**Comandes en pantalla:**

```bash
git show c95f4a7 -- helloGit.py
```

## Revert crea un commit nou (34.3–45.2 s)

**Locució:** Fem git revert amb l'identificador. L'opció no edit accepta el missatge automàtic. Git crea un commit amb el canvi invers.

**Animació:** S'executa git revert --no-edit sobre C i apareix D, fill de C, amb el missatge automàtic Revert. C no desapareix.

**Comandes en pantalla:**

```bash
git revert --no-edit c95f4a7
```

## C continua. D en desfà l'efecte. (45.2–56.3 s)

**Locució:** El commit problemàtic continua a l'historial. Just després n'apareix un de nou que el reverteix. La branca avança; no torna enrere.

**Animació:** La línia A–B–C–D conserva tots els commits. Main apunta a D, però origin/main encara és a C fins al push.

## El programa torna a funcionar (56.3–65.0 s)

**Locució:** El fitxer recupera el missatge correcte. Executem el programa i comprovem que no hi hagi canvis locals pendents.

**Animació:** HelloGit.py torna a print("Hello Git!"). Python mostra Hello Git! i status no mostra canvis locals.

**Comandes en pantalla:**

```bash
python3 helloGit.py
git status --short
```

## Publiquem el commit que reverteix (65.0–74.0 s)

**Locució:** Git push comparteix el nou commit. Els altres ordinadors el poden incorporar amb pull i conservar tota la seqüència.

**Animació:** D viatja del repositori local a GitHub. Origin/main avança a D. Un company encara a C pot fer pull sense reescriure l'historial.

**Comandes en pantalla:**

```bash
git push
```

## Desfer l'efecte. Conservar la història. (74.0–84.8 s)

**Locució:** Revert desfà l'efecte d'un commit amb un altre commit. L'original es conserva i la correcció queda registrada: una bona opció per a feina publicada.

**Animació:** Es ressalten C, que es conserva, i D, que reverteix el canvi. La branca i el remot comparteixen el nou historial.

**Comandes en pantalla:**

```bash
git log --oneline
git revert --no-edit c95f4a7
git push
```
