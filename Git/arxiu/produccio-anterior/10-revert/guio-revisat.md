# Lliçó 10 · Revert: desfés un commit publicat

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Desena lliçó, Revert.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a desfer l’efecte d’un commit publicat amb un nou commit invers.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Main i origin/main són a C, un commit ordinari ja publicat que introdueix una variable sense definir. Treball net. c95f4a7 és un hash il·lustratiu.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Una correcció que també queda registrada

**Locució:** El canvi que falla ja està publicat i altres persones el poden tenir. En aquest exemple crearem un commit nou que en desfà l’efecte, mantenint la seqüència de l’historial.

**Visual:** Graf A–B–C al local i remot. C queda visible durant tota la demostració.

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

**Locució:** Comencem sense edicions locals pendents. Així la correcció no barreja altres feines.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git log --oneline

**Terminal · comanda completa visible:**

```text
git log --oneline
```

**Subratllat:** `git log`.

**Locució:** Busquem el canvi a l’historial.

**Visual:** Mantenir visible el text complet: git log --oneline. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git log.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline
```

**Subratllat:** `--oneline`.

**Locució:** Mostra cada commit en una línia, amb identificador i missatge.

**Visual:** Mantenir visible el text complet: git log --oneline. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --oneline.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git log --oneline. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline
```

**Locució:** Localitzem C i copiem el seu identificador real. El hash escrit a la pantalla és només un exemple.

**Visual:** Ressaltar c95f4a7 amb una etiqueta HASH DE MOSTRA · COPIA EL TEU. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git show c95f4a7 -- helloGit.py

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Subratllat:** `git show`.

**Locució:** Amb git show revisem el canvi abans de desfer-lo.

**Visual:** Mantenir visible el text complet: git show c95f4a7 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git show.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Subratllat:** `c95f4a7`.

**Locució:** És el commit que hem identificat.

**Visual:** Mantenir visible el text complet: git show c95f4a7 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: c95f4a7.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Subratllat:** `--`.

**Locució:** El separador indica que tot seguit especifiquem un camí de fitxer.

**Visual:** Mantenir visible el text complet: git show c95f4a7 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** La consulta es limita al programa que estem investigant.

**Visual:** Mantenir visible el text complet: git show c95f4a7 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

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

**Locució:** El canvi substituïa la salutació vàlida per una variable sense definir. Ja sabem quin efecte volem invertir.

**Visual:** Mostrar el diff amb l’abans i el després del mateix fitxer. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git revert --no-edit c95f4a7

**Terminal · comanda completa visible:**

```text
git revert --no-edit c95f4a7
```

**Subratllat:** `git revert`.

**Locució:** git revert aplica el canvi invers del commit indicat.

**Visual:** Mantenir visible el text complet: git revert --no-edit c95f4a7. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git revert.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git revert --no-edit c95f4a7
```

**Subratllat:** `--no-edit`.

**Locució:** Accepta el missatge automàtic de la reversió, sense obrir l’editor.

**Visual:** Mantenir visible el text complet: git revert --no-edit c95f4a7. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --no-edit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git revert --no-edit c95f4a7
```

**Subratllat:** `c95f4a7`.

**Locució:** Indica el commit ordinari que volem revertir en aquest exemple.

**Visual:** Mantenir visible el text complet: git revert --no-edit c95f4a7. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: c95f4a7.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git revert --no-edit c95f4a7
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git revert --no-edit c95f4a7. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git revert --no-edit c95f4a7
```

**Locució:** Es crea D després de C. Main avança; C es conserva i D en desfà l’efecte.

**Visual:** Afegir D amb C com a pare. No moure main enrere ni esborrar C. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `python3`.

**Locució:** Provem la versió resultant.

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

**Locució:** La salutació torna a funcionar. La prova valida aquest comportament concret, no qualsevol altra part del projecte.

**Visual:** Sortida Hello Git! i contingut restaurat al programa. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** El remot incorpora D amb un enviament normal. Les altres còpies podran descarregar la correcció sense perdre l’historial compartit.

**Visual:** Conservar el mateix identificador a local i remot. La fletxa envia commits; no envia edicions sense confirmar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## L’abast és el canvi indicat

**Locució:** Revert no significa tornar qualsevol projecte sencer a una data. En aquest cas desfà l’últim canvi problemàtic. Amb commits posteriors compatibles, aquests es poden conservar.

**Visual:** Panell independent amb C, un canvi posterior només a notes.md i un commit invers de C; les notes es mantenen. No executar el cas alternatiu al projecte principal.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Revert crea un commit invers nou.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** L’original continua visible i la branca avança.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Després de provar la correcció, la publiquem com un commit més.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Reverteix un commit ordinari en un repositori teu de pràctiques. Compara el graf abans i després i comprova que el commit original encara hi és.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
