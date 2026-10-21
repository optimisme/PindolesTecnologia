# Lliçó 21 · Rebase: continua sobre una base nova

**Sèrie:** Píndoles de Git · **Capçalera:** REBASE — Continua sobre una base nova  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/21-rebase.sh`](../practiques/21-rebase.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-unena lliçó. *Rebase*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a tornar a aplicar els *commits* propis sobre una base actualitzada i veure per què canvien d’identificador. *(pausa 2.5 s)*

La nostra branca salutació té dos *commits* propis, encara no publicats. Mentrestant, *main* ha avançat amb un *commit* nou en un altre fitxer. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Una base que ha avançat

Volem continuar la nostra feina a partir de la versió actual de *main*. La branca salutació té dos *commits* propis que encara no hem compartit. *(pausa 3 s)*

**Visual:** B com a base; main a D; salutacio a E passant per C. Etiqueta NO PUBLICATS sobre C i E.

## Terminal · `git switch salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `salutacio` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Som a la branca que tornarem a construir. *main* farà de base i no es mourà. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'salutacio'
```

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució.

## Terminal · `git rebase main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git rebase` | *git rebase* torna a aplicar els *commits* de la branca activa a partir d’una altra base. | 2.5 s |
| `main` | És la nova base. No és la branca on integrem la feina. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Els dos canvis s’han tornat a aplicar a continuació de *main*. Són *commits* nous: tenen un altre pare i un altre identificador. *(pausa 3.5 s)*

Sortida real:

```text
Rebasing (1/2)
Rebasing (2/2)
Successfully rebased and updated refs/heads/salutacio.
```

**Visual:** Atenuar C i E; dibuixar C′ i E′ a partir de D. No moure els nodes originals com si fossin els mateixos.

## Seguim un canvi concret

La salutació que introduïa el primer *commit* també és a la seva còpia nova, ara a continuació de *main*. El contingut es conserva, però l’historial és diferent, perquè ha canviat el pare. *(pausa 3 s)*

**Visual:** Comparar el mateix canvi a C i C′; després, ressaltar els pares B i D.

## Terminal · `git log --oneline --graph --all`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Revisem l’historial després de l’operació. | 2.5 s |
| `--graph` | Dibuixa amb línies com es connecten els *commits*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* continua al seu lloc i salutació apunta al final de la línia nova. Encara no hem integrat la feina a *main*. *(pausa 3.5 s)*

Sortida real:

```text
* 5e1d6c1 Documenta la salutacio
* f66c70d Personalitza la salutacio
* c44cd15 Afegeix el README
* 99010b3 Afegeix una exclamacio
* d3fb44b Afegeix la salutacio inicial
```

**Visual:** Sortida real del graf amb una llegenda de les branques.

## Comparació amb merge

Des del mateix punt de partida, *merge* uniria els dos camins amb un *commit* de dos pares. *Rebase* reconstrueix els *commits* propis a continuació de la base nova, en una sola línia. *(pausa 3 s)*

**Visual:** Dos grafs, un al costat de l’altre, amb el mateix estat inicial. No executar una operació després de l’altra.

## Si apareix un conflicte

> **Si hi ha conflicte.** Parteix del seu propi punt; no s’encadena amb el camí principal.

En un altre cas, *main* havia canviat la mateixa línia i el *rebase* s’atura. Escrivim el contingut correcte i el provem. *(pausa 3 s)*

**Visual:** Separador SI HI HA CONFLICTE; indicador REBASE PAUSAT. El camí principal no tenia conflictes.

## Terminal · `python3 helloGit.py`

> **Si hi ha conflicte.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La resolució funciona. *(pausa 3.5 s)*

Sortida real:

```text
Hola, grup!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git add helloGit.py`

> **Si hi ha conflicte.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La resolució queda preparada per continuar. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git rebase --continue`

> **Si hi ha conflicte.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git rebase` | Reprenem el *rebase* pausat. | 2.5 s |
| `--continue` | Continua l’operació. Si hi ha més conflictes, repetim el mateix procés. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Pot obrir l’editor amb el missatge del *commit*; el desem i el tanquem. El *rebase* acaba amb la resolució que hem decidit. *(pausa 3.5 s)*

Sortida real:

```text
[detached HEAD 09e13c1] Personalitza la salutacio
 1 file changed, 1 insertion(+), 1 deletion(-)
Rebasing (2/2)
Successfully rebased and updated refs/heads/salutacio.
```

**Visual:** Pestanya de l’editor amb el missatge; en tancar-la, la línia nova queda completa.

## Alternativa, abandonar el rebase

> **Alternativa.** Parteix del seu propi punt; no s’encadena amb el camí principal.

Des del mateix conflicte, també podem abandonar l’operació en lloc de continuar-la. *(pausa 3 s)*

**Visual:** Bifurcació CONTINUAR / AVORTAR, sense executar les dues opcions seguides.

## Terminal · `git rebase --abort`

> **Alternativa.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git rebase` | Cancel·lem el *rebase* pendent. | 2.5 s |
| `--abort` | Torna la branca a l’estat d’abans de començar. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La branca salutació torna a tenir els seus *commits* originals, com si no haguéssim començat. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Tornar al graf inicial de salutacio.

## Resum final

*Rebase* canvia la base de la branca activa. *(pausa 2.5 s)*

Els *commits* tornats a aplicar tenen identificadors nous; *main* no es mou. *(pausa 2.5 s)*

Només fem *rebase* de feina pròpia que encara no hem publicat. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En una branca local de pràctiques amb canvis compatibles, torna a aplicar la teva feina sobre *main*. Compara el graf i prova el resultat. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
