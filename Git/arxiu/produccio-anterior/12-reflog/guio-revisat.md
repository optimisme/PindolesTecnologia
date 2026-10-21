# Lliçó 12 · Reflog: recupera un commit local

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Dotzena lliçó, Reflog.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a trobar un commit al reflog i donar-li una branca sense perdre canvis preparats.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Continuació de reset soft: main i HEAD a B, mentre treball i preparació conserven el contingut de C. Les entrades locals encara existeixen. recuperació serà una branca nova.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Un commit fora de la línia actual

**Locució:** C ja no surt al recorregut de main després del reset. Això no vol dir que el seu objecte s’hagi esborrat immediatament. Buscarem una referència local anterior.

**Visual:** Graf A–B amb main a B; C atenuat. Treball i preparació amb el contingut de C.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git log --oneline

**Terminal · comanda completa visible:**

```text
git log --oneline
```

**Subratllat:** `git log`.

**Locució:** Consultem la història accessible des de la branca activa.

**Visual:** Mantenir visible el text complet: git log --oneline. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git log.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline
```

**Subratllat:** `--oneline`.

**Locució:** Cada commit es resumeix en una línia.

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

**Locució:** Només veiem B i A en aquesta línia. Aquesta consulta no busca tots els moviments locals anteriors.

**Visual:** Ressaltar el camí recorregut des de main; deixar C fora d’aquest recorregut. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git reflog

**Terminal · comanda completa visible:**

```text
git reflog
```

**Subratllat:** `git reflog`.

**Locució:** git reflog mostra moviments locals de la referència consultada; aquí, HEAD.

**Visual:** Mantenir visible el text complet: git reflog. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git reflog.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git reflog
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git reflog. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git reflog
```

**Locució:** Hi veiem el reset a B i l’entrada anterior de C. Copiem l’identificador de C, no el del reset.

**Visual:** Ressaltar primer la fila reset i després la fila del commit anterior; hash de mostra c95f4a7. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git show c95f4a7 -- helloGit.py

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Subratllat:** `git show`.

**Locució:** Revisem el commit trobat abans de recuperar-lo.

**Visual:** Mantenir visible el text complet: git show c95f4a7 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git show.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Subratllat:** `c95f4a7`.

**Locució:** Substituïm el hash de mostra pel que hem copiat del nostre reflog.

**Visual:** Mantenir visible el text complet: git show c95f4a7 -- helloGit.py. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: c95f4a7.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show c95f4a7 -- helloGit.py
```

**Subratllat:** `helloGit.py`.

**Locució:** Consultem el canvi del programa en aquell commit.

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

**Locució:** La diferència correspon a la salutació personalitzada que buscàvem. La consulta no modifica els fitxers.

**Visual:** Diff de C i editor actual visibles alhora. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git branch recuperacio c95f4a7

**Terminal · comanda completa visible:**

```text
git branch recuperacio c95f4a7
```

**Subratllat:** `git branch`.

**Locució:** Creem una branca que torni a donar accés a C.

**Visual:** Mantenir visible el text complet: git branch recuperacio c95f4a7. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git branch.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git branch recuperacio c95f4a7
```

**Subratllat:** `recuperacio`.

**Locució:** És el nom de la branca nova: recuperació.

**Visual:** Mantenir visible el text complet: git branch recuperacio c95f4a7. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: recuperacio.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git branch recuperacio c95f4a7
```

**Subratllat:** `c95f4a7`.

**Locució:** Indica el commit on situem la nova etiqueta.

**Visual:** Mantenir visible el text complet: git branch recuperacio c95f4a7. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: c95f4a7.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git branch recuperacio c95f4a7
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git branch recuperacio c95f4a7. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git branch recuperacio c95f4a7
```

**Locució:** Recuperació apunta a C. Main continua a B i segueix sent la branca activa; no hem canviat de branca.

**Visual:** Afegir només l’etiqueta recuperacio a C. Conservar HEAD unit a main. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git log --oneline --decorate --all

**Terminal · comanda completa visible:**

```text
git log --oneline --decorate --all
```

**Subratllat:** `git log`.

**Locució:** Comprovem les referències de les dues branques.

**Visual:** Mantenir visible el text complet: git log --oneline --decorate --all. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git log.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline --decorate --all
```

**Subratllat:** `--decorate`.

**Locució:** Mostra els noms de les referències al costat dels commits.

**Visual:** Mantenir visible el text complet: git log --oneline --decorate --all. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --decorate.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline --decorate --all
```

**Subratllat:** `--all`.

**Locució:** Inclou les branques que no són l’activa.

**Visual:** Mantenir visible el text complet: git log --oneline --decorate --all. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --all.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline --decorate --all
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git log --oneline --decorate --all. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log --oneline --decorate --all
```

**Locució:** C torna a ser visible a través de recuperació. Els canvis preparats i els fitxers continuen com abans.

**Visual:** Main a B, recuperacio a C i preparació intacta. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** El canvi que havia deixat reset soft continua preparat. Crear la branca no l’ha descartat.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Una ajuda local amb límits

**Locució:** El reflog és local i les entrades poden caducar. Ajuda a recuperar referències a commits disponibles; no desa qualsevol edició que no hàgim confirmat.

**Visual:** Icona LOCAL, rellotge i distinció COMMIT EXISTENT / EDICIÓ SENSE CONFIRMAR.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Log recorre l’historial accessible des d’una referència.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Reflog permet investigar moviments locals anteriors.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Crear una branca al commit trobat no canvia automàticament el treball ni la branca activa.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Després d’un reset soft de pràctiques, localitza el commit al reflog, revisa’l i crea una branca de recuperació sense canviar-hi amb feina pendent.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
