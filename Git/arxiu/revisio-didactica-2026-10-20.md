> Document històric anterior a la reescriptura dels guions del 21 d’octubre.

# Revisió didàctica de les lliçons de Git

Revisió del 20 d’octubre de 2026. La sèrie té 26 lliçons (0–25). Les lliçons
0 i 1 ja s’han produït amb el nou estil i esperen valoració. Les millores
següents per a les altres 24 són propostes pendents d’aplicar. La guia acordada
és al [README](../README.md#guia-destil).

## Criteris comuns

- Fer visible el punt de partida, la branca activa i l’estat local o publicat.
- Explicar una acció cada vegada. Mantenir la comanda completa i subratllar
  cada part mentre s’explica: acció, paràmetre i valor. Per a `commit`, primer
  `commit`, després `-m` i finalment el text del missatge entre cometes.
- Donar 2–3 segons de lectura entre passos, ampliables segons el contingut.
  Mantenir la guia visual durant el silenci. No incloure preguntes.
- Conservar les referències visuals entre l’estat anterior i el resultat.
  Explicar també les consultes sense sortida.
- Utilitzar Andrew amb SSML explícit: català +5%, anglès +0% i pauses de
  500 ms en tots dos sentits quan canvia l’idioma. Conservar els accents catalans.
- Marcar els fragments anglesos entre cometes i en cursiva als subtítols;
  conservar la sintaxi literal de la terminal.
- Tancar amb una comprovació, fins a tres idees i una acció de pràctica.
  La durada pot superar dos minuts si l’exemple ho necessita.

## 00 · Introducció a Git

Aplicat: [episodi](../00-introduccio/episodi.json), **2:47**, 7 escenes.
Visió general de versions, historial, comparació, treball local i col·laboració.
Sense comandes ni requisits tècnics. Distingeix enregistrar una versió de desar
un fitxer i deixa la pràctica per a la lliçó següent.

## 01 · El primer commit

Aplicat: [episodi](../01-primer-commit/episodi.json), **6:14**, 11 escenes.
Punt de partida explícit, edició visible, consulta de l’estat, preparació,
commit local i publicació. `add`, `commit` i `push` es desglossen per parts.
`-m` té un pas propi abans d’explicar el missatge. El segon cicle incorpora
`git add .`, amb el punt subratllat i dos fitxers que es preparen junts. Les pauses i els resultats
s’ancoren als temps de la locució. L’exemple s’ha executat en repositoris temporals.

## 02 · Branques

Font: [episodi](../02-branques/episodi.json). Durada orientativa: **2:30–3:00**.

- Substituir la definició inicial per una etiqueta que apunta a un commit.
  Després mostrar com la branca activa avança amb els commits nous.
- Mantenir visible «Branca activa»; introduir `HEAD` com a indicador d’on
  estem treballant, sense desplegar encara tots els seus casos.
- Explicar que `main` és un nom de branca i que el seu paper de principal és
  una convenció del projecte. El nom no garanteix que el codi funcioni.
- Mostrar `git status --short` abans de l’intercanvi de branques. L’exemple
  utilitza feina confirmada; alguns canvis sense commit poden seguir-nos en
  canviar de branca. No s’han de presentar com a canvis ja desats en una branca.

**Frase proposada:** «Crear salutacio posa una segona etiqueta al mateix commit.
La branca avançarà quan hi fem el següent commit.»


## 03 · Desar, preparar i fer commit

Font: [episodi](../03-estats/episodi.json). Durada orientativa: **3:00–3:30**.

- Presentar les tres zones amb noms fixos: treball, preparació o índex,
  i últim commit. Són zones conceptuals; no tres fitxers que l’alumna hagi de crear.
- Mantenir el contingut V1, V2 i V3 llegible, amb la salutació i el comiat
  ressaltats. Fer visible que `add` copia un contingut concret a l’índex.
- Descompondre `MM helloGit.py`: primera columna, canvis preparats respecte de
  l’últim commit; segona, canvis del treball respecte de l’índex.
- Explicar que un fitxer nou no seguit és un altre cas, representat amb `??`.
  El commit desa la instantània preparada del projecte, inclosos els fitxers
  seguits que no hem modificat; no és només una llista de línies editades.


## 04 · Sincronització entre classe i casa

Font: [episodi](../04-sincronitzacio/episodi.json). Durada orientativa: **3:00–3:30**.

- Separar visualment les alternatives «crear una còpia amb clone» i «actualitzar
  una còpia existent amb pull». Mostrar sempre en quina carpeta s’executa l’ordre.
- Mantenir el mateix commit identificable als dos ordinadors i al servidor.
  La situació inicial de classe amb B es pot presentar com una anticipació;
  després cal indicar que tornem al moment d’editar i confirmar-lo.
- Fer visible que una edició sense commit no s’envia amb push. Mostrar la
  seqüència desar, preparar, confirmar i publicar amb resultats separats.
- Proposo `git pull --ff-only` en aquest cas sense divergències. El comportament
  queda explícit; si hi ha divergències, s’atura i cal decidir com integrar-les.
  [Referència: pull](https://git-scm.com/docs/git-pull).


## 05 · Merge

Font: [episodi](../05-merge/episodi.json). Durada orientativa: **2:30–3:00**.

- Ressaltar primer el destí: `git switch main`. Després assenyalar que el nom
  de `git merge salutacio` identifica la branca que volem incorporar.
- Desplaçar l’etiqueta main amb els nodes quiets per explicar el fast-forward.
  Es pot fer explícit amb `git merge --ff-only salutacio` per a aquest exemple.
- Donar una escena pròpia a l’alternativa amb divergències i explicar amb
  calma els dos pares del commit de merge. Separar-la amb «Un altre cas».
- Executar el programa a main després de la integració i mostrar que salutacio
  continua existint. Integrar i esborrar la branca són decisions diferents.


## 06 · Conflictes

Font: [episodi](../06-conflictes/episodi.json). Durada orientativa: **3:00–3:45**.

- Conservar el bon exemple de dues edicions de la mateixa línia. Explicar que
  un conflicte és una decisió de contingut pendent; encara no hi ha commit de fusió.
- Llegir els marcadors un per un: en aquest merge, `HEAD` correspon al costat
  actual main, el separador divideix les propostes i salutacio és l’altre costat.
- Animar l’edició fins a «Hola, grup!»: la resolució pot ser una tercera versió.
  Mostrar l’eliminació dels marcadors i la prova del programa abans d’add.
- Afegir una alternativa curta amb `git merge --abort` des del conflicte encara
  pendent, amb l’exemple iniciat net. Presentar-la en un panell separat del camí
  de resolució. Explicar que `add` prepara la decisió; no valida el seu significat.


## 07 · Rebase

Font: [episodi](../07-rebase/episodi.json). Durada orientativa: **3:00–3:45**.

- Fer una recapitulació breu de branca activa, base comuna i commits propis.
  Indicar des del principi que la branca és local i encara no s’ha compartit.
- Ensenyar què canvia un commit concret, per exemple el missatge del fitxer,
  i com aquell canvi es reaplica damunt del commit nou de main.
- Canviar «els nostres commits queden darrere» per «els canvis es recreen en
  commits nous després de D». Mantenir C i E atenuats i crear C′ i E′.
- Comparar merge i rebase des del mateix estat inicial i afegir `git rebase
  --abort` al cas condicional. Si hi ha més d’un conflicte, pot caldre repetir
  resolució, add i continue. [Referència: rebase](https://git-scm.com/docs/git-rebase).


## 08 · Stash

Font: [episodi](../08-stash/episodi.json). Durada orientativa: **2:30–3:00**.

- Fer servir dues targetes persistents: modificació d’un fitxer seguit i fitxer
  nou. Ressaltar `-u` quan el segon entra a l’stash; els ignorats queden fora.
- Mostrar el resultat de `stash list` i explicar què identifica `stash@{0}`.
- La petició de corregir main no arriba a executar-se a l’exemple actual.
  Indicar que s’omet aquella tasca o mostrar-la com un petit pas explícit,
  per conservar la continuïtat del relat.
- Mantenir el camí principal de pop correcte i afegir una explicació curta:
  si hi ha conflictes, l’entrada no s’elimina automàticament. `apply` és una
  alternativa quan volem conservar l’entrada. No demostrar una segona sessió
  completa. [Referència: stash](https://git-scm.com/docs/git-stash).


## 09 · Restore

Font: [episodi](../09-restore/episodi.json). Durada orientativa: **3:00–3:30**.

- Canviar «treure el fitxer de preparació» per «desfer la selecció dels canvis
  d’aquest fitxer»: el fitxer seguit continua tenint entrada a l’índex.
- Ressaltar origen i destinació: `--staged` copia HEAD a l’índex; l’ordre sense
  aquesta opció copia l’índex al treball. Conservar les fletxes actuals.
- Afegir una alternativa V3 al treball i V2 preparat: `git restore helloGit.py`
  retorna V2, encara que HEAD sigui V1. Això evita memoritzar «restore sempre
  torna a l’últim commit». [Referència: restore](https://git-scm.com/docs/git-restore).
- Mostrar la decisió de descartar abans d’executar l’ordre i comprovar després
  el diff que queda. Evitar presentar l’edició descartada com si continués desada.


## 10 · Revert

Font: [episodi](../10-revert/episodi.json). Durada orientativa: **2:45–3:15**.

- Conservar l’exemple publicat, el canvi invers i el nou commit que avança main.
- Afegir un cas compatible amb un commit posterior que només canviï notes.md.
  Revertir el canvi del programa mantenint les notes ajuda a distingir una
  inversió concreta d’un retorn de tot el projecte a una fotografia antiga.
- Mostrar el contingut que s’inverteix abans de fer revert i explicar
  `--no-edit` com l’acceptació del missatge automàtic.
- Separar trobar, revisar, revertir, provar i publicar. Comentar que revert
  també es pot utilitzar amb commits locals i que pot requerir resoldre conflictes.
  [Referència: revert](https://git-scm.com/docs/git-revert).


## 11 · Reset

Font: [episodi](../11-reset/episodi.json). Durada orientativa: **3:00–3:30**.

- Explicar `HEAD~1` sobre el graf lineal abans de pronunciar l’ordre completa.
- Comparar soft i mixed amb les mateixes tres zones i el mateix punt inicial C.
  Reiniciar l’esquema de manera visible abans de la segona alternativa.
- Acabar cada alternativa amb status i diff, interpretant-ne la sortida.
  La diferència és on queda preparat el canvi, no si el text continua al fitxer.
- Afegir una orientació breu: si només faltava completar l’últim commit local,
  també es pot valorar amend, que tindrà la seva lliçó. El focus aquí continua
  sent soft i mixed. [Referència: reset](https://git-scm.com/docs/git-reset).


## 12 · Reflog

Font: [episodi](../12-reflog/episodi.json). Durada orientativa: **2:30–3:00**.

- Recapitular el final concret del reset soft: main a B, amb treball i índex
  encara al contingut de C. No donar-ho per recordat.
- Mostrar log i reflog de costat i ressaltar una entrada concreta de cada un.
  Explicar què és el hash i què significa `HEAD@{1}` en aquella sortida.
- Mantenir la recuperació amb `git branch recuperacio <hash>` i indicar que
  crear la branca no la selecciona ni canvia els fitxers.
- Consultar `git show recuperacio:helloGit.py` com a comprovació sense canviar
  de branca. Mantenir la distinció actual entre commits recuperables, entrades
  locals amb caducitat i edicions que mai no s’han confirmat.


## 13 · Gitignore

Font: [episodi](../13-gitignore/episodi.json). Durada orientativa: **3:00–3:30**.

- Mostrar una carpeta curta amb el codi i els fitxers generats abans d’obrir
  status. Llegir `*.log` i `__pycache__/` assenyalant les parts del patró.
- Mantenir junts debug.log nou i app.log ja seguit durant tot l’exemple;
  aquesta diferència explica per què la mateixa regla produeix resultats diferents.
- Separar ignorar, deixar de seguir i confirmar la retirada. Després de `git
  rm --cached app.log`, mostrar el fitxer al disc i la D preparada a l’índex.
- Explicar que la retirada formarà part del commit compartit i que el fitxer
  continua als commits antics. `.gitignore` no elimina l’historial anterior.
  [Referència: gitignore](https://git-scm.com/docs/gitignore).


## 14 · Tags

Font: [episodi](../14-tags/episodi.json). Durada orientativa: **2:30–3:00**.

- Presentar una entrega provada abans d’etiquetar-la; el tag identifica un
  commit, sense certificar que el programa sigui correcte.
- Explicar `-a` i `-m` amb ressaltat de la comanda, i mostrar la informació
  addicional de l’etiqueta anotada a la sortida de show.
- Fer avançar main a C mentre v1.0 continua a B; després consultar el fitxer
  antic sense substituir el de treball.
- Separar clarament publicar la branca i publicar el tag. Esmentar en una
  frase que crear el tag no crea una Release de GitHub automàticament.


## 15 · Cherry-pick

Font: [episodi](../15-cherry-pick/episodi.json). Durada orientativa: **2:45–3:15**.

- Associar C a les notes de la feina pendent i D al diff concret de la correcció.
  Mostrar el contingut, a més dels nodes del graf.
- Fer explícit que es reaplica el canvi de D respecte del seu pare; no es
  porta tota la fotografia ni tota la branca d’origen.
- Ressaltar la branca receptora abans de l’ordre i comparar els pares de D i
  E després. D continua a la branca d’origen; E és nou en aquest exemple.
- Mantenir la comprovació de dependències i el programa funcionant sense les
  notes. El cas de conflicte ha de continuar separat del camí sense conflictes.


## 16 · Pull requests

Font: [episodi](../16-pull-requests/episodi.json). Durada orientativa: **3:30–4:15**.

- Identificar dues persones amb rols estables: autora i revisora. Mostrar les
  seves accions al costat del repositori on produeixen l’efecte.
- Dividir el recorregut en crear la branca, publicar, proposar, revisar,
  actualitzar i integrar. Deixar temps per llegir el diff i els comentaris.
- Fer que la petició de revisió expliqui un motiu: per exemple, un resultat que
  no coincideix amb l’esperat o una prova que falta. Una exclamació sola dona
  poc context sobre el valor de la revisió.
- Mantenir visible la mateixa PR quan arriba el segon push. La fusió remota i
  l’actualització de main local són passos diferents. El mètode de fusió escollit
  s’ha d’indicar. [Referència: pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).


## 17 · Blame

Font: [episodi](../17-blame/episodi.json). Durada orientativa: **2:45–3:15**.

- Conservar l’exemple actual: el darrer canvi d’espais no és l’origen de l’error.
  És una bona demostració de per què cal interpretar el resultat.
- Mantenir tres línies de codi numerades al costat de la sortida de blame.
  Assenyalar la línia seleccionada amb `-L 3,3` i explicar hash, autor i data.
- Animar la connexió entre la variable definida i la utilitzada abans de
  consultar el commit B. Fer llegibles els dos diffs en passos diferents.
- Tancar la investigació identificant el canvi que va introduir el problema.
  Deixar `blame -w` com a ampliació escrita opcional, sense carregar el recorregut.


## 18 · Bisect

Font: [episodi](../18-bisect/episodi.json). Durada orientativa: **3:15–3:45**.

- Definir una prova concreta i repetible abans de començar: mateixa execució,
  mateix criteri de funciona o falla i dos extrems coneguts.
- Mostrar el tram candidat que queda després de cada resposta. Donar temps
  per predir la següent reducció abans que Git seleccioni la versió següent.
- Mantenir dues etiquetes diferents: main continua a H i la versió de prova
  canvia. D i C són les seleccions d’aquest exemple, no una seqüència universal.
- Donar una escena clara a `git bisect reset` i recordar que el problema encara
  no s’ha corregit. Afegir una nota breu: si una versió no es pot provar, no
  s’ha de classificar a l’atzar; existeix `bisect skip`.
  [Referència: bisect](https://git-scm.com/docs/git-bisect).


## 19 · Amend

Font: [episodi](../19-amend/episodi.json). Durada orientativa: **2:30–3:00**.

- Mostrar què incloïa C i per què notes.md hi havia d’entrar. Revisar-ne el
  contingut preparat, a més del recompte de `--stat`.
- Explicar l’ordre per parts: `--amend` substitueix l’últim commit a la branca;
  `--no-edit` conserva el missatge.
- Mantenir B com a pare de C i C′; deixar temps perquè es vegi que no hem
  afegit C′ darrere de C i que l’identificador ha canviat.
- Separar la correcció només del missatge com a alternativa independent,
  amb índex sense altres canvis preparats. Mantenir el context de commit propi
  encara no publicat.


## 20 · Fetch

Font: [episodi](../20-fetch/episodi.json). Durada orientativa: **2:45–3:15**.

- Fixar la llegenda: origin és el remot configurat; main és la branca local;
  origin/main és la darrera posició coneguda localment de main a origin.
- Fer avançar origin/main amb fetch mentre main i el contingut de l’editor
  es mantenen quiets. Llegir el programa local abans i després.
- Descompondre `main..origin/main`: commits accessibles des d’origin/main que
  no tenim a main. Després comparar continguts amb diff, en una escena separada.
- Deixar la decisió d’integrar a l’alumna abans del merge explícit amb
  `--ff-only`. Relacionar-ho amb pull com a descàrrega seguida d’integració.


## 21 · Forks i upstream

Font: [episodi](../21-forks/episodi.json). Durada orientativa: **3:30–4:15**.

- Mantenir l’esquema local, fork i original durant tota la lliçó. Ressaltar
  una sola connexió quan es clona, es consulta o es publica.
- Diferenciar fork al compte de GitHub i clone a l’ordinador. Els noms origin
  i upstream són noms configurats en el clon de l’exemple.
- Explicar la diferència de vocabulari entre el remot anomenat upstream i la
  branca de seguiment configurada amb `push -u`; són usos diferents del terme.
- Afegir `git switch main` abans de sincronitzar-la i dividir fetch, merge i
  push en passos amb resultats visibles. A la PR final, llegir repositori i
  branca d’origen i de destinació.


## 22 · Rebase interactiu

Font: [episodi](../22-rebase-interactiu/episodi.json). Durada orientativa: **3:30–4:15**.

- Explicar per què les tres confirmacions descriuen una mateixa millora.
  L’objectiu és un historial comprensible, amb el mateix resultat final.
- Situar `HEAD~3` a B i ressaltar que la llista conté C, D i E, de més antic a
  més recent. No confondre-la amb l’ordre habitual de log.
- Distingir editor de llista, editor de missatge i terminal. `pick` i `squash`
  es canvien al fitxer obert; no són ordres de shell. Mostrar com desar i
  tancar l’editor triat per a la demostració.
- Donar temps als dos editors i a la comparació final. Mostrar el diff buit
  amb E i la prova del programa, a més del nou graf. Mantenir els conflictes
  com a alternativa explícita. [Referència: rebase](https://git-scm.com/docs/git-rebase).


## 23 · Add interactiu

Font: [episodi](../23-add-interactiu/episodi.json). Durada orientativa: **3:00–3:30**.

- Presentar un bloc de diff com una agrupació de línies relacionades.
  Mostrar el context suficient per distingir salutació i comiat.
- Deixar la pregunta de Git visible abans de respondre. Ressaltar y i n com
  respostes dins de la mateixa sessió interactiva.
- Reforçar que respondre n no desfà l’edició: el comiat continua al fitxer i
  queda fora de la preparació.
- Comprovar tant el diff preparat com el pendent abans de commit. Esmentar
  breument que els blocs no sempre surten separats; quan Git ofereix s, pot
  intentar dividir-los. La demostració principal conserva els dos blocs actuals.


## 24 · Worktree

Font: [episodi](../24-worktree/episodi.json). Durada orientativa: **3:15–3:45**.

- Obrir amb el mateix problema de canvi de tasca de stash i mostrar l’elecció:
  aquesta vegada mantenim dues carpetes disponibles alhora.
- Fer visible la ruta de la terminal i la branca activa en cada carpeta.
  Separar la carpeta principal de la branca anomenada main.
- Explicar la comanda llarga per parts: worktree add, branca nova, ruta i
  branca de partida. Ressaltar que cada carpeta té treball i índex propis,
  mentre comparteixen l’historial i les branques.
- Explicar abans del switch que main no està activa en un altre worktree.
  Després de retirar la carpeta auxiliar neta, consultar el commit de main.
  [Referència: worktree](https://git-scm.com/docs/git-worktree).


## 25 · Hooks

Font: [episodi](../25-hooks/episodi.json). Durada orientativa: **3:30–4:15**.

- Presentar el hook com un programa que Git executa en un moment concret:
  aquí, abans de crear el commit. Mostrar el resultat que el fa continuar o aturar-se.
- Dividir el codi en dues idees: llegir `:helloGit.py` de l’índex i comprovar-ne
  la sintaxi amb compile. El script complet queda consultable a l’exemple.
- Conservar els dos intents fallits: fitxer erroni preparat i fitxer corregit
  però encara sense tornar a fer add. Aturar-se per comparar editor i índex.
- Dir que l’exemple revisa només aquell fitxer, en un entorn amb Python i
  execució del hook configurats. El hook és local, no es distribueix amb push
  i es pot ometre; les comprovacions compartides del projecte necessiten la
  seva configuració. [Referència: hooks](https://git-scm.com/docs/githooks).


## Prioritats per aplicar la revisió

Primer, aclarir el punt de partida i el resultat de les lliçons 1, 3, 4, 9 i
20. Després, donar més temps a conflictes, rebase, reset i rebase interactiu.
Finalment, desenvolupar el recorregut de PR, forks, worktree i hooks.
Totes les lliçons incorporaran explicacions per passos, guies visuals i pauses de lectura; sense preguntes.

Es poden oferir itineraris de reproducció sense canviar números ni noms:

| Itinerari | Lliçons, en ordre recomanat |
| --- | --- |
| Bases i primers projectes | 0, 1, 3, 2, 4, 13 |
| Integració i actualització | 5, 6, 20 |
| Treball pendent i selecció | 8, 9, 23 |
| Completar, desfer i recuperar | 19, 10, 11, 12 |
| Col·laboració | 16, 21 |
| Organitzar l’historial i entregues | 7, 22, 14, 15 |
| Investigar errors | 17, 18 |
| Carpetes de treball i controls | 24, 25 |

## Temporització quan es produeixi la nova versió

L’allargament de la veu modifica la durada de les escenes i l’inici de les
següents. Les animacions actuals fan servir sovint una proporció del temps
de l’escena; això les adapta a una durada diferent, però no garanteix que el
ressaltat coincideixi amb la paraula adequada.

La producció revisada defineix moments explícits per a cada part de la
comanda, el subratllat, el resultat i les pauses de lectura. Els temps reals
de parla del servei permeten recalcular guió, SRT, animacions i muntatge.
El subtítol acaba amb la frase; durant la pausa es manté la guia visual.
La música inicial conserva els seus quatre segons. No s’hi incorporen preguntes.

Les propostes no impliquen substituir únicament la pista d’àudio dels MP4
actuals. L’aplicació inclou revisar els exemples modificats en repositoris
temporals i comprovar que comanda, sortida, graf i contingut continuen sent
coherents abans de la síntesi definitiva.
