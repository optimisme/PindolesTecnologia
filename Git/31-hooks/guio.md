# Lliçó 31 · Hooks: comprova la sintaxi abans del commit

**Sèrie:** Píndoles de Git · **Capçalera:** HOOKS — Comprova la sintaxi abans del commit  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/31-hooks.sh`](../practiques/31-hooks.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Trenta-unena lliçó. *Hooks*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a crear un control local que revisi la sintaxi del contingut preparat abans de cada *commit*. *(pausa 2.5 s)*

Tenim un projecte de pràctiques amb el programa confirmat. Volem que *Git* ens avisi si intentem confirmar codi amb errors de sintaxi. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Un control abans del commit

Un *hook* és un programa que *Git* executa en un moment concret. El de tipus *pre-commit* s’executa just abans de crear un *commit*, i el pot aturar. *(pausa 3 s)*

**Visual:** Línia temporal ADD → HOOK → COMMIT. El control s’interposa abans de crear el node.

## El control llegeix la preparació

Creem el fitxer del control a la carpeta de *hooks* del repositori i hi desem el codi que veus. *(pausa 3 s)*

Llegeix el programa des de la preparació, que és el que entrarà al *commit*, encara que l’editor tingui una altra versió. *(pausa 3 s)*

**Visual:** Editor amb el codi complet de exemples/pre-commit a la ruta .git/hooks/pre-commit. Ressaltar primer la ruta i després :helloGit.py.

## Dues parts del codi

*git show* amb dos punts davant del nom llegeix el contingut preparat. La funció *compile* comprova que la sintaxi sigui vàlida, sense executar el programa. Si troba un error, mostra un missatge i atura el *commit*. *(pausa 3 s)*

**Visual:** Mantenir el codi complet. Subratllar la lectura de l’índex, després compile i després el missatge d’error.

## Terminal · `chmod +x .git/hooks/pre-commit`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `chmod` | Fem que el fitxer es pugui executar. | 2.5 s |
| `+x` | Afegeix el permís d’execució. | 2.5 s |
| `.git/hooks/pre-commit` | És el fitxer que acabem de desar. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *Git* executarà aquest control abans de cada *commit* en aquest repositori. No forma part dels fitxers del projecte. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Ruta completa, fitxer desat i indicador EXECUTABLE.

## Preparem una errada a propòsit

Treiem el parèntesi final de la salutació i desem. Aquesta versió incorrecta ens servirà per provar el control. *(pausa 3 s)*

**Visual:** Editor amb print("Hola, Anna!" sense el parèntesi final. Etiqueta PROVA DEL CONTROL.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La versió sense parèntesi entra a la preparació. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Personalitza la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Intentem confirmar el contingut preparat. | 2.5 s |
| `-m` | El guionet ema indica que a continuació escrivim el missatge del canvi. | 2.5 s |
| `"Personalitza la salutacio"` | El text entre cometes descriu la feina: Personalitza la salutació. Les cometes mantenen el missatge com un sol argument. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El control mostra l’error de sintaxi i la línia, i *Git* no crea el *commit*. *(pausa 3.5 s)*

Sortida real:

```text
pre-commit: error de sintaxi a helloGit.py, línia 1: '(' was never closed
```

**Visual:** Sortida real del hook; cap node nou. Panell PREPARACIÓ · INCORRECTA.

## Corregim només l’editor

Tornem a posar el parèntesi i desem. Però encara no hem preparat la correcció: el treball és correcte i la preparació conserva l’error. *(pausa 3 s)*

**Visual:** Dos panells, TREBALL amb el parèntesi i PREPARACIÓ sense.

## Terminal · `git commit -m "Personalitza la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Tornem a intentar el *commit*, sense preparar la correcció. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El control torna a fallar, perquè revisa la preparació. Corregir l’editor no n’hi ha prou. *(pausa 3.5 s)*

Sortida real:

```text
pre-commit: error de sintaxi a helloGit.py, línia 1: '(' was never closed
```

**Visual:** Fletxa HOOK → PREPARACIÓ, no cap a l’editor. Cap node nou.

## Terminal · `git add helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git add` | Preparem el fitxer amb *git add*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Ara la preparació té la versió correcta. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Copiar el contingut desat a la preparació.

## Terminal · `git commit -m "Personalitza la salutacio"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git commit` | Confirmem el canvi amb *git commit* i el missatge: Personalitza la salutació. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El control passa sense errors i *Git* crea el *commit*. *(pausa 3.5 s)*

Sortida real:

```text
[main 20b71e1] Personalitza la salutacio
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Visual:** Crear el node nou només en executar.

## Què fa i què no fa aquest control

Comprova la sintaxi, no que el programa faci el que volem. És local: no arriba als altres ordinadors amb un *push*. I es pot saltar amb doble guionet *no-verify*, així que és una ajuda, no una garantia. *(pausa 3 s)*

**Visual:** Etiquetes SINTAXI · LOCAL · NO VIATJA AMB EL PUSH · git commit --no-verify el salta.

## Resum final

El *pre-commit* s’executa abans de crear el *commit* i el pot aturar. *(pausa 2.5 s)*

El control d’aquest exemple revisa el contingut preparat. *(pausa 2.5 s)*

Cal preparar la correcció perquè el control la vegi; és una ajuda local. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques, instal·la el control i prova tres intents. Un amb un error preparat, un amb l’error corregit només a l’editor i l’últim després de preparar la correcció. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
