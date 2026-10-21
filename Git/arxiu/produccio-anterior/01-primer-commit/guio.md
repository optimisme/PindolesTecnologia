# El primer commit: preparar, confirmar i publicar

Sèrie: Píndoles de Git
Veu: en-US-AndrewMultilingualNeural · català +5%, anglès +0%, pauses d’idioma de 500 ms.

Punt de partida: Git i Python disponibles; identitat configurada al repositori, remot origin i accés a GitHub. Repositori HelloGit buit ja clonat, HEAD a main sense commits, cap fitxer del programa creat. La demostració executable es valida en repositoris temporals amb un remot local.

## Capçalera musical (0:00–0:04)

Sintonia comuna de quatre segons, sense locució.

## Presentació (4,00–7.38 s)

Primera lliçó. El primer commit.

## Preparar, confirmar i publicar (7.38–19.29 s)

**Animació:** Tres accions visibles. Es presenta l’objectiu pràctic sense repetir la introducció conceptual.

### objectiu (7.73–18.71 s)

**Locució:** En aquesta lliçó guardarem una primera versió del projecte i la compartirem. Farem cada pas a la terminal i en comprovarem el resultat.

**Pausa de lectura i assimilació:** 2 s; es manté el mateix visual.

## Un projecte buit ja preparat (19.29–32.08 s)

**Animació:** Requisits visibles i estables; el punt de partida s’explica dins del vídeo.

### preparacio (19.66–31.50 s)

**Locució:** Comencem dins de la carpeta del projecte. El repositori està buit, la identitat està configurada i tenim accés al remot.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

## Escrivim i provem la salutació (32.08–55.29 s)

**Animació:** Editor desat i execució del programa en dos passos amb espera.

### desar (32.48–42.81 s)

**Locució:** Creem el fitxer del programa, escrivim la salutació i el desem. El nom del fitxer és el que veus a l’editor.

**Pausa de lectura i assimilació:** 2.5 s; es manté el mateix visual.

### provar (42.81–54.70 s)

**Locució:** Executem el programa. La terminal mostra la salutació. El fitxer està desat, però encara no tenim cap versió a l’historial.

**Comanda en pantalla:**

```bash
python3 helloGit.py
```

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

## Consultem què tenim pendent (55.29–78.33 s)

**Animació:** Git status sense opcions; extracte de la sortida i traducció del seu significat.

### status_ordre (55.69–66.75 s)

**Locució:** git status consulta l’estat del projecte. Aquesta ordre ens informa; no confirma ni envia cap canvi.

**Comanda en pantalla:**

```bash
git status
```

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### status_resultat (66.75–77.74 s)

**Locució:** El fitxer apareix a la llista de fitxers nous sense seguir. Encara l’hem de seleccionar per incloure’l a la primera versió.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

## Llegim la comanda per parts (78.33–122.75 s)

**Animació:** Comanda gran i persistent: git, add i nom del fitxer. Es ressalta una part a cada explicació; després es prepara el contingut.

### add_objectiu (78.72–86.98 s)

**Locució:** Ara seleccionarem el contingut del fitxer que volem confirmar. Aquest pas s’anomena preparar.

**Pausa de lectura i assimilació:** 2 s; es manté el mateix visual.

### add_accio (86.98–97.50 s)

**Locució:** git add és l’ordre de preparació. El primer mot identifica el programa; el segon indica l’acció que li demanem.

**Pausa de lectura i assimilació:** 2.5 s; es manté el mateix visual.

### add_fitxer (97.50–109.00 s)

**Locució:** A continuació escrivim el nom del fitxer. Així seleccionem només aquest fitxer, en lloc de preparar tots els canvis del projecte.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### add_resultat (109.00–122.19 s)

**Locució:** Executem la comanda completa. El contingut actual queda preparat i el fitxer continua al seu lloc. Encara no hem creat cap commit.

**Comanda en pantalla:**

```bash
git add helloGit.py
```

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

## Desem la primera versió local (122.75–169.92 s)

**Animació:** La comanda es descompon en acció, opció -m i missatge. El commit apareix només després d’executar-la.

### commit_accio (123.14–133.40 s)

**Locució:** git commit crea una versió amb el contingut que hem preparat. Aquesta versió queda al repositori del nostre ordinador.

**Pausa de lectura i assimilació:** 2.5 s; es manté el mateix visual.

### commit_opcio (133.40–146.10 s)

**Locució:** El guionet ema introdueix el missatge del canvi. Escrivim el missatge entre cometes perquè la terminal el tracti com un sol argument.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### commit_missatge (146.10–157.62 s)

**Locució:** El missatge descriu què hem fet: afegir la salutació inicial. Ens ajudarà a reconèixer aquesta versió més endavant.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### commit_resultat (157.62–169.35 s)

**Locució:** Ara executem l’ordre. Apareix la primera versió a l’historial local, amb el seu identificador. El remot encara és buit.

