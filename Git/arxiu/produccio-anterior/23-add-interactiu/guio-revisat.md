# Lliçó 23 · Add interactiu: prepara només una part del fitxer

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Vint-i-tresena lliçó, Add interactiu.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a preparar una part d’un fitxer i deixar l’altra edició pendent al treball.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** helloGit.py ja seguit, sense canvis preparats. Modifiquem salutació i comiat, prou separats perquè apareguin en dos blocs independents de diff.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Dues edicions, dos canvis separables

**Locució:** El programa té una funció de salutació i una de comiat, separades per altres funcions que no canviem. Mostrem el contingut inicial abans d’editar.

**Visual:** Editor amb les dues edicions ressaltades i les funcions intermèdies sense canvis. No presentar dos blocs garantits per a qualsevol fitxer.
Codi inicial complet:
```python
def saluda():
    return "Hello Git!"


def doble(valor):
    return valor * 2


def suma(a, b):
    return a + b


def comiat():
    return "Fins aviat!"


print(saluda())
print(comiat())
```
Codi editat complet:
```python
def saluda():
    return "Hola, Anna!"


def doble(valor):
    return valor * 2


def suma(a, b):
    return a + b


def comiat():
    return "Adeu!"


print(saluda())
print(comiat())
```
Mostrar les dues funcions modificades per torns; conservar les intermèdies sense canvis com a context.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

**Locució:** Canviem la salutació a Hola, Anna! i el comiat a Adeu! Volem confirmar només la salutació i conservar el comiat com a feina pendent.

**Visual:** Editor amb les dues edicions ressaltades i les funcions intermèdies sense canvis. No presentar dos blocs garantits per a qualsevol fitxer.
Codi inicial complet:
```python
def saluda():
    return "Hello Git!"


def doble(valor):
    return valor * 2


def suma(a, b):
    return a + b


def comiat():
    return "Fins aviat!"


print(saluda())
print(comiat())
```
Codi editat complet:
```python
def saluda():
    return "Hola, Anna!"


def doble(valor):
    return valor * 2


def suma(a, b):
    return a + b


def comiat():
    return "Adeu!"


print(saluda())
print(comiat())
```
Mostrar les dues funcions modificades per torns; conservar les intermèdies sense canvis com a context.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git diff -- helloGit.py

**Terminal · comanda completa visible:**

```text
git diff -- helloGit.py
```

**Subratllat:** `git diff`.

**Locució:** Revisem el contingut abans de seleccionar-lo.

**Visual:** Mantenir visible el text complet: git diff -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git diff.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff -- helloGit.py
```

**Subratllat:** `--`.

**Locució:** Separa les opcions del camí de fitxer.

**Visual:** Mantenir visible el text complet: git diff -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff -- helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** Consultem els dos blocs del mateix fitxer.

**Visual:** Mantenir visible el text complet: git diff -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff -- helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git diff -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff -- helloGit.py
```

**Locució:** El primer bloc modifica la salutació i el segon, el comiat. Els signes de diff no formen part del codi que editem.

**Visual:** Dos blocs clarament separats i numerats BLOC 1 / BLOC 2. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git add -p helloGit.py

**Terminal · comanda completa visible:**

```text
git add -p helloGit.py
```

**Subratllat:** `git add`.

**Locució:** Entrem a la preparació interactiva.

**Visual:** Mantenir visible el text complet: git add -p helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git add.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add -p helloGit.py
```

**Subratllat:** `-p`.

**Locució:** El guionet pe permet seleccionar blocs de canvi.

**Visual:** Mantenir visible el text complet: git add -p helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -p.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add -p helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** Limitem la sessió al fitxer del programa.

**Visual:** Mantenir visible el text complet: git add -p helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add -p helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git add -p helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add -p helloGit.py
```

**Locució:** Git mostra el primer bloc i espera una resposta. Encara no introduïm una altra comanda de terminal.

**Visual:** Terminal en mode INTERACTIU, primer bloc de salutació i opcions de resposta. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## y

**Resposta interactiva · comanda completa visible:**

```text
y
```

**Subratllat:** `y`.

**Locució:** Responem i grega, de yes, per preparar el primer bloc.

**Visual:** Mantenir visible el text complet: y. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: y.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Resposta interactiva · comanda completa visible:**

```text
y
```

**Locució:** Introduïm la resposta.

**Visual:** Mantenir visible el text complet: y. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Resposta interactiva · comanda completa visible:**

```text
y
```

**Locució:** La salutació passa a la preparació. La mateixa sessió continua amb el segon bloc.

**Visual:** Moure només el bloc de salutació del treball a l’índex. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## n

**Resposta interactiva · comanda completa visible:**

```text
n
```

**Subratllat:** `n`.

**Locució:** Responem ena per deixar fora el segon bloc.

**Visual:** Mantenir visible el text complet: n. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: n.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Resposta interactiva · comanda completa visible:**

```text
n
```

**Locució:** Introduïm la resposta.

**Visual:** Mantenir visible el text complet: n. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Resposta interactiva · comanda completa visible:**

```text
n
```

**Locució:** El comiat continua al treball i no entra a la preparació. La sessió acaba en aquest exemple de dos blocs.

**Visual:** Conservar el comiat al treball. Tornar a mostrar el prompt normal de la terminal. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git diff --staged

**Terminal · comanda completa visible:**

```text
git diff --staged
```

**Subratllat:** `git diff`.

**Locució:** Comprovem què hem preparat.

**Visual:** Mantenir visible el text complet: git diff --staged. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git diff.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff --staged
```

**Subratllat:** `--staged`.

**Locució:** Compara la preparació amb l’últim commit.

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

**Locució:** Només hi ha la salutació nova. Aquesta és la selecció que enregistrarem.

**Visual:** Fletxa ÚLTIM COMMIT → PREPARACIÓ; comiat antic a les dues zones. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git diff

**Terminal · comanda completa visible:**

```text
git diff
```

**Subratllat:** `git diff`.

**Locució:** Comprovem què queda pendent.

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

**Locució:** Només apareix el comiat nou. La salutació ja coincideix entre treball i preparació.

**Visual:** Fletxa PREPARACIÓ → TREBALL; destacar el comiat sense preparar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** El commit nou incorpora la salutació. L’edició del comiat continua al treball; el commit no l’ha eliminada.

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

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

**Locució:** El fitxer encara apareix modificat sense preparar pel canvi de comiat.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## El bloc és la unitat de selecció d’aquest exemple

**Locució:** Aquí les edicions formen dos blocs independents. Si Git les agrupa en un sol bloc, cal revisar com dividir-lo o ajustar la selecció; no assumim que cada línia es presenta separadament.

**Visual:** Comparació conceptual DOS BLOCS SEPARATS / UN BLOC CONJUNT, sense introduir noves respostes interactives en aquesta lliçó.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** L’opció p permet preparar blocs concrets.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Les respostes y i n pertanyen a la sessió interactiva.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** El commit enregistra la selecció i conserva la resta d’edicions al treball.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En un fitxer de pràctiques amb dues edicions separades, prepara un bloc i rebutja l’altre. Compara els dos diffs abans de confirmar.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
