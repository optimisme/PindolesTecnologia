# Lliçó 16 · Pull requests: revisa i integra una feina en equip

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Setzena lliçó, Pull requests.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a publicar una branca, obrir una proposta, revisar-la i incorporar la versió acordada.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Projecte ja clonat, main actualitzada i treball net. Tenim permís per publicar branques al mateix repositori i una altra persona revisarà la proposta.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Una proposta abans d’integrar

**Locució:** Una pull request proposa incorporar canvis entre branques i ofereix un espai per revisar-los. Publicar una branca i integrar-la són passos diferents.

**Visual:** Esquema main / salutacio / PROPOSTA. Encara no moure main.

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

**Locució:** Comencem amb main al dia i sense canvis pendents.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** Treballarem en una branca pròpia perquè es pugui revisar per separat.

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Mostrem el canvi abans de confirmar

**Locució:** Editem el programa per personalitzar la salutació i el provem. L’edició visible és la que després seleccionarem per al commit.

**Visual:** Editor print("Hola, Anna") i execució amb sortida coincident.

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

**Locució:** Veiem la salutació personalitzada encara sense exclamació. Aquesta és la primera versió que proposem.

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

**Locució:** La salutació personalitzada queda preparada.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Millora la salutacio"

**Terminal · comanda completa visible:**

```text
git commit -m "Millora la salutacio"
```

**Subratllat:** `git commit`.

**Locució:** Amb git commit enregistrarem el contingut preparat en una versió local.

**Visual:** Mantenir visible el text complet: git commit -m "Millora la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Millora la salutacio"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema indica que a continuació escrivim el missatge del canvi.

**Visual:** Mantenir visible el text complet: git commit -m "Millora la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Millora la salutacio"
```

**Subratllat:** `"Millora la salutacio"`.

**Locució:** El text entre cometes descriu la feina: Millora la salutació. Les cometes agrupen el missatge en un sol argument.

**Visual:** Mantenir visible el text complet: git commit -m "Millora la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Millora la salutacio".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Millora la salutacio"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit -m "Millora la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Millora la salutacio"
```

**Locució:** El canvi és un commit local de salutació; main continua al punt inicial.

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

**Locució:** La branca ja és al remot i es pot comparar amb main. Encara no l’hi hem integrat.

**Visual:** Conservar el mateix identificador a local i remot. La fletxa envia commits; no envia edicions sense confirmar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Triem origen i destinació

**Locució:** A la interfície obrim una proposta amb main com a branca de destinació. La branca de comparació és salutació, que conté el nostre canvi.

**Visual:** Esquema de formulari: base main; compare salutacio. Subratllar primer destinació, després origen. Text complet d’exemple: Personalitza la salutació; prova: python3 helloGit.py.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Escrivim un títol, expliquem la millora i indiquem com l’hem provat. Revisem el diff abans de crear la proposta.

**Visual:** Esquema de formulari: base main; compare salutacio. Subratllar primer destinació, després origen. Text complet d’exemple: Personalitza la salutació; prova: python3 helloGit.py.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## La revisió concreta el resultat

**Locució:** La persona revisora proposa afegir una exclamació. Editem la mateixa branca, desem, provem la salutació amb exclamació i preparem el canvi.

**Visual:** Comentari docent simulat i editor print("Hola, Anna!"). No simular una aprovació anterior com si cobrís automàticament aquesta nova versió.

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

**Locució:** La salutació ara acaba en exclamació. Prepararem aquesta correcció a la mateixa branca.

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

**Locució:** La millora demanada queda preparada.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Completa la salutacio"

**Terminal · comanda completa visible:**

```text
git commit -m "Completa la salutacio"
```

**Subratllat:** `git commit`.

**Locució:** Amb git commit enregistrarem el contingut preparat en una versió local.

**Visual:** Mantenir visible el text complet: git commit -m "Completa la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Completa la salutacio"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema indica que a continuació escrivim el missatge del canvi.

**Visual:** Mantenir visible el text complet: git commit -m "Completa la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Completa la salutacio"
```

**Subratllat:** `"Completa la salutacio"`.

**Locució:** El text entre cometes descriu la feina: Completa la salutació. Les cometes agrupen el missatge en un sol argument.

**Visual:** Mantenir visible el text complet: git commit -m "Completa la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Completa la salutacio".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Completa la salutacio"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit -m "Completa la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Completa la salutacio"
```

**Locució:** El commit nou completa la mateixa branca de la proposta.

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git push

**Terminal · comanda completa visible:**

```text
git push
```

**Subratllat:** `git push`.

**Locució:** Amb git push compartim els commits de la branca amb el remot.

**Visual:** Mantenir visible el text complet: git push. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git push.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git push. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git push
```

**Locució:** La mateixa pull request incorpora el commit nou. No cal obrir una proposta diferent.

**Visual:** Conservar el mateix identificador a local i remot. La fletxa envia commits; no envia edicions sense confirmar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Revisem la versió actualitzada

**Locució:** Després de revisar l’actualització i complir els requisits del repositori, una persona amb permís pot integrar-la. En aquest exemple es crea un commit de merge.

**Visual:** Interfície esquemàtica amb nova revisió i Create a merge commit. Graf remot amb M i dos pares. No actuar sobre cap servei real.

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

**Locució:** La nostra branca local main encara ha d’incorporar la fusió del remot.

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git pull --ff-only

**Terminal · comanda completa visible:**

```text
git pull --ff-only
```

**Subratllat:** `git pull`.

**Locució:** Actualitzem la còpia local de main.

**Visual:** Mantenir visible el text complet: git pull --ff-only. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git pull.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git pull --ff-only
```

**Subratllat:** `--ff-only`.

**Locució:** L’avançament directe és possible perquè el main local no ha divergit.

**Visual:** Mantenir visible el text complet: git pull --ff-only. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --ff-only.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git pull --ff-only
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git pull --ff-only. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git pull --ff-only
```

**Locució:** Main local incorpora M i el programa mostra el resultat revisat.

**Visual:** Fer coincidir el mateix M al remot i al local; executar la prova final. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** La branca publicada permet comparar la proposta.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Un push a la mateixa branca actualitza la proposta existent.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Revisió i integració són passos explícits; després actualitzem el main local.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Amb un repositori de pràctiques i una persona col·laboradora, publica una branca, revisa la diferència i actualitza la mateixa proposta amb una millora petita.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