**Comanda en pantalla:**

```bash
git commit -m "Afegeix la salutacio inicial"
```

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

## Llegim la versió registrada (169.92–182.50 s)

**Animació:** Git log complet amb extracte de hash i missatge. No s’introdueixen opcions noves.

### log (170.29–181.93 s)

**Locució:** git log permet consultar les versions registrades. A la sortida hi veiem l’identificador i el missatge que acabem d’escriure.

**Comanda en pantalla:**

```bash
git log
```

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

## Llegim també la comanda de publicació (182.50–243.29 s)

**Animació:** Comanda persistent i ressaltat successiu de push, origin, main i -u. El resultat s’observa amb una pausa pròpia.

### push_accio (182.90–195.46 s)

**Locució:** git push publica les versions confirmades en un repositori remot. La comanda que veus indica també on les volem enviar.

**Pausa de lectura i assimilació:** 2.5 s; es manté el mateix visual.

### push_remot (195.46–209.00 s)

**Locució:** origin és el nom que identifica el nostre remot. En aquest exemple, la connexió apunta al repositori del projecte a GitHub.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### push_branca (209.00–218.81 s)

**Locució:** main és la branca que volem publicar. Aquest nom coincideix amb la branca on estem treballant.

**Pausa de lectura i assimilació:** 2.5 s; es manté el mateix visual.

### push_seguiment (218.81–232.17 s)

**Locució:** El guionet u desa aquesta relació de seguiment. Als enviaments següents d’aquesta mateixa branca podrem escriure només git push.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### push_resultat (232.17–242.73 s)

**Locució:** Executem l’ordre completa. La mateixa versió que teníem al repositori local ara també apareix al remot.

**Comanda en pantalla:**

```bash
git push -u origin main
```

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

## Repetim els passos amb calma (243.29–336.83 s)

**Animació:** Una salutació modificada i un fitxer de notes nou. El punt de git add . s’explica amb subratllat, es preparen els dos fitxers i es confirmen junts.

### segon_canvi (243.67–254.06 s)

**Locució:** Canviem la salutació, desem i tornem a executar el programa. Encara només ha canviat el fitxer de treball.

**Comanda en pantalla:**

```bash
python3 helloGit.py
```

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### segones_notes (254.06–266.14 s)

**Locució:** També creem un fitxer de notes i el desem. Ara tenim un fitxer modificat i un fitxer nou. Encara no hem preparat aquests canvis.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### segon_add_punt (266.14–281.60 s)

**Locució:** Ara escrivim git add seguit d’un punt. El punt representa la carpeta actual i les seves subcarpetes. Com que som a l’arrel del projecte, l’ordre abasta tot el projecte.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### segon_add_fitxers (281.60–297.44 s)

**Locució:** Això permet preparar fitxers modificats, fitxers nous i eliminacions. En aquest cas, seleccionem el programa modificat i les notes noves. Els fitxers nous ignorats queden fora.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### segon_add (297.44–310.50 s)

**Locució:** Executem l’ordre. Els dos fitxers queden preparats en un mateix pas. Abans de confirmar, revisem que tots dos canvis són els que volem.

**Comanda en pantalla:**

```bash
git add .
```

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### segon_commit (310.50–323.44 s)

**Locució:** Creem el segon commit amb un missatge que descriu la salutació i les notes. L’historial conserva la primera versió i hi afegeix la nova.

**Comanda en pantalla:**

```bash
git commit -m "Personalitza la salutacio i afegeix notes"
```

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

### segon_push (323.44–336.28 s)

**Locució:** Finalment, git push envia aquesta versió al remot. Desar, preparar, confirmar i publicar han estat accions diferents.

**Comanda en pantalla:**

```bash
git push
```

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

## Tres comandes. Tres funcions. (336.83–358.21 s)

**Animació:** Tres targetes amb ressaltat successiu i espai després de cada funció.

### resum_preparar (337.23–343.59 s)

**Locució:** Preparar selecciona el contingut que entrarà a la versió següent.

**Pausa de lectura i assimilació:** 2.5 s; es manté el mateix visual.

### resum_confirmar (343.59–350.20 s)

**Locució:** Confirmar desa una versió a l’historial del nostre ordinador.

**Pausa de lectura i assimilació:** 2.5 s; es manté el mateix visual.

### resum_publicar (350.20–357.65 s)

**Locució:** Publicar comparteix les versions confirmades amb el repositori remot.

**Pausa de lectura i assimilació:** 3 s; es manté el mateix visual.

## Practica el cicle complet (358.21–373.67 s)

**Animació:** Petit exercici final sense pregunta ni resposta; les instruccions es mantenen visibles.

### practica (358.59–373.10 s)

**Locució:** Al teu repositori de pràctiques, canvia el missatge i repeteix aquests passos. Consulta l’historial abans i després per veure la versió que has afegit.

**Pausa de lectura i assimilació:** 4 s; es manté el mateix visual.
