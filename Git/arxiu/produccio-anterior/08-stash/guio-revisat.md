# Lliçó 8 · Stash: aparca la feina pendent

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Vuitena lliçó, Stash.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a aparcar canvis pendents, canviar temporalment de tasca i recuperar-los.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Som a salutació, al mateix commit que main. helloGit.py té una edició sense preparar i notes.md és nou. No hi ha canvis preparats ni fitxers ignorats que vulguem guardar.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## La feina pendent té dues formes

**Locució:** Hem modificat el programa i creat unes notes. Encara no volem confirmar aquesta feina. L’aparcarem temporalment per poder canviar de tasca.

**Visual:** Dues targetes: helloGit.py MODIFICAT; notes.md NOU. Main i salutacio continuen a B.

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

**Locució:** La modificació del programa apareix sense preparar i les notes apareixen com a fitxer nou. Cap dels dos canvis és a l’historial.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git stash push -u -m "Salutacio pendent"

**Terminal · comanda completa visible:**

```text
git stash push -u -m "Salutacio pendent"
```

**Subratllat:** `git stash push`.

**Locució:** git stash push desa una entrada temporal amb la feina pendent.

**Visual:** Mantenir visible el text complet: git stash push -u -m "Salutacio pendent". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git stash push.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash push -u -m "Salutacio pendent"
```

**Subratllat:** `-u`.

**Locució:** El guionet u inclou també els fitxers nous no seguits. Els fitxers ignorats queden fora.

**Visual:** Mantenir visible el text complet: git stash push -u -m "Salutacio pendent". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -u.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash push -u -m "Salutacio pendent"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema introdueix un missatge per identificar aquesta entrada.

**Visual:** Mantenir visible el text complet: git stash push -u -m "Salutacio pendent". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash push -u -m "Salutacio pendent"
```

**Subratllat:** `"Salutacio pendent"`.

**Locució:** El text descriu la tasca aparcada: salutació pendent.

**Visual:** Mantenir visible el text complet: git stash push -u -m "Salutacio pendent". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Salutacio pendent".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash push -u -m "Salutacio pendent"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git stash push -u -m "Salutacio pendent". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash push -u -m "Salutacio pendent"
```

**Locució:** El programa recupera el contingut confirmat i les notes noves desapareixen del treball. Els canvis són a l’entrada temporal; la branca no avança.

**Visual:** Els dos continguts viatgen a una caixa STASH. Conservar main i salutacio a B. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git stash list

**Terminal · comanda completa visible:**

```text
git stash list
```

**Subratllat:** `git stash list`.

**Locució:** Consultem les entrades amb git stash list.

**Visual:** Mantenir visible el text complet: git stash list. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git stash list.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash list
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git stash list. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash list
```

**Locució:** La primera entrada apareix amb un identificador i el missatge que acabem d’escriure. És la feina aparcada, no un commit nou de la branca.

**Visual:** Ressaltar stash@{0} i Salutacio pendent com a dues parts de la mateixa entrada. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** Ara podem atendre l’altra tasca amb el treball net. En aquesta demostració ometem aquella correcció i tornem directament a la nostra feina.

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

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

**Locució:** Tornem a la branca de la funcionalitat abans de recuperar-hi els canvis.

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució. Mostrar el resultat concret i conservar l’estat anterior per comparar.

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

**Locució:** El treball continua net. Recuperarem l’entrada sobre aquest estat.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git stash pop

**Terminal · comanda completa visible:**

```text
git stash pop
```

**Subratllat:** `git stash pop`.

**Locució:** git stash pop intenta recuperar els canvis i retirar l’entrada si s’apliquen bé.

**Visual:** Mantenir visible el text complet: git stash pop. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git stash pop.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash pop
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git stash pop. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash pop
```

**Locució:** Reapareixen la salutació modificada i les notes noves. Tornen a ser feina pendent, sense confirmar.

**Visual:** Obrir la caixa STASH i retornar cada contingut al seu fitxer. No crear cap node a la branca. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git stash list

**Terminal · comanda completa visible:**

```text
git stash list
```

**Subratllat:** `git stash list`.

**Locució:** Comprovem la llista després de recuperar l’entrada.

**Visual:** Mantenir visible el text complet: git stash list. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git stash list.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash list
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git stash list. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git stash list
```

**Locució:** En aquest cas queda buida perquè l’aplicació ha estat correcta. Si hi hagués conflictes, l’entrada no s’eliminaria automàticament.

**Visual:** Mostrar llista buida amb la llegenda textual CAP ENTRADA; panell condicional separat per al conflicte. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Conservar l’entrada és una altra opció

**Locució:** Amb git stash apply podem recuperar els canvis conservant l’entrada. És una alternativa a pop; no cal executar les dues ordres per recuperar la mateixa feina.

**Visual:** Comparació APPLY: conserva / POP: retira si s’aplica bé. No obrir una segona sessió d’operacions.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Stash aparca feina pendent sense avançar la branca.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** L’opció u inclou els fitxers nous no seguits, sense incloure els ignorats.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Recuperar els canvis els retorna al treball; encara caldrà confirmar-los.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Aparca una edició i un fitxer nou en un repositori de pràctiques. Consulta l’entrada, torna a la branca adequada i recupera-la amb el treball net.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
