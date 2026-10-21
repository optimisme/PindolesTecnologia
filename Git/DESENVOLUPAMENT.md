# Desenvolupament de les lliçons

Com s’escriu una lliçó, com es comprova i com es produeix. La guia d’estil és al
[README](README.md#guia-destil).

## El fitxer `llico.yaml`

És l’únic fitxer que s’edita a mà. Exemple reduït:

```yaml
titol: "Branques: prova una idea sense tocar main"
titol_curt: BRANQUES                        # capçalera de cada escena
capcalera: [BRANQUES, Prova una idea sense tocar main]
presentacio: Branques                       # «Vuitena lliçó. Branques.»
objectiu: crear una branca, confirmar-hi una prova i tornar a les dues versions.
inici: Nota de producció amb l’estat exacte (no es llegeix).
inici_parlat: Frase que la veu diu per presentar el punt de partida.
preparacio: [...]                           # construeix l’estat inicial (repetició i pràctica)
camins: {...}                               # camins alternatius o condicionals
etapes: [...]                               # el vídeo, pas a pas
resum: [tres idees]
practica: Acció final per a l’alumnat.
```

Escriviu en YAML amb compte amb `: ` dins d’un text: si n’hi ha, feu servir `>-` o
cometes. El text entre `[[ ]]` es llegeix en anglès; els termes de `termes_angles`
de `serie.yaml` també, sense marcar-los.

### Etapes

**Explicació**, sense ordre:

```yaml
- explica: Títol de l’escena
  text: Una frase o una llista de frases (un pas per frase).
  visual: Instrucció per a l’animació.
  pausa: 3                    # opcional, segons després de cada frase
  accions: [...]              # canvis que fa la persona (editar un fitxer...)
```

**Ordre**, amb subratllat de les parts:

```yaml
- ordre: git switch -c salutacio
  text: Frase que presenta l’acció.
  parts:
    - -c: El guionet ce crea una branca nova i hi canvia.
    - salutacio: És el nom de la branca nova.
  resultat: Explicació del resultat, després d’executar.
  visual: Instrucció per a l’animació del resultat.
  comprova: {head: salutacio, refs: {main: B, salutacio: B}}
```

O bé amb una plantilla de `serie.yaml` (`status`, `status-breu`, `add`, `add-breu`, `commit`,
`commit-breu`, `switch`, `switch-crea`, `push`, `push-u`, `programa`):

```yaml
- plantilla: commit-breu
  missatge: Personalitza la salutacio
  crea: C                     # dona el nom C al commit nou
  resultat: ...
```

Camps opcionals d’una ordre: `falla: true` (s’espera un error), `entrada` (text per a
ordres interactives), `editor` (missatge que «escriu» la persona a l’editor),
`sequencia` (llista d’un rebase interactiu), `simulat: true` (no s’executa: web o `gh`),
`sortida_mostra` (es mostra en lloc de la real, marcada com a mostra), `tipus: interactiu`
(resposta dins d’una sessió interactiva, com `y` o `n`), `cami` (nom d’un camí) i `despres`
(accions posteriors). `{C}` dins d’una ordre o d’un visual es substitueix per l’identificador
real del commit C; a la locució no s’hi pot posar.

### Accions de preparació

| Acció | Efecte |
| --- | --- |
| `repositori: HelloGit` | Crea un repositori amb `main` i hi entra |
| `remot_nu: origin` | Crea un remot nu local (fa de GitHub) |
| `clona: carpeta`, `de: origin` | Clona un remot nu |
| `cd: carpeta`, `carpeta: carpeta` | Canvia de carpeta o en crea una |
| `fitxer: nom`, `contingut:` o `origen: exemples/...` | Escriu un fitxer |
| `git: ...` (amb `falla: true` opcional) | Executa una ordre de Git |
| `commit: C`, `missatge:` | Fa un commit i li dona el nom C |
| `etiqueta: C`, `ref:` | Dona el nom C a un commit existent |
| `servidor: [ordres]`, `remot:`, `crea:` | Canvi fet al remot per una altra persona o a la web |
| `sh: ...`, `esborra: nom` | Ordre de terminal o esborrar |

### Comprovacions (`comprova`)

`refs`, `head` (branca o `separat:C`), `status` (sortida exacta de `status --short`),
`programa` (text que ha de mostrar `python3 helloGit.py`), `treball` i `index` (contingut),
`treball_igual_a` i `index_igual_a` (contingut d’un fitxer d’exemples), `existeix`,
`no_existeix`, `pares`, `mateix_arbre`, `stash`, `remot`, `sortida` (fragments de la
sortida), `commits` (nombre de commits d’una ref) i `ignorat`. Afegiu `dir` per comprovar
una altra carpeta.

### Camins alternatius i condicionals

```yaml
camins:
  avorta:
    tipus: alternatiu           # o condicional
    titol: Alternativa          # etiqueta visible
    des_de: inici               # punt de partida; per defecte, on era el camí principal
    preparacio: [...]
```

Les etapes amb `cami: avorta` s’executen en una còpia separada. En tornar al camí
principal, l’estat es recupera tal com era.

## Repetició: `eines/repeticio.py`

Construeix el punt de partida, executa les etapes en l’ordre del vídeo i comprova
totes les afirmacions. Fa servir dates i autoria fixes (`Anna Puig`), de manera que
els identificadors són reproduïbles, i la configuració de Git en anglès (`LC_ALL=C`).
Desa a `execucio.json` la sortida de cada ordre i l’estat del repositori (graf,
branques, `HEAD`, estat breu i fitxers), que fan servir el compilador i els visuals.
Amb `--sense-desar` només comprova (és el que fa la integració contínua).

Les lliçons 1 i 2 parteixen d’una configuració neta (`configuracio_neta: true`) o d’una
carpeta sense repositori (`carpeta: .`). Les ordres de `gh` i les pantalles web són
`simulat` i les seves sortides, de mostra.

## Compilador: `motor/guions.py`

Converteix cada lliçó en escenes i passos: una escena per explicació i, per a cada ordre,
els passos acció → parts → execució → resultat. Revisa:

- termes anglesos dins de fragments catalans, identificadors sense accent;
- hashes, rutes, `~`, `__`, intervals de lletres, V1/V2, preguntes i marcadors sense substituir;
- pauses entre 1,5 i 4 s;
- opcions sense explicar la primera vegada que surten a la sèrie (les llargues, un cop per
  a tota la sèrie; les curtes, per a cada ordre) i `-m` abans del missatge;
- resum de tres idees i pràctica final.

Les lliçons 0 i 3 tenen vistes fetes a mida (`escenes:` amb `vista` per pas) i
`etiquetatge: explicit`: només el text entre `[[ ]]` es llegeix en anglès, perquè els
fragments coincideixin exactament amb l’àudio aprovat i se’n pugui reaprofitar la caché.

## Visuals

- Lliçons 0 i 3: [eines/visuals_introduccio.py](eines/visuals_introduccio.py) i
  [eines/visuals_primer_commit.py](eines/visuals_primer_commit.py).
- Resta: [eines/escenes.py](eines/escenes.py) dibuixa cada pas a partir de l’estat real
  (graf, branques, HEAD, estat breu, fitxer principal i terminal amb subratllat i sortida).
  Per revisar-los sense produir vídeo: `python Git/eines/escenes.py Git 09-merge`
  (full de contacte a `09-merge/build/`). Si una lliçó necessita una vista pròpia, es
  pot afegir un mòdul com els de les lliçons 0 i 3.

## Producció

[eines/render.py](eines/render.py) comprova que tot està al dia i crida
[motor/muntatge.py](../motor/muntatge.py):

1. Azure genera la veu de cada escena amb SSML explícit i marques de paraula.
2. Cada subratllat, execució i pausa s’ancora als temps reals de la locució.
3. Es dibuixen les animacions, es munten amb la capçalera i la veu, i es generen els SRT
   (amb cursiva per a l’anglès i sense format), la portada i `produccio.json`.
4. El vídeo final es desa a `Git/output/NN-nom.mp4` (camp `videos` de `serie.yaml`) i la
   resta de fitxers a `NN-nom/output/`. Després es verifica (còdecs, durades, subtítols
   fidels i silenci a les pauses).

La caché de veu (`audio/`) es reaprofita mentre el text i la configuració de cada escena
no canviïn. Les credencials es llegeixen de `.env` a l’arrel; mai no es desen als informes.

## Història

La veu anterior (Enric amb glossari fonètic), el generador anterior i els vídeos amb la
numeració antiga són a [arxiu/](arxiu/README.md). L’elecció d’Andrew amb SSML explícit
i les mostres aprovades són a [veu/andrew](veu/andrew/README.md).
