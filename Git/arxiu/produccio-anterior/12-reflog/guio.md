# Reflog: recupera un commit local

Veu: `ca-ES-EnricNeural` · Català · 91.9 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Continuació de l’alternativa soft de la lliçó 11: A–B–C, després git reset --soft HEAD~1. Main i HEAD són a B; treball i índex conserven V2 de C. C té hash il·lustratiu c95f4a7, B b62d8e1, A a31b2c4. Reflog local conté el reset i el commit C. No s’han expirat les entrades ni eliminat els objectes. Recuperacio és una branca nova. No es canvia de branca ni es descarten les edicions pendents. Els identificadors reals es copien del reflog.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.62 s)

**Locució:** Dotzena lliçó, Reflog.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## On ha anat a parar C? (6.6–17.6 s)

**Locució:** Continuem després del reset amb soft. Main és a B, però volem recuperar el commit C. Que no surti al log de main no vol dir que s’hagi esborrat immediatament.

**Animació:** Graf A–B–C, C atenuat i main B. Nota: canvis de C encara preparats.

## Log mostra el que arriba a main (17.6–27.1 s)

**Locució:** Git log segueix l’historial de la branca actual. Com que main apunta a B, veiem B i A. C ha quedat fora d’aquesta línia.

**Animació:** Terminal log B–A, graf C atenuat.

**Comandes en pantalla:**

```bash
git log --oneline
```

## Reflog recorda on era HEAD (27.1–37.0 s)

**Locució:** Git reflog mostra els moviments locals de HEAD. Hi veiem el reset a B i, just abans, el commit C. En copiem l’identificador.

**Animació:** Terminal reflog amb B HEAD@{0} reset: moving to HEAD~1, C HEAD@{1} commit: Canvia missatge. Ressaltar c95f4a7.

**Comandes en pantalla:**

```bash
git reflog
```

## Revisem C abans de recuperar-lo (37.0–48.2 s)

**Locució:** Amb show revisem el commit trobat. La diferència confirma que C havia canviat el missatge per Hola, Anna. Aquest és el commit que buscàvem.

**Animació:** Terminal git show c95f4a7, diff dels missatges. Hash etiquetat com a exemple.

**Comandes en pantalla:**

```bash
git show c95f4a7 -- helloGit.py
```

## Creem una branca a C (48.2–59.0 s)

**Locució:** Creem la branca recuperacio a l’identificador copiat. Això torna a donar una referència al commit C. Main continua a B i encara és la branca activa.

**Animació:** C torna a tenir color, apareix recuperacio a C, main i HEAD queden a B.

**Comandes en pantalla:**

```bash
git branch recuperacio c95f4a7
```

## C torna a aparèixer amb una branca (59.0–69.2 s)

**Locució:** Amb log i all veiem les dues branques. Recuperacio apunta a C. Hem recuperat un accés al commit sense moure main ni canviar de branca.

**Animació:** Terminal log --all mostra C recuperacio, B HEAD->main, A.

**Comandes en pantalla:**

```bash
git log --oneline --decorate --all
```

## Els canvis preparats es conserven (69.2–81.2 s)

**Locució:** Crear la branca tampoc modifica els fitxers ni la preparació. Els canvis que havia deixat el reset amb soft continuen preparats. Ho comprovem amb status.

**Animació:** Zones treball V2, preparació V2, HEAD V1. M primera columna. Branch recuperacio visible separat.

**Comandes en pantalla:**

```bash
git status --short
```

## Trobar, revisar i donar una referència (81.2–91.9 s)

**Locució:** Reflog és local i les entrades poden caducar. Pot ajudar a recuperar commits, però no és una còpia de seguretat de qualsevol edició sense confirmar.

**Animació:** Tres targetes: Reflog / Show / Branch. Nota final: commits locals disponibles; no qualsevol edició sense commit.
