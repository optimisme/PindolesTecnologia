# Lliçó 26 · Forks i upstream: una còpia pròpia al dia

**Sèrie:** Píndoles de Git · **Capçalera:** FORKS I UPSTREAM — Una còpia pròpia d’un projecte  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/26-forks-upstream.sh`](../practiques/26-forks-upstream.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-sisena lliçó. *Forks* i *upstream*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a relacionar el projecte original, el *fork* i el clon local, i mantenir el *fork* al dia amb l’original. *(pausa 2.5 s)*

Volem contribuir a un projecte d’una altra persona, on no tenim permís per publicar. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Tres repositoris

L’original és el projecte on volem contribuir. El *fork* és una còpia de l’original al nostre compte de *GitHub*. El clon és la còpia de treball del nostre ordinador. *(pausa 3 s)*

**Visual:** Tres caixes persistents, ORIGINAL, FORK PROPI i CLON LOCAL. El fork no és una carpeta local.

## Creem el fork

A la pàgina de l’original, fem clic al botó *Fork* i triem el nostre compte. La còpia queda a *GitHub*; encara no la tenim a l’ordinador. *(pausa 3 s)*

**Visual:** Esquema del botó Fork i del formulari, amb comptes inventats.

## Terminal · `git clone <URL-del-fork> HelloGit`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git clone` | Clonem el *fork*, el repositori del nostre compte. | 2.5 s |
| `<URL-del-fork>` | És l’adreça del nostre *fork*, sense els signes de menor i major. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La carpeta conté el projecte i el remot *origin* apunta al nostre *fork*. *(pausa 3.5 s)*

Sortida de mostra:

```text
Cloning into 'HelloGit'...
```

**Visual:** Fletxa FORK → LOCAL; etiqueta origin vinculada al fork.

## Terminal · `cd HelloGit`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `cd` | Entrem a la còpia local. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La terminal és dins del projecte. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Ruta visible a la terminal.

## Terminal · `git remote add upstream <URL-original>`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git remote add` | Afegim una segona connexió amb *git remote*. | 2.5 s |
| `add` | Afegeix un remot nou. | 2.5 s |
| `upstream` | És el nom que donem al remot de l’original. És un costum, no una paraula obligatòria. | 2.5 s |
| `<URL-original>` | És l’adreça del projecte original, diferent de la del *fork*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *origin* continua apuntant al *fork* i *upstream* apunta a l’original. Afegir-lo encara no descarrega res. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Dues connexions amb noms i adreces diferenciades.

## Terminal · `git remote -v`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git remote` | Comprovem les connexions. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Cada nom té la seva adreça. Enviarem la nostra feina a *origin* i descarregarem les novetats de *upstream*. *(pausa 3.5 s)*

Sortida de mostra:

```text
origin	https://github.com/anna-puig/HelloGit.git (fetch)
origin	https://github.com/anna-puig/HelloGit.git (push)
upstream	https://github.com/projecte-original/HelloGit.git (fetch)
upstream	https://github.com/projecte-original/HelloGit.git (push)
```

**Visual:** Taula amb nom, adreça i direcció; ressaltar una fila cada vegada.

## L’original avança

Mentrestant, l’original incorpora un *commit* nou. El nostre *fork* i la nostra còpia local no se n’assabenten sols: els hem de posar al dia. *(pausa 3 s)*

**Visual:** ORIGINAL amb C; FORK i LOCAL encara a B. La novetat és un README.md.

## Terminal · `git fetch upstream`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git fetch` | Descarreguem les novetats de l’original. | 2.5 s |
| `upstream` | Consultem l’original, no el nostre *fork*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La referència *upstream/main* apunta al *commit* nou. El nostre *main* encara no ha canviat. *(pausa 3.5 s)*

Sortida real:

```text
From ~/original
 * [new branch]      main       -> upstream/main
```

**Visual:** Actualitzar només la referència upstream/main.

## Terminal · `git merge --ff-only upstream/main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git merge` | Incorporem la novetat al nostre *main*. | 2.5 s |
| `upstream/main` | És la versió de l’original que acabem de descarregar. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El nostre *main* avança fins al *commit* nou. El *fork* de *GitHub* encara no el té. *(pausa 3.5 s)*

Sortida real:

```text
Updating f5f5973..119bbc7
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

**Visual:** Moure només main local.

## Terminal · `git push origin main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | Enviem *main* al nostre *fork*. | 2.5 s |
| `origin` | La destinació és el nostre *fork*. | 2.5 s |
| `main` | Publiquem la branca *main*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** L’original, el *fork* i la còpia local tornen a coincidir. *(pausa 3.5 s)*

Sortida real:

```text
To ~/fork.git
   f5f5973..119bbc7  main -> main
```

**Visual:** Fletxa LOCAL → FORK; cap fletxa cap a l’original.

## Resum final

El *fork* és una còpia remota al nostre compte; el clon és la còpia local. *(pausa 2.5 s)*

*origin* apunta al *fork* i *upstream*, a l’original. *(pausa 2.5 s)*

Per posar-nos al dia, descarreguem d’*upstream* i publiquem a *origin*. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Fes un *fork* d’un projecte de pràctiques, clona’l i afegeix-hi el remot *upstream*. Comprova les dues adreces abans de continuar. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
