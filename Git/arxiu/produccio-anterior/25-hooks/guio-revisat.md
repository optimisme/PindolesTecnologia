# Lliçó 25 · Hooks: comprova la sintaxi abans del commit

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Vint-i-cinquena lliçó, Hooks.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a entendre un control local pre-commit que comprova la sintaxi de la versió preparada.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Repositori de pràctiques ordinari amb .git i sense hooks actius ni core.hooksPath personalitzat. Git i python3 disponibles; entorn compatible amb shebang i chmod. El programa ja està seguit.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Comprovar abans de crear el commit

**Locució:** Un hook és un programa que Git pot executar en un moment concret. Prepararem un control local de tipus pre-commit per revisar la sintaxi abans de crear el commit.

**Visual:** Línia temporal ADD → HOOK → COMMIT. El control s’interposa abans de crear el node, no després.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## El control llegeix la preparació

**Locució:** Creem el fitxer de control a la ruta que veus a la pantalla i hi desem el codi complet.

**Visual:** Editor complet a .git/hooks/pre-commit:
```python
#!/usr/bin/env python3
import subprocess

source = subprocess.check_output(
    ["git", "show", ":helloGit.py"], text=True
)
compile(source, "helloGit.py", "exec")
```
Ressaltar primer la ruta i després :helloGit.py.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

**Locució:** El control ha de comprovar el que entrarà al commit. Per això llegim el programa des de l’índex, encara que l’editor tingui una altra versió.

**Visual:** Editor complet a .git/hooks/pre-commit:
```python
#!/usr/bin/env python3
import subprocess

source = subprocess.check_output(
    ["git", "show", ":helloGit.py"], text=True
)
compile(source, "helloGit.py", "exec")
```
Ressaltar primer la ruta i després :helloGit.py.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Dues parts del codi

**Locució:** La consulta amb git show i els dos punts llegeix el contingut preparat. La funció compile comprova que el text tingui sintaxi vàlida; aquí no executa el programa ni prova la seva lògica.

**Visual:** Mantenir el codi complet. Subratllar la lectura de l’índex i després compile. Si no es pot llegir el fitxer obligatori, el control també falla.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## chmod +x .git/hooks/pre-commit

**Terminal · comanda completa visible:**

```text
chmod +x .git/hooks/pre-commit
```

**Subratllat:** `chmod`.

**Locució:** En aquest entorn fem executable el control.

**Visual:** Mantenir visible el text complet: chmod +x .git/hooks/pre-commit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: chmod.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
chmod +x .git/hooks/pre-commit
```

**Subratllat:** `+x`.

**Locució:** Afegeix el permís d’execució.

**Visual:** Mantenir visible el text complet: chmod +x .git/hooks/pre-commit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: +x.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
chmod +x .git/hooks/pre-commit
```

**Subratllat:** `.git/hooks/pre-commit`.

**Locució:** És el fitxer que acabem de desar al repositori de pràctiques.

**Visual:** Mantenir visible el text complet: chmod +x .git/hooks/pre-commit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: .git/hooks/pre-commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
chmod +x .git/hooks/pre-commit
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: chmod +x .git/hooks/pre-commit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
chmod +x .git/hooks/pre-commit
```

**Locució:** Git executarà aquest control local en intentar confirmar. No l’hem afegit com un fitxer versionat del projecte.

**Visual:** Ruta completa visible, fitxer desat i indicador EXECUTABLE. No donar per fet que tots els entorns gestionen permisos igual. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Preparem deliberadament una sintaxi incorrecta

**Locució:** Traiem el parèntesi final de la salutació i desem el fitxer. Aquesta és la versió incorrecta que prepararem per comprovar el control.

**Visual:** Editor print("Hola, Anna!" sense el parèntesi final. Etiqueta PROVA DEL CONTROL.

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

**Locució:** La versió sense parèntesi entra a la preparació.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Personalitza la salutacio"

**Terminal · comanda completa visible:**

```text
git commit -m "Personalitza la salutacio"
```

**Subratllat:** `git commit`.

**Locució:** Intentem confirmar el contingut preparat.

**Visual:** Mantenir visible el text complet: git commit -m "Personalitza la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Personalitza la salutacio"
```

**Subratllat:** `-m`.

**Locució:** Aquest argument introdueix el missatge del commit; el control encara pot impedir-ne la creació.

**Visual:** Mantenir visible el text complet: git commit -m "Personalitza la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Personalitza la salutacio"
```

**Subratllat:** `"Personalitza la salutacio"`.

**Locució:** El missatge descriu la personalització de la salutació. Les cometes el mantenen en un sol argument.

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

**Locució:** El hook falla amb un error de sintaxi. Git atura l’operació i no crea cap commit nou.

**Visual:** Node C encara inexistent. Terminal amb error i panell ÍNDEX: INCORRECTE. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Corregim només el treball

**Locució:** Reposem el parèntesi i desem a l’editor. Encara no hem preparat la correcció: el treball és correcte, però l’índex conserva el text anterior.

**Visual:** Dos panells amb el parèntesi present al treball i absent a la preparació.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Personalitza la salutacio"

**Terminal · comanda completa visible:**

```text
git commit -m "Personalitza la salutacio"
```

**Subratllat:** `git commit`.

**Locució:** Tornem a intentar confirmar abans de preparar la correcció.

**Visual:** Mantenir visible el text complet: git commit -m "Personalitza la salutacio". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

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

**Locució:** El control continua fallant perquè llegeix la preparació. Corregir l’editor per si sol no canvia el contingut seleccionat.

**Visual:** Fletxa HOOK → ÍNDEX, no cap a l’editor; cap node nou. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** Ara la preparació rep la versió amb sintaxi correcta.

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

**Locució:** El control acaba correctament i Git crea el commit. Treball, preparació i historial coincideixen amb el text corregit.

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Un control concret, amb un abast concret

**Locució:** Aquest control comprova sintaxi, no que el programa faci el que volem. És local, no s’instal·la als altres ordinadors amb un push i es pot ometre. Els controls compartits necessiten una configuració acordada.

**Visual:** Etiquetes SINTAXI / LOCAL / NO DISTRIBUÏT PEL PUSH. No presentar-lo com una garantia general de qualitat.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** El pre-commit s’executa abans de crear el commit.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** El control de l’exemple comprova el contingut de l’índex.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Cal preparar la correcció perquè la comprovi; continua sent una ajuda local de sintaxi.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En un repositori de pràctiques separat, instal·la el codi mostrat i compara un intent amb sintaxi incorrecta, un altre corregint només l’editor i el final després d’add.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
