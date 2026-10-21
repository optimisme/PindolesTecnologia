# Lliçó 6 · Conflictes: dues edicions, una decisió

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Sisena lliçó, Conflictes.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a llegir un conflicte de merge, decidir el resultat i confirmar la resolució.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Treball net a main. Main i salutació han canviat la mateixa línia des de B: Hola, classe! i Hola, Anna!, respectivament.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Dues propostes incompatibles

**Locució:** Les dues branques han modificat la mateixa línia de manera diferent. Git detecta que necessita una decisió sobre el contingut. Un conflicte pendent encara no és una fusió acabada.

**Visual:** Comparació de les dues línies amb els noms de branca visibles.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git merge salutacio

**Terminal · comanda completa visible:**

```text
git merge salutacio
```

**Subratllat:** `git merge`.

**Locució:** Intentem integrar salutació a la branca activa.

**Visual:** Mantenir visible el text complet: git merge salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git merge.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge salutacio
```

**Subratllat:** `salutacio`.

**Locució:** La proposta entrant és aquesta branca; la destinació continua sent main.

**Visual:** Mantenir visible el text complet: git merge salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: salutacio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge salutacio
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git merge salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge salutacio
```

**Locució:** La fusió s’atura. No s’ha creat el commit que uneix els dos historials.

**Visual:** Terminal amb conflicte i graf sense node M. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** Dues us majúscules indiquen un fitxer encara sense resoldre en aquesta fusió. Llegim també el seu contingut.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Llegim els marcadors per parts

**Locució:** El primer marcador obre la versió del costat actual. En aquest merge, HEAD correspon a main.

**Visual:** Mostrar <<<<<<< HEAD, print("Hola, classe!"), =======, print("Hola, Anna!"), >>>>>>> salutacio. Subratllar un marcador cada vegada.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** La línia central separa les dues propostes. El marcador final tanca la versió entrant, que és salutació. Aquests marcadors no són codi del programa.

**Visual:** Mostrar <<<<<<< HEAD, print("Hola, classe!"), =======, print("Hola, Anna!"), >>>>>>> salutacio. Subratllar un marcador cada vegada.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Escrivim el resultat acordat

**Locució:** Decidim escriure Hola, grup! Eliminem tots els marcadors i deixem una sola instrucció vàlida. La resolució pot combinar les idees; no cal conservar una proposta sencera.

**Visual:** Animar l’edició fins a print("Hola, grup!"). No preparar el fitxer abans de mostrar aquesta decisió.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `python3`.

**Locució:** Provem el contingut resolt abans de confirmar.

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

**Locució:** La salutació final s’executa correctament. Encara falta preparar-la i acabar la fusió.

**Visual:** Sortida Hola, grup!; el graf continua sense M. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** La resolució queda preparada. Això informa Git que hem resolt el fitxer; no valida per si mateix que el programa sigui correcte.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Resol conflicte"

**Terminal · comanda completa visible:**

```text
git commit -m "Resol conflicte"
```

**Subratllat:** `git commit`.

**Locució:** Amb git commit enregistrarem el contingut preparat en una versió local.

**Visual:** Mantenir visible el text complet: git commit -m "Resol conflicte". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Resol conflicte"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema indica que a continuació escrivim el missatge del canvi.

**Visual:** Mantenir visible el text complet: git commit -m "Resol conflicte". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Resol conflicte"
```

**Subratllat:** `"Resol conflicte"`.

**Locució:** El text entre cometes descriu la feina: Resol conflicte. Les cometes agrupen el missatge en un sol argument.

**Visual:** Mantenir visible el text complet: git commit -m "Resol conflicte". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Resol conflicte".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Resol conflicte"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit -m "Resol conflicte". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Resol conflicte"
```

**Locució:** Ara sí: es crea el commit de fusió amb dos pares i el contingut revisat.

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Alternativa des del conflicte pendent

**Locució:** En un cas alternatiu podem abandonar una fusió encara sense acabar. Tornem a mostrar el moment del conflicte, abans de preparar-lo o confirmar-lo.

**Visual:** Separador ALTERNATIVA. Recuperar l’estat conflictiu original, no el resultat ja confirmat.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git merge --abort

**Camí:** `alternative:abort`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git merge --abort
```

**Subratllat:** `git merge`.

**Locució:** Cancel·lem la fusió pendent.

**Visual:** Mantenir visible el text complet: git merge --abort. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git merge.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --abort
```

**Subratllat:** `--abort`.

**Locució:** Aquesta opció abandona l’operació en curs. En el nostre exemple s’havia començat amb el treball net.

**Visual:** Mantenir visible el text complet: git merge --abort. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --abort.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --abort
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git merge --abort. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git merge --abort
```

**Locució:** Recuperem l’estat anterior a intentar la fusió. Aquest camí no s’executa després de crear el commit de merge.

**Visual:** Retirar marcadors i indicador de fusió pendent sense crear cap node. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Un conflicte assenyala una decisió de contingut pendent.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Cal editar, provar i preparar la resolució.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** El commit acaba la fusió; avortar és un camí alternatiu anterior.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Reprodueix dues salutacions incompatibles en un repositori de pràctiques. Resol-les en una tercera salutació, prova el programa i completa la fusió.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
