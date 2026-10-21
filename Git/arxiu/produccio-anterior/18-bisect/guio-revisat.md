# Lliçó 18 · Bisect: troba el primer commit que falla

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Divuitena lliçó, Bisect.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a localitzar el primer commit que falla amb una prova repetible i sortir de la cerca.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Historial lineal A–H, main a H i treball net. La mateixa prova funciona a v1.0, situada a A, i falla a H. D introdueix l’error i aquest persisteix fins a H.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Acotar una regressió amb una prova

**Locució:** Coneixem una versió que funciona i una que falla. Bisect tria versions intermèdies per reduir el tram que investiguem. La prova ha de ser la mateixa a cada pas.

**Visual:** Graf A–H; A FUNCIONA, H FALLA. Prova fixa: python3 helloGit.py.

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

**Locució:** No hi ha canvis locals que es puguin barrejar amb els canvis temporals de versió.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git bisect start

**Terminal · comanda completa visible:**

```text
git bisect start
```

**Subratllat:** `git bisect start`.

**Locució:** Iniciem la sessió de cerca.

**Visual:** Mantenir visible el text complet: git bisect start. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git bisect start.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect start
```

**Subratllat:** `start`.

**Locució:** Aquesta subordre inicia la investigació; encara hem d’indicar els dos límits.

**Visual:** Mantenir visible el text complet: git bisect start. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: start.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect start
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git bisect start. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect start
```

**Locució:** La sessió queda oberta, pendent de classificar els extrems.

**Visual:** Indicador CERCA ACTIVA. Main encara és a H. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git bisect bad

**Terminal · comanda completa visible:**

```text
git bisect bad
```

**Subratllat:** `git bisect bad`.

**Locució:** Classifiquem l’extrem actual com a fallada coneguda.

**Visual:** Mantenir visible el text complet: git bisect bad. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git bisect bad.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect bad
```

**Subratllat:** `bad`.

**Locució:** Indica que la prova falla en el commit actual, que és H.

**Visual:** Mantenir visible el text complet: git bisect bad. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: bad.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect bad
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git bisect bad. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect bad
```

**Locució:** H es converteix en el límit que falla.

**Visual:** Ressaltar H amb etiqueta FALLA, a més del color. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git bisect good v1.0

**Terminal · comanda completa visible:**

```text
git bisect good v1.0
```

**Subratllat:** `git bisect good`.

**Locució:** Indiquem la versió que ja hem provat com a correcta.

**Visual:** Mantenir visible el text complet: git bisect good v1.0. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git bisect good.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect good v1.0
```

**Subratllat:** `good`.

**Locució:** Indica que aquesta versió supera la mateixa prova.

**Visual:** Mantenir visible el text complet: git bisect good v1.0. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: good.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect good v1.0
```

**Subratllat:** `v1.0`.

**Locució:** L’etiqueta assenyala A, l’extrem conegut que funciona.

**Visual:** Mantenir visible el text complet: git bisect good v1.0. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: v1.0.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect good v1.0
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git bisect good v1.0. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect good v1.0
```

**Locució:** En aquest historial Git selecciona D per provar-lo. Main continua a H; canvia temporalment la versió de treball.

**Visual:** HEAD separat a D, main quieta a H. No presentar sempre D com la selecció de qualsevol projecte. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `python3`.

**Locució:** Executem exactament la mateixa prova a D.

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

**Locució:** La prova falla amb l’error de nom. Comuniquem aquest resultat a la cerca.

**Visual:** Terminal amb error i interval A–D ressaltat. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git bisect bad

**Terminal · comanda completa visible:**

```text
git bisect bad
```

**Subratllat:** `git bisect bad`.

**Locució:** Marquem D com a versió que falla.

**Visual:** Mantenir visible el text complet: git bisect bad. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git bisect bad.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect bad
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git bisect bad. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect bad
```

**Locució:** Git redueix el tram i, en aquest exemple, selecciona C.

**Visual:** HEAD separat passa a C; main continua a H. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `python3`.

**Locució:** Provem C de la mateixa manera.

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

**Locució:** La salutació funciona. Ara classifiquem aquesta versió com a correcta.

**Visual:** Sortida Hello Git!, sense canviar la prova. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git bisect good

**Terminal · comanda completa visible:**

```text
git bisect good
```

**Subratllat:** `git bisect good`.

**Locució:** Marquem el resultat correcte de C.

**Visual:** Mantenir visible el text complet: git bisect good. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git bisect good.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect good
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git bisect good. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect good
```

**Locució:** C i D són consecutius: D és el primer que falla dins del tram investigat. Això localitza un canvi per revisar; encara no l’hem corregit.

**Visual:** Ressaltar D com a RESULTAT. Conservar HEAD a C, que és l’últim commit provat en aquesta seqüència. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git show d04f7a2 -- helloGit.py

**Terminal · comanda completa visible:**

```text
git show d04f7a2 -- helloGit.py
```

**Subratllat:** `git show`.

**Locució:** Revisem el canvi identificat.

**Visual:** Mantenir visible el text complet: git show d04f7a2 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git show.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show d04f7a2 -- helloGit.py
```

**Subratllat:** `d04f7a2`.

**Locució:** Substituïm el hash de mostra pel que ha trobat la nostra cerca.

**Visual:** Mantenir visible el text complet: git show d04f7a2 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: d04f7a2.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show d04f7a2 -- helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git show d04f7a2 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show d04f7a2 -- helloGit.py
```

**Locució:** El diff mostra la variable sense definir introduïda a D. La consulta no modifica la versió seleccionada.

**Visual:** Diff de D al costat del resultat de la prova. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git bisect reset

**Terminal · comanda completa visible:**

```text
git bisect reset
```

**Subratllat:** `git bisect reset`.

**Locució:** Tanquem la cerca i recuperem el punt de partida.

**Visual:** Mantenir visible el text complet: git bisect reset. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git bisect reset.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect reset
```

**Subratllat:** `reset`.

**Locució:** En aquesta subordre de bisect, reset finalitza la sessió i torna al punt inicial; no és git reset.

**Visual:** Mantenir visible el text complet: git bisect reset. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: reset.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect reset
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git bisect reset. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git bisect reset
```

**Locució:** Tornem a main H. No s’ha creat cap commit ni s’ha arreglat encara el programa.

**Visual:** Retirar CERCA ACTIVA i tornar HEAD a main H. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Cal una prova repetible i dos extrems coneguts.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Provem cada versió abans de classificar-la.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Bisect localitza la regressió; reset tanca la cerca i després queda corregir-la.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En un historial de pràctiques amb una fallada persistent, identifica un extrem correcte i un de fallit. Mantén la mateixa prova i acaba la sessió amb bisect reset.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
