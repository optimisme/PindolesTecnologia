# Lliçó 18 · Stash: aparca la feina pendent

**Sèrie:** Píndoles de Git · **Capçalera:** STASH — Aparca la feina pendent  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/18-stash.sh`](../practiques/18-stash.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Divuitena lliçó. *Stash*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a aparcar canvis pendents, atendre una altra tasca i recuperar-los després. *(pausa 2.5 s)*

Som a la branca salutació, a mitja feina. Hem modificat el programa i hem creat un fitxer de notes, però encara no ho volem confirmar. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Una interrupció

Ens demanen una correcció urgent a *main*. No volem barrejar-hi la feina a mitges, ni confirmar-la encara. L’aparcarem un moment. *(pausa 3 s)*

**Visual:** Dues targetes, helloGit.py MODIFICAT i notes.md NOU. main i salutacio a B.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El programa apareix modificat sense preparar, i les notes, com a fitxer nou. Cap dels dos canvis és a l’historial. *(pausa 3.5 s)*

Sortida real:

```text
 M helloGit.py
?? notes.md
```

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git stash push -u -m "Salutacio pendent"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git stash push` | *git stash push* desa la feina pendent en una entrada temporal. | 2.5 s |
| `-u` | El guionet u inclou també els fitxers nous. Els fitxers ignorats queden fora. | 2.5 s |
| `-m` | El guionet ema introdueix un missatge per reconèixer l’entrada. | 2.5 s |
| `"Salutacio pendent"` | Descriu la feina aparcada, la salutació pendent. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El programa torna a la versió confirmada i les notes desapareixen de la carpeta. Els canvis són a l’entrada temporal; la branca no ha avançat. *(pausa 3.5 s)*

Sortida real:

```text
Saved working directory and index state On salutacio: Salutacio pendent
```

**Visual:** Els dos continguts viatgen a una caixa STASH. main i salutacio continuen a B.

## Terminal · `git stash list`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git stash list` | Consultem les entrades guardades. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Apareix una entrada amb el seu número i el missatge que hem escrit. És feina aparcada, no un *commit* de la branca. *(pausa 3.5 s)*

Sortida real:

```text
stash@{0}: On salutacio: Salutacio pendent
```

**Visual:** Ressaltar stash@{0} i el missatge com a parts de la mateixa entrada a la sortida real.

## Terminal · `git switch main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `main` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Amb la carpeta neta, podríem fer la correcció a *main*. Per no allargar l’exemple, ometem aquesta correcció i tornem a la nostra feina. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'main'
```

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució.

## Terminal · `git switch salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `salutacio` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Tornem a la branca de la salutació abans de recuperar-hi els canvis. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'salutacio'
```

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució.

## Terminal · `git stash pop`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git stash pop` | *git stash pop* recupera els canvis i retira l’entrada si tot va bé. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Tornen la salutació modificada i les notes. Continuen sent feina pendent, sense confirmar. *(pausa 3.5 s)*

Sortida real:

```text
On branch salutacio
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   helloGit.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	notes.md

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (0188bb6641725b34c62da46afa3c5604f194a718)
```

**Visual:** S’obre la caixa STASH i cada contingut torna al seu fitxer. Cap node nou.

## Terminal · `git stash list`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git stash list` | Comprovem la llista després de recuperar-la. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara és buida, perquè els canvis s’han aplicat bé. Si hi hagués hagut un conflicte, l’entrada no s’hauria esborrat. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Llista buida amb la llegenda CAP ENTRADA; panell condicional separat per al cas amb conflicte.

## Conservar l’entrada

*git stash apply* també recupera els canvis, però conserva l’entrada. És una alternativa a *pop*; no cal fer servir totes dues ordres per recuperar la mateixa feina. *(pausa 3 s)*

**Visual:** Comparació APPLY · conserva l’entrada / POP · la retira si s’aplica bé.

## Resum final

*Stash* aparca la feina pendent sense fer avançar la branca. *(pausa 2.5 s)*

El guionet u hi inclou els fitxers nous, però no els ignorats. *(pausa 2.5 s)*

En recuperar-la, la feina torna al treball; encara caldrà confirmar-la. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques, aparca una edició i un fitxer nou. Consulta l’entrada, canvia de branca i torna, i recupera la feina amb la carpeta neta. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
