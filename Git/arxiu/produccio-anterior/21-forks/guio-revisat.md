# Lliçó 21 · Forks i upstream: contribueix a un projecte

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Vint-i-unena lliçó, Forks i upstream.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a relacionar original, fork i clon local, i proposar una contribució a l’original.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Projecte original a GitHub que admet contribucions. Crearem un fork propi i el clonarem. Les adreces entre angles són marcadors, no text per executar literalment.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Tres repositoris amb funcions diferents

**Locució:** L’original és el projecte al qual volem contribuir. El fork és un repositori al nostre compte. El clon és la còpia de treball que tindrem a l’ordinador.

**Visual:** Tres caixes persistents: ORIGINAL, FORK PROPI i CLON LOCAL. No presentar el fork com una carpeta local.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Creem el fork al nostre compte

**Locució:** A la interfície del projecte creem el fork i triem el nostre compte com a destinació. El repositori propi queda al servidor; encara falta copiar-lo a l’ordinador.

**Visual:** Esquema de creació de fork amb comptes ficticis; cap publicació real durant la producció del vídeo.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git clone <URL-del-fork> hello-git

**Terminal · comanda completa visible:**

```text
git clone <URL-del-fork> hello-git
```

**Subratllat:** `git clone`.

**Locució:** Clonem el repositori del nostre compte.

**Visual:** Mantenir visible el text complet: git clone <URL-del-fork> hello-git. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git clone.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git clone <URL-del-fork> hello-git
```

**Subratllat:** `<URL-del-fork>`.

**Locució:** Posem l’adreça real del fork, sense els angles del marcador.

**Visual:** Mantenir visible el text complet: git clone <URL-del-fork> hello-git. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: <URL-del-fork>.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git clone <URL-del-fork> hello-git
```

**Subratllat:** `hello-git`.

**Locució:** Aquest és el nom de la carpeta local que es crearà.

**Visual:** Mantenir visible el text complet: git clone <URL-del-fork> hello-git. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: hello-git.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git clone <URL-del-fork> hello-git
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git clone <URL-del-fork> hello-git. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git clone <URL-del-fork> hello-git
```

**Locució:** La carpeta conté el projecte i origin apunta al nostre fork.

**Visual:** Fletxa FORK → LOCAL; etiqueta origin vinculada al fork. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## cd hello-git

**Terminal · comanda completa visible:**

```text
cd hello-git
```

**Subratllat:** `cd`.

**Locució:** Entrem a la còpia local.

**Visual:** Mantenir visible el text complet: cd hello-git. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: cd.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd hello-git
```

**Subratllat:** `hello-git`.

**Locució:** Les ordres següents s’executen dins d’aquesta carpeta.

**Visual:** Mantenir visible el text complet: cd hello-git. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: hello-git.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd hello-git
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: cd hello-git. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd hello-git
```

**Locució:** La terminal queda al projecte local.

**Visual:** Ruta visible a la terminal. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git remote add upstream <URL-original>

**Terminal · comanda completa visible:**

```text
git remote add upstream <URL-original>
```

**Subratllat:** `git remote add`.

**Locució:** Afegim una segona connexió amb git remote add.

**Visual:** Mantenir visible el text complet: git remote add upstream <URL-original>. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git remote add.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git remote add upstream <URL-original>
```

**Subratllat:** `upstream`.

**Locució:** És el nom que donem al remot de l’original. És una convenció de l’exemple.

**Visual:** Mantenir visible el text complet: git remote add upstream <URL-original>. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: upstream.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git remote add upstream <URL-original>
```

**Subratllat:** `<URL-original>`.

**Locució:** Aquí posem l’adreça del projecte original, diferent de la del fork.

**Visual:** Mantenir visible el text complet: git remote add upstream <URL-original>. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: <URL-original>.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git remote add upstream <URL-original>
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git remote add upstream <URL-original>. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git remote add upstream <URL-original>
```

**Locució:** Origin continua apuntant al fork i upstream apunta a l’original. Afegir el remot no descarrega encara les novetats.

**Visual:** Dues connexions amb noms i adreces diferenciades. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git remote -v

**Terminal · comanda completa visible:**

```text
git remote -v
```

**Subratllat:** `git remote`.

**Locució:** Comprovem les connexions.

**Visual:** Mantenir visible el text complet: git remote -v. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git remote.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git remote -v
```

**Subratllat:** `-v`.

**Locució:** El guionet ve mostra les adreces configurades per consultar i publicar.

**Visual:** Mantenir visible el text complet: git remote -v. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -v.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git remote -v
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git remote -v. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git remote -v
```

**Locució:** Llegim quin servidor correspon a cada nom. No confonem origin amb upstream.

**Visual:** Taula amb nom, adreça i direcció d’ús; ressaltar una fila cada vegada. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## L’original incorpora una novetat

**Locució:** L’original avança a C mentre el nostre fork i main local continuen a B. Amb el treball net i sense divergències, primer actualitzarem la còpia local i després el fork.

**Visual:** Original C; fork B; local B. La novetat és a README.md i no toca la salutació.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git fetch upstream

**Terminal · comanda completa visible:**

```text
git fetch upstream
```

**Subratllat:** `git fetch`.

**Locució:** Descarreguem de l’original.

**Visual:** Mantenir visible el text complet: git fetch upstream. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git fetch.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git fetch upstream
```

**Subratllat:** `upstream`.

**Locució:** Consultem l’original, no el fork propi.

**Visual:** Mantenir visible el text complet: git fetch upstream. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: upstream.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git fetch upstream
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git fetch upstream. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git fetch upstream
```

**Locució:** La referència upstream/main local apunta a C. Main local encara és a B.

**Visual:** Actualitzar només la referència de seguiment. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git merge --ff-only upstream/main

**Terminal · comanda completa visible:**

