# Lliçó 9 · Restore: desmarca o descarta un canvi local

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Novena lliçó, Restore.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a desfer la selecció d’un canvi o descartar una edició, identificant origen i destinació.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** El programa ja és seguit. Últim commit V1; treball i preparació V2 després d’una edició i add. No hi ha altres canvis.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Dues destinacions diferents

**Locució:** Podem canviar la preparació o el treball. Abans d’executar restore, identificarem quina zona volem restaurar i de quina versió copiem el contingut.

**Visual:** Tres panells V2 al treball i índex; V1 a l’últim commit.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git restore --staged helloGit.py

**Terminal · comanda completa visible:**

```text
git restore --staged helloGit.py
```

**Subratllat:** `git restore`.

**Locució:** Primer desfem la selecció del canvi, conservant l’edició del fitxer.

**Visual:** Mantenir visible el text complet: git restore --staged helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git restore.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git restore --staged helloGit.py
```

**Subratllat:** `--staged`.

**Locució:** Aquesta opció tria la preparació com a destinació. Per defecte, copia el contingut de l’últim commit.

**Visual:** Mantenir visible el text complet: git restore --staged helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --staged.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git restore --staged helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** Limitem la restauració a aquest fitxer; no desmarquem la resta del projecte.

**Visual:** Mantenir visible el text complet: git restore --staged helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git restore --staged helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git restore --staged helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git restore --staged helloGit.py
```

**Locució:** La preparació torna a V1 i el treball conserva V2. El fitxer continua seguit; només hem desfet la selecció dels seus canvis.

**Visual:** Fletxa ÚLTIM COMMIT V1 → PREPARACIÓ. Cap fletxa cap al treball. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** La modificació ara apareix a la columna de treball, sense preparar. El contingut editat es conserva.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git diff

**Terminal · comanda completa visible:**

```text
git diff
```

**Subratllat:** `git diff`.

**Locució:** Llegim el canvi que continua al fitxer.

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

**Locució:** La salutació nova encara és al treball. Després de revisar-la, decidim que aquest canvi concret no el volem conservar.

**Visual:** Comparació V1 de la preparació amb V2 del treball. Mostrar la decisió DESCARTAR AQUESTA EDICIÓ abans de l’ordre següent. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git restore helloGit.py

**Terminal · comanda completa visible:**

```text
git restore helloGit.py
```

**Subratllat:** `git restore`.

**Locució:** Ara restaurem el fitxer de treball.

**Visual:** Mantenir visible el text complet: git restore helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git restore.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git restore helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** Sense staged, la destinació és el treball i l’origen per defecte és la preparació.

**Visual:** Mantenir visible el text complet: git restore helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git restore helloGit.py
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git restore helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git restore helloGit.py
```

**Locució:** El treball torna a V1, perquè la preparació ja era V1. L’edició sense confirmar s’ha descartat.

**Visual:** Fletxa PREPARACIÓ V1 → TREBALL. Retirar V2 del panell de treball sense insinuar que s’ha guardat en un commit. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git status --short. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git status --short
```

**Locució:** Les tres zones coincideixen i no hi ha canvis pendents. L’historial no ha canviat.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Un altre cas: la preparació conté V2

**Locució:** En un cas independent, imaginem V1 a l’historial, V2 preparat i V3 al treball. Restaurar el treball des de la preparació recupera V2, no V1.

**Visual:** Separador CAS INDEPENDENT. Mostrar V1 / V2 / V3 i fletxa PREPARACIÓ V2 → TREBALL V2. No encadenar aquest exemple a l’anterior.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Amb staged, restaurem la preparació i conservem l’edició del treball.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Sense staged, restaurem el treball des de la preparació per defecte.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Abans de descartar una edició, en revisem el contingut i la destinació.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En un fitxer de pràctiques, prepara una edició i desmarca-la conservant el treball. Revisa-la amb diff abans de decidir si la vols preparar de nou o descartar.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
