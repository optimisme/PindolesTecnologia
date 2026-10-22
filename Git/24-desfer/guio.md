# Lliçó 24 · Desfer canvis: quina ordre triar

**Sèrie:** Píndoles de Git · **Capçalera:** DESFER CANVIS — Quina ordre triar en cada cas  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-quatrena lliçó. Desfer canvis.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a triar l’ordre adequada per desfer un canvi segons on és i si ja l’hem compartit. *(pausa 2.5 s)*

Ja coneixem diverses ordres per desfer canvis. En aquesta lliçó les ordenem per saber quan fer servir cadascuna. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Dues coses a mirar primer

Abans de desfer res, mirem on és el canvi, al treball, a la preparació o en un *commit*. I, si és en un *commit*, si ja l’hem publicat. *(pausa 3 s)*

**Visual:** Esquema de decisió amb dues preguntes en forma d’etiqueta, ON ÉS EL CANVI i JA ESTÀ PUBLICAT, sense signes d’interrogació.

## El canvi encara no està confirmat

Si només és al treball i no el volem, *git restore* amb el nom del fitxer el descarta. No es pot recuperar, perquè mai no l’hem confirmat. *(pausa 3 s)*

Si està preparat però encara no el volem confirmar, *git restore* amb doble guionet *staged* desfà la preparació i conserva l’edició. *(pausa 3 s)*

Si és feina a mitges que volem guardar per més tard, *git stash* l’aparca. *(pausa 3 s)*

**Visual:** Branca SENSE CONFIRMAR de l’esquema, amb les tres ordres git restore helloGit.py, git restore --staged helloGit.py i git stash.

## El canvi és en un commit que no hem publicat

Si a l’últim *commit* li falta alguna cosa o té el missatge malament, el completem amb *git commit* doble guionet *amend*. *(pausa 3 s)*

Si volem refer un o més *commits* locals, *git reset* fa tornar la branca enrere. Amb *soft* o *mixed*, els canvis continuen al treball. *(pausa 3 s)*

Si després d’un *reset* trobem a faltar un *commit*, el *git reflog* ens diu on era i una branca nova el recupera. *(pausa 3 s)*

**Visual:** Branca CONFIRMAT, NO PUBLICAT, amb git commit --amend, git reset --soft HEAD~1 i git reflog.

## El canvi ja està publicat

Si altres persones ja poden tenir el *commit*, no el traiem de l’historial. *git revert* crea un *commit* nou que en desfà l’efecte, i l’enviem amb un *push* normal. *(pausa 3 s)*

**Visual:** Branca PUBLICAT, amb git revert i una fletxa cap a git push.

## La regla que ho resumeix

*Amend*, *reset* i *rebase* reescriuen l’historial: només els fem servir amb feina pròpia que encara no hem compartit. Per a la feina compartida, desfem amb un *commit* nou. *(pausa 4 s)*

**Visual:** Taula de dues columnes, REESCRIU L’HISTORIAL · amend, reset, rebase / AFEGEIX UN COMMIT · revert.

## Resum final

Sense confirmar, *git restore*; per guardar-ho per més tard, *git stash*. *(pausa 2.5 s)*

En *commits* locals, *amend* o *reset*, i el *reflog* si cal recuperar-ne un. *(pausa 2.5 s)*

En *commits* publicats, *git revert*. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Escriu en un paper l’esquema de decisió amb un exemple propi per a cada cas. Després, prova-ne un parell en un repositori de pràctiques. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
