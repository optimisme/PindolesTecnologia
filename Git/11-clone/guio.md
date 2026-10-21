# Lliçó 11 · Clone: el projecte en un altre ordinador

**Sèrie:** Píndoles de Git · **Capçalera:** CLONE — El projecte en un altre ordinador  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/11-clone.sh`](../practiques/11-clone.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Onzena lliçó. *Clone*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a publicar un canvi des de classe i obtenir el projecte complet en un altre ordinador. *(pausa 2.5 s)*

A classe tenim el projecte publicat a *GitHub*. A casa encara no en tenim cap còpia. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Cada ordinador té la seva còpia

L’ordinador de classe i el de casa tenen repositoris independents. *GitHub* és el punt de trobada. Fer un *commit* en un ordinador no actualitza els altres. *(pausa 3 s)*

**Visual:** Classe i casa amb el servidor al mig. Les fletxes només apareixen quan s’executa una ordre.

## Acabem el canvi a classe

Editem la salutació i desem. Abans de marxar, la confirmarem i la publicarem. *(pausa 3 s)*

**Visual:** Editor de CLASSE amb print("Hola des de classe!").

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El canvi de classe queda preparat. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Practica de classe"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Pràctica de classe. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* nou existeix a classe. El servidor encara no el té. *(pausa 3.5 s)*

Sortida real:

```text
[main efdd511] Practica de classe
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Crear el node nou només en executar.

## Terminal · `git push`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | Amb *git push* enviem els *commits* de la branca al remot. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El servidor ja té el *commit* de classe. Ara és el punt de trobada amb la versió nova. *(pausa 3.5 s)*

Sortida real:

```text
To ~/origin.git
   17875ff..efdd511  main -> main
```

**Visual:** Conservar el mateix identificador al local i al remot. La fletxa envia commits; no envia edicions sense confirmar.

## A casa, el primer cop

A casa encara no tenim el projecte. Per obtenir-lo, el clonem una sola vegada; després ja treballarem sempre en aquella carpeta. *(pausa 3 s)*

**Visual:** Canvi clar de context a la ruta CASA. Panell CAP CÒPIA LOCAL.

## Terminal · `git clone <URL-del-repositori> HelloGit`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git clone` | *git clone* crea una còpia local amb tots els fitxers i tot l’historial. | 2.5 s |
| `<URL-del-repositori>` | Substituïm aquest marcador per l’adreça del repositori, sense els signes de menor i major. | 2.5 s |
| `HelloGit` | És el nom de la carpeta que es crearà. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La carpeta nova ja conté el projecte i el remot *origin* queda configurat. *(pausa 3.5 s)*

Sortida de mostra:

```text
Cloning into 'HelloGit'...
```

**Visual:** Animar la creació de la carpeta HelloGit a CASA i la còpia dels commits A i B.

## Terminal · `cd HelloGit`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `cd` | Entrem a la carpeta del projecte. | 2.5 s |
| `HelloGit` | És la carpeta creada pel clonatge. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La terminal de casa és dins del projecte. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Ruta CASA · ~/HelloGit a la terminal.

## Terminal · `git log --oneline`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Comprovem l’historial que hem rebut. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Hi ha els dos *commits*, també el que vam fer a classe. Els identificadors són els mateixos als dos ordinadors. *(pausa 3.5 s)*

Sortida real:

```text
efdd511 Practica de classe
17875ff Afegeix la salutacio inicial
```

**Visual:** Sortida real al costat del graf de classe; ressaltar el mateix identificador als dos llocs.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** A casa ja tenim la versió de classe i podem continuar la feina. *(pausa 3.5 s)*

Sortida real:

```text
Hola des de classe!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Resum final

Cada ordinador té un repositori propi; el servidor és el punt de trobada. *(pausa 2.5 s)*

*git push* envia els *commits* confirmats al servidor. *(pausa 2.5 s)*

*git clone* es fa un sol cop per ordinador i porta tot l’historial. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Publica un *commit* d’un repositori de pràctiques i clona’l en una altra carpeta, com si fos un altre ordinador. Compara l’historial de les dues còpies. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
