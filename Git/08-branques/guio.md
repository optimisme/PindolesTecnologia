# Lliçó 8 · Branques: prova una idea sense tocar main

**Sèrie:** Píndoles de Git · **Capçalera:** BRANQUES — Prova una idea sense tocar main  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/08-branques.sh`](../practiques/08-branques.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vuitena lliçó. Branques.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a crear una branca, confirmar-hi una prova i tornar a les dues versions. *(pausa 2.5 s)*

Partim d’un projecte amb dos *commits* a *main*. El programa mostra la salutació original i no hi ha cap canvi pendent. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Una idea nova, una línia de treball pròpia

Volem provar una salutació personalitzada sense perdre la versió que ja funciona a *main*. Una branca ens permet continuar aquesta prova amb *commits* propis. *(pausa 3 s)*

**Visual:** Editor amb print("Hello Git!") i, al costat, la proposta encara no aplicada print("Hola, Anna!").

## Una branca és una etiqueta

Una branca és una etiqueta que apunta a un *commit*. Crear-ne una no copia els fitxers ni crea cap *commit*. Dues etiquetes poden apuntar al mateix lloc. *(pausa 3 s)*

**Visual:** Graf amb A i B; etiqueta main a B. Afegir l’etiqueta salutacio a B sense crear cap node.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** No surt cap línia, perquè no hi ha canvis pendents. Això no vol dir que el programa funcioni; només que no hi ha res per confirmar. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git switch -c salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* seleccionem la branca on treballarem. | 2.5 s |
| `-c` | El guionet ce crea una branca nova i hi canvia. | 2.5 s |
| `salutacio` | És el nom de la branca nova. Comença al *commit* actual. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La branca activa ara és salutació. *main* continua al mateix *commit*, i tampoc s’ha creat cap *commit* nou. *(pausa 3.5 s)*

Sortida real:

```text
Switched to a new branch 'salutacio'
```

**Visual:** Etiquetes main i salutacio a B; l’indicador de branca activa passa a salutacio.

## Editem la salutació

Canviem la salutació i desem el fitxer. De moment, el canvi només és a la carpeta de treball. *(pausa 3 s)*

**Visual:** Editor amb print("Hola, Anna!") desat.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Surt la salutació personalitzada. El canvi encara no està preparat ni confirmat. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Anna!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació nova queda preparada. Encara no hi ha cap versió nova a l’historial. *(pausa 3.5 s)*

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
[salutacio ef335f4] Personalitza la salutacio
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Nou node C després de B; l’etiqueta salutacio avança fins a C i main es queda a B.

## Terminal · `git switch main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `main` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Tornem a veure la salutació original. El *commit* de la prova continua guardat a la branca salutació. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'main'
```

**Visual:** L’indicador de branca activa torna a main; l’editor mostra print("Hello Git!"). C continua al graf.

## Terminal · `git switch salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `salutacio` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Recuperem la salutació personalitzada. Canviar de branca no ha esborrat cap de les dues versions. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'salutacio'
```

**Visual:** L’indicador torna a salutacio i l’editor mostra print("Hola, Anna!").

## La branca activa

*HEAD* indica on estem treballant; en aquest exemple segueix la branca activa. El nom *main* és només una convenció: no garanteix que el programa funcioni. *(pausa 3 s)*

**Visual:** HEAD unit a salutacio; main quieta a B. El nom de la branca activa també es veu a la terminal.

## Resum final

Crear una branca afegeix una etiqueta; no crea cap *commit*. *(pausa 2.5 s)*

Un *commit* fa avançar només la branca activa. *(pausa 2.5 s)*

Canviar de branca recupera la seva versió; integrar-la a *main* serà un pas posterior. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques sense canvis pendents, crea una branca de prova, confirma-hi una salutació diferent i alterna les dues branques per comparar el fitxer. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
