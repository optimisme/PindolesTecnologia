# Lliçó 10 · Branques: prova idees sense tocar main

**Sèrie:** Píndoles de Git · **Capçalera:** BRANQUES — Prova idees sense tocar main  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/10-branques.sh`](../practiques/10-branques.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Desena lliçó. Branques.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a crear dues branques des de *main*, confirmar-hi una idea a cadascuna i comparar les tres versions. *(pausa 2.5 s)*

Partim d’un projecte amb dos *commits* a *main*. El programa saluda i dona la benvinguda, i no hi ha cap canvi pendent. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Dues idees, dues línies de treball

Tenim dues idees per al programa: saludar per nom i afegir un comiat. Volem provar-les per separat, sense tocar la versió que funciona a *main*. Cada idea tindrà la seva branca, amb *commits* propis. *(pausa 3 s)*

**Visual:** Graf amb A i B a main; dues fletxes discontínues que surten de B cap a salutacio i comiat.

## Una branca és una etiqueta

Una branca és una etiqueta que apunta a un *commit*. Crear-ne una no copia els fitxers ni crea cap *commit*. Diverses etiquetes poden apuntar al mateix lloc. *(pausa 3 s)*

**Visual:** Graf amb A i B; etiqueta main a B. Afegir l’etiqueta salutacio a B sense crear cap node.

## Terminal · `git switch -c salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* seleccionem la branca on treballarem. | 2.5 s |
| `-c` | El guionet ce crea una branca nova i hi canvia. | 2.5 s |
| `salutacio` | És el nom de la branca nova. Comença al *commit* actual. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La branca activa ara és salutació. *main* continua al mateix *commit*, i no s’ha creat cap *commit* nou. *(pausa 3.5 s)*

Sortida real:

```text
Switched to a new branch 'salutacio'
```

**Visual:** Etiquetes main i salutacio a B; l’indicador de branca activa passa a salutacio.

## Primera idea, la salutació

Canviem la primera línia per saludar per nom i desem el fitxer. *(pausa 3 s)*

**Visual:** Editor amb la primera línia canviada a print("Hola, Ermessenda!").

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació nova queda preparada. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Personalitza la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Personalitza la salutació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* nou fa avançar salutació. *main* continua apuntant a la versió original. *(pausa 3.5 s)*

Sortida real:

```text
[salutacio 59ecb8b] Personalitza la salutacio
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Nou node C després de B; l’etiqueta salutacio avança fins a C i main es queda a B.

## Terminal · `git switch main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `main` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Tornem a la versió original. Ho fem abans de crear la segona branca, perquè una branca nova comença al *commit* on som: així el comiat no portarà la salutació nova. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'main'
```

**Visual:** L’indicador de branca activa torna a main; l’editor mostra print("Hello Git!"). C continua al graf.

## Terminal · `git switch -c comiat`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* seleccionem la branca on treballarem. | 2.5 s |
| `-c` | El guionet ce crea una branca nova i hi canvia. | 2.5 s |
| `comiat` | És el nom de la branca nova. Comença al *commit* actual. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara hi ha tres etiquetes. *main* i comiat apunten a la versió original; salutació, al seu *commit*. *(pausa 3.5 s)*

Sortida real:

```text
Switched to a new branch 'comiat'
```

**Visual:** Etiqueta comiat nova a B, al costat de main. HEAD passa a comiat.

## Segona idea, el comiat

Afegim una línia de comiat al final del fitxer i el desem. *(pausa 3 s)*

**Visual:** Editor amb la línia print("Fins aviat!") afegida al final.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El comiat queda preparat. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Afegeix un comiat"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Afegeix un comiat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* nou fa avançar comiat. Des de la versió original surten ara dos camins, un per a cada idea. *(pausa 3.5 s)*

Sortida real:

```text
[comiat 2695aaa] Afegeix un comiat
 1 file changed, 1 insertion(+)
```

**Visual:** Nou node D després de B, en una línia diferent de C. Etiqueta comiat a D; main es queda a B.

## Terminal · `git log --oneline --graph --all --decorate`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | La terminal també pot dibuixar l’historial de totes les branques. | 2.5 s |
| `--graph` | Doble guionet *graph* dibuixa les línies que uneixen els *commits*. | 2.5 s |
| `--all` | Doble guionet *all* mostra totes les branques, no només l’activa. | 2.5 s |
| `--decorate` | Doble guionet *decorate* escriu el nom de cada branca al costat del seu *commit*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Les línies mostren la bifurcació: els dos *commits* nous surten del mateix *commit* de *main*, cadascun a la seva branca. *(pausa 3.5 s)*

Sortida real:

```text
* 2695aaa (HEAD -> comiat) Afegeix un comiat
| * 59ecb8b (salutacio) Personalitza la salutacio
|/  
* 1c65395 (main) Afegeix una exclamacio
* 34631ab Afegeix la salutacio inicial
```

**Visual:** Sortida real al costat del graf; ressaltar els noms de les tres branques.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** A la branca del comiat, el programa saluda en anglès i s’acomiada. *(pausa 3.5 s)*

Sortida real:

```text
Hello Git!
Benvinguda al projecte.
Fins aviat!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git switch salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `salutacio` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El fitxer canvia sol a la versió d’aquesta branca. No hi ha comiat, perquè és en una altra branca. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'salutacio'
```

**Visual:** L’indicador passa a salutacio i l’editor mostra la salutació nova, sense comiat.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara surt la salutació personalitzada. Cada branca conserva la seva versió del codi. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Ermessenda!
Benvinguda al projecte.
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## La branca activa

*HEAD* indica on estem treballant; en aquest exemple segueix la branca activa. Canviar de branca no esborra res: les tres versions continuen guardades, i el nom *main* no garanteix que el programa funcioni. *(pausa 3 s)*

**Visual:** HEAD unit a salutacio; main quieta a B i comiat a D. El nom de la branca activa també es veu a la terminal.

## Resum final

Crear una branca afegeix una etiqueta al *commit* on som; no crea cap *commit*. *(pausa 2.5 s)*

Un *commit* fa avançar només la branca activa; cada branca guarda la seva versió. *(pausa 2.5 s)*

Canviar de branca recupera la seva versió; ajuntar-les serà la lliçó següent. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques sense canvis pendents, crea dues branques des de *main*, confirma un canvi diferent a cadascuna i alterna-les per comparar el fitxer i la sortida del programa. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
