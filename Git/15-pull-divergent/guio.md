# Lliçó 15 · Quan pull s’atura: històries divergents

**Sèrie:** Píndoles de Git · **Capçalera:** QUAN PULL S’ATURA — Dues còpies que han avançat alhora  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/15-pull-divergent.sh`](../practiques/15-pull-divergent.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Quinzena lliçó. Quan *pull* s’atura.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a integrar una còpia local i un servidor que han avançat amb *commits* diferents. *(pausa 2.5 s)*

A casa hem fet un *commit* sense actualitzar abans. Mentrestant, des de classe s’havia publicat un altre *commit*. Les dues còpies han avançat per camins diferents. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Dos camins des del mateix commit

El servidor té el *commit* de classe i la nostra còpia té el de casa. Tots dos parteixen de la mateixa versió, però cap dels dos conté l’altre. *(pausa 3 s)*

**Visual:** Graf amb A; B a origin/main i X a main, tots dos fills d’A.

## Terminal · `git pull --ff-only`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git pull` | Provem d’actualitzar com sempre. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** L’ordre s’atura sense canviar res, perquè no es pot avançar directament. Cal decidir com unim les dues històries. *(pausa 3.5 s)*

Sortida real:

```text
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

**Visual:** Sortida real amb l’error ressaltat; el graf no canvia.

## Dues maneres d’unir-les

Podem fusionar-les, amb un *commit* de dos pares, com a la lliçó de *merge*. O podem tornar a aplicar el nostre *commit* a continuació del del servidor, en una sola línia. Veurem totes dues. *(pausa 3 s)*

**Visual:** Dos grafs, FUSIÓ amb M i dos pares / REAPLICAR amb X′ després de B.

## Terminal · `git pull --no-rebase`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git pull` | Primer, la fusió. | 2.5 s |
| `--no-rebase` | Descarrega i integra amb una fusió, sense tornar a aplicar els nostres *commits*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** S’obre l’editor amb un missatge proposat; el desem i el tanquem. Es crea un *commit* de fusió que uneix el *commit* de casa i el de classe. *(pausa 3.5 s)*

Sortida real:

```text
Merge made by the 'ort' strategy.
 notes.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 notes.md
```

**Visual:** Pestanya de l’editor; en tancar-la, apareix M connectat a X i a B.

## Terminal · `git push`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | Amb *git push* enviem els *commits* de la branca al remot. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara el servidor té els dos *commits* i la fusió. Classe ja es podrà actualitzar amb un avançament directe. *(pausa 3.5 s)*

Sortida real:

```text
To ~/origin.git
   4a35a7e..75a8ff6  main -> main
```

**Visual:** Conservar el mateix identificador al local i al remot. La fletxa envia commits; no envia edicions sense confirmar.

## L’altra opció, reaplicar

> **L’altra opció.** Parteix del seu propi punt; no s’encadena amb el camí principal.

Tornem al moment de l’error. En lloc de fusionar, podem tornar a aplicar el *commit* de casa a continuació del de classe. *(pausa 3 s)*

**Visual:** Separador L’ALTRA OPCIÓ. Graf inicial amb B i X.

## Terminal · `git pull --rebase`

> **L’altra opció.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git pull` | Actualitzem tornant a aplicar els nostres *commits*. | 2.5 s |
| `--rebase` | Descarrega les novetats i torna a aplicar a sobre els *commits* locals que encara no hem publicat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El *commit* de casa es torna a crear després del de classe, amb un identificador nou. La història queda en una sola línia, sense *commit* de fusió. *(pausa 3.5 s)*

Sortida real:

```text
Rebasing (1/1)
Successfully rebased and updated refs/heads/main.
```

**Visual:** X atenuat; X′ nou després de B.

## Terminal · `git push`

> **L’altra opció.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git push` | Amb *git push* enviem els *commits* de la branca al remot. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El servidor rep el *commit* tornat a aplicar. *(pausa 3.5 s)*

Sortida real:

```text
To ~/origin.git
   4a35a7e..2e0c127  main -> main
```

**Visual:** Conservar el mateix identificador al local i al remot. La fletxa envia commits; no envia edicions sense confirmar.

## Terminal · `git config --global pull.rebase false`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git config` | Podem deixar triada l’opció per defecte. | 2.5 s |
| `pull.rebase` | Aquesta clau indica què fa *pull* quan les històries divergeixen. | 2.5 s |
| `false` | Fals vol dir fusionar. Amb true, tornaria a aplicar els *commits* locals. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Si no ho configurem, les versions recents de *Git* s’aturen i ens demanen que triem. Si teniu dubtes, la fusió és l’opció més segura; si hi ha conflictes, es resolen com a la lliçó de conflictes. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Línia rebase = false a la secció pull de la configuració global.

## Resum final

Si les dues còpies han avançat, doble guionet *ff-only* s’atura sense canviar res. *(pausa 2.5 s)*

Doble guionet *no-rebase* uneix les històries amb un *commit* de fusió. *(pausa 2.5 s)*

Doble guionet *rebase* torna a aplicar els *commits* locals que encara no hem publicat. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Amb dos clons de pràctiques, fes un *commit* a cadascun sense actualitzar. Uneix les històries una vegada amb fusió i, en una altra prova, tornant a aplicar els *commits*. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
