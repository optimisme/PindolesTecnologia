# Lliçó 8 · Gitignore: deixa fora els fitxers generats

**Sèrie:** Píndoles de Git · **Capçalera:** GITIGNORE — Deixa fora els fitxers generats  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/08-gitignore.sh`](../practiques/08-gitignore.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vuitena lliçó. *Gitignore*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a escriure un fitxer de regles per ignorar fitxers generats i secrets, i distingir-los dels que *Git* ja seguia. *(pausa 2.5 s)*

El programa fa servir un segon fitxer amb les salutacions i deixa un registre de cada execució. També tenim un fitxer amb una clau privada i un registre de mostra per a la documentació. Fa temps, vam confirmar per error un registre antic. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El programa funciona. En executar-lo, ha creat el registre d’execució i una carpeta de memòria cau, perquè importa el fitxer de salutacions. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Ermessenda!
```

**Visual:** Apareixen debug.log i la carpeta __pycache__/ a l’explorador de fitxers.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Tot apareix com a no seguit: la clau, la memòria cau i els registres. Un *git add* punt els afegiria tots, també la clau, i qualsevol persona que veiés el repositori la podria llegir. *(pausa 3.5 s)*

Sortida real:

```text
?? .env
?? __pycache__/
?? debug.log
?? mostra.log
```

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Un fitxer de regles, línia a línia

Creem el fitxer punt *gitignore* a l’arrel del projecte, amb una regla per línia. La primera comença amb el coixinet: és un comentari. *(pausa 3 s)*

Asterisc punt *log* ignora tots els fitxers que acaben en punt *log*, a qualsevol carpeta. *(pausa 3 s)*

L’exclamació fa una excepció: el registre de mostra sí que es compartirà. Una excepció no pot entrar dins d’una carpeta que s’ignora sencera. *(pausa 3 s)*

La barra final vol dir que la regla només s’aplica a carpetes, a qualsevol nivell. *Python* crea una carpeta de memòria cau dins de cada carpeta de codi. *(pausa 3 s)*

Una barra al davant limita la regla a l’arrel del projecte. *(pausa 3 s)*

L’última regla deixa fora el fitxer de la clau. Aquest fitxer de regles sí que el confirmarem, perquè tothom faci servir els mateixos criteris. *GitHub* ofereix plantilles per a cada llenguatge. *(pausa 3 s)*

**Visual:** Editor .gitignore amb les set línies literals. Ressaltar una línia per frase, en ordre: comentari, *.log, !mostra.log, __pycache__/, /build/ i .env.

## Terminal · `git status --short --ignored`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Comprovem l’efecte de les regles amb *git status*. | 2.5 s |
| `--ignored` | Doble guionet *ignored* també mostra els fitxers ignorats, marcats amb dues exclamacions. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El fitxer de regles i el registre de mostra surten com a nous: l’excepció funciona. La clau, la memòria cau i el registre d’execució surten amb dues exclamacions. Són al disc, però *Git* no els afegirà. *(pausa 3.5 s)*

Sortida real:

```text
?? .gitignore
?? mostra.log
!! .env
!! __pycache__/
!! debug.log
```

**Visual:** Sortida real; ressaltar primer les dues línies amb interrogants i després les tres amb exclamacions.

## Terminal · `git check-ignore -v debug.log`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git check-ignore` | Quan un fitxer no es comporta com esperem, *git check-ignore* explica per què s’ignora. | 2.5 s |
| `-v` | El guionet ve demana el detall de la regla que hi coincideix. | 2.5 s |
| `debug.log` | És el registre que volem investigar. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La sortida indica el fitxer de regles, el número de línia i el patró que coincideix amb el registre. *(pausa 3.5 s)*

Sortida real:

```text
.gitignore:2:*.log	debug.log
```

**Visual:** Separar a la sortida real .gitignore, el número de línia, el patró *.log i el nom del fitxer.

## Terminal · `git rm --cached app.log`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git rm` | El registre antic també acaba en punt *log*, però no ha sortit a la llista: ja formava part d’un *commit*, i les regles només afecten els fitxers que *Git* encara no seguia. Decidim deixar de seguir-lo, però conservar-lo a l’ordinador. | 2.5 s |
| `--cached` | Doble guionet *cached* el retira només del repositori; el fitxer continua al disc. | 2.5 s |
| `app.log` | És el registre que ja estava seguit. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Queda preparada la retirada del registre, i ara la regla ja l’ignora. Dos avisos. Quan una altra persona baixi aquest *commit*, *Git* esborrarà el fitxer de la seva carpeta. I els *commits* antics el continuen guardant: una clau que ja s’ha publicat s’ha de canviar. *(pausa 3.5 s)*

Sortida real:

```text
rm 'app.log'
```

**Visual:** Retirar app.log del panell PREPARACIÓ amb una D; mantenir-lo a la carpeta de treball, sense animació d’esborrar.

## Terminal · `git add .gitignore mostra.log`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer de regles i el registre de mostra amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Les regles i la mostra queden preparades. La retirada del registre antic ja ho era. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar .gitignore i mostra.log a la preparació.

## Terminal · `git commit -m "Ignora els fitxers generats i els secrets"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Ignora els fitxers generats i els secrets. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* guarda les regles, la mostra i la retirada del registre. El registre antic continua al disc i ara queda ignorat, igual que la clau. *(pausa 3.5 s)*

Sortida real:

```text
[main f15e457] Ignora els fitxers generats i els secrets
 3 files changed, 9 insertions(+), 1 deletion(-)
 create mode 100644 .gitignore
 delete mode 100644 app.log
 create mode 100644 mostra.log
```

**Visual:** Crear el node nou només en executar.

## Resum final

Punt *gitignore* té una regla per línia; l’exclamació hi fa excepcions. *(pausa 2.5 s)*

Les claus no han d’arribar mai a un *commit*; si s’han publicat, cal canviar-les. *(pausa 2.5 s)*

Les regles no afecten fitxers ja seguits; doble guionet *cached* els deixa de seguir i els conserva al disc. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un projecte de pràctiques, genera un registre executant el programa i escriu un punt *gitignore* amb una regla i una excepció. Comprova-ho amb *git status* doble guionet *ignored* i amb *git check-ignore*. Els fitxers propis de l’editor es poden ignorar només al teu ordinador, amb el fitxer *exclude* de la carpeta punt *git*. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
