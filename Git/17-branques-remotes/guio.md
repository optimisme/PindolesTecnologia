# Lliçó 17 · Branques remotes: consultar, seguir i esborrar

**Sèrie:** Píndoles de Git · **Capçalera:** BRANQUES REMOTES — Consultar, seguir i esborrar  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/17-branques-remotes.sh`](../practiques/17-branques-remotes.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Dissetena lliçó. Branques remotes.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a veure quines branques hi ha al servidor, treballar en una d’elles i netejar les que ja no calen. *(pausa 2.5 s)*

Treballem en equip. Una companya ha publicat una branca nova, i al servidor n’hi ha d’altres que ja no fan falta. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Branques del servidor, vistes des de casa

Les referències com *origin/main* són una còpia local del que hi havia al servidor l’últim cop que el vam consultar. Si al servidor s’hi creen o s’hi esborren branques, no ho sabrem fins que tornem a consultar-lo. *(pausa 3 s)*

**Visual:** Servidor amb main, proves i menu; la nostra còpia encara amb origin/main, origin/proves i origin/prova-antiga.

## Terminal · `git branch -vv`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git branch` | *git branch* amb dues uves mostra les nostres branques amb més detall. | 2.5 s |
| `-vv` | Les dues uves afegeixen la branca del servidor que segueix cada branca local. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Cada branca local indica entre claudàtors quina branca remota segueix. Si estigués endarrerida o avançada, també ho diria. *(pausa 3.5 s)*

Sortida real:

```text
* main   afc44d6 [origin/main] Afegeix la salutacio inicial
  proves afc44d6 [origin/proves] Afegeix la salutacio inicial
```

**Visual:** Sortida real; ressaltar [origin/main] i [origin/proves].

## Terminal · `git fetch --prune`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git fetch` | Consultem el servidor i netegem les referències velles. | 2.5 s |
| `--prune` | Esborra les referències locals de les branques que ja no existeixen al servidor. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Arriba la branca nova de la companya, i la referència de la branca esborrada desapareix de la nostra còpia. *(pausa 3.5 s)*

Sortida real:

```text
From ~/origin
 - [deleted]         (none)     -> origin/prova-antiga
 * [new branch]      menu       -> origin/menu
```

**Visual:** Sortida real; ressaltar la línia de la branca nova i la de la branca esborrada.

## Terminal · `git branch -r`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git branch` | Llistem les branques del servidor que coneixem. | 2.5 s |
| `-r` | El guionet erra mostra només les branques remotes. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Hi ha *main*, la branca nova i la nostra branca de proves. *(pausa 3.5 s)*

Sortida real:

```text
  origin/HEAD -> origin/main
  origin/main
  origin/menu
  origin/proves
```

**Visual:** Sortida real amb tres branques remotes.

## Terminal · `git switch menu`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Volem treballar a la branca de la companya. | 2.5 s |
| `menu` | És el nom de la branca. Com que només existeix al servidor, *Git* en crea una de local que la segueix. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ja som a la branca, amb els fitxers de la companya, i la nostra branca local queda connectada amb la del servidor. *(pausa 3.5 s)*

Sortida real:

```text
branch 'menu' set up to track 'origin/menu'.
Switched to a new branch 'menu'
```

**Visual:** Apareix l’etiqueta local menu al costat d’origin/menu; HEAD s’hi uneix.

## Terminal · `git push origin --delete proves`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | La nostra branca de proves ja no cal al servidor. L’esborrem amb *git push*. | 2.5 s |
| `--delete` | Esborra la branca indicada al servidor. | 2.5 s |
| `proves` | És la branca que retirem. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La branca desapareix del servidor. La nostra branca local amb el mateix nom encara existeix. *(pausa 3.5 s)*

Sortida real:

```text
To ~/origin.git
 - [deleted]         proves
```

**Visual:** L’etiqueta proves desapareix del servidor; la local es manté.

## Terminal · `git branch -d proves`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git branch` | Esborrem també la branca local. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara la branca de proves ja no existeix enlloc. Els *commits* que contenia continuen a *main*. *(pausa 3.5 s)*

Sortida real:

```text
Deleted branch proves (was afc44d6).
```

**Visual:** Desapareix l’etiqueta local proves.

## Resum final

*git branch* amb dues uves mostra quina branca remota segueix cada branca local. *(pausa 2.5 s)*

*git fetch* amb doble guionet *prune* porta les novetats i neteja les referències velles. *(pausa 2.5 s)*

*git switch* crea la branca local d’una de remota; *git push* amb doble guionet *delete* l’esborra del servidor. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Amb dos clons de pràctiques, publica una branca des d’un i esborra’n una altra al servidor. Des de l’altre clon, actualitza amb neteja, canvia a la branca nova i comprova quina branca remota segueix. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
