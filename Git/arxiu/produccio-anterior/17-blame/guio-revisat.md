# Lliçó 17 · Blame: investiga l’origen d’una línia

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Dissetena lliçó, Blame.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a investigar una línia amb blame i comprovar la causa amb show i el context.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Historial A–B–C. B canvia la definició salutació per missatge, però deixa l’ús antic. C només afegeix espais a la línia d’impressió. Treball net; hashes il·lustratius.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Una línia que falla té un context

**Locució:** El programa imprimeix una variable que ja no està definida amb aquell nom. Investigarem les línies relacionades i els commits que les han modificat.

**Visual:** Editor amb línies numerades: 1 comentari; 2 missatge = "Hola, Anna!"; 3 print( salutacio ).

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `python3`.

**Locució:** Reproduïm el problema amb la mateixa prova.

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

**Locució:** La terminal mostra un error de nom a la línia tres. La línia de l’error orienta la investigació, però encara no identifica la causa històrica.

**Visual:** Ressaltar NameError i línia 3 sense atribuir responsabilitats. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git blame helloGit.py

**Terminal · comanda completa visible:**

```text
git blame helloGit.py
```

**Subratllat:** `git blame`.

**Locució:** git blame associa les línies a commits de l’historial consultat.

**Visual:** Mantenir visible el text complet: git blame helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git blame.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git blame helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** Consultem les línies del programa actual.

**Visual:** Mantenir visible el text complet: git blame helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git blame helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git blame helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git blame helloGit.py
```

**Locució:** La línia tres s’associa a C. Això indica una modificació de la línia, no una demostració que C introduís l’error.

**Visual:** Separar columnes hash, autoria, data i contingut. La columna d’autoria es mostra com a context, sense llenguatge de culpabilitat. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git blame -L 3,3 helloGit.py

**Terminal · comanda completa visible:**

```text
git blame -L 3,3 helloGit.py
```

**Subratllat:** `git blame`.

**Locució:** Limitem la consulta a la línia de l’error.

**Visual:** Mantenir visible el text complet: git blame -L 3,3 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git blame.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git blame -L 3,3 helloGit.py
```

**Subratllat:** `-L`.

**Locució:** El guionet ela limita la consulta a un rang de línies.

**Visual:** Mantenir visible el text complet: git blame -L 3,3 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -L.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git blame -L 3,3 helloGit.py
```

**Subratllat:** `3,3`.

**Locució:** El primer número és l’inici i el segon el final; aquí consultem només la línia tres.

**Visual:** Mantenir visible el text complet: git blame -L 3,3 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: 3,3.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git blame -L 3,3 helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git blame -L 3,3 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git blame -L 3,3 helloGit.py
```

**Locució:** Copiem l’identificador de C per revisar què hi va canviar.

**Visual:** Subratllar -L, després el rang i després la fila de la sortida. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git show c95f4a7 -- helloGit.py

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Subratllat:** `git show`.

**Locució:** Comprovem el canvi concret de C.

**Visual:** Mantenir visible el text complet: git show c95f4a7 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git show.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Subratllat:** `c95f4a7`.

**Locució:** És el commit de mostra atribuït a la línia tres.

**Visual:** Mantenir visible el text complet: git show c95f4a7 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: c95f4a7.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git show c95f4a7 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Locució:** C només hi havia afegit espais. La variable ja era incorrecta abans d’aquell retoc.

**Visual:** Diff C amb print(salutacio) → print( salutacio ). Destacar els espais com a canvi de format. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git blame -L 2,2 helloGit.py

**Terminal · comanda completa visible:**

```text
git blame -L 2,2 helloGit.py
```

**Subratllat:** `git blame`.

**Locució:** Seguim la dependència: la línia que defineix la variable.

**Visual:** Mantenir visible el text complet: git blame -L 2,2 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git blame.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git blame -L 2,2 helloGit.py
```

**Subratllat:** `2,2`.

**Locució:** Ara consultem només la línia dos, on es defineix el nom utilitzat pel programa.

**Visual:** Mantenir visible el text complet: git blame -L 2,2 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: 2,2.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git blame -L 2,2 helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git blame -L 2,2 helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git blame -L 2,2 helloGit.py
```

**Locució:** Aquesta línia ens porta a B. El nom definit i el nom imprès no coincideixen.

**Visual:** Unir amb una fletxa missatge de la línia 2 i salutacio de la línia 3. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git show b62d8e1 -- helloGit.py

**Terminal · comanda completa visible:**

```text
git show b62d8e1 -- helloGit.py
```

**Subratllat:** `git show`.

**Locució:** Revisem el canvi de B.

**Visual:** Mantenir visible el text complet: git show b62d8e1 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git show.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show b62d8e1 -- helloGit.py
```

**Subratllat:** `b62d8e1`.

**Locució:** És el commit que modificava la definició de la variable.

**Visual:** Mantenir visible el text complet: git show b62d8e1 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: b62d8e1.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show b62d8e1 -- helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git show b62d8e1 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show b62d8e1 -- helloGit.py
```

**Locució:** B va canviar el nom sense actualitzar-ne l’ús. Ja tenim una explicació del canvi que introdueix la regressió.

**Visual:** Diff B amb la definició anterior i la nova; mantenir la línia d’impressió visible. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Blame orienta cap a modificacions de línies.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Show explica què canviava el commit concret.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Cal seguir el context i les dependències abans d’atribuir l’origen d’un error.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Investiga dues línies relacionades d’un fitxer de pràctiques. Revisa els commits amb show i anota el canvi funcional, separant-lo dels retocs de format.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
