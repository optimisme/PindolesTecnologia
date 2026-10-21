# Lliçó 3 · Desar, preparar i fer commit: els tres estats

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Tercera lliçó, Els tres estats.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a distingir treball, preparació i historial, inclosa una edició posterior a add.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** helloGit.py ja està confirmat amb la salutació original. Comencem sense canvis pendents. V1, V2 i V3 són continguts del mateix fitxer.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Tres zones del mateix projecte

**Locució:** Desar a l’editor modifica el treball. Preparar selecciona un contingut concret. Confirmar enregistra la instantània preparada a l’historial. Són tres funcions diferents.

**Visual:** Tres panells persistents: TREBALL, PREPARACIÓ i ÚLTIM COMMIT. Inicialment tots amb V1.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Editem el treball

**Locució:** Canviem la salutació i desem. El treball ara conté V2. La preparació i l’últim commit encara contenen V1.

**Visual:** Editor V2: salutació personalitzada. Les altres zones mantenen la salutació original.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git diff

**Terminal · comanda completa visible:**

```text
git diff
```

**Subratllat:** `git diff`.

**Locució:** git diff compara el treball amb la preparació.

**Visual:** Mantenir visible el text complet: git diff. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git diff.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git diff. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff
```

**Locució:** Hi veiem el canvi de salutació que encara no hem preparat. Els signes menys i més representen la línia anterior i la nova.

**Visual:** Fletxa PREPARACIÓ V1 → TREBALL V2. Llegenda textual per a - i +. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git add helloGit.py

**Terminal · comanda completa visible:**

```text
git add helloGit.py
```

**Subratllat:** `git add`.

**Locució:** Amb git add seleccionem el contingut que volem confirmar.

**Visual:** Mantenir visible el text complet: git add helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git add.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** El nom identifica el fitxer que preparem. La còpia desada ara és la que entra a la preparació.

**Visual:** Mantenir visible el text complet: git add helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git add helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add helloGit.py
```

**Locució:** Treball i preparació ara contenen V2. La preparació és una instantània seleccionada; no és un vincle que segueixi totes les edicions futures.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git diff --staged

**Terminal · comanda completa visible:**

```text
git diff --staged
```

**Subratllat:** `git diff`.

**Locució:** Ara comparem la preparació amb l’últim commit.

**Visual:** Mantenir visible el text complet: git diff --staged. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git diff.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff --staged
```

**Subratllat:** `--staged`.

**Locució:** Doble guionet staged selecciona aquesta altra comparació: últim commit respecte de preparació.

**Visual:** Mantenir visible el text complet: git diff --staged. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --staged.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff --staged
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git diff --staged. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff --staged
```

**Locució:** La salutació nova està preparada per entrar al següent commit.

**Visual:** Fletxa ÚLTIM COMMIT V1 → PREPARACIÓ V2. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Desem una altra edició

**Locució:** Afegim una línia de comiat i desem. El treball passa a V3, però la preparació continua a V2. El comiat encara no està seleccionat.

**Visual:** Treball amb salutació i comiat; preparació amb salutació sola; historial V1.

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

**Locució:** Apareixen dues emes al mateix fitxer. La primera indica canvis preparats; la segona, canvis al treball encara sense preparar. El cas de fitxer nou, representat amb dos interrogants, és diferent.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git diff

**Terminal · comanda completa visible:**

```text
git diff
```

**Subratllat:** `git diff`.

**Locució:** Revisem el que encara queda fora de la preparació.

**Visual:** Mantenir visible el text complet: git diff. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git diff.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git diff. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff
```

**Locució:** Només apareix el comiat. El canvi de salutació ja no és pendent: és a la preparació.

**Visual:** Ressaltar només el comiat a TREBALL V3. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Canvia salutacio"

**Terminal · comanda completa visible:**

```text
git commit -m "Canvia salutacio"
```

**Subratllat:** `git commit`.

**Locució:** Amb git commit enregistrarem el contingut preparat en una versió local.

**Visual:** Mantenir visible el text complet: git commit -m "Canvia salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Canvia salutacio"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema indica que a continuació escrivim el missatge del canvi.

**Visual:** Mantenir visible el text complet: git commit -m "Canvia salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Canvia salutacio"
```

**Subratllat:** `"Canvia salutacio"`.

**Locució:** El text entre cometes descriu la feina: Canvia salutació. Les cometes agrupen el missatge en un sol argument.

**Visual:** Mantenir visible el text complet: git commit -m "Canvia salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Canvia salutacio".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Canvia salutacio"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit -m "Canvia salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Canvia salutacio"
```

**Locució:** L’historial enregistra V2. El comiat continua al treball, sense confirmar. El commit no l’ha eliminat.

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git add helloGit.py

**Terminal · comanda completa visible:**

```text
git add helloGit.py
```

**Subratllat:** `git add`.

**Locució:** Amb git add seleccionem el contingut que volem confirmar.

**Visual:** Mantenir visible el text complet: git add helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git add.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** El nom identifica el fitxer que preparem. La còpia desada ara és la que entra a la preparació.

**Visual:** Mantenir visible el text complet: git add helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git add helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add helloGit.py
```

**Locució:** Ara sí: seleccionem també el comiat i preparem V3.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Afegeix comiat"

**Terminal · comanda completa visible:**

```text
git commit -m "Afegeix comiat"
```

**Subratllat:** `git commit`.

**Locució:** Amb git commit enregistrarem el contingut preparat en una versió local.

**Visual:** Mantenir visible el text complet: git commit -m "Afegeix comiat". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Afegeix comiat"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema indica que a continuació escrivim el missatge del canvi.

**Visual:** Mantenir visible el text complet: git commit -m "Afegeix comiat". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Afegeix comiat"
```

**Subratllat:** `"Afegeix comiat"`.

**Locució:** El text entre cometes descriu la feina: Afegeix comiat. Les cometes agrupen el missatge en un sol argument.

**Visual:** Mantenir visible el text complet: git commit -m "Afegeix comiat". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Afegeix comiat".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Afegeix comiat"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit -m "Afegeix comiat". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Afegeix comiat"
```

**Locució:** Les tres zones coincideixen amb V3. La salutació i el comiat s’han registrat en commits diferents.

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Desar canvia el treball.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Add selecciona el contingut que hi havia en aquell moment.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Commit enregistra la preparació i conserva les altres edicions pendents.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Edita, prepara i torna a editar el mateix fitxer. Compara els dos diffs abans de confirmar per comprovar exactament què entrarà al commit.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
