# Lliçó 5 · Merge: portem la prova a main

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Cinquena lliçó, Merge.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a integrar salutació a main i distingir avançament directe i fusió amb dos pares.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Som a salutació, amb el treball net. Main és a B i salutació a C, descendent directe de B. La salutació nova està confirmada i provada.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Origen i destinació

**Locució:** Volem portar a main el canvi de salutació. La branca activa és la destinació del merge. Per això primer ens hi hem de situar.

**Visual:** Graf A–B–C; main a B, salutacio a C. Etiquetes ORIGEN i DESTINACIÓ.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git switch main

**Terminal · comanda completa visible:**

```text
git switch main
```

**Subratllat:** `git switch`.

**Locució:** Amb git switch seleccionem la branca on treballarem.

**Visual:** Mantenir visible el text complet: git switch main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git switch.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git switch main
```

**Subratllat:** `main`.

**Locució:** Aquest és el nom de la branca de destinació. Els fitxers s’actualitzaran a la versió seleccionada.

**Visual:** Mantenir visible el text complet: git switch main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: main.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git switch main
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git switch main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git switch main
```

**Locució:** La destinació activa ara és main. La branca de salutació es conserva.

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git branch --show-current

**Terminal · comanda completa visible:**

```text
git branch --show-current
```

**Subratllat:** `git branch`.

**Locució:** Confirmem on som abans d’integrar.

**Visual:** Mantenir visible el text complet: git branch --show-current. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git branch.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git branch --show-current
```

**Subratllat:** `--show-current`.

**Locució:** Aquesta opció mostra només el nom de la branca activa.

**Visual:** Mantenir visible el text complet: git branch --show-current. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --show-current.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git branch --show-current
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git branch --show-current. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git branch --show-current
```

**Locució:** La terminal mostra main. Encara no hem integrat el canvi.

**Visual:** Ressaltar main tant a la sortida com al graf. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git merge --ff-only salutacio

**Terminal · comanda completa visible:**

```text
git merge --ff-only salutacio
```

**Subratllat:** `git merge`.

**Locució:** git merge incorporarà la història de la branca indicada.

**Visual:** Mantenir visible el text complet: git merge --ff-only salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git merge.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only salutacio
```

**Subratllat:** `--ff-only`.

**Locució:** Només acceptem un avançament directe: la destinació ha de ser un avantpassat de l’origen.

**Visual:** Mantenir visible el text complet: git merge --ff-only salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --ff-only.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only salutacio
```

**Subratllat:** `salutacio`.

**Locució:** És la branca que volem incorporar, no la que volem canviar automàticament a activa.

**Visual:** Mantenir visible el text complet: git merge --ff-only salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: salutacio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only salutacio
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git merge --ff-only salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only salutacio
```

**Locució:** main avança de B a C. Les dues etiquetes apunten al mateix commit; no s’ha creat cap commit de fusió.

**Visual:** Moure només l’etiqueta main sobre el graf existent. Conservar salutacio i tots els nodes. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `python3`.

**Locució:** Comprovem el resultat executant el programa.

**Visual:** Mantenir visible el text complet: python3 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: python3.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** Provem el fitxer de la branca que acabem d’actualitzar.

**Visual:** Mantenir visible el text complet: python3 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

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

**Locució:** A main també apareix la salutació personalitzada. La comprovació funcional complementa la consulta de l’historial.

**Visual:** Terminal amb Hola, Anna! i editor amb el mateix contingut. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Un altre cas: dues branques han avançat

**Locució:** Partim ara d’un cas independent: main i salutació tenen commits diferents després de B. Ja no podem fer un avançament directe. Una fusió compatible pot crear M, un commit amb dos pares.

**Visual:** Separador UN ALTRE CAS. Tornar a B i dibuixar dos camins nous. No moure nodes del cas anterior per inventar el resultat.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git merge salutacio

**Camí:** `alternative:divergent`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git merge salutacio
```

**Subratllat:** `git merge`.

**Locució:** En aquest altre cas, la fusió combina dues històries compatibles.

**Visual:** Mantenir visible el text complet: git merge salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git merge.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge salutacio
```

**Subratllat:** `salutacio`.

**Locució:** Incorporem aquesta branca a la destinació activa, que continua sent main.

**Visual:** Mantenir visible el text complet: git merge salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: salutacio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge salutacio
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git merge salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge salutacio
```

**Locució:** El commit M té dos pares. Si les edicions fossin incompatibles, caldria resoldre el conflicte abans d’acabar.

**Visual:** Graf amb M connectat als dos extrems; indicar que l’editor pot demanar un missatge de fusió i s’ha de desar i tancar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** La branca activa rep la integració.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Un avançament directe mou l’etiqueta sense crear un commit.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Una fusió amb dos pares connecta històries divergents; la branca d’origen es conserva.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En un projecte de pràctiques net, crea un canvi en una branca i integra’l a main amb avançament directe. Revisa el graf i executa el programa.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
