# Lliçó 1 · Configuració inicial: identitat, branca i editor

**Sèrie:** Píndoles de Git · **Capçalera:** CONFIGURACIÓ — Prepara l’ordinador per treballar amb Git  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Primera lliçó. Configuració inicial.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a comprovar la versió de *Git* i deixar configurades l’autoria, la branca inicial i l’editor. *(pausa 2.5 s)*

Partim d’un ordinador amb *Git* instal·lat i una terminal oberta. Encara no hem configurat res. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Per què cal configurar Git

Cada *commit* guarda qui l’ha fet i quan. Per això, abans del primer, cal indicar el nom i el correu. *(pausa 3 s)*

També triarem el nom de la branca inicial i l’editor que obrirà *Git* quan ens demani un text llarg. *(pausa 3 s)*

**Visual:** Targeta d’un commit amb els camps AUTORIA, DATA i MISSATGE ressaltats per torns.

## Terminal · `git --version`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git --version` | Primer comprovem quina versió tenim instal·lada. | 2.5 s |
| `--version` | Doble guionet *version* demana el número de versió; no canvia res. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La terminal mostra el número de versió. Les lliçons fan servir ordres com *git switch* i *git restore*, que necessiten la versió dos punt vint-i-tres o una de posterior. *(pausa 3.5 s)*

Sortida real:

```text
git version 2.55.0
```

**Visual:** Terminal amb la versió real; etiqueta MÍNIM 2.23 al costat.

## Missatges en català o en anglès

Si l’ordinador està configurat en català, *Git* pot respondre en català. Les ordres són exactament les mateixes; als vídeos, les respostes surten en anglès. *(pausa 3 s)*

**Visual:** La mateixa sortida en dos panells, ANGLÈS i CATALÀ, amb l’ordre idèntica a sobre.

## Terminal · `git config --global user.name "Ermessenda Carcassona"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git config` | Amb *git config* desem una opció de configuració. | 2.5 s |
| `--global` | Doble guionet *global* desa l’opció per a tots els repositoris del nostre usuari en aquest ordinador. | 2.5 s |
| `user.name` | És la clau que guarda el nom de l’autoria. | 2.5 s |
| `"Ermessenda Carcassona"` | És el valor. Escriu-hi el teu nom; les cometes el mantenen com un sol argument. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** L’ordre no mostra res quan funciona. A partir d’ara, els *commits* d’aquest usuari portaran aquest nom. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Fitxer de configuració global amb la línia name = Ermessenda Carcassona afegida.

## Terminal · `git config --global user.email "ermessenda@example.com"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git config` | Ara desem el correu de l’autoria. | 2.5 s |
| `user.email` | És la clau del correu que acompanya cada *commit*. | 2.5 s |
| `"ermessenda@example.com"` | És un correu d’exemple. Fes servir el teu, o l’adreça privada que ofereix *GitHub* al teu compte. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El correu queda desat al mateix fitxer de configuració. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** La línia email = ermessenda@example.com s’afegeix sota el nom.

## Un ordinador compartit

En un ordinador de l’aula, compartit amb altres persones, no fem servir doble guionet *global*. Executem la mateixa ordre dins del nostre repositori i l’autoria només s’hi aplica allà. *(pausa 3 s)*

**Visual:** Dues columnes: ORDINADOR PROPI · git config --global user.name ... / ORDINADOR COMPARTIT · dins del repositori, git config user.name ... sense --global.

## Terminal · `git config --global init.defaultBranch main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git config` | Triem el nom de la primera branca dels repositoris nous. | 2.5 s |
| `init.defaultBranch` | Aquesta clau indica el nom de la branca inicial quan creem un repositori. | 2.5 s |
| `main` | És el nom que fan servir les lliçons i també *GitHub*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Els repositoris que creem a partir d’ara començaran a la branca *main*. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Línia defaultBranch = main a la secció init del fitxer.

## Un editor que sapiguem tancar

Algunes ordres obren un editor perquè hi escrivim un missatge. Si no en triem cap, sovint s’obre un editor de terminal difícil de tancar. Triarem *Visual Studio Code*. *(pausa 3 s)*

**Visual:** Editor de terminal amb el cursor parpellejant i, al costat, Visual Studio Code amb una pestanya COMMIT_EDITMSG.

## Terminal · `git config --global core.editor "code --wait"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git config` | Configurem l’editor. | 2.5 s |
| `core.editor` | És la clau de l’editor que obrirà *Git*. | 2.5 s |
| `"code --wait"` | Obre *Visual Studio Code* i espera que tanquem la pestanya abans de continuar. Cal que l’ordre code funcioni a la terminal; si fas servir un altre editor, posa-hi la seva ordre. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Quan *Git* necessiti un missatge, obrirà una pestanya de l’editor. Desem, tanquem la pestanya i l’ordre continua. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Línia editor = code --wait. Animació · s’obre una pestanya, es desa, es tanca i la terminal continua.

## Terminal · `git config --global --list`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git config` | Revisem tota la configuració global. | 2.5 s |
| `--list` | Doble guionet *list* mostra totes les opcions desades. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Hi veiem les quatre opcions que hem configurat. Si n’hi ha alguna d’equivocada, la tornem a escriure amb el valor correcte. *(pausa 3.5 s)*

Sortida real:

```text
user.name=Ermessenda Carcassona
user.email=ermessenda@example.com
init.defaultbranch=main
core.editor=code --wait
```

**Visual:** Sortida real; ressaltar una línia cada vegada.

## Resum final

*git config* desa opcions; doble guionet *global* les aplica a tots els repositoris de l’usuari. *(pausa 2.5 s)*

Nom i correu identifiquen l’autoria de cada *commit*. *(pausa 2.5 s)*

La branca inicial i l’editor eviten sorpreses a les lliçons següents. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Comprova la versió de *Git*, configura el teu nom, el teu correu, la branca inicial i l’editor, i revisa el resultat amb la llista de configuració. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
