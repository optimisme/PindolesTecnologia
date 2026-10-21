# Lliçó 5 · Llegir l’historial: log, show i diff

**Sèrie:** Píndoles de Git · **Capçalera:** LLEGIR L’HISTORIAL — Qui, quan i què ha canviat  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/05-historial.sh`](../practiques/05-historial.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Cinquena lliçó. Llegir l’historial.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a consultar els *commits* d’un projecte, veure què va canviar cadascun i comparar dues versions. *(pausa 2.5 s)*

Partim d’un projecte amb tres *commits* a *main*: la salutació inicial, una exclamació i un comiat. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## L’historial és una llista de commits

Cada *commit* guarda una instantània del projecte, qui la va fer, quan i un missatge. Llegir l’historial ens ajuda a entendre com hem arribat a la versió actual. *(pausa 3 s)*

**Visual:** Línia de temps A, B i C amb els missatges reals.

## Terminal · `git log`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | *git log* mostra els *commits* de la branca actual. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Surten del més recent al més antic. Cada un té un identificador llarg, l’autoria, la data i el missatge. Si la llista és llarga, sortim de la vista amb la tecla q. *(pausa 3.5 s)*

Sortida real:

```text
commit 424337671399e356687a0be79c217d5b2a788fb1
Author: Anna Puig <anna@example.com>
Date:   Tue Oct 20 12:09:00 2026 +0200

    Afegeix un comiat

commit 4a464f8ba8264fea7948d3ed2a9c2e2731451cf5
Author: Anna Puig <anna@example.com>
Date:   Tue Oct 20 12:06:00 2026 +0200

    Afegeix una exclamacio

commit d3fb44b0696e4f913b7637f461983ae0fd5f1cb3
Author: Anna Puig <anna@example.com>
Date:   Tue Oct 20 12:03:00 2026 +0200

```

**Visual:** Sortida real; ressaltar per torns l’identificador, l’autoria, la data i el missatge del primer commit.

## Terminal · `git log --oneline`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Ara en demanem un resum. | 2.5 s |
| `--oneline` | Doble guionet *oneline* mostra cada *commit* en una sola línia, amb l’identificador abreujat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Els set primers caràcters de l’identificador són suficients per referir-nos a un *commit* en aquest projecte. *(pausa 3.5 s)*

Sortida real:

```text
4243376 Afegeix un comiat
4a464f8 Afegeix una exclamacio
d3fb44b Afegeix la salutacio inicial
```

**Visual:** Sortida real en tres línies; relacionar cada línia amb A, B i C de la línia de temps.

## HEAD i els passos enrere

*HEAD* és el *commit* on som ara; en aquest exemple, el darrer de *main*. Per anomenar *commits* anteriors sense copiar identificadors, hi afegim una titlla i un número. *(pausa 3 s)*

*HEAD* titlla u és el *commit* anterior; *HEAD* titlla dos, dos passos enrere. *(pausa 3 s)*

**Visual:** Línia de temps amb HEAD a C, HEAD~1 a B i HEAD~2 a A. Ressaltar cada etiqueta per torns.

## Terminal · `git show HEAD`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | *git show* mostra el contingut d’un *commit*. | 2.5 s |
| `HEAD` | Consultem el *commit* actual, el del comiat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Primer surten les dades del *commit* i després el canvi. La línia amb el signe més és la que s’hi va afegir. *(pausa 3.5 s)*

Sortida real:

```text
commit 424337671399e356687a0be79c217d5b2a788fb1
Author: Anna Puig <anna@example.com>
Date:   Tue Oct 20 12:09:00 2026 +0200

    Afegeix un comiat

diff --git a/helloGit.py b/helloGit.py
index 52662af..097ee02 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1,2 @@
 print("Hello Git!")
+print("Fins aviat!")
```

**Visual:** Sortida real; separar DADES DEL COMMIT i CANVI amb una línia.

## Terminal · `git show HEAD~1`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | Consultem el *commit* anterior. | 2.5 s |
| `HEAD~1` | Un pas enrere des d’on som; és el *commit* de l’exclamació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Hi veiem la línia antiga, sense exclamació, i la nova, amb exclamació. *(pausa 3.5 s)*

Sortida real:

```text
commit 4a464f8ba8264fea7948d3ed2a9c2e2731451cf5
Author: Anna Puig <anna@example.com>
Date:   Tue Oct 20 12:06:00 2026 +0200

    Afegeix una exclamacio

diff --git a/helloGit.py b/helloGit.py
index 078d6bf..52662af 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1 @@
-print("Hello Git")
+print("Hello Git!")
```

**Visual:** Sortida real; ressaltar la parella de línies menys i més.

## Terminal · `git diff HEAD~2 HEAD -- helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | *git diff* també compara dues versions qualssevol. | 2.5 s |
| `HEAD~2` | El primer punt de comparació és la salutació inicial. | 2.5 s |
| `HEAD` | El segon és la versió actual. | 2.5 s |
| `--` | Els dos guionets separen les versions del nom del fitxer. | 2.5 s |
| `helloGit.py` | Limitem la comparació al programa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La comparació acumula els dos canvis: l’exclamació i el comiat. No modifica cap fitxer; només els llegeix. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 078d6bf..097ee02 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1,2 @@
-print("Hello Git")
+print("Hello Git!")
+print("Fins aviat!")
```

**Visual:** Sortida real; esquema A → C amb els dos canvis agrupats.

## Com es llegeix un diff

Les línies amb el signe menys desapareixen, i les del signe més s’hi afegeixen. Les línies sense signe són context, per situar el canvi dins del fitxer. *(pausa 3 s)*

**Visual:** Diff anotat amb tres etiquetes textuals, ESBORRADA, AFEGIDA i CONTEXT, a més dels colors.

## Resum final

*git log* llista els *commits*; doble guionet *oneline* en fa un resum. *(pausa 2.5 s)*

*git show* explica què va canviar un *commit* concret. *(pausa 2.5 s)*

*git diff* compara dues versions sense modificar cap fitxer. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori teu amb uns quants *commits*, llegeix l’historial resumit, consulta el *commit* anterior a l’actual i compara la primera versió amb la darrera. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
