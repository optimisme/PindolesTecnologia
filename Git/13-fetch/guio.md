# Lliçó 13 · Fetch: consulta els canvis abans d’integrar-los

**Sèrie:** Píndoles de Git · **Capçalera:** FETCH — Consulta els canvis abans d’integrar  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/13-fetch.sh`](../practiques/13-fetch.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Tretzena lliçó. *Fetch*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a descarregar, revisar i integrar les novetats del servidor en tres passos separats. *(pausa 2.5 s)*

La nostra còpia és al dia de l’última vegada que vam consultar el servidor. Mentrestant, una altra persona hi ha publicat un *commit* nou. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Una referència que no s’actualitza sola

Al nostre repositori, *origin/main* recorda on era *main* al servidor l’última vegada que el vam consultar. No és una vista en directe: encara apunta a l’antic *commit*. *(pausa 3 s)*

**Visual:** Tres elements separats, main LOCAL a B, origin/main LOCAL a B i main AL SERVIDOR a C.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** No hi ha canvis pendents. Així veurem clarament què canvia cada pas. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git fetch origin`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git fetch` | *git fetch* descarrega les novetats i actualitza les referències del remot. | 2.5 s |
| `origin` | És el remot que consultem. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* nou ja és al nostre repositori i *origin/main* l’assenyala. *main*, la preparació i els fitxers no han canviat. *(pausa 3.5 s)*

Sortida real:

```text
From ~/origin
   f5f5973..a5259f2  main       -> origin/main
```

**Visual:** Animar la descàrrega de C i el moviment d’origin/main. No moure main ni canviar l’editor.

## Terminal · `git log --oneline main..origin/main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Consultem quins *commits* té el remot que la nostra branca encara no té. | 2.5 s |
| `main..origin/main` | Els dos punts formen un rang. Llista els *commits* d’*origin/main* que no són a *main*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** En aquest exemple només n’hi ha un. Consultar-lo tampoc l’integra. *(pausa 3.5 s)*

Sortida real:

```text
a5259f2 Personalitza la salutacio
```

**Visual:** Subratllar main, els dos punts i origin/main per torns; ressaltar C a la sortida real.

## Terminal · `git diff main origin/main -- helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Comparem el contingut de les dues versions. | 2.5 s |
| `main` | El primer punt de comparació és la nostra branca. | 2.5 s |
| `origin/main` | El segon és la versió descarregada del servidor. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Veiem la salutació nova, mentre el fitxer del nostre treball encara té l’original. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 52662af..55b21a2 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1 @@
-print("Hello Git!")
+print("Hola, Anna!")
```

**Visual:** Sortida real i editor actual, visibles alhora. Cap fletxa de sobreescriptura.

## Terminal · `git merge --ff-only origin/main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git merge` | Després de revisar-ho, decidim incorporar el canvi. | 2.5 s |
| `origin/main` | És la referència descarregada que incorporem a *main*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* avança fins al *commit* nou i el fitxer s’actualitza. Aquest és el pas que integra la novetat. *(pausa 3.5 s)*

Sortida real:

```text
Updating f5f5973..a5259f2
Fast-forward
 helloGit.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Moure main fins a C i actualitzar l’editor després de l’execució.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El programa ja mostra la salutació nova. Hem separat descarregar, revisar i integrar. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Anna!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Resum final

*git fetch* descarrega i actualitza *origin/main* sense tocar *main*. *(pausa 2.5 s)*

Amb *git log* i *git diff* revisem el que hem descarregat. *(pausa 2.5 s)*

Integrar és un pas posterior; *git pull* fa la descàrrega i la integració alhora. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Amb dos clons de pràctiques, publica una novetat des d’un i fes *fetch* a l’altre. Compara *main* i *origin/main* abans d’integrar. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
