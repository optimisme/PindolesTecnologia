# Lliçó 22 · Rebase interactiu: agrupa commits abans de publicar

**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.

**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.
**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.
**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.
**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.

## Capçalera i presentació

4 s de música comuna. Després, llegir el número i el títol:

> Vint-i-dosena lliçó, Rebase interactiu.

## Objectiu i punt de partida

**Locució:** En aquesta lliçó aprendrem a agrupar tres commits relacionats no publicats i conservar el contingut final.

**Visual:** Objectiu en una frase; esquema general del resultat.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Salutacio activa a E amb C, D i E propis no publicats sobre B. Main a B; treball net. C personalitza, D retoca la puntuació i E documenta la mateixa millora.

**Visual:** Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Una millora explicada en tres commits

**Locució:** La feina és una mateixa millora repartida en tres commits. Abans de publicar-los, els agruparem perquè l’historial expliqui el resultat de manera coherent.

**Visual:** Graf A–B–C–D–E; etiqueta NO PUBLICATS sobre C–E i main a B.

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

**Locució:** Comencem sense canvis locals pendents. Conservem l’identificador real d’E per comparar després el contingut final.

**Visual:** Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git log -3 --oneline

**Terminal · comanda completa visible:**

```text
git log -3 --oneline
```

**Subratllat:** `git log`.

**Locució:** Revisem els tres commits que volem agrupar.

**Visual:** Mantenir visible el text complet: git log -3 --oneline. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git log.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log -3 --oneline
```

**Subratllat:** `-3`.

**Locució:** Limita la consulta als tres últims commits.

**Visual:** Mantenir visible el text complet: git log -3 --oneline. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -3.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log -3 --oneline
```

**Subratllat:** `--oneline`.

**Locució:** Permet llegir-ne els identificadors i els missatges en un resum.

**Visual:** Mantenir visible el text complet: git log -3 --oneline. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --oneline.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log -3 --oneline
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git log -3 --oneline. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git log -3 --oneline
```

**Locució:** Confirmem que els tres canvis són propis, relacionats i encara no publicats.

**Visual:** Distingir ordre del log, més recent primer, de l’ordre que tindrà l’editor interactiu. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git rebase -i HEAD~3

**Terminal · comanda completa visible:**

```text
git rebase -i HEAD~3
```

**Subratllat:** `git rebase`.

**Locució:** Obrim una reescriptura interactiva d’aquest tram.

**Visual:** Mantenir visible el text complet: git rebase -i HEAD~3. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git rebase.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase -i HEAD~3
```

**Subratllat:** `-i`.

**Locució:** El guionet i obre una llista editable d’operacions.

**Visual:** Mantenir visible el text complet: git rebase -i HEAD~3. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: -i.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase -i HEAD~3
```

**Subratllat:** `HEAD~3`.

**Locució:** La base és B, tres passos enrere des d’E. La llista inclou els commits posteriors: C, D i E.

**Visual:** Mantenir visible el text complet: git rebase -i HEAD~3. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: HEAD~3.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase -i HEAD~3
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git rebase -i HEAD~3. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase -i HEAD~3
```

**Locució:** L’editor mostra els commits del més antic al més recent. Encara falta editar, desar i tancar.

**Visual:** Editor amb pick C Personalitza, pick D Puntuacio, pick E Documenta. No representar la reescriptura com a acabada. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Escollim les operacions

**Locució:** Deixem pick al primer commit. Als altres dos canviem l’acció a squash, que els agrupa amb l’anterior.

**Visual:** Llista final: pick C Personalitza; squash D Puntuacio; squash E Documenta. Subratllar cada acció per separat.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Desem i tanquem l’editor de la llista. Aquesta acció permet que Git continuï; escriure la llista sense desar-la no completa el pas.

**Visual:** Llista final: pick C Personalitza; squash D Puntuacio; squash E Documenta. Subratllar cada acció per separat.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Escrivim el missatge conjunt

**Locució:** A continuació s’obre l’editor del missatge. Escrivim Personalitza la salutació i documenta el canvi. Desem i tanquem també aquest editor.

**Visual:** Missatge conjunt complet visible; dos indicadors diferents LLISTA DESADA i MISSATGE DESAT.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## Un node nou amb el mateix resultat

