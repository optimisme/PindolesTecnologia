# Lliçó 24 · Worktree: prepara una correcció sense interrompre la feina

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Vint-i-quatrena lliçó, Worktree.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a fer una correcció en una altra carpeta de treball conservant la feina pendent original.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Carpeta projecte a salutació amb una edició sense preparar. Main a B no està activa en cap altre worktree. La carpeta auxiliar encara no existeix.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Dues carpetes, preparacions separades

**Locució:** Volem corregir main sense interrompre la salutació pendent. Un worktree afegeix una carpeta de treball vinculada al mateix repositori, amb el seu índex i la seva branca activa.

**Visual:** Dos espais diferenciats; ORIGINAL a salutacio amb canvi pendent i AUXILIAR encara inexistent.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git worktree add -b correccio ../projecte-correccio main

**Terminal · comanda completa visible:**

```text
git worktree add -b correccio ../projecte-correccio main
```

**Subratllat:** `git worktree add`.

**Locució:** Creem una altra carpeta per a la correcció.

**Visual:** Mantenir visible el text complet: git worktree add -b correccio ../projecte-correccio main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git worktree add.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree add -b correccio ../projecte-correccio main
```

**Subratllat:** `-b`.

**Locució:** El guionet be crea una branca nova per al worktree.

**Visual:** Mantenir visible el text complet: git worktree add -b correccio ../projecte-correccio main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -b.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree add -b correccio ../projecte-correccio main
```

**Subratllat:** `correccio`.

**Locució:** És el nom de la branca de la correcció.

**Visual:** Mantenir visible el text complet: git worktree add -b correccio ../projecte-correccio main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: correccio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree add -b correccio ../projecte-correccio main
```

**Subratllat:** `../projecte-correccio`.

**Locució:** És el camí de la nova carpeta, al costat de l’original.

**Visual:** Mantenir visible el text complet: git worktree add -b correccio ../projecte-correccio main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: ../projecte-correccio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree add -b correccio ../projecte-correccio main
```

**Subratllat:** `main`.

**Locució:** És el punt de partida; la correcció comença a la versió de main.

**Visual:** Mantenir visible el text complet: git worktree add -b correccio ../projecte-correccio main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: main.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree add -b correccio ../projecte-correccio main
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git worktree add -b correccio ../projecte-correccio main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree add -b correccio ../projecte-correccio main
```

**Locució:** L’auxiliar comença neta a correcció. La carpeta original conserva l’edició pendent a salutació.

**Visual:** Crear la segona carpeta i índex; conservar el text de l’editor original sense moviments. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git worktree list

**Terminal · comanda completa visible:**

```text
git worktree list
```

**Subratllat:** `git worktree list`.

**Locució:** Consultem les carpetes vinculades.

**Visual:** Mantenir visible el text complet: git worktree list. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git worktree list.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree list
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git worktree list. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree list
```

**Locució:** La llista relaciona camins i branques actives. Encara estem treballant des de la carpeta original.

**Visual:** Dues files amb ruta completa i branca, i un indicador AQUÍ SOM. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## cd ../projecte-correccio

**Terminal · comanda completa visible:**

```text
cd ../projecte-correccio
```

**Subratllat:** `cd`.

**Locució:** Entrem a la carpeta auxiliar.

**Visual:** Mantenir visible el text complet: cd ../projecte-correccio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: cd.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd ../projecte-correccio
```

**Subratllat:** `../projecte-correccio`.

**Locució:** El camí ens porta al directori nou, no canvia la branca de la carpeta original.

**Visual:** Mantenir visible el text complet: cd ../projecte-correccio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: ../projecte-correccio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd ../projecte-correccio
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: cd ../projecte-correccio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd ../projecte-correccio
```

**Locució:** La terminal queda a la correcció amb el treball net.

**Visual:** Moure AQUÍ SOM a l’auxiliar; conservar l’editor original com a referència. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Editem només la correcció

**Locució:** Afegim una coma a la salutació original, desem i provem el programa. Aquest retoc es fa al worktree auxiliar.

**Visual:** Editor auxiliar print("Hello, Git!") i prova. L’original continua amb print("Hola, Anna!") sense confirmar.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `python3`.

**Locució:** Executem el programa per comprovar el contingut desat.

**Visual:** Mantenir visible el text complet: python3 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: python3.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** És el fitxer de la còpia de treball que acabem d’editar.

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

**Locució:** La sortida és Hello, Git! a la carpeta auxiliar. La feina de l’original continua al seu lloc.

**Visual:** Mostrar la sortida real del programa al costat de l’editor. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** La correcció queda preparada només a l’índex de la carpeta auxiliar.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Corregeix la puntuacio"

**Terminal · comanda completa visible:**

```text
git commit -m "Corregeix la puntuacio"
```

**Subratllat:** `git commit`.

**Locució:** Amb git commit enregistrarem el contingut preparat en una versió local.

**Visual:** Mantenir visible el text complet: git commit -m "Corregeix la puntuacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Corregeix la puntuacio"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema indica que a continuació escrivim el missatge del canvi.

