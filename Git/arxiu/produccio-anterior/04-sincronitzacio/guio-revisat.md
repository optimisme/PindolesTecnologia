# Lliçó 4 · De classe a casa: clone, pull i push

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Quarta lliçó, Sincronització.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a continuar un projecte entre dos ordinadors sense confondre clone, pull i push.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** A classe tenim el repositori configurat amb main i origin. Treballem en sèrie i comprovem que no hi hagi canvis locals abans d’actualitzar.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Cada ordinador té una còpia local

**Locució:** L’ordinador de classe i el de casa tenen repositoris independents. GitHub és el punt de trobada. Desar o fer un commit en un ordinador no actualitza automàticament els altres.

**Visual:** Classe i casa amb el mateix commit A; servidor entre els dos. Les fletxes només apareixen quan s’executa push o pull.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Acabem el canvi de classe

**Locució:** Editem la salutació, desem i provem el programa. El canvi és al treball de classe; primer el registrarem localment.

**Visual:** Editor de classe amb la versió nova, casa encara amb l’anterior.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

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

**Locució:** El canvi de classe queda preparat.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Practica de classe"

**Terminal · comanda completa visible:**

```text
git commit -m "Practica de classe"
```

**Subratllat:** `git commit`.

**Locució:** Amb git commit enregistrarem el contingut preparat en una versió local.

**Visual:** Mantenir visible el text complet: git commit -m "Practica de classe". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Practica de classe"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema indica que a continuació escrivim el missatge del canvi.

**Visual:** Mantenir visible el text complet: git commit -m "Practica de classe". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Practica de classe"
```

**Subratllat:** `"Practica de classe"`.

**Locució:** El text entre cometes descriu la feina: Pràctica de classe. Les cometes agrupen el missatge en un sol argument.

**Visual:** Mantenir visible el text complet: git commit -m "Practica de classe". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Practica de classe".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Practica de classe"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit -m "Practica de classe". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Practica de classe"
```

**Locució:** El commit B existeix a classe. El servidor i casa continuen a A.

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

**Locució:** El servidor ja conté B. Casa encara no l’ha descarregat.

**Visual:** Conservar el mateix identificador a local i remot. La fletxa envia commits; no envia edicions sense confirmar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Camí A: obtenir el projecte per primer cop

**Locució:** Si en aquest ordinador encara no tenim el projecte, el clonem una vegada. Aquest camí i el d’actualitzar una còpia existent són alternatives.

**Visual:** Panell CAMÍ A · CAP CÒPIA LOCAL. No fer clone i després repetir el camí B com si faltés encara el mateix commit.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git clone <URL-del-repositori> HelloGit

**Camí:** `alternative:first-copy`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git clone <URL-del-repositori> HelloGit
```

**Subratllat:** `git clone`.

**Locució:** git clone crea una còpia local amb fitxers i historial.

**Visual:** Mantenir visible el text complet: git clone <URL-del-repositori> HelloGit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git clone.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git clone <URL-del-repositori> HelloGit
```

**Subratllat:** `<URL-del-repositori>`.

**Locució:** Substituïm aquest marcador per l’adreça real del repositori. No escrivim els signes de menor i major.

**Visual:** Mantenir visible el text complet: git clone <URL-del-repositori> HelloGit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: <URL-del-repositori>.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git clone <URL-del-repositori> HelloGit
```

**Subratllat:** `HelloGit`.

**Locució:** Aquest argument tria el nom de la carpeta nova.

**Visual:** Mantenir visible el text complet: git clone <URL-del-repositori> HelloGit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: HelloGit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git clone <URL-del-repositori> HelloGit
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git clone <URL-del-repositori> HelloGit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git clone <URL-del-repositori> HelloGit
```

**Locució:** La còpia nova ja conté B i té el remot origin configurat.

**Visual:** Animar la creació de la carpeta i després la còpia de B. No presentar-ho com una carpeta buida. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## cd HelloGit

**Camí:** `alternative:first-copy`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
cd HelloGit
```

**Subratllat:** `cd`.

**Locució:** Entrem a la carpeta amb cd.

**Visual:** Mantenir visible el text complet: cd HelloGit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: cd.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd HelloGit
```

**Subratllat:** `HelloGit`.

**Locució:** És la carpeta creada pel clonatge. Les ordres següents s’executen des de dins.

