# Lliçó 15 · Cherry-pick: porta una correcció a una altra branca

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Quinzena lliçó, Cherry pick.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a reaplicar una correcció independent a una altra branca sense integrar la feina anterior.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Main a B amb un error. Salutacio té C, que afegeix notes d’una funcionalitat pendent, i D, que corregeix només el programa. Treball net; el canvi de D no depèn de C.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Una correcció útil dins d’una altra feina

**Locució:** La branca de prova conté una funcionalitat pendent i una correcció que necessitem a main. Portarem només el canvi de la correcció, després de comprovar que sigui independent.

**Visual:** Graf main a B; salutacio a D amb C entremig. C: notes.md; D: correcció de helloGit.py.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git log --oneline salutacio

**Terminal · comanda completa visible:**

```text
git log --oneline salutacio
```

**Subratllat:** `git log`.

**Locució:** Identifiquem el commit de la correcció.

**Visual:** Mantenir visible el text complet: git log --oneline salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git log.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline salutacio
```

**Subratllat:** `--oneline`.

**Locució:** Mostra el resum de cada commit.

**Visual:** Mantenir visible el text complet: git log --oneline salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --oneline.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline salutacio
```

**Subratllat:** `salutacio`.

**Locució:** Consultem la història d’aquesta branca, sense canviar-hi.

**Visual:** Mantenir visible el text complet: git log --oneline salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: salutacio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline salutacio
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git log --oneline salutacio. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline salutacio
```

**Locució:** Copiem l’identificador de D. El hash d04f7a2 és una mostra; en un projecte propi copiem el real.

**Visual:** Ressaltar D i deixar C visible com FEINA PENDENT. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git show d04f7a2 -- helloGit.py

**Terminal · comanda completa visible:**

```text
git show d04f7a2 -- helloGit.py
```

**Subratllat:** `git show`.

**Locució:** Revisem què modifica D.

**Visual:** Mantenir visible el text complet: git show d04f7a2 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git show.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show d04f7a2 -- helloGit.py
```

**Subratllat:** `d04f7a2`.

**Locució:** És el commit seleccionat.

**Visual:** Mantenir visible el text complet: git show d04f7a2 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: d04f7a2.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show d04f7a2 -- helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** La consulta es limita al fitxer del programa, després del separador de camins.

**Visual:** Mantenir visible el text complet: git show d04f7a2 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: helloGit.py.

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

**Locució:** La correcció no necessita les notes de C. Aquest exemple permet aplicar-la independentment.

**Visual:** Diff de D amb només la correcció; panell notes.md exclòs. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** No hi ha feina local pendent que es barregi amb l’operació.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

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

**Locució:** La correcció s’aplicarà a main, que és la branca activa.

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git cherry-pick d04f7a2

**Terminal · comanda completa visible:**

```text
git cherry-pick d04f7a2
```

**Subratllat:** `git cherry-pick`.

**Locució:** git cherry-pick reaplica el canvi del commit indicat a la branca activa.

**Visual:** Mantenir visible el text complet: git cherry-pick d04f7a2. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git cherry-pick.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git cherry-pick d04f7a2
```

**Subratllat:** `d04f7a2`.

**Locució:** Indiquem D, no el seu pare C ni tota la branca de salutació.

**Visual:** Mantenir visible el text complet: git cherry-pick d04f7a2. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: d04f7a2.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git cherry-pick d04f7a2
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git cherry-pick d04f7a2. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git cherry-pick d04f7a2
```

**Locució:** Es crea E a main amb pare B. El seu identificador és nou; D continua a la branca original amb pare C.

**Visual:** Conservar C i D. Crear E com a fill de B i dibuixar una relació conceptual de canvi D → E, diferent d’una relació de pare. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

**Terminal · comanda completa visible:**

```text
python3 helloGit.py
```

**Subratllat:** `python3`.

**Locució:** Comprovem la correcció aplicada.

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

**Locució:** El programa funciona a main i les notes de C no hi han entrat. Aplicar un canvi concret no substitueix la prova del resultat.

**Visual:** Sortida vàlida i llista de fitxers sense notes.md a main. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Camí condicional: resoldre o abandonar

**Locució:** Si l’aplicació s’atura per un conflicte, revisem el fitxer, escrivim el resultat correcte, el provem i el preparem. Després podem continuar l’operació pendent.

**Visual:** Panell condicional amb passos editor → prova → git add helloGit.py, separats i amb espera.

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

## git cherry-pick --continue

**Camí:** `conditional:conflict`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git cherry-pick --continue
```

**Subratllat:** `git cherry-pick`.

**Locució:** Reprenem una aplicació pausada després de preparar la resolució.

**Visual:** Mantenir visible el text complet: git cherry-pick --continue. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git cherry-pick.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git cherry-pick --continue
```

**Subratllat:** `--continue`.

**Locució:** Continua el cherry-pick pendent; no inicia una segona selecció de commits.

**Visual:** Mantenir visible el text complet: git cherry-pick --continue. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --continue.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git cherry-pick --continue
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git cherry-pick --continue. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git cherry-pick --continue
```

**Locució:** La correcció queda confirmada amb la resolució revisada.

**Visual:** Només camí CONTINUAR del cas conflictiu. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git cherry-pick --abort

**Camí:** `alternative:abort`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git cherry-pick --abort
```

**Subratllat:** `git cherry-pick`.

**Locució:** En lloc de continuar, podem abandonar l’operació pendent.

**Visual:** Mantenir visible el text complet: git cherry-pick --abort. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git cherry-pick.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git cherry-pick --abort
```

**Subratllat:** `--abort`.

**Locució:** Recupera el punt de partida d’aquest cherry-pick.

**Visual:** Mantenir visible el text complet: git cherry-pick --abort. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --abort.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git cherry-pick --abort
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git cherry-pick --abort. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git cherry-pick --abort
```

**Locució:** No s’aplica la correcció en aquest camí alternatiu.

**Visual:** Bifurcació AVORTAR des del conflicte, sense executar-la després de continue. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Seleccionem un canvi concret i en revisem les dependències.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** La branca activa rep un commit nou amb un pare diferent.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** La branca original es conserva i cal provar el resultat reaplicat.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En un repositori de pràctiques, prepara una correcció independent d’un altre canvi. Reaplica només la correcció a main i comprova els fitxers de les dues branques.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
