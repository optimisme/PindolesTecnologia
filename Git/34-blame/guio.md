# Lliçó 34 · Blame: investiga l’origen d’una línia

**Sèrie:** Píndoles de Git · **Capçalera:** BLAME — Investiga l’origen d’una línia  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/34-blame.sh`](../practiques/34-blame.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Trenta-quatrena lliçó. *Blame*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a investigar una línia amb *git blame* i confirmar la causa d’un error amb *git show*. *(pausa 2.5 s)*

El programa ha deixat de funcionar i volem saber quin canvi ho ha provocat. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Una línia que falla té un context

El programa imprimeix una variable que ja no existeix amb aquell nom. Investigarem les línies relacionades i els *commits* que les van canviar. *(pausa 3 s)*

**Visual:** Editor amb línies numerades. 1 · comentari; 2 · missatge = "Hola, Ermessenda!"; 3 · print( salutacio ).

## Terminal · `python3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `python3` | Provem el programa amb la versió desada del fitxer. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Surt un error de nom a la línia tres. La línia ens orienta, però encara no sabem quin canvi l’ha provocat. *(pausa 3.5 s)*

Sortida real:

```text
Traceback (most recent call last):
  File "~/HelloGit/helloGit.py", line 3, in <module>
    print( salutacio )
           ^^^^^^^^^
NameError: name 'salutacio' is not defined
```

**Visual:** Ressaltar NameError i la línia 3 a la sortida real, sense atribuir responsabilitats.

## Terminal · `git blame helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git blame` | *git blame* mostra, per a cada línia, l’últim *commit* que la va modificar. | 2.5 s |
| `helloGit.py` | Consultem les línies del programa actual. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La línia tres s’associa a l’últim *commit*. Això vol dir que la va tocar, no que hi introduís l’error. *(pausa 3.5 s)*

Sortida real:

```text
^9cc686f (Ermessenda Carcassona 2026-10-20 12:03:00 +0200 1) # Salutació del projecte
b5e2fac2 (Ermessenda Carcassona 2026-10-20 12:05:00 +0200 2) missatge = "Hola, Ermessenda!"
4cd6c24c (Ermessenda Carcassona 2026-10-20 12:07:00 +0200 3) print( salutacio )
```

**Visual:** Separar a la sortida real les columnes identificador, autoria, data i contingut. Sense llenguatge de culpa.

## Terminal · `git blame -L 3,3 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git blame` | Limitem la consulta a la línia de l’error. | 2.5 s |
| `-L` | El guionet ela limita la consulta a un rang de línies. | 2.5 s |
| `3,3` | El primer número és l’inici i el segon, el final. Aquí només demanem la línia tres. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Copiem l’identificador del *commit* per veure què hi va canviar. *(pausa 3.5 s)*

Sortida real:

```text
4cd6c24c (Ermessenda Carcassona 2026-10-20 12:07:00 +0200 3) print( salutacio )
```

**Visual:** Subratllar -L, després el rang i després la fila de la sortida.

## Terminal · `git show 4cd6c24 -- helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | Comprovem el canvi concret d’aquell *commit*. | 2.5 s |
| `4cd6c24` | És l’identificador que ens ha donat *blame*. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només hi va afegir espais. La variable ja era incorrecta abans d’aquell retoc. *(pausa 3.5 s)*

Sortida real:

```text
commit 4cd6c24c00954b367f49d0fdea19c179e7d14ca2
Author: Ermessenda Carcassona <ermessenda@example.com>
Date:   Tue Oct 20 12:07:00 2026 +0200

    Ajusta el format

diff --git a/helloGit.py b/helloGit.py
index a40a883..9fbd2db 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1,3 +1,3 @@
 # Salutació del projecte
 missatge = "Hola, Ermessenda!"
-print(salutacio)
+print( salutacio )
```

**Visual:** Diff real, print(salutacio) → print( salutacio ). Destacar els espais com un canvi de format.

## Terminal · `git blame -L 2,2 helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git blame` | Seguim la pista fins a la línia que defineix la variable. | 2.5 s |
| `2,2` | Ara consultem la línia dos. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Aquesta línia ens porta a un altre *commit*. El nom definit i el nom que s’imprimeix no coincideixen. *(pausa 3.5 s)*

Sortida real:

```text
b5e2fac2 (Ermessenda Carcassona 2026-10-20 12:05:00 +0200 2) missatge = "Hola, Ermessenda!"
```

**Visual:** Fletxa entre missatge a la línia 2 i salutacio a la línia 3.

## Terminal · `git show b5e2fac -- helloGit.py`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git show` | Revisem aquest altre *commit*. | 2.5 s |
| `b5e2fac` | És el *commit* que va canviar la definició de la variable. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Va canviar el nom de la variable sense actualitzar-ne l’ús. Aquí és on va començar l’error. *(pausa 3.5 s)*

Sortida real:

```text
commit b5e2fac2210a9e89fb636275a470a4a8786b7468
Author: Ermessenda Carcassona <ermessenda@example.com>
Date:   Tue Oct 20 12:05:00 2026 +0200

    Reanomena la variable

diff --git a/helloGit.py b/helloGit.py
index dfc4341..a40a883 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1,3 +1,3 @@
 # Salutació del projecte
-salutacio = "Hola, Ermessenda!"
+missatge = "Hola, Ermessenda!"
 print(salutacio)
```

**Visual:** Diff real de B amb la definició antiga i la nova; mantenir visible la línia del print.

## Resum final

*git blame* indica l’últim *commit* que va modificar cada línia. *(pausa 2.5 s)*

*git show* explica què va canviar aquell *commit*. *(pausa 2.5 s)*

Cal seguir les dependències entre línies abans de concloure d’on ve un error. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un fitxer de pràctiques, investiga dues línies relacionades. Revisa els *commits* que les van canviar i separa els canvis funcionals dels retocs de format. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
