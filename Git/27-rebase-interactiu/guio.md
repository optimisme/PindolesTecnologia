# Lliçó 27 · Rebase interactiu: agrupa commits abans de publicar

**Sèrie:** Píndoles de Git · **Capçalera:** REBASE INTERACTIU — Agrupa commits abans de publicar  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/27-rebase-interactiu.sh`](../practiques/27-rebase-interactiu.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-setena lliçó. *Rebase* interactiu.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a agrupar tres *commits* relacionats que encara no hem publicat, conservant el contingut final. *(pausa 2.5 s)*

A la branca salutació hi ha tres *commits* petits sobre la mateixa millora: la salutació, una correcció de puntuació i unes notes. Encara no els hem publicat. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Una millora explicada en tres commits

Els tres *commits* formen una sola millora. Abans de publicar-los, els agruparem perquè l’historial expliqui el resultat d’una vegada. *(pausa 3 s)*

**Visual:** Graf A, B, C, D i E; etiqueta NO PUBLICATS sobre els tres últims; main a B.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** No tenim canvis pendents. Ens quedem l’identificador de l’últim *commit* per comparar-lo al final. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git log -3 --oneline`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Revisem els tres *commits* que volem agrupar. | 2.5 s |
| `-3` | Limita la llista als tres últims *commits*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Són propis, relacionats i encara no publicats. Fixem-nos que surten del més recent al més antic. *(pausa 3.5 s)*

Sortida real:

```text
0d33d2d Documenta la salutacio
a9e2f78 Corregeix la puntuacio
f448d88 Personalitza la salutacio
```

**Visual:** Sortida real; distingir aquest ordre del de la llista que obrirà l’editor.

## Terminal · `git rebase -i HEAD~3`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git rebase` | Obrim un *rebase* interactiu d’aquest tram. | 2.5 s |
| `-i` | El guionet i obre una llista d’operacions que podem editar. | 2.5 s |
| `HEAD~3` | La base és tres *commits* enrere. La llista inclou els tres *commits* posteriors. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** S’obre l’editor amb la llista, del *commit* més antic al més recent. Ara hi triarem les operacions. *(pausa 3.5 s)*

Sortida real:

```text
[detached HEAD 15b9ac1] Personalitza la salutacio i documenta el canvi
 Date: Tue Oct 20 12:08:00 2026 +0200
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 notes.md
Rebasing (2/3)
Rebasing (3/3)
Successfully rebased and updated refs/heads/salutacio.
```

**Visual:** Editor amb pick C, pick D i pick E, amb els identificadors reals. No representar encara el resultat.

## Triem les operacions

Deixem *pick* al primer *commit*. Als altres dos, canviem la paraula per *squash*, que els ajunta amb l’anterior. *(pausa 3.5 s)*

Desem i tanquem la pestanya de la llista. Fins que no la tanquem, *Git* no continua. *(pausa 3.5 s)*

**Visual:** Llista final pick C, squash D i squash E. Subratllar cada acció per separat.

## Escrivim el missatge conjunt

Tot seguit s’obre una altra pestanya per al missatge del *commit* nou. Escrivim Personalitza la salutació i documenta el canvi. Desem i tanquem també aquesta pestanya. *(pausa 3 s)*

**Visual:** Missatge complet visible; dos indicadors diferents, LLISTA DESADA i MISSATGE DESAT.

## Un commit nou amb el mateix resultat

Ara salutació apunta a un sol *commit* nou, a continuació de *main*. Els tres *commits* antics queden fora de la branca, però no s’esborren de seguida. *(pausa 3 s)*

**Visual:** Graf abans i després amb C, D i E atenuats i S nou; contingut final igual al d’E.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El programa funciona igual que abans d’agrupar els *commits*. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Ermessenda!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git diff 0d33d2d HEAD`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Comparem el contingut final amb l’últim *commit* antic. | 2.5 s |
| `0d33d2d` | És l’identificador de l’últim *commit* antic, el que ens havíem guardat. | 2.5 s |
| `HEAD` | És el *commit* nou. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La sortida és buida. No hi ha cap diferència de contingut, només un historial més clar. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Terminal sense sortida amb la llegenda CONTINGUT IGUAL.

## Si l’operació s’atura

Si en algun pas hi ha un conflicte, el resolem, el provem i el preparem. Després continuem amb *git rebase* doble guionet *continue*, o abandonem amb doble guionet *abort*. *(pausa 3 s)*

**Visual:** Panell condicional amb els passos editor, prova, git add, i les dues ordres de continuar o avortar.

## Resum final

Només agrupem *commits* relacionats que encara no hem publicat. *(pausa 2.5 s)*

Cal desar i tancar tant la llista com el missatge. *(pausa 2.5 s)*

Els identificadors canvien; comprovem que el contingut final és el mateix. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En una branca local de pràctiques, agrupa tres *commits* relacionats. Guarda l’identificador de l’últim abans de començar i compara el contingut al final. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
