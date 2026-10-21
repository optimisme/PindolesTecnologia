# Lliçó 18 · Reflog: recupera un commit local

**Sèrie:** Píndoles de Git · **Capçalera:** REFLOG — Recupera un commit local  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/18-reflog.sh`](../practiques/18-reflog.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Divuitena lliçó. *Reflog*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a trobar un *commit* al *reflog* i tornar-hi a donar accés amb una branca, sense perdre els canvis preparats. *(pausa 2.5 s)*

Continuem on ho vam deixar amb *reset soft*. La branca ha tornat enrere i el *commit* de la salutació ja no apareix a l’historial de *main*. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Un commit fora de la línia actual

El *commit* de la salutació ja no surt a la història de *main*, però no s’ha esborrat. Buscarem on era abans. *(pausa 3 s)*

**Visual:** Graf A i B amb main a B; C atenuat. Treball i preparació amb la salutació nova.

## Terminal · `git log --oneline`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Consultem l’historial de la branca activa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només hi ha dos *commits*. *git log* recorre la història a partir de la branca; no mostra on havíem estat abans. *(pausa 3.5 s)*

Sortida real:

```text
99010b3 Afegeix una exclamacio
d3fb44b Afegeix la salutacio inicial
```

**Visual:** Ressaltar el camí des de main; deixar C fora del recorregut.

## Terminal · `git reflog`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git reflog` | *git reflog* mostra per on ha passat *HEAD* en aquest repositori. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La primera línia és el *reset*. La segona és el *commit* de la salutació, abans de tornar enrere. Copiem l’identificador d’aquesta segona línia. *(pausa 3.5 s)*

Sortida real:

```text
99010b3 HEAD@{0}: reset: moving to HEAD~1
11b767c HEAD@{1}: commit: Personalitza la salutacio
99010b3 HEAD@{2}: commit: Afegeix una exclamacio
d3fb44b HEAD@{3}: commit (initial): Afegeix la salutacio inicial
```

**Visual:** Sortida real; ressaltar primer la fila del reset i després la del commit anterior.

## Terminal · `git show 11b767c -- helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | Revisem el *commit* trobat abans de recuperar-lo. | 2.5 s |
| `11b767c` | És l’identificador que hem copiat. Al teu repositori serà diferent. | 2.5 s |
| `helloGit.py` | Mirem només el canvi del programa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** És la salutació personalitzada que buscàvem. Consultar-la no modifica cap fitxer. *(pausa 3.5 s)*

Sortida real:

```text
commit 11b767cf0d70d83ee9a4feb07315dfc2076516dc
Author: Anna Puig <anna@example.com>
Date:   Tue Oct 20 12:07:00 2026 +0200

    Personalitza la salutacio

diff --git a/helloGit.py b/helloGit.py
index 52662af..55b21a2 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1 @@
-print("Hello Git!")
+print("Hola, Anna!")
```

**Visual:** Diff real del commit al costat de l’editor actual.

## Terminal · `git branch recuperacio 11b767c`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git branch` | Creem una branca que torni a donar accés a aquest *commit*. | 2.5 s |
| `recuperacio` | És el nom de la branca nova, recuperació. | 2.5 s |
| `11b767c` | Indica el *commit* on posem l’etiqueta. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La branca recuperació apunta al *commit* trobat. *main* continua on era i segueix sent la branca activa: no hem canviat de branca. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Afegir només l’etiqueta recuperacio a C. HEAD continua unit a main.

## Terminal · `git log --oneline --decorate --all`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Comprovem totes les branques alhora. | 2.5 s |
| `--decorate` | Escriu el nom de les branques al costat dels seus *commits*. | 2.5 s |
| `--all` | Doble guionet *all* inclou totes les branques, no només l’activa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* torna a ser visible a través de recuperació. *(pausa 3.5 s)*

Sortida real:

```text
11b767c (recuperacio) Personalitza la salutacio
99010b3 (HEAD -> main) Afegeix una exclamacio
d3fb44b Afegeix la salutacio inicial
```

**Visual:** Sortida real amb main i recuperacio; preparació intacta.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El canvi que havia deixat *reset soft* continua preparat. Crear la branca no l’ha tocat. *(pausa 3.5 s)*

Sortida real:

```text
M  helloGit.py
```

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Una ajuda local amb límits

El *reflog* només existeix al nostre ordinador i les entrades antigues caduquen. Recupera *commits*; les edicions que mai no hem confirmat no hi són. *(pausa 3 s)*

**Visual:** Icones LOCAL i RELLOTGE; distinció COMMIT EXISTENT / EDICIÓ SENSE CONFIRMAR.

## Resum final

*git log* recorre la història a partir d’una branca. *(pausa 2.5 s)*

*git reflog* mostra per on ha passat *HEAD* en aquest ordinador. *(pausa 2.5 s)*

Una branca nova torna a donar accés a un *commit* sense canviar la branca activa. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Després d’un *reset soft* de pràctiques, troba el *commit* al *reflog*, revisa’l i crea-hi una branca de recuperació sense canviar de branca. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