```text
git merge --ff-only upstream/main
```

**Subratllat:** `git merge`.

**Locució:** Incorporem la novetat a main local.

**Visual:** Mantenir visible el text complet: git merge --ff-only upstream/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git merge.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only upstream/main
```

**Subratllat:** `--ff-only`.

**Locució:** La integració només continua si pot ser un avançament directe.

**Visual:** Mantenir visible el text complet: git merge --ff-only upstream/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --ff-only.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only upstream/main
```

**Subratllat:** `upstream/main`.

**Locució:** És l’estat de main que acabem de descarregar de l’original.

**Visual:** Mantenir visible el text complet: git merge --ff-only upstream/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: upstream/main.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only upstream/main
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git merge --ff-only upstream/main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --ff-only upstream/main
```

**Locució:** Main local avança a C. El fork encara és a B.

**Visual:** Moure només main local. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git push origin main

**Terminal · comanda completa visible:**

```text
git push origin main
```

**Subratllat:** `git push`.

**Locució:** Enviem la branca actualitzada al nostre fork.

**Visual:** Mantenir visible el text complet: git push origin main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git push.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push origin main
```

**Subratllat:** `origin`.

**Locució:** La destinació és el fork propi.

**Visual:** Mantenir visible el text complet: git push origin main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: origin.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push origin main
```

**Subratllat:** `main`.

**Locució:** Publiquem la seva branca main.

**Visual:** Mantenir visible el text complet: git push origin main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: main.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push origin main
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git push origin main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push origin main
```

**Locució:** Original, fork i còpia local coincideixen a C.

**Visual:** Fletxa LOCAL → FORK; no enviar aquesta ordre a upstream. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git switch -c salutacio

**Terminal · comanda completa visible:**

```text
git switch -c salutacio
```

**Subratllat:** `git switch`.

**Locució:** Amb git switch seleccionem la branca on treballarem.

**Visual:** Mantenir visible el text complet: git switch -c salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git switch.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git switch -c salutacio
```

**Subratllat:** `-c`.

**Locució:** El guionet ce crea una branca nova i hi canvia.

**Visual:** Mantenir visible el text complet: git switch -c salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -c.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git switch -c salutacio
```

**Subratllat:** `salutacio`.

**Locució:** Aquest és el nom de la branca de destinació. La nova etiqueta comença al commit actual.

**Visual:** Mantenir visible el text complet: git switch -c salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: salutacio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git switch -c salutacio
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git switch -c salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git switch -c salutacio
```

**Locució:** Creem la branca de la contribució des de la base actualitzada.

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Editem la contribució

**Locució:** Personalitzem la salutació i la provem. Després preparem el fitxer i confirmem la millora a la nostra branca.

**Visual:** Editor i prova python3 helloGit.py abans de preparar el canvi.

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

**Locució:** La salutació nova funciona a la branca de contribució. Encara no l’hem confirmada ni publicada.

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

**Locució:** La contribució queda preparada.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Personalitza la salutacio"

**Terminal · comanda completa visible:**

```text
git commit -m "Personalitza la salutacio"
```

**Subratllat:** `git commit`.

**Locució:** Amb git commit enregistrarem el contingut preparat en una versió local.

**Visual:** Mantenir visible el text complet: git commit -m "Personalitza la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Personalitza la salutacio"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema indica que a continuació escrivim el missatge del canvi.

**Visual:** Mantenir visible el text complet: git commit -m "Personalitza la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Personalitza la salutacio"
```

**Subratllat:** `"Personalitza la salutacio"`.

**Locució:** El text entre cometes descriu la feina: Personalitza la salutació. Les cometes agrupen el missatge en un sol argument.

**Visual:** Mantenir visible el text complet: git commit -m "Personalitza la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Personalitza la salutacio".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Personalitza la salutacio"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit -m "Personalitza la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Personalitza la salutacio"
```

**Locució:** El commit D és a salutació local; l’original continua a C.

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git push -u origin salutacio

**Terminal · comanda completa visible:**

```text
git push -u origin salutacio
```

**Subratllat:** `git push`.

**Locució:** Amb git push compartim els commits de la branca amb el remot.

**Visual:** Mantenir visible el text complet: git push -u origin salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git push.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push -u origin salutacio
```

**Subratllat:** `-u`.

**Locució:** El guionet u desa la relació de seguiment per als enviaments següents.

**Visual:** Mantenir visible el text complet: git push -u origin salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -u.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push -u origin salutacio
```

**Subratllat:** `origin`.

**Locució:** origin és el nom del remot al qual enviem els commits.

**Visual:** Mantenir visible el text complet: git push -u origin salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: origin.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push -u origin salutacio
```

**Subratllat:** `salutacio`.

**Locució:** Aquest és el nom de la branca que publiquem.

**Visual:** Mantenir visible el text complet: git push -u origin salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: salutacio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push -u origin salutacio
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git push -u origin salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push -u origin salutacio
```

**Locució:** La branca de la contribució es publica al fork propi.

**Visual:** Conservar el mateix identificador a local i remot. La fletxa envia commits; no envia edicions sense confirmar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Proposem el canvi a l’original

**Locució:** A la pull request triem main de l’original com a destinació i salutació del nostre fork com a origen. Descrivim la millora i com l’hem provat. La revisió encara queda pendent.

**Visual:** Formulari amb repositori i branca en tots dos costats. No representar una fusió ni una aprovació que encara no s’han produït.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Fork és un repositori remot propi; clon és una còpia local.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Origin i upstream connecten amb repositoris diferents en aquest exemple.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Publiquem al fork i proposem la contribució a l’original.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Amb un projecte de pràctiques, identifica les dues adreces remotes i dibuixa el recorregut original, fork i local abans de preparar una contribució.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