**Visual:** Mantenir visible el text complet: cd HelloGit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: HelloGit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd HelloGit
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: cd HelloGit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
cd HelloGit
```

**Locució:** La terminal queda situada al projecte.

**Visual:** Mostrar la ruta de la terminal actualitzada. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Camí B: actualitzar una còpia existent

**Locució:** Si ja teníem el projecte a casa, entrem a la seva carpeta i revisem l’estat. En aquest exemple és net i no hi ha històries divergents.

**Visual:** Panell CAMÍ B · CÒPIA A CASA A A. Presentar explícitament un retorn a aquesta situació alternativa.

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

**Locució:** No hi ha canvis locals pendents. Podem continuar l’actualització d’aquest exemple.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git pull --ff-only

**Terminal · comanda completa visible:**

```text
git pull --ff-only
```

**Subratllat:** `git pull`.

**Locució:** git pull descarrega les novetats i intenta incorporar-les.

**Visual:** Mantenir visible el text complet: git pull --ff-only. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git pull.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git pull --ff-only
```

**Subratllat:** `--ff-only`.

**Locució:** Aquesta opció només permet avançar la branca directament. Si les històries divergeixen, s’atura i cal revisar la situació.

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

**Locució:** Casa incorpora B i els fitxers s’actualitzen. Ara podem continuar la pràctica.

**Visual:** Casa avança d’A a B després de la descàrrega. Mostrar el contingut nou a l’editor. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Continuem des de casa

**Locució:** Editem i desem una altra millora a casa, ja actualitzada. Aquesta vegada el commit nou naixerà a la còpia de casa.

**Visual:** Editor i ruta CASA visibles. Classe continua a B.

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

**Locució:** La millora funciona a casa i encara és feina pendent.

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

**Locució:** Seleccionem la millora de casa.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Millora des de casa"

**Terminal · comanda completa visible:**

```text
git commit -m "Millora des de casa"
```

**Subratllat:** `git commit`.

**Locució:** Amb git commit enregistrarem el contingut preparat en una versió local.

**Visual:** Mantenir visible el text complet: git commit -m "Millora des de casa". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Millora des de casa"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema indica que a continuació escrivim el missatge del canvi.

**Visual:** Mantenir visible el text complet: git commit -m "Millora des de casa". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Millora des de casa"
```

**Subratllat:** `"Millora des de casa"`.

**Locució:** El text entre cometes descriu la feina: Millora des de casa. Les cometes agrupen el missatge en un sol argument.

**Visual:** Mantenir visible el text complet: git commit -m "Millora des de casa". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Millora des de casa".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Millora des de casa"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit -m "Millora des de casa". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Millora des de casa"
```

**Locució:** C és un commit local de casa. El servidor i classe continuen a B.

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

**Locució:** El servidor incorpora C. Encara falta actualitzar classe.

**Visual:** Conservar el mateix identificador a local i remot. La fletxa envia commits; no envia edicions sense confirmar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Tornem a l’ordinador de classe

**Locució:** A classe encara tenim B. Abans de començar a editar, comprovem l’estat i actualitzem aquesta còpia amb la feina publicada des de casa.

**Visual:** Canvi clar de context: ruta CLASSE. No reutilitzar el prompt de casa.

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

**Locució:** No hi ha canvis pendents a classe; en aquest exemple la història és lineal.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git pull --ff-only

**Terminal · comanda completa visible:**

```text
git pull --ff-only
```

**Subratllat:** `git pull`.

**Locució:** Descarreguem i incorporem el commit que havíem publicat des de casa.

**Visual:** Mantenir visible el text complet: git pull --ff-only. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git pull.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git pull --ff-only
```

**Subratllat:** `--ff-only`.

**Locució:** Només avancem directament. Una divergència s’hauria de revisar com un cas diferent.

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

**Locució:** Classe arriba a C. Les tres còpies comparteixen el mateix commit.

**Visual:** Classe B → C; servidor i casa ja eren a C. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Clone crea la còpia local inicial.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Pull descarrega i integra segons l’opció triada.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Push comparteix commits; les edicions sense confirmar no viatgen.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Practica amb dos clons d’un repositori teu: confirma i publica en un, actualitza l’altre amb el treball net i comprova el mateix identificador als dos.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