**Visual:** Mantenir visible el text complet: git commit -m "Corregeix la puntuacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Corregeix la puntuacio"
```

**Subratllat:** `"Corregeix la puntuacio"`.

**Locució:** El text entre cometes descriu la feina: Corregeix la puntuació. Les cometes agrupen el missatge en un sol argument.

**Visual:** Mantenir visible el text complet: git commit -m "Corregeix la puntuacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Corregeix la puntuacio".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Corregeix la puntuacio"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit -m "Corregeix la puntuacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Corregeix la puntuacio"
```

**Locució:** D és un commit de correcció. La feina pendent de salutació queda fora d’aquest commit.

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

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

**Locució:** Canviem a main dins de l’auxiliar. Això és possible perquè main no està activa en cap altre worktree.

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git merge --ff-only correccio

**Terminal · comanda completa visible:**

```text
git merge --ff-only correccio
```

**Subratllat:** `git merge`.

**Locució:** Incorporem la correcció a main.

**Visual:** Mantenir visible el text complet: git merge --ff-only correccio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git merge.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only correccio
```

**Subratllat:** `--ff-only`.

**Locució:** Només permet l’avançament directe d’aquest exemple.

**Visual:** Mantenir visible el text complet: git merge --ff-only correccio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --ff-only.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only correccio
```

**Subratllat:** `correccio`.

**Locució:** És la branca de la correcció que acabem de confirmar.

**Visual:** Mantenir visible el text complet: git merge --ff-only correccio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: correccio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only correccio
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git merge --ff-only correccio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only correccio
```

**Locució:** Main avança a D. L’original continua a salutació B amb l’edició pendent intacta.

**Visual:** Main i correccio a D; salutacio a B; dos índexs encara separats. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git -C ../projecte status --short

**Terminal · comanda completa visible:**

```text
git -C ../projecte status --short
```

**Subratllat:** `status`.

**Locució:** Consultem la carpeta original sense abandonar encara l’auxiliar.

**Visual:** Mantenir visible el text complet: git -C ../projecte status --short. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: status.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git -C ../projecte status --short
```

**Subratllat:** `-C`.

**Locució:** El guionet ce majúscula indica la carpeta des d’on Git executarà la consulta.

**Visual:** Mantenir visible el text complet: git -C ../projecte status --short. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -C.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git -C ../projecte status --short
```

**Subratllat:** `../projecte`.

**Locució:** És el directori original.

**Visual:** Mantenir visible el text complet: git -C ../projecte status --short. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: ../projecte.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git -C ../projecte status --short
```

**Subratllat:** `--short`.

**Locució:** Mostra l’estat breu del treball d’aquella carpeta.

**Visual:** Mantenir visible el text complet: git -C ../projecte status --short. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --short.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git -C ../projecte status --short
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git -C ../projecte status --short. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git -C ../projecte status --short
```

**Locució:** L’original continua amb la salutació modificada sense preparar. L’auxiliar és neta després de la correcció.

**Visual:** Mostrar la consulta identificada com ORIGINAL, diferenciada de l’estat local de l’auxiliar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## cd ../projecte

**Terminal · comanda completa visible:**

```text
cd ../projecte
```

**Subratllat:** `cd`.

**Locució:** Tornem a la carpeta original.

**Visual:** Mantenir visible el text complet: cd ../projecte. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: cd.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd ../projecte
```

**Subratllat:** `..`.

**Locució:** Els dos punts formen part del camí relatiu per pujar al directori pare.

**Visual:** Mantenir visible el text complet: cd ../projecte. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: ...

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd ../projecte
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: cd ../projecte. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd ../projecte
```

**Locució:** Tornem a treballar a salutació. La correcció confirmada ja és a main.

**Visual:** Ruta original i editor pendent intacte. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git worktree remove ../projecte-correccio

**Terminal · comanda completa visible:**

```text
git worktree remove ../projecte-correccio
```

**Subratllat:** `git worktree remove`.

**Locució:** Retirem la carpeta auxiliar des de fora.

**Visual:** Mantenir visible el text complet: git worktree remove ../projecte-correccio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git worktree remove.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree remove ../projecte-correccio
```

**Subratllat:** `../projecte-correccio`.

**Locució:** La carpeta ha d’estar neta en aquest exemple. La retirem sense forçar.

**Visual:** Mantenir visible el text complet: git worktree remove ../projecte-correccio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: ../projecte-correccio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree remove ../projecte-correccio
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git worktree remove ../projecte-correccio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git worktree remove ../projecte-correccio
```

**Locució:** Desapareix el directori auxiliar. Main, correcció i el commit D continuen al repositori.

**Visual:** Retirar només la icona de carpeta, sense esborrar les etiquetes ni el node del graf. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Els worktrees comparteixen historial i branques.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Cada carpeta té treball, índex i branca activa propis.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Retirar una carpeta auxiliar neta conserva els commits i les branques.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En un repositori de pràctiques, deixa una edició pendent i crea un worktree auxiliar per a una correcció petita. Comprova els dos estats abans de retirar l’auxiliar neta.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
