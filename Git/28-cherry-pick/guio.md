# Lliçó 28 · Cherry-pick: porta una correcció a una altra branca

**Sèrie:** Píndoles de Git · **Capçalera:** CHERRY-PICK — Porta una correcció a una altra branca  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/28-cherry-pick.sh`](../practiques/28-cherry-pick.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-vuitena lliçó. *Cherry-pick*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a aplicar a *main* només una correcció d’una altra branca, sense portar-hi la resta de la feina. *(pausa 2.5 s)*

*main* té una errada a la salutació. A la branca salutació, entre altres feines encara pendents, ja hi ha un *commit* que la corregeix. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Una correcció dins d’una altra feina

La branca de la salutació conté una feina encara pendent i una correcció que necessitem ara a *main*. Portarem només la correcció, després de comprovar que no depèn de la resta. *(pausa 3 s)*

**Visual:** Graf main a B; salutacio a D, amb C entremig. C · notes.md; D · correcció de helloGit.py.

## Terminal · `git log --oneline salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Busquem el *commit* de la correcció. | 2.5 s |
| `salutacio` | Consultem la història d’aquesta branca, sense canviar-hi. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El primer de la llista és la correcció. En copiem l’identificador. *(pausa 3.5 s)*

Sortida real:

```text
2e324d3 Corregeix l'errada de la salutacio
1ec3a9e Comença les notes de la salutacio
ee67d11 Afegeix una exclamacio
8bb43f8 Afegeix la salutacio inicial
```

**Visual:** Ressaltar D a la sortida real i deixar C visible com a FEINA PENDENT.

## Terminal · `git show 2e324d3 -- helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | Revisem què canvia aquest *commit*. | 2.5 s |
| `2e324d3` | És l’identificador que hem copiat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només corregeix la salutació; no necessita les notes del *commit* anterior. *(pausa 3.5 s)*

Sortida real:

```text
commit 2e324d360e2a13d077d1b3d692a1126a56072556
Author: Ermessenda Carcassona <ermessenda@example.com>
Date:   Tue Oct 20 12:11:00 2026 +0200

    Corregeix l'errada de la salutacio

diff --git a/helloGit.py b/helloGit.py
index e383206..52662af 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1 @@
-print("Helo Git!")
+print("Hello Git!")
```

**Visual:** Diff real amb només la correcció; panell notes.md EXCLÒS.

## Terminal · `git status --short`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git status` | Consultem l’estat breu amb *git status*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** No hi ha feina pendent que es pugui barrejar amb l’operació. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Sortida literal amb la llegenda de les dues columnes.

## Terminal · `git switch main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `main` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La correcció s’aplicarà a *main*, que ara és la branca activa. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'main'
```

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució.

## Terminal · `git cherry-pick 2e324d3`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git cherry-pick` | *git cherry-pick* torna a aplicar a la branca activa el canvi d’un *commit* concret. | 2.5 s |
| `2e324d3` | Indiquem només la correcció, no tota la branca de la salutació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Es crea un *commit* nou a *main*, amb el mateix canvi i un identificador diferent. La branca de la salutació es queda com estava. *(pausa 3.5 s)*

Sortida real:

```text
[main 0375971] Corregeix l'errada de la salutacio
 Date: Tue Oct 20 12:11:00 2026 +0200
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Crear E com a fill de B. Relació conceptual de canvi D → E, diferent d’una relació de pare.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació ja és correcta a *main*, i les notes pendents no hi han entrat. *(pausa 3.5 s)*

Sortida real:

```text
Hello Git!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Si l’aplicació s’atura

> **Si hi ha conflicte.** Parteix del seu propi punt; no s’encadena amb el camí principal.

En un altre cas, *main* havia canviat la mateixa línia i l’operació s’atura amb un conflicte. Escrivim el resultat correcte i el provem. *(pausa 3 s)*

**Visual:** Panell condicional amb el conflicte real al fitxer.

## Terminal · `python3 helloGit.py`

> **Si hi ha conflicte.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La resolució funciona. *(pausa 3.5 s)*

Sortida real:

```text
Hello, Git!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git add helloGit.py`

> **Si hi ha conflicte.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La resolució queda preparada. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git cherry-pick --continue`

> **Si hi ha conflicte.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git cherry-pick` | Reprenem l’operació pausada. | 2.5 s |
| `--continue` | Continua el *cherry-pick* pendent; no en comença cap de nou. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Es crea el *commit* amb la resolució. Pot obrir l’editor amb el missatge original; el desem i el tanquem. *(pausa 3.5 s)*

Sortida real:

```text
[main c1b8aaf] Corregeix l'errada de la salutacio
 Date: Tue Oct 20 12:11:00 2026 +0200
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Només el camí CONTINUAR del cas amb conflicte.

## Alternativa, abandonar

> **Alternativa.** Parteix del seu propi punt; no s’encadena amb el camí principal.

Des del mateix conflicte, també podem abandonar l’operació. *(pausa 3 s)*

**Visual:** Bifurcació AVORTAR des del conflicte, mai després de continuar.

## Terminal · `git cherry-pick --abort`

> **Alternativa.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git cherry-pick` | Cancel·lem el *cherry-pick* pendent. | 2.5 s |
| `--abort` | Torna a l’estat d’abans de començar. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* queda com estava abans d’intentar-ho. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Desapareixen el conflicte i l’indicador d’operació pendent.

## Resum final

Triem un *commit* concret i comprovem que no depengui d’altres canvis. *(pausa 2.5 s)*

La branca activa rep un *commit* nou, amb un pare i un identificador diferents. *(pausa 2.5 s)*

La branca original es conserva; el resultat s’ha de provar. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques, crea en una branca una correcció independent d’una altra feina. Porta només la correcció a *main* i comprova els fitxers de les dues branques. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
