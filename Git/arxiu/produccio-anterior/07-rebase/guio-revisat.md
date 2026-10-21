# Lliçó 7 · Rebase: continua sobre una base nova

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Setena lliçó, Rebase.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a reaplicar commits propis sobre una base nova i reconèixer que els identificadors canvien.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Salutacio té C i E sobre B, encara sense publicar. Main ha avançat a D en un altre fitxer. Treball i preparació nets; els canvis principals són compatibles.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Una base que ha avançat

**Locució:** Volem continuar la nostra funcionalitat sobre les novetats de main. La branca de salutació té dos commits propis que encara no hem compartit.

**Visual:** B com a base; main a D, salutacio a E passant per C. Etiqueta NO PUBLICATS a C i E.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git switch salutacio

**Terminal · comanda completa visible:**

```text
git switch salutacio
```

**Subratllat:** `git switch`.

**Locució:** Amb git switch seleccionem la branca on treballarem.

**Visual:** Mantenir visible el text complet: git switch salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git switch.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git switch salutacio
```

**Subratllat:** `salutacio`.

**Locució:** Aquest és el nom de la branca de destinació. Els fitxers s’actualitzaran a la versió seleccionada.

**Visual:** Mantenir visible el text complet: git switch salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: salutacio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git switch salutacio
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git switch salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git switch salutacio
```

**Locució:** La branca que reescriurem és salutació. main serà la base i es mantindrà al seu lloc.

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git rebase main

**Terminal · comanda completa visible:**

```text
git rebase main
```

**Subratllat:** `git rebase`.

**Locució:** git rebase reaplica els canvis de la branca activa sobre una altra base.

**Visual:** Mantenir visible el text complet: git rebase main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git rebase.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase main
```

**Subratllat:** `main`.

**Locució:** Aquest nom indica la base actualitzada. No és la branca a la qual estem incorporant la funcionalitat.

**Visual:** Mantenir visible el text complet: git rebase main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: main.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase main
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git rebase main. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase main
```

**Locució:** Els canvis de C i E es recreen com C prima i E prima després de D. Tenen pares i identificadors nous.

**Visual:** Atenuar C i E; dibuixar C′ i E′ a partir de D. No moure els nodes originals com si fossin els mateixos. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Seguim un canvi concret

**Locució:** La salutació que introduïa C també existeix a C prima, ara aplicada sobre D. El contingut pot conservar-se, però l’historial és diferent perquè ha canviat el pare.

**Visual:** Comparar el mateix canvi de text a C i C′, i després ressaltar els pares B i D.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git log --oneline --graph --all

**Terminal · comanda completa visible:**

```text
git log --oneline --graph --all
```

**Subratllat:** `git log`.

**Locució:** Revisem l’historial després de l’operació.

**Visual:** Mantenir visible el text complet: git log --oneline --graph --all. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git log.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline --graph --all
```

**Subratllat:** `--oneline`.

**Locució:** Mostra un resum de cada commit en una línia.

**Visual:** Mantenir visible el text complet: git log --oneline --graph --all. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --oneline.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline --graph --all
```

**Subratllat:** `--graph`.

**Locució:** Dibuixa les connexions entre commits.

**Visual:** Mantenir visible el text complet: git log --oneline --graph --all. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --graph.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline --graph --all
```

**Subratllat:** `--all`.

**Locució:** Inclou les referències de totes les branques.

**Visual:** Mantenir visible el text complet: git log --oneline --graph --all. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --all.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline --graph --all
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git log --oneline --graph --all. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline --graph --all
```

**Locució:** main continua a D i salutació apunta al final de la línia nova. Encara no hem integrat la funcionalitat a main.

**Visual:** Graf estable, llegenda per a les branques i hashes nous. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Comparació amb merge

**Locució:** Des del mateix punt de partida, merge pot connectar els dos camins amb un commit de dos pares. Rebase reconstrueix els commits propis sobre la base nova.

**Visual:** Dos grafs laterals amb exactament el mateix estat inicial. No executar una operació després de l’altra.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Cas condicional: apareix un conflicte

**Locució:** En una altra situació el rebase es pot aturar. Editem el contingut correcte, el provem i preparem la resolució abans de continuar.

**Visual:** Separador SI HI HA CONFLICTE; indicador REBASE PAUSAT. El camí principal anterior no tenia conflictes.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

**Camí:** `conditional:conflict`. Respectar el punt de partida indicat; no encadenar alternatives.

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

**Locució:** La resolució funciona amb la prova d’aquest exemple.

**Visual:** Mostrar la sortida real del programa al costat de l’editor. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git add helloGit.py

**Camí:** `conditional:conflict`. Respectar el punt de partida indicat; no encadenar alternatives.

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

**Locució:** La resolució revisada queda preparada per continuar l’operació pendent.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git rebase --continue

**Camí:** `conditional:conflict`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git rebase --continue
```

**Subratllat:** `git rebase`.

**Locució:** Després de resoldre i preparar el fitxer, reprenem el rebase.

**Visual:** Mantenir visible el text complet: git rebase --continue. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git rebase.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase --continue
```

**Subratllat:** `--continue`.

**Locució:** Continua l’operació pendent. Pot caldre resoldre més d’un conflicte, repetint el mateix procés.

**Visual:** Mantenir visible el text complet: git rebase --continue. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --continue.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase --continue
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git rebase --continue. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase --continue
```

**Locució:** L’operació avança amb els canvis resolts.

**Visual:** Mostrar prèviament git add helloGit.py i la prova, en passos separats. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git rebase --abort

**Camí:** `alternative:abort`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git rebase --abort
```

**Subratllat:** `git rebase`.

**Locució:** Una altra opció és abandonar el rebase pendent.

**Visual:** Mantenir visible el text complet: git rebase --abort. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git rebase.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase --abort
```

**Subratllat:** `--abort`.

**Locució:** Cancel·la aquesta operació i recupera l’estat de partida del cas mostrat.

**Visual:** Mantenir visible el text complet: git rebase --abort. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --abort.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase --abort
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git rebase --abort. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase --abort
```

**Locució:** Tornem a la branca anterior al rebase. Avortar i continuar són alternatives.

**Visual:** Bifurcació CONTINUAR / AVORTAR, sense executar les dues opcions seguides. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Rebase canvia la base de la branca activa.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Els commits reaplicats tenen identificadors nous; main no es mou.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** En aquest exemple només reescrivim feina pròpia encara no publicada.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En una branca local de pràctiques amb canvis compatibles, reaplica la teva feina sobre main. Compara el graf i prova el contingut resultant.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
