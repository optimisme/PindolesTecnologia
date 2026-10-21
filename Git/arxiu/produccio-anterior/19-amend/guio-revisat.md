# Lliçó 19 · Amend: completa l’últim commit local

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Dinovena lliçó, Amend.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a completar l’últim commit propi amb un fitxer oblidat i entendre la substitució del commit.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Main a C, últim commit propi no publicat. notes.md és nou i havia de formar part de C. No hi ha altres canvis locals ni preparats.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Completar l’últim canvi abans de publicar

**Locució:** Hem confirmat la salutació però hem oblidat les notes. Amend crea un commit nou que substitueix l’últim a la branca, amb el contingut preparat que indiquem.

**Visual:** Graf A–B–C i notes.md NOU al treball. Etiqueta NO PUBLICAT a C.

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

**Locució:** Només les notes són pendents. Comprovem aquesta premissa abans de substituir el commit.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git add notes.md

**Terminal · comanda completa visible:**

```text
git add notes.md
```

**Subratllat:** `git add`.

**Locució:** Amb git add seleccionem el contingut que volem confirmar.

**Visual:** Mantenir visible el text complet: git add notes.md. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git add.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add notes.md
```

**Subratllat:** `notes.md`.

**Locució:** El nom identifica el fitxer que preparem. La còpia desada ara és la que entra a la preparació.

**Visual:** Mantenir visible el text complet: git add notes.md. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: notes.md.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add notes.md
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git add notes.md. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add notes.md
```

**Locució:** Les notes queden preparades. La resta del contingut preparat continua coincidint amb C.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git diff --staged --stat

**Terminal · comanda completa visible:**

```text
git diff --staged --stat
```

**Subratllat:** `git diff`.

**Locució:** Revisem què hem seleccionat.

**Visual:** Mantenir visible el text complet: git diff --staged --stat. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git diff.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff --staged --stat
```

**Subratllat:** `--staged`.

**Locució:** Consulta els canvis preparats respecte de l’últim commit.

**Visual:** Mantenir visible el text complet: git diff --staged --stat. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --staged.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff --staged --stat
```

**Subratllat:** `--stat`.

**Locució:** Mostra un resum dels fitxers afectats; per llegir les línies completes podem consultar el diff preparat sense aquesta opció.

**Visual:** Mantenir visible el text complet: git diff --staged --stat. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --stat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff --staged --stat
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git diff --staged --stat. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff --staged --stat
```

**Locució:** El resum només mostra les notes noves. No afegirem altres feines per accident.

**Visual:** Mostrar notes.md al resum i una comprovació del seu contingut. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit --amend --no-edit

**Terminal · comanda completa visible:**

```text
git commit --amend --no-edit
```

**Subratllat:** `git commit`.

**Locució:** Substituïm l’últim commit amb git commit.

**Visual:** Mantenir visible el text complet: git commit --amend --no-edit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit --amend --no-edit
```

**Subratllat:** `--amend`.

**Locució:** Crea un commit nou amb el mateix pare que l’anterior, incorporant el contingut preparat.

**Visual:** Mantenir visible el text complet: git commit --amend --no-edit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --amend.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit --amend --no-edit
```

**Subratllat:** `--no-edit`.

**Locució:** Conserva el missatge anterior sense obrir l’editor.

**Visual:** Mantenir visible el text complet: git commit --amend --no-edit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --no-edit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit --amend --no-edit
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit --amend --no-edit. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit --amend --no-edit
```

**Locució:** Main passa a C prima, amb pare B i identificador nou. El missatge i l’autoria es conserven; les notes ja hi són incloses.

**Visual:** Atenuar C fora de la línia actual i crear C′ des de B. No dibuixar C′ com un fill de C. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git show --stat HEAD

**Terminal · comanda completa visible:**

```text
git show --stat HEAD
```

**Subratllat:** `git show`.

**Locució:** Comprovem el commit resultant.

**Visual:** Mantenir visible el text complet: git show --stat HEAD. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git show.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show --stat HEAD
```

**Subratllat:** `--stat`.

**Locució:** Resumeix els fitxers del commit consultat.

**Visual:** Mantenir visible el text complet: git show --stat HEAD. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --stat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show --stat HEAD
```

**Subratllat:** `HEAD`.

**Locució:** Assenyala el nou commit actual en aquest exemple.

**Visual:** Mantenir visible el text complet: git show --stat HEAD. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: HEAD.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show --stat HEAD
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git show --stat HEAD. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git show --stat HEAD
```

**Locució:** La salutació i les notes formen part del mateix canvi complet. L’estat del treball queda net.

**Visual:** Mostrar missatge conservat i fitxer de notes inclòs; main a C′. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Alternativa: canviar només el missatge

**Locució:** En un cas independent tornem a C amb la preparació sense diferències. Podem substituir només el missatge, conservant el contingut i el pare.

**Visual:** Separador CAS INDEPENDENT; recuperar C amb índex igual a C, sense les notes preparades del camí anterior.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git commit --amend -m "Personalitza el missatge"

**Camí:** `alternative:message`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git commit --amend -m "Personalitza el missatge"
```

**Subratllat:** `git commit`.

**Locució:** Escrivim un altre missatge per a l’últim commit.

**Visual:** Mantenir visible el text complet: git commit --amend -m "Personalitza el missatge". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit --amend -m "Personalitza el missatge"
```

**Subratllat:** `--amend`.

**Locució:** Substitueix l’últim commit a la branca.

**Visual:** Mantenir visible el text complet: git commit --amend -m "Personalitza el missatge". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --amend.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit --amend -m "Personalitza el missatge"
```

**Subratllat:** `-m`.

**Locució:** Introdueix el missatge nou.

**Visual:** Mantenir visible el text complet: git commit --amend -m "Personalitza el missatge". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit --amend -m "Personalitza el missatge"
```

**Subratllat:** `"Personalitza el missatge"`.

**Locució:** Aquest és el text nou. En aquest cas no hem preparat cap canvi de contingut.

**Visual:** Mantenir visible el text complet: git commit --amend -m "Personalitza el missatge". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Personalitza el missatge".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit --amend -m "Personalitza el missatge"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit --amend -m "Personalitza el missatge". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit --amend -m "Personalitza el missatge"
```

**Locució:** Es crea un altre identificador, amb el mateix arbre i pare B. És una alternativa al cas anterior.

**Visual:** Comparar arbre igual / missatge diferent / hash diferent. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Amend substitueix l’últim commit a la branca; no n’afegeix un fill.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Revisem el contingut preparat abans de fer-lo.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** En aquesta lliçó només reescrivim l’últim commit propi encara no publicat.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En un repositori de pràctiques sense publicar, afegeix un fitxer oblidat a l’últim commit. Compara el pare, el missatge, els fitxers i l’identificador abans i després.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
