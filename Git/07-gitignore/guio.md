# Lliçó 7 · Gitignore: deixa fora els fitxers generats

**Sèrie:** Píndoles de Git · **Capçalera:** GITIGNORE — Deixa fora els fitxers generats  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/07-gitignore.sh`](../practiques/07-gitignore.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Setena lliçó. *Gitignore*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a ignorar els fitxers que genera el programa i distingir-los dels que *Git* ja seguia. *(pausa 2.5 s)*

El programa fa servir un segon fitxer amb les salutacions i deixa un registre de cada execució. Fa temps, també vam confirmar per error un registre antic. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Codi i fitxers generats

Volem versionar el codi. Els fitxers que crea el programa quan s’executa, com els registres o la memòria cau de *Python*, no han d’entrar als *commits*. *(pausa 3 s)*

**Visual:** Targetes helloGit.py i salutacions.py marcades CODI; app.log marcat REGISTRE ANTIC, JA SEGUIT.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El programa funciona. En executar-lo, ha creat el registre d’execució i una carpeta de memòria cau, perquè importa el fitxer de salutacions. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Anna!
```

**Visual:** Apareixen debug.log i la carpeta __pycache__/ a l’explorador de fitxers.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El registre nou i la carpeta de memòria cau apareixen amb dos interrogants, com a fitxers no seguits. *(pausa 3.5 s)*

Sortida real:

```text
?? __pycache__/
?? debug.log
```

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Escrivim les regles

Creem el fitxer punt *gitignore* a l’arrel del projecte, amb una regla per línia. Asterisc punt *log* selecciona tots els noms que acaben en punt *log*. *(pausa 3 s)*

La segona regla acaba amb una barra i selecciona la carpeta de memòria cau. Aquest fitxer de regles sí que el confirmarem, perquè tothom faci servir els mateixos criteris. *(pausa 3 s)*

**Visual:** Editor .gitignore amb dues línies literals, *.log i __pycache__/. Ressaltar primer l’asterisc i després la barra final.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El registre nou i la memòria cau ja no hi surten. Només hi apareix el fitxer de regles, perquè encara és nou. *(pausa 3.5 s)*

Sortida real:

```text
?? .gitignore
```

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git check-ignore -v debug.log`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git check-ignore` | *git check-ignore* explica per què s’ignora un fitxer. | 2.5 s |
| `-v` | El guionet ve demana el detall de la regla que hi coincideix. | 2.5 s |
| `debug.log` | És el registre que volem investigar. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La sortida indica el fitxer de regles, el número de línia i el patró que coincideix amb el registre. *(pausa 3.5 s)*

Sortida real:

```text
.gitignore:1:*.log	debug.log
```

**Visual:** Separar a la sortida real .gitignore, el número de línia, el patró *.log i el nom del fitxer.

## Una regla no deixa de seguir un fitxer

El registre antic també acaba en punt *log*, però ja formava part d’un *commit*. Les regles només afecten els fitxers que *Git* encara no seguia. *(pausa 3 s)*

**Visual:** app.log amb l’etiqueta SEGUIT i debug.log amb l’etiqueta IGNORAT.

## Terminal · `git ls-files`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git ls-files` | Llistem els fitxers que *Git* segueix. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El registre antic continua a la llista, al costat del codi. *(pausa 3.5 s)*

Sortida real:

```text
app.log
helloGit.py
salutacions.py
```

**Visual:** Sortida real; ressaltar app.log.

## Terminal · `git rm --cached app.log`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git rm` | Decidim deixar de seguir el registre antic, però conservar-lo a l’ordinador. | 2.5 s |
| `--cached` | Doble guionet *cached* el retira només del repositori; el fitxer continua al disc. | 2.5 s |
| `app.log` | És el registre que ja estava seguit. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Queda preparada la retirada del registre. Com que ara coincideix amb una regla, el fitxer local ja no apareix com a nou. *(pausa 3.5 s)*

Sortida real:

```text
rm 'app.log'
```

**Visual:** Retirar app.log del panell PREPARACIÓ amb una D; mantenir-lo a la carpeta de treball, sense animació d’esborrar.

## Terminal · `git add .gitignore`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Preparem també les regles. La retirada del registre ja era preparada. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Ignora els fitxers generats"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Ignora els fitxers generats. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* guarda les regles i la retirada del registre. El fitxer local continua existint i ara queda ignorat. *(pausa 3.5 s)*

Sortida real:

```text
[main 20e78ee] Ignora els fitxers generats
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 .gitignore
 delete mode 100644 app.log
```

**Visual:** Crear el node nou només en executar.

## Resum final

Punt *gitignore* filtra els fitxers no seguits que coincideixen amb les regles. *(pausa 2.5 s)*

El fitxer de regles es confirma perquè tothom en comparteixi els criteris. *(pausa 2.5 s)*

Deixar de seguir un fitxer és una decisió a part; doble guionet *cached* el conserva al disc. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un projecte de pràctiques, genera un registre executant el programa i crea una regla per ignorar-lo. Comprova la regla amb *git check-ignore* i compara-ho amb un fitxer que ja estigui seguit. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
