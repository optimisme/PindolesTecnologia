# Lliçó 11 · Reset: torna enrere un commit local

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Onzena lliçó, Reset.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a comparar reset soft i mixed sense confondre què passa amb treball i preparació.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Main a C, commit propi no publicat, amb treball i preparació nets. B té la salutació original i C la personalitzada. Les dues opcions parteixen independentment de C.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Reprendre un canvi local

**Locució:** Volem continuar treballant en el contingut de l’últim commit propi, encara no publicat. Compararem dos tipus de reset que conserven el fitxer de treball.

**Visual:** Graf A–B–C; main i HEAD a C. Panells treball, preparació i historial amb V2.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Llegim el punt de destinació

**Locució:** HEAD segueix main en aquest exemple. El sufix titlla u indica un pas enrere pel primer pare. Per tant, la destinació és B.

**Visual:** Subratllar HEAD i després ~1 a HEAD~1; assenyalar C i B amb una fletxa conceptual, sense executar encara.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git reset --soft HEAD~1

**Camí:** `alternative:soft`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git reset --soft HEAD~1
```

**Subratllat:** `git reset`.

**Locució:** Comencem per l’alternativa soft.

**Visual:** Mantenir visible el text complet: git reset --soft HEAD~1. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git reset.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git reset --soft HEAD~1
```

**Subratllat:** `--soft`.

**Locució:** Mou la branca i conserva tant la preparació com el treball.

**Visual:** Mantenir visible el text complet: git reset --soft HEAD~1. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --soft.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git reset --soft HEAD~1
```

**Subratllat:** `HEAD~1`.

**Locució:** La destinació és el commit anterior al punt actual.

**Visual:** Mantenir visible el text complet: git reset --soft HEAD~1. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: HEAD~1.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git reset --soft HEAD~1
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git reset --soft HEAD~1. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git reset --soft HEAD~1
```

**Locució:** Main passa a B. El treball i la preparació continuen amb V2; el canvi queda preparat respecte de B.

**Visual:** Moure només main i HEAD. Conservar C atenuat fora de la línia actual, sense esborrar-ne l’objecte. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git diff --staged

**Camí:** `alternative:soft`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git diff --staged
```

**Subratllat:** `git diff`.

**Locució:** Comprovem el canvi que ha quedat preparat.

**Visual:** Mantenir visible el text complet: git diff --staged. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git diff.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff --staged
```

**Subratllat:** `--staged`.

**Locució:** Compara la preparació conservada amb el nou últim commit, que és B.

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

**Locució:** La salutació personalitzada apareix com a canvi preparat. Podem editar-la, tornar a preparar-la i confirmar una versió nova.

**Visual:** Fletxa HISTORIAL V1 → PREPARACIÓ V2. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Reiniciem la comparació a C

**Locució:** Ara tornem visualment al punt inicial: main a C, treball net i preparació V2. L’opció següent és una alternativa; no s’executa després de soft.

**Visual:** Separador TORNEM AL PUNT DE PARTIDA. Restaurar el dibuix inicial complet.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git reset --mixed HEAD~1

**Camí:** `alternative:mixed`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git reset --mixed HEAD~1
```

**Subratllat:** `git reset`.

**Locució:** Comparem l’alternativa mixed.

**Visual:** Mantenir visible el text complet: git reset --mixed HEAD~1. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git reset.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git reset --mixed HEAD~1
```

**Subratllat:** `--mixed`.

**Locució:** Mou la branca i restaura la preparació a la destinació. Conserva el treball.

**Visual:** Mantenir visible el text complet: git reset --mixed HEAD~1. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --mixed.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git reset --mixed HEAD~1
```

**Subratllat:** `HEAD~1`.

**Locució:** Des del punt inicial C, un pas enrere ens torna a B.

**Visual:** Mantenir visible el text complet: git reset --mixed HEAD~1. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: HEAD~1.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git reset --mixed HEAD~1
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git reset --mixed HEAD~1. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git reset --mixed HEAD~1
```

**Locució:** Main i preparació passen a B, però el treball manté V2. La salutació nova queda sense preparar.

**Visual:** Moure main i HEAD a B; copiar V1 a preparació; deixar V2 al treball. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## La diferència és a la preparació

**Locució:** En tots dos casos la branca torna a B i el fitxer conserva V2. Soft deixa el canvi preparat; mixed el deixa pendent de preparar. C pot continuar com a objecte accessible localment.

**Visual:** Taula de dues files amb B / V2 / V2 per soft i B / V1 / V2 per mixed; etiquetes textuals, a més de colors.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** En aquest exemple reset mou la branca local a B.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Soft conserva la preparació; mixed la restaura a B.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Tots dos conserven el treball; les alternatives es comparen des del mateix inici.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** Reprodueix cada alternativa en un repositori de pràctiques separat, amb un últim commit no publicat. Compara treball, índex i historial abans de continuar.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
