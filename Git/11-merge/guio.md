# Lliçó 11 · Merge: porta les idees a main

**Sèrie:** Píndoles de Git · **Capçalera:** MERGE — Porta les idees a main  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/11-merge.sh`](../practiques/11-merge.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Onzena lliçó. *Merge*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a integrar dues branques a *main* i distingir l’avançament directe de la fusió amb dos pares. *(pausa 2.5 s)*

Continuem amb les dues idees de la lliçó anterior: una branca saluda per nom i l’altra afegeix un comiat. Totes dues estan confirmades i provades, i *main* encara té la versió original. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Origen i destinació

Volem portar les dues idees a *main*. *git merge* incorpora una branca a la branca activa; per això, primer ens hem de situar a la destinació. *(pausa 3 s)*

**Visual:** Graf amb B a main i dos camins, C a salutacio i D a comiat. Etiquetes ORIGEN a les dues branques i DESTINACIÓ a main.

## Terminal · `git switch main`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git switch` | Amb *git switch* canviem a la branca on treballarem. | 2.5 s |
| `main` | És el nom de la branca de destinació. Els fitxers s’actualitzen a la seva versió. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La destinació activa ara és *main*, amb la versió original. Les dues branques es conserven. *(pausa 3.5 s)*

Sortida real:

```text
Switched to branch 'main'
```

**Visual:** Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució.

## Terminal · `git branch --show-current`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git branch` | Confirmem on som abans d’integrar. | 2.5 s |
| `--show-current` | Aquesta opció mostra només el nom de la branca activa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La terminal respon *main*. Encara no hem integrat res. *(pausa 3.5 s)*

Sortida real:

```text
main
```

**Visual:** Ressaltar main tant a la sortida com al graf.

## Terminal · `git merge --ff-only salutacio`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git merge` | Comencem per la salutació. *git merge* incorpora la història de la branca que indiquem. | 2.5 s |
| `--ff-only` | Només acceptem un avançament directe. Funciona quan *main* no té *commits* propis que la branca no tingui; si no, l’ordre s’atura sense canviar res. | 2.5 s |
| `salutacio` | És la branca que incorporem. No canvia la branca activa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* avança fins al *commit* de la salutació. Les dues etiquetes apunten al mateix *commit* i no s’ha creat cap *commit* nou. *(pausa 3.5 s)*

Sortida real:

```text
Updating 1c65395..0a043f5
Fast-forward
 helloGit.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Moure només l’etiqueta main de B a C sobre el graf existent. Conservar comiat i tots els nodes.

## Terminal · `git merge --ff-only comiat`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git merge` | Provem el mateix amb el comiat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara no és possible. *main* ja té la salutació, que el comiat no té: les dues branques han avançat per camins diferents. L’ordre s’atura i no canvia res. *(pausa 3.5 s)*

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

**Visual:** Sortida real de l’error; ressaltar que main i comiat surten de B per camins diferents.

## Terminal · `git merge comiat`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git merge` | Sense l’opció, *git merge* crea un *commit* de fusió que uneix les dues històries. | 2.5 s |
| `comiat` | Incorporem aquesta branca a la branca activa, que continua sent *main*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** S’obre l’editor que vam configurar amb un missatge proposat. El desem i tanquem la pestanya, i es crea el *commit* de fusió, amb dos pares: la salutació i el comiat. *(pausa 3.5 s)*

Sortida real:

```text
Auto-merging helloGit.py
Merge made by the 'ort' strategy.
 helloGit.py | 1 +
 1 file changed, 1 insertion(+)
```

**Visual:** Pestanya de l’editor amb el missatge Merge branch 'comiat'. En tancar-la, aparèixer M connectat a C i D.

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** A *main* hi ha les dues idees: la salutació personalitzada i el comiat. Com que tocaven línies diferents, *Git* les ha pogut ajuntar sola. *(pausa 3.5 s)*

Sortida real:

```text
Hola, Ermessenda!
Benvinguda al projecte.
Fins aviat!
```

**Visual:** Mostrar la sortida real del programa al costat de l’editor.

## Terminal · `git branch -d salutacio comiat`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git branch` | Les branques de les idees ja han fet la seva feina. Amb *git branch* les podem esborrar. | 2.5 s |
| `-d` | El guionet de esborra les etiquetes de les branques, no els *commits*. Només ho fa si la branca ja està integrada; si no, *Git* s’hi nega i ens avisa. | 2.5 s |
| `salutacio comiat` | Són les dues branques que retirem. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Desapareixen les dues etiquetes. Els seus *commits* continuen a la història de *main*. *(pausa 3.5 s)*

Sortida real:

```text
Deleted branch salutacio (was 0a043f5).
Deleted branch comiat (was 155f5ba).
```

**Visual:** Retirar les etiquetes salutacio i comiat; els nodes C i D continuen al graf, units per M.

## Resum final

La branca activa és la que rep la integració. *(pausa 2.5 s)*

Si la destinació no té *commits* propis, l’avançament directe només mou l’etiqueta. *(pausa 2.5 s)*

Si les dues branques han avançat, la fusió crea un *commit* amb dos pares. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques, crea dues branques des de *main* amb canvis en línies diferents. Integra la primera amb avançament directe i la segona amb una fusió. Executa el programa i esborra les dues branques. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
