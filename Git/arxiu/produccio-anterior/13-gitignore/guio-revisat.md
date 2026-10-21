# Lliçó 13 · Gitignore: tria què entra al repositori

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Tretzena lliçó, Git ignore.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a ignorar fitxers generats i distingir fitxers nous dels que Git ja seguia.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Exemple independent: helloGit.py i app.log ja seguits. app.log té una edició sense preparar. debug.log i __pycache__/ són nous. Encara no hi ha .gitignore.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Separar el codi dels fitxers generats

**Locució:** Volem versionar el codi i les regles del projecte. Els registres d’execució i la memòria cau nous no han d’entrar a cada commit.

**Visual:** Quatre targetes amb estat: codi seguit, app.log seguit, debug.log nou i __pycache__/ nou.

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

**Locució:** El registre nou i la memòria cau apareixen com a fitxers no seguits. El registre antic també apareix, però com a fitxer seguit modificat.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Escrivim les regles al projecte

**Locució:** Creem el fitxer punt gitignore. Escrivim una regla per línia. Asterisc punt log selecciona noms acabats en aquesta extensió.

**Visual:** Editor .gitignore amb dues línies literals: *.log i __pycache__/. Ressaltar primer l’asterisc i després la barra.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

**Locució:** La regla de memòria cau acaba en barra i selecciona aquestes carpetes. El fitxer de regles també es pot confirmar perquè el projecte comparteixi els criteris.

**Visual:** Editor .gitignore amb dues línies literals: *.log i __pycache__/. Ressaltar primer l’asterisc i després la barra.

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

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git status --short. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git status --short
```

**Locució:** El registre nou i la memòria cau ja no apareixen. El fitxer de regles sí, perquè encara és nou. El registre antic continua modificat.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git check-ignore -v debug.log

**Terminal · comanda completa visible:**

```text
git check-ignore -v debug.log
```

**Subratllat:** `git check-ignore`.

**Locució:** Investiguem la regla que afecta el registre nou.

**Visual:** Mantenir visible el text complet: git check-ignore -v debug.log. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git check-ignore.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git check-ignore -v debug.log
```

**Subratllat:** `-v`.

**Locució:** El guionet ve demana informació detallada de la regla.

**Visual:** Mantenir visible el text complet: git check-ignore -v debug.log. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -v.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git check-ignore -v debug.log
```

**Subratllat:** `debug.log`.

**Locució:** Aquest argument indica el fitxer nou que estem consultant.

**Visual:** Mantenir visible el text complet: git check-ignore -v debug.log. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: debug.log.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git check-ignore -v debug.log
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git check-ignore -v debug.log. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git check-ignore -v debug.log
```

**Locució:** La sortida identifica el fitxer de regles, la línia i el patró que coincideix.

**Visual:** Separar visualment .gitignore, número de línia, *.log i debug.log. La locució diu registre o punt log; no interpreta l’extensió com logaritme. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Una regla no deixa de seguir un fitxer

**Locució:** El registre antic ja formava part dels commits. La regla filtra fitxers no seguits, però no en retira automàticament un que ja estava versionat.

**Visual:** Conservar app.log ressaltat com SEGUIT i debug.log com NO SEGUIT IGNORAT.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## git rm --cached app.log

**Terminal · comanda completa visible:**

```text
git rm --cached app.log
```

**Subratllat:** `git rm`.

**Locució:** Decidim deixar de versionar el registre antic, conservant-ne la còpia local.

**Visual:** Mantenir visible el text complet: git rm --cached app.log. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git rm.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rm --cached app.log
```

**Subratllat:** `--cached`.

**Locució:** Aquesta opció retira el fitxer de la preparació sense esborrar-lo del disc.

**Visual:** Mantenir visible el text complet: git rm --cached app.log. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --cached.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rm --cached app.log
```

**Subratllat:** `app.log`.

**Locució:** És el registre que ja estava seguit. En aquest exemple la seva còpia preparada coincidia amb l’últim commit.

**Visual:** Mantenir visible el text complet: git rm --cached app.log. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: app.log.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rm --cached app.log
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git rm --cached app.log. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rm --cached app.log
```

**Locució:** Queda preparada la retirada del fitxer del repositori. La còpia local continua existint.

**Visual:** Retirar app.log de l’índex; mantenir-lo al treball. Mostrar una D preparada, sense animació d’esborrat al disc. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git add .gitignore

**Terminal · comanda completa visible:**

```text
git add .gitignore
```

**Subratllat:** `git add`.

**Locució:** Amb git add seleccionem el contingut que volem confirmar.

**Visual:** Mantenir visible el text complet: git add .gitignore. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git add.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add .gitignore
```

**Subratllat:** `.gitignore`.

**Locució:** El nom identifica el fitxer que preparem. La còpia desada ara és la que entra a la preparació.

**Visual:** Mantenir visible el text complet: git add .gitignore. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: .gitignore.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add .gitignore
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git add .gitignore. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git add .gitignore
```

**Locució:** Preparem també les regles noves. La retirada del registre ja era preparada.

**Visual:** Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git commit -m "Ignora fitxers generats"

**Terminal · comanda completa visible:**

```text
git commit -m "Ignora fitxers generats"
```

**Subratllat:** `git commit`.

**Locució:** Amb git commit enregistrarem el contingut preparat en una versió local.

**Visual:** Mantenir visible el text complet: git commit -m "Ignora fitxers generats". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git commit.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Ignora fitxers generats"
```

**Subratllat:** `-m`.

**Locució:** El guionet ema indica que a continuació escrivim el missatge del canvi.

**Visual:** Mantenir visible el text complet: git commit -m "Ignora fitxers generats". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -m.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Ignora fitxers generats"
```

**Subratllat:** `"Ignora fitxers generats"`.

**Locució:** El text entre cometes descriu la feina: Ignora fitxers generats. Les cometes agrupen el missatge en un sol argument.

**Visual:** Mantenir visible el text complet: git commit -m "Ignora fitxers generats". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: "Ignora fitxers generats".

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Ignora fitxers generats"
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git commit -m "Ignora fitxers generats". Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git commit -m "Ignora fitxers generats"
```

**Locució:** El commit enregistra les regles i la retirada del registre. La còpia local del registre es conserva i ara queda ignorada com a fitxer no seguit.

**Visual:** Subratllar commit, després -m i després el missatge. Crear el node nou només en executar. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Gitignore filtra fitxers no seguits que coincideixen amb les regles.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Les regles també es poden compartir amb un commit.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Retirar un fitxer ja versionat és una decisió separada; cached conserva la còpia local.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En un projecte de pràctiques, crea un registre nou i una regla per ignorar-lo. Comprova la coincidència i contrasta el resultat amb un fitxer que ja estigui seguit.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
