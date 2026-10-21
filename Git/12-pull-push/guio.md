# Lliçó 12 · Pull i push: dues còpies al dia

**Sèrie:** Píndoles de Git · **Capçalera:** PULL I PUSH — Classe i casa, sempre al dia  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/12-pull-push.sh`](../practiques/12-pull-push.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Dotzena lliçó. *Pull* i *push*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a mantenir al dia dues còpies del projecte, treballant per torns a classe i a casa. *(pausa 2.5 s)*

A classe hem publicat un *commit* nou. A casa ja tenim el projecte clonat, però encara amb la versió anterior. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## La còpia de casa està endarrerida

La còpia de casa encara té la versió anterior. Abans de tocar res, la posarem al dia amb la feina publicada. *(pausa 3 s)*

**Visual:** Casa a A; servidor i classe a B. Ruta CASA visible a la terminal.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** No hi ha canvis pendents a casa. Podem actualitzar sense barrejar feines. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git pull --ff-only`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git pull` | *git pull* descarrega les novetats del servidor i les incorpora a la branca. | 2.5 s |
| `--ff-only` | Només acceptem avançar directament. Si les dues còpies han divergit, l’ordre s’atura. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Casa arriba al *commit* de classe i el fitxer s’actualitza. *(pausa 3.5 s)*

Sortida real:

```text
Updating 17875ff..57f0305
Fast-forward
 helloGit.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
From ~/origin
   17875ff..57f0305  main       -> origin/main
```

**Visual:** Casa avança d’A a B; l’editor mostra la versió nova.

## Continuem des de casa

Editem i desem una millora a casa. Aquesta vegada, el *commit* nou naixerà en aquest ordinador. *(pausa 3 s)*

**Visual:** Editor i ruta CASA. Classe continua a B.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La millora de casa queda preparada. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Millora des de casa"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Millora des de casa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* nou és a casa. El servidor i classe encara no el tenen. *(pausa 3.5 s)*

Sortida real:

```text
[main d300f4a] Millora des de casa
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Crear el node nou només en executar.

## Terminal · `git push`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | Amb *git push* enviem els *commits* de la branca al remot. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El servidor ja té la millora de casa. Falta actualitzar classe. *(pausa 3.5 s)*

Sortida real:

```text
To ~/origin.git
   57f0305..d300f4a  main -> main
```

**Visual:** Conservar el mateix identificador al local i al remot. La fletxa envia commits; no envia edicions sense confirmar.

## Tornem a classe

A classe encara tenim la versió anterior. Abans de començar a editar, comprovem l’estat i actualitzem. *(pausa 3 s)*

**Visual:** Canvi clar de context a la ruta CLASSE. No reutilitzar la terminal de casa.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** No hi ha canvis pendents a classe. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git pull --ff-only`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git pull` | Descarreguem i incorporem el *commit* publicat des de casa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Classe arriba a la mateixa versió. Les tres còpies comparteixen el mateix *commit*. *(pausa 3.5 s)*

Sortida real:

```text
Updating 57f0305..d300f4a
Fast-forward
 helloGit.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
From ~/origin
   57f0305..d300f4a  main       -> origin/main
```

**Visual:** Classe passa de B a C; servidor i casa ja eren a C.

## Si oblidem actualitzar

> **Si les dues còpies han avançat.** Parteix del seu propi punt; no s’encadena amb el camí principal.

Un altre cas. A casa fem un *commit* sense haver actualitzat abans. Ara casa i servidor tenen *commits* diferents després de la mateixa versió. *(pausa 3 s)*

**Visual:** Separador UN ALTRE CAS. Graf amb A; B al servidor i X a casa, tots dos fills d’A.

## Terminal · `git pull --ff-only`

> **Si les dues còpies han avançat.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git pull` | Provem d’actualitzar igual que abans. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** L’ordre s’atura i no canvia res: no es pot avançar directament. Caldrà integrar les dues històries, per exemple amb una fusió com la de la lliçó de *merge*. *(pausa 3.5 s)*

Sortida real:

```text
From ~/origin
   17875ff..57f0305  main       -> origin/main
hint: Diverging branches can't be fast-forwarded, you need to either:
hint:
hint: 	git merge --no-ff
hint:
hint: or:
hint:
hint: 	git rebase
hint:
hint: Disable this message with "git config set advice.diverging false"
fatal: Not possible to fast-forward, aborting.
```

**Visual:** Sortida real amb el missatge d’error ressaltat; el graf no canvia.

## Resum final

Abans d’editar, actualitzem amb *git pull*. *(pausa 2.5 s)*

Després de confirmar, publiquem amb *git push*. *(pausa 2.5 s)*

Doble guionet *ff-only* atura l’actualització si les còpies han divergit. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Amb dos clons de pràctiques, confirma i publica en un, actualitza l’altre amb *git pull* i repeteix-ho en sentit contrari. Comprova que tots dos acaben amb el mateix identificador. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
