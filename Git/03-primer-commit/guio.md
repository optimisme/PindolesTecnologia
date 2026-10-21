# Lliçó 3 · El primer commit: preparar, confirmar i publicar

**Sèrie:** Píndoles de Git · **Capçalera:** EL PRIMER COMMIT — Preparar, confirmar i publicar  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/03-primer-commit.sh`](../practiques/03-primer-commit.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Tercera lliçó. El primer *commit*.

## Preparar, confirmar i publicar

En aquesta lliçó guardarem una primera versió del projecte i la compartirem. Farem cada pas a la terminal i en comprovarem el resultat. *(pausa 2 s)*

**Visual:** Tres accions visibles. Es presenta l’objectiu pràctic sense repetir la introducció conceptual.

## Un projecte buit ja preparat

Comencem dins de la carpeta del projecte. El repositori està buit, la identitat està configurada i tenim accés al remot. *(pausa 3 s)*

**Visual:** Requisits visibles i estables; el punt de partida s’explica dins del vídeo.

## Escrivim i provem la salutació

Creem el fitxer del programa, escrivim la salutació i el desem. El nom del fitxer és el que veus a l’editor. *(pausa 2.5 s)*

Executem el programa. La terminal mostra la salutació. El fitxer està desat, però encara no tenim cap versió a l’historial. *(pausa 3 s)*

**Visual:** Editor desat i execució del programa en dos passos amb espera.

## Consultem què tenim pendent

*git status* consulta l’estat del projecte. Aquesta ordre ens informa; no confirma ni envia cap canvi. *(pausa 3 s)*

El fitxer apareix a la llista de fitxers nous sense seguir. Encara l’hem de seleccionar per incloure’l a la primera versió. *(pausa 3 s)*

**Visual:** Git status sense opcions; extracte de la sortida i traducció del seu significat.

## Llegim la comanda per parts

Ara seleccionarem el contingut del fitxer que volem confirmar. Aquest pas s’anomena preparar. *(pausa 2 s)*

*git add* és l’ordre de preparació. El primer mot identifica el programa; el segon indica l’acció que li demanem. *(pausa 2.5 s)*

A continuació escrivim el nom del fitxer. Així seleccionem només aquest fitxer, en lloc de preparar tots els canvis del projecte. *(pausa 3 s)*

Executem la comanda completa. El contingut actual queda preparat i el fitxer continua al seu lloc. Encara no hem creat cap *commit*. *(pausa 3 s)*

**Visual:** Comanda gran i persistent: git, add i nom del fitxer. Es ressalta una part a cada explicació; després es prepara el contingut.

## Desem la primera versió local

*git commit* crea una versió amb el contingut que hem preparat. Aquesta versió queda al repositori del nostre ordinador. *(pausa 2.5 s)*

El guionet ema introdueix el missatge del canvi. Escrivim el missatge entre cometes perquè la terminal el tracti com un sol argument. *(pausa 3 s)*

El missatge descriu què hem fet: afegir la salutació inicial. Ens ajudarà a reconèixer aquesta versió més endavant. *(pausa 3 s)*

Ara executem l’ordre. Apareix la primera versió a l’historial local, amb el seu identificador. El remot encara és buit. *(pausa 3 s)*

**Visual:** La comanda es descompon en acció, opció -m i missatge. El commit apareix només després d’executar-la.

## Llegim la versió registrada

*git log* permet consultar les versions registrades. A la sortida hi veiem l’identificador i el missatge que acabem d’escriure. *(pausa 3 s)*

**Visual:** Git log complet amb extracte de hash i missatge. No s’introdueixen opcions noves.

## Llegim també la comanda de publicació

*git push* publica les versions confirmades en un repositori remot. La comanda que veus indica també on les volem enviar. *(pausa 2.5 s)*

*origin* és el nom que identifica el nostre remot. En aquest exemple, la connexió apunta al repositori del projecte a *GitHub*. *(pausa 3 s)*

*main* és la branca que volem publicar. Aquest nom coincideix amb la branca on estem treballant. *(pausa 2.5 s)*

El guionet u desa aquesta relació de seguiment. Als enviaments següents d’aquesta mateixa branca podrem escriure només *git push*. *(pausa 3 s)*

Executem l’ordre completa. La mateixa versió que teníem al repositori local ara també apareix al remot. *(pausa 3 s)*

**Visual:** Comanda persistent i ressaltat successiu de push, origin, main i -u. El resultat s’observa amb una pausa pròpia.

## Repetim els passos amb calma

Canviem la salutació, desem i tornem a executar el programa. Encara només ha canviat el fitxer de treball. *(pausa 3 s)*

També creem un fitxer de notes i el desem. Ara tenim un fitxer modificat i un fitxer nou. Encara no hem preparat aquests canvis. *(pausa 3 s)*

Ara escrivim *git add* seguit d’un punt. El punt representa la carpeta actual i les seves subcarpetes. Com que som a l’arrel del projecte, l’ordre abasta tot el projecte. *(pausa 3 s)*

Això permet preparar fitxers modificats, fitxers nous i eliminacions. En aquest cas, seleccionem el programa modificat i les notes noves. Els fitxers nous ignorats queden fora. *(pausa 3 s)*

Executem l’ordre. Els dos fitxers queden preparats en un mateix pas. Abans de confirmar, revisem que tots dos canvis són els que volem. *(pausa 3 s)*

Creem el segon *commit* amb un missatge que descriu la salutació i les notes. L’historial conserva la primera versió i hi afegeix la nova. *(pausa 3 s)*

Finalment, *git push* envia aquesta versió al remot. Desar, preparar, confirmar i publicar han estat accions diferents. *(pausa 3 s)*

**Visual:** Una salutació modificada i un fitxer de notes nou. El punt de git add . s’explica amb subratllat, es preparen els dos fitxers i es confirmen junts.

## Tres comandes. Tres funcions.

Preparar selecciona el contingut que entrarà a la versió següent. *(pausa 2.5 s)*

Confirmar desa una versió a l’historial del nostre ordinador. *(pausa 2.5 s)*

Publicar comparteix les versions confirmades amb el repositori remot. *(pausa 3 s)*

**Visual:** Tres targetes amb ressaltat successiu i espai després de cada funció.

## Practica el cicle complet

Al teu repositori de pràctiques, canvia el missatge i repeteix aquests passos. Consulta l’historial abans i després per veure la versió que has afegit. *(pausa 4 s)*

**Visual:** Petit exercici final sense pregunta ni resposta; les instruccions es mantenen visibles.
