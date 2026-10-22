# Lliçó 33 · Cercar a l’historial: autoria, fitxers i text

**Sèrie:** Píndoles de Git · **Capçalera:** CERCAR A L’HISTORIAL — Autoria, fitxers i text  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/33-cercar-historial.sh`](../practiques/33-cercar-historial.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Trenta-tresena lliçó. Cercar a l’historial.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a trobar *commits* concrets filtrant l’historial per autoria, per fitxer, per missatge i pel text que canvien. *(pausa 2.5 s)*

Dues persones han fet cinc *commits* al projecte. Volem trobar-ne de concrets sense llegir tot l’historial. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Filtrar en lloc de llegir-ho tot

En un projecte real, l’historial pot tenir centenars de *commits*. *git log* accepta filtres que deixen només els que ens interessen. *(pausa 3 s)*

**Visual:** Llista llarga de commits que es redueix a uns pocs en aplicar un filtre.

## Terminal · `git log --oneline --author="Pau"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Primer filtrem per autoria. | 2.5 s |
| `--author` | Doble guionet *author* deixa només els *commits* d’una persona. | 2.5 s |
| `"Pau"` | És el text que ha d’aparèixer al nom o al correu de l’autoria. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Només surten els dos *commits* de les notes, els que va fer en Pau. *(pausa 3.5 s)*

Sortida real:

```text
855fb71 Amplia les notes
045fcf8 Afegeix les notes
```

**Visual:** Sortida real amb dues línies; nom de l’autoria al costat de cada una.

## Terminal · `git log --oneline -- notes.md`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Ara, els *commits* que han tocat un fitxer concret. | 2.5 s |
| `--` | Els dos guionets separen les opcions del nom del fitxer. | 2.5 s |
| `notes.md` | És el fitxer que ens interessa. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Surten els *commits* que van canviar les notes, sense els del programa. *(pausa 3.5 s)*

Sortida real:

```text
855fb71 Amplia les notes
045fcf8 Afegeix les notes
```

**Visual:** Sortida real; ressaltar notes.md a l’explorador.

## Terminal · `git log --oneline --grep="comiat"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | També podem buscar dins dels missatges. | 2.5 s |
| `--grep` | Doble guionet *grep* busca un text als missatges dels *commits*. | 2.5 s |
| `"comiat"` | És la paraula que busquem. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Surten els dos *commits* que parlen del comiat al missatge. *(pausa 3.5 s)*

Sortida real:

```text
e6140d0 Canvia el comiat
a47f91c Afegeix el comiat
```

**Visual:** Sortida real amb la paraula comiat ressaltada a cada missatge.

## Terminal · `git log --oneline -S "Fins aviat"`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git log` | Finalment, busquem quan va aparèixer o desaparèixer un text del codi. | 2.5 s |
| `-S` | La essa majúscula busca els *commits* que afegeixen o treuen aquest text dels fitxers, no dels missatges. | 2.5 s |
| `"Fins aviat"` | És el text del programa que busquem. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Surten dos *commits*, el que va afegir aquest comiat i el que el va canviar per un altre. Així sabem quan va entrar al codi i quan en va sortir. *(pausa 3.5 s)*

Sortida real:

```text
e6140d0 Canvia el comiat
a47f91c Afegeix el comiat
```

**Visual:** Sortida real; al costat, el fitxer amb la línia print("Fins aviat!") que apareix a C i desapareix a E.

## Combinar filtres

Els filtres es poden combinar en una mateixa ordre, per exemple autoria i fitxer. Quan hem trobat el *commit*, *git show* ens n’explica el contingut. *(pausa 3 s)*

**Visual:** Ordre de mostra git log --oneline --author="Ermessenda" -- helloGit.py i, a sota, git show amb l’identificador trobat.

## Resum final

Doble guionet *author* i el nom d’un fitxer filtren per persona i per fitxer. *(pausa 2.5 s)*

Doble guionet *grep* busca als missatges. *(pausa 2.5 s)*

La essa majúscula busca quan un text va entrar o sortir del codi. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

En un repositori de pràctiques amb uns quants *commits*, busca els teus *commits*, els que han tocat un fitxer i el *commit* que va afegir una línia concreta. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
