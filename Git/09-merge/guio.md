# Lliçó 9 · Merge: porta la prova a main

**Sèrie:** Píndoles de Git · **Capçalera:** MERGE — Porta la prova a main  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/09-merge.sh`](../practiques/09-merge.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Novena lliçó. *Merge*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a integrar la branca salutació a *main* i distingir l’avançament directe de la fusió amb dos pares. *(pausa 2.5 s)*

Som a la branca salutació, amb la salutació personalitzada ja confirmada i provada. *main* encara té la versió original. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Origen i destinació

Volem portar a *main* el canvi de la salutació. *git merge* incorpora una branca a la branca activa; per això, primer ens hem de situar a la destinació. *(pausa 3 s)*

**Visual:** Graf A, B i C; main a B i salutacio a C. Etiquetes ORIGEN a salutacio i DESTINACIÓ a main.

## Terminal · `git switch main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `main` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La destinació activa ara és *main*, amb la salutació original. La branca salutació es conserva. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'main'
```

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució.

## Terminal · `git branch --show-current`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git branch` | Confirmem on som abans d’integrar. | 2.5 s |
| `--show-current` | Aquesta opció mostra només el nom de la branca activa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La terminal respon *main*. Encara no hem integrat res. *(pausa 3.5 s)*

Sortida real:

```text
main
```

**Visual:** Ressaltar main tant a la sortida com al graf.

## Terminal · `git merge --ff-only salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git merge` | *git merge* incorpora la història de la branca que indiquem. | 2.5 s |
| `--ff-only` | Només acceptem un avançament directe. Funciona quan *main* no té *commits* propis que la branca no tingui; si no, l’ordre s’atura sense canviar res. | 2.5 s |
| `salutacio` | És la branca que incorporem. No canvia la branca activa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* avança fins al *commit* de la salutació. Les dues etiquetes apunten al mateix *commit* i no s’ha creat cap *commit* nou. *(pausa 3.5 s)*

Sortida real:

```text
Updating 4a464f8..7452593
Fast-forward
 helloGit.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Moure només l’etiqueta main de B a C sobre el graf existent. Conservar salutacio i tots els nodes.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** A *main* també surt la salutació personalitzada. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Anna!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git branch -d salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git branch` | La branca de la prova ja ha fet la seva feina. Amb *git branch* la podem esborrar. | 2.5 s |
| `-d` | El guionet de esborra l’etiqueta de la branca, no els *commits*. Només ho fa si la branca ja està integrada; si no, *Git* s’hi nega i ens avisa. | 2.5 s |
| `salutacio` | És la branca que retirem. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Desapareix l’etiqueta salutació. El *commit* de la salutació continua a la història de *main*. *(pausa 3.5 s)*

Sortida real:

```text
Deleted branch salutacio (was 7452593).
```

**Visual:** Retirar l’etiqueta salutacio; el node C continua al graf amb l’etiqueta main.

## Un altre cas, dues branques que han avançat

> **Un altre cas.** Parteix del seu propi punt; no s’encadena amb el camí principal.

Partim ara d’un cas diferent. Abans d’integrar, algú ha afegit un *commit* a *main* amb unes notes. Les dues branques han avançat i ja no és possible un avançament directe. *(pausa 3 s)*

**Visual:** Separador UN ALTRE CAS. Tornar a B i dibuixar dos camins, C a salutacio i D a main. No reutilitzar el resultat anterior.

## Terminal · `git merge salutacio`

> **Un altre cas.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git merge` | En aquest cas, *git merge* crea un *commit* de fusió que uneix les dues històries. | 2.5 s |
| `salutacio` | Incorporem aquesta branca a la branca activa, que continua sent *main*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** S’obre l’editor que vam configurar amb un missatge proposat. El desem i tanquem la pestanya, i es crea el *commit* de fusió, amb dos pares. *(pausa 3.5 s)*

Sortida real:

```text
Merge made by the 'ort' strategy.
 helloGit.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Pestanya de l’editor amb el missatge Merge branch 'salutacio'. En tancar-la, aparèixer M connectat a D i C.

## Resum final

La branca activa és la que rep la integració. *(pausa 2.5 s)*

Un avançament directe mou l’etiqueta sense crear cap *commit*. *(pausa 2.5 s)*

Quan les branques han divergit, la fusió crea un *commit* amb dos pares. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques, crea una branca, confirma-hi un canvi i integra’l a *main* amb avançament directe. Executa el programa i esborra la branca integrada. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
