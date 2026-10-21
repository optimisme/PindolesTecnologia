# Lliçó 20 · Fetch: consulta els canvis abans d’integrar-los

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Vintena lliçó, Fetch.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a descarregar, comparar i integrar novetats en tres passos explícits.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Main local i origin/main a B, treball net. El servidor origin ja té C. La història és lineal i main segueix origin/main.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## La referència local no és una vista en directe

**Locució:** El servidor pot haver avançat sense que el nostre ordinador ho sàpiga. origin/main és una referència local de l’última consulta; encara apunta a B.

**Visual:** Tres elements separats: main LOCAL B; origin/main LOCAL B; main SERVIDOR C.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git status --short

**Terminal · comanda completa visible:**

```text
git status --short
```

**Subratllat:** `git status`.

**Locució:** Consultem l’estat amb git status. Aquesta consulta no modifica el projecte.

**Visual:** Mantenir visible el text complet: git status --short. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git status.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git status --short
```

**Subratllat:** `--short`.

**Locució:** Doble guionet short demana la forma breu. La primera columna compara preparació i últim commit; la segona, treball i preparació.

**Visual:** Mantenir visible el text complet: git status --short. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --short.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git status --short
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git status --short. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git status --short
```

**Locució:** No hi ha canvis locals pendents. Podem observar amb claredat què modifica cada pas.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git fetch origin

**Terminal · comanda completa visible:**

```text
git fetch origin
```

**Subratllat:** `git fetch`.

**Locució:** git fetch descarrega les novetats i actualitza les referències de seguiment.

**Visual:** Mantenir visible el text complet: git fetch origin. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git fetch.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git fetch origin
```

**Subratllat:** `origin`.

**Locució:** Indica el remot que consultem. És el servidor del projecte.

**Visual:** Mantenir visible el text complet: git fetch origin. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: origin.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git fetch origin
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git fetch origin. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git fetch origin
```

**Locució:** C ja existeix al repositori local i origin/main apunta a C. Main, preparació i treball continuen a B.

**Visual:** Animar descàrrega C i actualització de origin/main. No moure main ni canviar el text de l’editor. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git log --oneline main..origin/main

**Terminal · comanda completa visible:**

```text
git log --oneline main..origin/main
```

**Subratllat:** `git log`.

**Locució:** Consultem els commits que la branca local encara no conté.

**Visual:** Mantenir visible el text complet: git log --oneline main..origin/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git log.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline main..origin/main
```

**Subratllat:** `--oneline`.

**Locució:** Mostra un resum de cada commit.

**Visual:** Mantenir visible el text complet: git log --oneline main..origin/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --oneline.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline main..origin/main
```

**Subratllat:** `main..origin/main`.

**Locució:** El rang mostra commits accessibles des d’origin/main que no són accessibles des de main.

**Visual:** Mantenir visible el text complet: git log --oneline main..origin/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: main..origin/main.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline main..origin/main
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git log --oneline main..origin/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline main..origin/main
```

**Locució:** En aquest exemple només apareix C. La consulta tampoc integra el canvi.

**Visual:** Subratllar primer main, després els dos punts i després origin/main; representar conjunts amb el mateix C. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git diff main origin/main -- helloGit.py

**Terminal · comanda completa visible:**

```text
git diff main origin/main -- helloGit.py
```

**Subratllat:** `git diff`.

**Locució:** Comparem el contingut de les dues versions.

**Visual:** Mantenir visible el text complet: git diff main origin/main -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git diff.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff main origin/main -- helloGit.py
```

**Subratllat:** `main`.

**Locució:** El primer punt de comparació és la nostra branca local.

**Visual:** Mantenir visible el text complet: git diff main origin/main -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: main.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff main origin/main -- helloGit.py
```

**Subratllat:** `origin/main`.

**Locució:** El segon és l’estat descarregat del remot.

**Visual:** Mantenir visible el text complet: git diff main origin/main -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: origin/main.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff main origin/main -- helloGit.py
```

**Subratllat:** `--`.

**Locució:** Separa les versions del camí de fitxer.

**Visual:** Mantenir visible el text complet: git diff main origin/main -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff main origin/main -- helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** Limitem la comparació al programa.

**Visual:** Mantenir visible el text complet: git diff main origin/main -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff main origin/main -- helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git diff main origin/main -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff main origin/main -- helloGit.py
```

**Locució:** Veiem la salutació nova de C, mentre el fitxer del treball encara té l’original de B.

**Visual:** Diff i editor actual visibles alhora; cap fletxa de sobreescriptura. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git merge --ff-only origin/main

**Terminal · comanda completa visible:**

```text
git merge --ff-only origin/main
```

**Subratllat:** `git merge`.

**Locució:** Després de revisar, decidim incorporar el canvi.

**Visual:** Mantenir visible el text complet: git merge --ff-only origin/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git merge.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only origin/main
```

**Subratllat:** `--ff-only`.

**Locució:** Només permet avançar main directament; amb divergències l’ordre s’aturaria.

**Visual:** Mantenir visible el text complet: git merge --ff-only origin/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --ff-only.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only origin/main
```

**Subratllat:** `origin/main`.

**Locució:** És la referència local actualitzada que volem incorporar.

**Visual:** Mantenir visible el text complet: git merge --ff-only origin/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: origin/main.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only origin/main
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git merge --ff-only origin/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only origin/main
```

**Locució:** Main avança a C i el treball s’actualitza. Aquest és el pas que integra la novetat.

**Visual:** Moure main fins a C i actualitzar l’editor després de l’execució. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `python3`.

**Locució:** Provem la versió incorporada.

**Visual:** Mantenir visible el text complet: python3 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: python3.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: python3 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Locució:** El programa executa la salutació de C. Hem separat descarregar, llegir i integrar.

**Visual:** Sortida Hola, Anna! i graf local coincident amb el servidor. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Fetch actualitza les referències de seguiment, sense integrar a main.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Log i diff permeten revisar el que hem descarregat.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** La integració és posterior; pull combina descàrrega i intent d’integració.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Amb dos clons de pràctiques, publica una novetat en un i fes fetch a l’altre. Compara main i origin/main abans d’integrar amb el treball net.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