**Locució:** La branca de salutació apunta a S, amb pare B i un identificador nou. Main continua a B. Els antics C, D i E queden fora de la línia de la branca, sense esborrar-se immediatament.

**Visual:** Graf abans/després amb C–E atenuats i S nou; contingut final igual al d’E.

**Pausa:** 3 s sense locució; mantenir el visual i el subratllat.

## python3 helloGit.py

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

**Locució:** El programa conserva el resultat final després d’agrupar els commits.

**Visual:** Mostrar la sortida real del programa al costat de l’editor. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git diff e18a3b6 HEAD --

**Terminal · comanda completa visible:**

```text
git diff e18a3b6 HEAD --
```

**Subratllat:** `git diff`.

**Locució:** Comparem els fitxers finals amb l’antic E.

**Visual:** Mantenir visible el text complet: git diff e18a3b6 HEAD --. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git diff.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff e18a3b6 HEAD --
```

**Subratllat:** `e18a3b6`.

**Locució:** És el hash de mostra de l’antic E; fem servir el que havíem conservat.

**Visual:** Mantenir visible el text complet: git diff e18a3b6 HEAD --. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: e18a3b6.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff e18a3b6 HEAD --
```

**Subratllat:** `HEAD`.

**Locució:** És el nou commit S.

**Visual:** Mantenir visible el text complet: git diff e18a3b6 HEAD --. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: HEAD.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff e18a3b6 HEAD --
```

**Subratllat:** `--`.

**Locució:** Tanquem la llista de versions sense restringir-la a un fitxer.

**Visual:** Mantenir visible el text complet: git diff e18a3b6 HEAD --. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar únicament: --.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff e18a3b6 HEAD --
```

**Locució:** Executem l’ordre.

**Visual:** Mantenir visible el text complet: git diff e18a3b6 HEAD --. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Executar després de la locució, sense mostrar abans el resultat.

**Pausa:** 1.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git diff e18a3b6 HEAD --
```

**Locució:** La sortida buida indica que no hi ha diferències de contingut en aquesta comparació. Provem també el programa per comprovar-ne el comportament.

**Visual:** Sortida buida amb llegenda CONTINGUT IGUAL; terminal de prova separat. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Si l’operació s’atura

**Locució:** En un cas amb conflictes, editem la resolució, la provem i fem add del fitxer. Després podem continuar; també podem abandonar l’operació pendent.

**Visual:** Panell condicional separat amb editor → prova → git add helloGit.py.

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

**Locució:** Reprenem el rebase pausat després de preparar la resolució.

**Visual:** Mantenir visible el text complet: git rebase --continue. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git rebase.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase --continue
```

**Subratllat:** `--continue`.

**Locució:** Continua l’operació en curs; pot demanar més resolucions.

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

**Locució:** La reescriptura avança fins al resultat revisat.

**Visual:** Només camí CONTINUAR. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## git rebase --abort

**Camí:** `alternative:abort`. Respectar el punt de partida indicat; no encadenar alternatives.

**Terminal · comanda completa visible:**

```text
git rebase --abort
```

**Subratllat:** `git rebase`.

**Locució:** Podem optar per abandonar el rebase pendent.

**Visual:** Mantenir visible el text complet: git rebase --abort. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat. Subratllar l’acció: git rebase.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Terminal · comanda completa visible:**

```text
git rebase --abort
```

**Subratllat:** `--abort`.

**Locució:** Recupera l’estat de partida d’aquesta operació.

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

**Locució:** Aquest camí alternatiu conserva la història inicial.

**Visual:** Camí AVORTAR des de l’aturada, mai després de completar continue. Mostrar el resultat concret i conservar l’estat anterior per comparar.

**Pausa:** 3.5 s sense locució; mantenir el visual i el subratllat.

## Resum final

**Locució:** Agrupem només els commits relacionats del tram seleccionat.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** Cal desar i tancar tant la llista com el missatge conjunt.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

**Locució:** L’historial canvia i els identificadors són nous; comprovem que el contingut final es conservi.

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

**Pausa:** 2.5 s sense locució; mantenir el visual i el subratllat.

## Pràctica final

**Locució:** En una branca local de pràctiques no publicada, agrupa tres commits relacionats. Conserva el hash final antic i compara els continguts després de la reescriptura.

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.

**Pausa:** 4 s sense locució; mantenir el visual i el subratllat.
