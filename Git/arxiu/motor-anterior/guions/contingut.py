"""Guions revisats: contingut editorial, encara sense síntesi ni muntatge."""

def N(title, speech, visual, pause=3, mode='main'):
    return dict(kind='explanation', title=title, speech=speech, visual=visual, pause=pause, mode=mode)


def C(command, speech, parts, result, visual, mode='main', input_kind='terminal'):
    return dict(kind='command', title=command, command=command, speech=speech,
                parts=parts, result=result, visual=visual, mode=mode, input_kind=input_kind)


def A(result, filename='helloGit.py'):
    return C('git add '+filename, 'Amb [[git add]] seleccionem el contingut que volem confirmar.',
             [(filename,'El nom identifica el fitxer que preparem. La còpia desada ara és la que entra a la preparació.')],
             result, 'Conservar treball, preparació i historial. Copiar només el contingut seleccionat a la preparació.')


def M(message, result):
    spoken=message.replace('salutacio','salutació').replace('puntuacio','puntuació').replace('correccio','correcció').replace('Practica','Pràctica')
    return C('git commit -m "'+message+'"', 'Amb [[git commit]] enregistrarem el contingut preparat en una versió local.',
             [('-m','El guionet ema indica que a continuació escrivim el missatge del canvi.'),
              ('"'+message+'"','El text entre cometes descriu la feina: '+spoken+'. Les cometes agrupen el missatge en un sol argument.')],
             result, 'Subratllar commit, després -m i després el missatge. Crear el node nou només en executar.')


def T(result, detail=True):
    return C('git status --short', 'Consultem l’estat amb [[git status]]. Aquesta consulta no modifica el projecte.',
             [('--short','Doble guionet [[short]] demana la forma breu. La primera columna compara preparació i últim commit; la segona, treball i preparació.')] if detail else [],
             result, 'Mostrar la sortida literal amb les dues columnes separades i una llegenda; conservar els espais de davant de cada lletra.')


def W(branch, result, create=False):
    return C('git switch '+('-c ' if create else '')+branch, 'Amb [[git switch]] seleccionem la branca on treballarem.',
             ([('-c','El guionet ce crea una branca nova i hi canvia.')] if create else [])+
             [(branch,'Aquest és el nom de la branca de destinació. '+('La nova etiqueta comença al commit actual.' if create else 'Els fitxers s’actualitzaran a la versió seleccionada.'))],
             result, 'Mantenir tots els commits quiets. Moure l’indicador de branca activa i actualitzar l’editor després de l’execució.')


def P(result, branch=None):
    command='git push'+(' -u origin '+branch if branch else '')
    return C(command,'Amb [[git push]] compartim els commits de la branca amb el remot.',
             [('-u','El guionet u desa la relació de seguiment per als enviaments següents.'),
              ('origin','[[origin]] és el nom del remot al qual enviem els commits.'),
              (branch,'Aquest és el nom de la branca que publiquem.')] if branch else [],
             result,'Conservar el mateix identificador a local i remot. La fletxa envia commits; no envia edicions sense confirmar.')


LESSONS = {
2: dict(goal='Crear una branca, confirmar-hi una prova i recuperar les dues versions.',
 start='Repositori a main amb el programa original confirmat i cap canvi pendent. Els commits A i B del graf són identificadors didàctics.',
 stages=[
 N('Una idea nova, una línia de treball pròpia','Volem provar una salutació personalitzada i conservar la versió actual a [[main]]. Una branca ens permet identificar una línia de treball i continuar-la amb commits nous.','Editor amb print("Hello Git!") i una proposta encara no aplicada: print("Hola, Anna!").'),
 N('Una branca és una referència','Una branca és una etiqueta que apunta a un [[commit]]. En crear-ne una altra no dupliquem tots els fitxers ni creem un commit. Les dues etiquetes poden apuntar al mateix lloc.','Graf A–B, etiqueta main a B; afegir salutacio a B sense crear cap node.'),
 T('No surt cap línia: no hi ha canvis pendents detectats per Git. Això no és una prova del funcionament del programa.'),
 W('salutacio','La branca activa ara és salutació. [[main]] es conserva al mateix commit.',True),
 N('Editem i provem la funcionalitat','Canviem la salutació, desem el fitxer i executem el programa. Aquesta edició encara és al treball; cal preparar-la i confirmar-la.','Editor amb print("Hola, Anna!"); terminal python3 helloGit.py i sortida Hola, Anna!.'),
 A('La salutació nova queda preparada; encara no s’ha creat cap versió.'),
 M('Personalitza salutacio','El commit nou fa avançar salutació. [[main]] continua apuntant a la versió original.'),
 W('main','Reapareix la salutació original. El commit de la prova continua accessible des de salutació.'),
 W('salutacio','Recuperem la salutació personalitzada. Canviar de branca no ha esborrat cap de les dues versions.'),
 N('La branca activa importa','[[HEAD]] indica on estem treballant; en aquest exemple segueix la branca activa. Els noms de branca són convencions: dir-se [[main]] no garanteix que el programa funcioni.','HEAD unit a salutacio; main quieta. Mostrar el nom actiu també a la terminal. En aquest exemple canviem de branca amb el treball net.')],
 summary=['Crear una branca afegeix una etiqueta; no crea un commit.','Un commit fa avançar la branca activa.','Canviar de branca recupera la seva versió; integrar-la serà un pas posterior.'],
 practice='En un repositori de pràctiques net, crea una branca de prova, confirma una salutació diferent i alterna les dues branques per comparar els fitxers.'),
3: dict(goal='Distingir treball, preparació i historial, inclosa una edició posterior a add.',
 start='helloGit.py ja està confirmat amb la salutació original. Comencem sense canvis pendents. V1, V2 i V3 són continguts del mateix fitxer.',
 stages=[
 N('Tres zones del mateix projecte','Desar a l’editor modifica el treball. Preparar selecciona un contingut concret. Confirmar enregistra la instantània preparada a l’historial. Són tres funcions diferents.','Tres panells persistents: TREBALL, PREPARACIÓ i ÚLTIM COMMIT. Inicialment tots amb V1.'),
 N('Editem el treball','Canviem la salutació i desem. El treball ara conté V2. La preparació i l’últim commit encara contenen V1.','Editor V2: salutació personalitzada. Les altres zones mantenen la salutació original.'),
 C('git diff','[[git diff]] compara el treball amb la preparació.',[],'Hi veiem el canvi de salutació que encara no hem preparat. Els signes menys i més representen la línia anterior i la nova.','Fletxa PREPARACIÓ V1 → TREBALL V2. Llegenda textual per a - i +.'),
 A('Treball i preparació ara contenen V2. La preparació és una instantània seleccionada; no és un vincle que segueixi totes les edicions futures.'),
 C('git diff --staged','Ara comparem la preparació amb l’últim [[commit]].',[('--staged','Doble guionet [[staged]] selecciona aquesta altra comparació: últim commit respecte de preparació.')],'La salutació nova està preparada per entrar al següent commit.','Fletxa ÚLTIM COMMIT V1 → PREPARACIÓ V2.'),
 N('Desem una altra edició','Afegim una línia de comiat i desem. El treball passa a V3, però la preparació continua a V2. El comiat encara no està seleccionat.','Treball amb salutació i comiat; preparació amb salutació sola; historial V1.'),
 T('Apareixen dues emes al mateix fitxer. La primera indica canvis preparats; la segona, canvis al treball encara sense preparar. El cas de fitxer nou, representat amb dos interrogants, és diferent.'),
 C('git diff','Revisem el que encara queda fora de la preparació.',[],'Només apareix el comiat. El canvi de salutació ja no és pendent: és a la preparació.','Ressaltar només el comiat a TREBALL V3.'),
 M('Canvia salutacio','L’historial enregistra V2. El comiat continua al treball, sense confirmar. El commit no l’ha eliminat.'),
 A('Ara sí: seleccionem també el comiat i preparem V3.'),
 M('Afegeix comiat','Les tres zones coincideixen amb V3. La salutació i el comiat s’han registrat en commits diferents.')],
 summary=['Desar canvia el treball.','Add selecciona el contingut que hi havia en aquell moment.','Commit enregistra la preparació i conserva les altres edicions pendents.'],
 practice='Edita, prepara i torna a editar el mateix fitxer. Compara els dos diffs abans de confirmar per comprovar exactament què entrarà al commit.'),
4: dict(goal='Continuar un projecte entre dos ordinadors sense confondre clone, pull i push.',
 start='A classe tenim el repositori configurat amb main i origin. Treballem en sèrie i comprovem que no hi hagi canvis locals abans d’actualitzar.',
 stages=[
 N('Cada ordinador té una còpia local','L’ordinador de classe i el de casa tenen repositoris independents. [[GitHub]] és el punt de trobada. Desar o fer un commit en un ordinador no actualitza automàticament els altres.','Classe i casa amb el mateix commit A; servidor entre els dos. Les fletxes només apareixen quan s’executa push o pull.'),
 N('Acabem el canvi de classe','Editem la salutació, desem i provem el programa. El canvi és al treball de classe; primer el registrarem localment.','Editor de classe amb la versió nova, casa encara amb l’anterior.'),
 A('El canvi de classe queda preparat.'),M('Practica de classe','El commit B existeix a classe. El servidor i casa continuen a A.'),P('El servidor ja conté B. Casa encara no l’ha descarregat.'),
 N('Camí A: obtenir el projecte per primer cop','Si en aquest ordinador encara no tenim el projecte, el clonem una vegada. Aquest camí i el d’actualitzar una còpia existent són alternatives.','Panell CAMÍ A · CAP CÒPIA LOCAL. No fer clone i després repetir el camí B com si faltés encara el mateix commit.'),
 C('git clone <URL-del-repositori> HelloGit','[[git clone]] crea una còpia local amb fitxers i historial.', [('<URL-del-repositori>','Substituïm aquest marcador per l’adreça real del repositori. No escrivim els signes de menor i major.'),('HelloGit','Aquest argument tria el nom de la carpeta nova.')],'La còpia nova ja conté B i té el remot [[origin]] configurat.','Animar la creació de la carpeta i després la còpia de B. No presentar-ho com una carpeta buida.',mode='alternative:first-copy'),
 C('cd HelloGit','Entrem a la carpeta amb [[cd]].',[('HelloGit','És la carpeta creada pel clonatge. Les ordres següents s’executen des de dins.')],'La terminal queda situada al projecte.','Mostrar la ruta de la terminal actualitzada.',mode='alternative:first-copy'),
 N('Camí B: actualitzar una còpia existent','Si ja teníem el projecte a casa, entrem a la seva carpeta i revisem l’estat. En aquest exemple és net i no hi ha històries divergents.','Panell CAMÍ B · CÒPIA A CASA A A. Presentar explícitament un retorn a aquesta situació alternativa.'),
 T('No hi ha canvis locals pendents. Podem continuar l’actualització d’aquest exemple.'),
 C('git pull --ff-only','[[git pull]] descarrega les novetats i intenta incorporar-les.', [('--ff-only','Aquesta opció només permet avançar la branca directament. Si les històries divergeixen, s’atura i cal revisar la situació.')],'Casa incorpora B i els fitxers s’actualitzen. Ara podem continuar la pràctica.','Casa avança d’A a B després de la descàrrega. Mostrar el contingut nou a l’editor.'),
 N('La tornada també necessita sincronització','A casa fem un altre canvi, el preparem, el confirmem i el publiquem. Quan tornem a classe, actualitzem abans de continuar treballant.','Seqüència visual separada: edició → add → commit C → push → consulta d’estat a classe → pull --ff-only. Deixar un interval entre cada efecte.')],
 summary=['Clone crea la còpia local inicial.','Pull descarrega i integra segons l’opció triada.','Push comparteix commits; les edicions sense confirmar no viatgen.'],
 practice='Practica amb dos clons d’un repositori teu: confirma i publica en un, actualitza l’altre amb el treball net i comprova el mateix identificador als dos.'),
5: dict(goal='Integrar salutacio a main i distingir avançament directe i fusió amb dos pares.',
 start='Som a salutacio, amb el treball net. Main és a B i salutacio a C, descendent directe de B. La salutació nova està confirmada i provada.',
 stages=[
 N('Origen i destinació','Volem portar a [[main]] el canvi de salutació. La branca activa és la destinació del [[merge]]. Per això primer ens hi hem de situar.','Graf A–B–C; main a B, salutacio a C. Etiquetes ORIGEN i DESTINACIÓ.'),
 W('main','La destinació activa ara és [[main]]. La branca de salutació es conserva.'),
 C('git branch --show-current','Confirmem on som abans d’integrar.', [('--show-current','Aquesta opció mostra només el nom de la branca activa.')],'La terminal mostra [[main]]. Encara no hem integrat el canvi.','Ressaltar main tant a la sortida com al graf.'),
 C('git merge --ff-only salutacio','[[git merge]] incorporarà la història de la branca indicada.', [('--ff-only','Només acceptem un avançament directe: la destinació ha de ser un avantpassat de l’origen.'),('salutacio','És la branca que volem incorporar, no la que volem canviar automàticament a activa.')],'[[main]] avança de B a C. Les dues etiquetes apunten al mateix commit; no s’ha creat cap commit de fusió.','Moure només l’etiqueta main sobre el graf existent. Conservar salutacio i tots els nodes.'),
 C('python3 helloGit.py','Comprovem el resultat executant el programa.', [('helloGit.py','Provem el fitxer de la branca que acabem d’actualitzar.')],'A [[main]] també apareix la salutació personalitzada. La comprovació funcional complementa la consulta de l’historial.','Terminal amb Hola, Anna! i editor amb el mateix contingut.'),
 N('Un altre cas: dues branques han avançat','Partim ara d’un cas independent: [[main]] i salutació tenen commits diferents després de B. Ja no podem fer un avançament directe. Una fusió compatible pot crear M, un commit amb dos pares.','Separador UN ALTRE CAS. Tornar a B i dibuixar dos camins nous. No moure nodes del cas anterior per inventar el resultat.'),
 C('git merge salutacio','En aquest altre cas, la fusió combina dues històries compatibles.', [('salutacio','Incorporem aquesta branca a la destinació activa, que continua sent main.')],'El commit M té dos pares. Si les edicions fossin incompatibles, caldria resoldre el conflicte abans d’acabar.','Graf amb M connectat als dos extrems; indicar que l’editor pot demanar un missatge de fusió i s’ha de desar i tancar.',mode='alternative:divergent')],
 summary=['La branca activa rep la integració.','Un avançament directe mou l’etiqueta sense crear un commit.','Una fusió amb dos pares connecta històries divergents; la branca d’origen es conserva.'],
 practice='En un projecte de pràctiques net, crea un canvi en una branca i integra’l a main amb avançament directe. Revisa el graf i executa el programa.'),
6: dict(goal='Llegir un conflicte de merge, decidir el resultat i confirmar la resolució.',
 start='Treball net a main. Main i salutacio han canviat la mateixa línia des de B: Hola, classe! i Hola, Anna!, respectivament.',
 stages=[
 N('Dues propostes incompatibles','Les dues branques han modificat la mateixa línia de manera diferent. [[Git]] detecta que necessita una decisió sobre el contingut. Un conflicte pendent encara no és una fusió acabada.','Comparació de les dues línies amb els noms de branca visibles.'),
 C('git merge salutacio','Intentem integrar salutació a la branca activa.', [('salutacio','La proposta entrant és aquesta branca; la destinació continua sent main.')],'La fusió s’atura. No s’ha creat el commit que uneix els dos historials.','Terminal amb conflicte i graf sense node M.'),
 T('Dues us majúscules indiquen un fitxer encara sense resoldre en aquesta fusió. Llegim també el seu contingut.'),
 N('Llegim els marcadors per parts',['El primer marcador obre la versió del costat actual. En aquest merge, [[HEAD]] correspon a [[main]].','La línia central separa les dues propostes. El marcador final tanca la versió entrant, que és salutació. Aquests marcadors no són codi del programa.'],'Mostrar <<<<<<< HEAD, print("Hola, classe!"), =======, print("Hola, Anna!"), >>>>>>> salutacio. Subratllar un marcador cada vegada.',pause=3.5),
 N('Escrivim el resultat acordat','Decidim escriure Hola, grup! Eliminem tots els marcadors i deixem una sola instrucció vàlida. La resolució pot combinar les idees; no cal conservar una proposta sencera.','Animar l’edició fins a print("Hola, grup!"). No preparar el fitxer abans de mostrar aquesta decisió.'),
 C('python3 helloGit.py','Provem el contingut resolt abans de confirmar.',[],'La salutació final s’executa correctament. Encara falta preparar-la i acabar la fusió.','Sortida Hola, grup!; el graf continua sense M.'),
 A('La resolució queda preparada. Això informa Git que hem resolt el fitxer; no valida per si mateix que el programa sigui correcte.'),
 M('Resol conflicte','Ara sí: es crea el commit de fusió amb dos pares i el contingut revisat.'),
 N('Alternativa des del conflicte pendent','En un cas alternatiu podem abandonar una fusió encara sense acabar. Tornem a mostrar el moment del conflicte, abans de preparar-lo o confirmar-lo.','Separador ALTERNATIVA. Recuperar l’estat conflictiu original, no el resultat ja confirmat.'),
 C('git merge --abort','Cancel·lem la fusió pendent.', [('--abort','Aquesta opció abandona l’operació en curs. En el nostre exemple s’havia començat amb el treball net.')],'Recuperem l’estat anterior a intentar la fusió. Aquest camí no s’executa després de crear el commit de merge.','Retirar marcadors i indicador de fusió pendent sense crear cap node.',mode='alternative:abort')],
 summary=['Un conflicte assenyala una decisió de contingut pendent.','Cal editar, provar i preparar la resolució.','El commit acaba la fusió; avortar és un camí alternatiu anterior.'],
 practice='Reprodueix dues salutacions incompatibles en un repositori de pràctiques. Resol-les en una tercera salutació, prova el programa i completa la fusió.'),
7: dict(goal='Reaplicar commits propis sobre una base nova i reconèixer que els identificadors canvien.',
 start='Salutacio té C i E sobre B, encara sense publicar. Main ha avançat a D en un altre fitxer. Treball i preparació nets; els canvis principals són compatibles.',
 stages=[
 N('Una base que ha avançat','Volem continuar la nostra funcionalitat sobre les novetats de [[main]]. La branca de salutació té dos commits propis que encara no hem compartit.','B com a base; main a D, salutacio a E passant per C. Etiqueta NO PUBLICATS a C i E.'),
 W('salutacio','La branca que reescriurem és salutació. [[main]] serà la base i es mantindrà al seu lloc.'),
 C('git rebase main','[[git rebase]] reaplica els canvis de la branca activa sobre una altra base.', [('main','Aquest nom indica la base actualitzada. No és la branca a la qual estem incorporant la funcionalitat.')],'Els canvis de C i E es recreen com C prima i E prima després de D. Tenen pares i identificadors nous.','Atenuar C i E; dibuixar C′ i E′ a partir de D. No moure els nodes originals com si fossin els mateixos.'),
 N('Seguim un canvi concret','La salutació que introduïa C també existeix a C prima, ara aplicada sobre D. El contingut pot conservar-se, però l’historial és diferent perquè ha canviat el pare.','Comparar el mateix canvi de text a C i C′, i després ressaltar els pares B i D.'),
 C('git log --oneline --graph --all','Revisem l’historial després de l’operació.', [('--oneline','Mostra un resum de cada commit en una línia.'),('--graph','Dibuixa les connexions entre commits.'),('--all','Inclou les referències de totes les branques.')],'[[main]] continua a D i salutació apunta al final de la línia nova. Encara no hem integrat la funcionalitat a main.','Graf estable, llegenda per a les branques i hashes nous.'),
 N('Comparació amb merge','Des del mateix punt de partida, [[merge]] pot connectar els dos camins amb un commit de dos pares. [[Rebase]] reconstrueix els commits propis sobre la base nova.','Dos grafs laterals amb exactament el mateix estat inicial. No executar una operació després de l’altra.'),
 N('Cas condicional: apareix un conflicte','En una altra situació el rebase es pot aturar. Editem el contingut correcte, el provem i preparem la resolució abans de continuar.','Separador SI HI HA CONFLICTE; indicador REBASE PAUSAT. El camí principal anterior no tenia conflictes.'),
 C('git rebase --continue','Després de resoldre i preparar el fitxer, reprenem el rebase.', [('--continue','Continua l’operació pendent. Pot caldre resoldre més d’un conflicte, repetint el mateix procés.')],'L’operació avança amb els canvis resolts.','Mostrar prèviament git add helloGit.py i la prova, en passos separats.',mode='conditional:conflict'),
 C('git rebase --abort','Una altra opció és abandonar el rebase pendent.', [('--abort','Cancel·la aquesta operació i recupera l’estat de partida del cas mostrat.')],'Tornem a la branca anterior al rebase. Avortar i continuar són alternatives.','Bifurcació CONTINUAR / AVORTAR, sense executar les dues opcions seguides.',mode='alternative:abort')],
 summary=['Rebase canvia la base de la branca activa.','Els commits reaplicats tenen identificadors nous; main no es mou.','En aquest exemple només reescrivim feina pròpia encara no publicada.'],
 practice='En una branca local de pràctiques amb canvis compatibles, reaplica la teva feina sobre main. Compara el graf i prova el contingut resultant.'),
}

LESSONS.update({
8: dict(goal='Aparcar canvis pendents, canviar temporalment de tasca i recuperar-los.',
 start='Som a salutacio, al mateix commit que main. helloGit.py té una edició sense preparar i notes.md és nou. No hi ha canvis preparats ni fitxers ignorats que vulguem guardar.',
 stages=[
 N('La feina pendent té dues formes','Hem modificat el programa i creat unes notes. Encara no volem confirmar aquesta feina. L’aparcarem temporalment per poder canviar de tasca.','Dues targetes: helloGit.py MODIFICAT; notes.md NOU. Main i salutacio continuen a B.'),
 T('La modificació del programa apareix sense preparar i les notes apareixen com a fitxer nou. Cap dels dos canvis és a l’historial.'),
 C('git stash push -u -m "Salutacio pendent"','[[git stash push]] desa una entrada temporal amb la feina pendent.', [('-u','El guionet u inclou també els fitxers nous no seguits. Els fitxers ignorats queden fora.'),('-m','El guionet ema introdueix un missatge per identificar aquesta entrada.'),('"Salutacio pendent"','El text descriu la tasca aparcada: salutació pendent.')],'El programa recupera el contingut confirmat i les notes noves desapareixen del treball. Els canvis són a l’entrada temporal; la branca no avança.','Els dos continguts viatgen a una caixa STASH. Conservar main i salutacio a B.'),
 C('git stash list','Consultem les entrades amb [[git stash list]].', [],'La primera entrada apareix amb un identificador i el missatge que acabem d’escriure. És la feina aparcada, no un commit nou de la branca.','Ressaltar stash@{0} i Salutacio pendent com a dues parts de la mateixa entrada.'),
 W('main','Ara podem atendre l’altra tasca amb el treball net. En aquesta demostració ometem aquella correcció i tornem directament a la nostra feina.'),
 W('salutacio','Tornem a la branca de la funcionalitat abans de recuperar-hi els canvis.'),
 T('El treball continua net. Recuperarem l’entrada sobre aquest estat.',False),
 C('git stash pop','[[git stash pop]] intenta recuperar els canvis i retirar l’entrada si s’apliquen bé.', [],'Reapareixen la salutació modificada i les notes noves. Tornen a ser feina pendent, sense confirmar.','Obrir la caixa STASH i retornar cada contingut al seu fitxer. No crear cap node a la branca.'),
 C('git stash list','Comprovem la llista després de recuperar l’entrada.', [],'En aquest cas queda buida perquè l’aplicació ha estat correcta. Si hi hagués conflictes, l’entrada no s’eliminaria automàticament.','Mostrar llista buida amb la llegenda textual CAP ENTRADA; panell condicional separat per al conflicte.'),
 N('Conservar l’entrada és una altra opció','Amb [[git stash apply]] podem recuperar els canvis conservant l’entrada. És una alternativa a pop; no cal executar les dues ordres per recuperar la mateixa feina.','Comparació APPLY: conserva / POP: retira si s’aplica bé. No obrir una segona sessió d’operacions.')],
 summary=['Stash aparca feina pendent sense avançar la branca.','L’opció u inclou els fitxers nous no seguits, sense incloure els ignorats.','Recuperar els canvis els retorna al treball; encara caldrà confirmar-los.'],
 practice='Aparca una edició i un fitxer nou en un repositori de pràctiques. Consulta l’entrada, torna a la branca adequada i recupera-la amb el treball net.'),
9: dict(goal='Desfer la selecció d’un canvi o descartar una edició, identificant origen i destinació.',
 start='El programa ja és seguit. Últim commit V1; treball i preparació V2 després d’una edició i add. No hi ha altres canvis.',
 stages=[
 N('Dues destinacions diferents','Podem canviar la preparació o el treball. Abans d’executar [[restore]], identificarem quina zona volem restaurar i de quina versió copiem el contingut.','Tres panells V2 al treball i índex; V1 a l’últim commit.'),
 C('git restore --staged helloGit.py','Primer desfem la selecció del canvi, conservant l’edició del fitxer.', [('--staged','Aquesta opció tria la preparació com a destinació. Per defecte, copia el contingut de l’últim commit.'),('helloGit.py','Limitem la restauració a aquest fitxer; no desmarquem la resta del projecte.')],'La preparació torna a V1 i el treball conserva V2. El fitxer continua seguit; només hem desfet la selecció dels seus canvis.','Fletxa ÚLTIM COMMIT V1 → PREPARACIÓ. Cap fletxa cap al treball.'),
 T('La modificació ara apareix a la columna de treball, sense preparar. El contingut editat es conserva.'),
 C('git diff','Llegim el canvi que continua al fitxer.', [],'La salutació nova encara és al treball. Després de revisar-la, decidim que aquest canvi concret no el volem conservar.','Comparació V1 de la preparació amb V2 del treball. Mostrar la decisió DESCARTAR AQUESTA EDICIÓ abans de l’ordre següent.'),
 C('git restore helloGit.py','Ara restaurem el fitxer de treball.', [('helloGit.py','Sense staged, la destinació és el treball i l’origen per defecte és la preparació.')],'El treball torna a V1, perquè la preparació ja era V1. L’edició sense confirmar s’ha descartat.','Fletxa PREPARACIÓ V1 → TREBALL. Retirar V2 del panell de treball sense insinuar que s’ha guardat en un commit.'),
 T('Les tres zones coincideixen i no hi ha canvis pendents. L’historial no ha canviat.',False),
 N('Un altre cas: la preparació conté V2','En un cas independent, imaginem V1 a l’historial, V2 preparat i V3 al treball. Restaurar el treball des de la preparació recupera V2, no V1.','Separador CAS INDEPENDENT. Mostrar V1 / V2 / V3 i fletxa PREPARACIÓ V2 → TREBALL V2. No encadenar aquest exemple a l’anterior.')],
 summary=['Amb staged, restaurem la preparació i conservem l’edició del treball.','Sense staged, restaurem el treball des de la preparació per defecte.','Abans de descartar una edició, en revisem el contingut i la destinació.'],
 practice='En un fitxer de pràctiques, prepara una edició i desmarca-la conservant el treball. Revisa-la amb diff abans de decidir si la vols preparar de nou o descartar.'),
10: dict(goal='Desfer l’efecte d’un commit publicat amb un nou commit invers.',
 start='Main i origin/main són a C, un commit ordinari ja publicat que introdueix una variable sense definir. Treball net. c95f4a7 és un hash il·lustratiu.',
 stages=[
 N('Una correcció que també queda registrada','El canvi que falla ja està publicat i altres persones el poden tenir. En aquest exemple crearem un commit nou que en desfà l’efecte, mantenint la seqüència de l’historial.','Graf A–B–C al local i remot. C queda visible durant tota la demostració.'),
 T('Comencem sense edicions locals pendents. Així la correcció no barreja altres feines.'),
 C('git log --oneline','Busquem el canvi a l’historial.', [('--oneline','Mostra cada commit en una línia, amb identificador i missatge.')],'Localitzem C i copiem el seu identificador real. El hash escrit a la pantalla és només un exemple.','Ressaltar c95f4a7 amb una etiqueta HASH DE MOSTRA · COPIA EL TEU.'),
 C('git show c95f4a7 -- helloGit.py','Amb [[git show]] revisem el canvi abans de desfer-lo.', [('c95f4a7','És el commit que hem identificat.'),('--','El separador indica que tot seguit especifiquem un camí de fitxer.'),('helloGit.py','La consulta es limita al programa que estem investigant.')],'El canvi substituïa la salutació vàlida per una variable sense definir. Ja sabem quin efecte volem invertir.','Mostrar el diff amb l’abans i el després del mateix fitxer.'),
 C('git revert --no-edit c95f4a7','[[git revert]] aplica el canvi invers del commit indicat.', [('--no-edit','Accepta el missatge automàtic de la reversió, sense obrir l’editor.'),('c95f4a7','Indica el commit ordinari que volem revertir en aquest exemple.')],'Es crea D després de C. Main avança; C es conserva i D en desfà l’efecte.','Afegir D amb C com a pare. No moure main enrere ni esborrar C.'),
 C('python3 helloGit.py','Provem la versió resultant.', [],'La salutació torna a funcionar. La prova valida aquest comportament concret, no qualsevol altra part del projecte.','Sortida Hello Git! i contingut restaurat al programa.'),
 P('El remot incorpora D amb un enviament normal. Les altres còpies podran descarregar la correcció sense perdre l’historial compartit.'),
 N('L’abast és el canvi indicat','Revert no significa tornar qualsevol projecte sencer a una data. En aquest cas desfà l’últim canvi problemàtic. Amb commits posteriors compatibles, aquests es poden conservar.','Panell independent amb C, un canvi posterior només a notes.md i un commit invers de C; les notes es mantenen. No executar el cas alternatiu al projecte principal.')],
 summary=['Revert crea un commit invers nou.','L’original continua visible i la branca avança.','Després de provar la correcció, la publiquem com un commit més.'],
 practice='Reverteix un commit ordinari en un repositori teu de pràctiques. Compara el graf abans i després i comprova que el commit original encara hi és.'),
11: dict(goal='Comparar reset soft i mixed sense confondre què passa amb treball i preparació.',
 start='Main a C, commit propi no publicat, amb treball i preparació nets. B té la salutació original i C la personalitzada. Les dues opcions parteixen independentment de C.',
 stages=[
 N('Reprendre un canvi local','Volem continuar treballant en el contingut de l’últim commit propi, encara no publicat. Compararem dos tipus de [[reset]] que conserven el fitxer de treball.','Graf A–B–C; main i HEAD a C. Panells treball, preparació i historial amb V2.'),
 N('Llegim el punt de destinació','[[HEAD]] segueix main en aquest exemple. El sufix titlla u indica un pas enrere pel primer pare. Per tant, la destinació és B.','Subratllar HEAD i després ~1 a HEAD~1; assenyalar C i B amb una fletxa conceptual, sense executar encara.'),
 C('git reset --soft HEAD~1','Comencem per l’alternativa [[soft]].', [('--soft','Mou la branca i conserva tant la preparació com el treball.'),('HEAD~1','La destinació és el commit anterior al punt actual.')],'Main passa a B. El treball i la preparació continuen amb V2; el canvi queda preparat respecte de B.','Moure només main i HEAD. Conservar C atenuat fora de la línia actual, sense esborrar-ne l’objecte.',mode='alternative:soft'),
 C('git diff --staged','Comprovem el canvi que ha quedat preparat.', [('--staged','Compara la preparació conservada amb el nou últim commit, que és B.')],'La salutació personalitzada apareix com a canvi preparat. Podem editar-la, tornar a preparar-la i confirmar una versió nova.','Fletxa HISTORIAL V1 → PREPARACIÓ V2.',mode='alternative:soft'),
 N('Reiniciem la comparació a C','Ara tornem visualment al punt inicial: main a C, treball net i preparació V2. L’opció següent és una alternativa; no s’executa després de soft.','Separador TORNEM AL PUNT DE PARTIDA. Restaurar el dibuix inicial complet.'),
 C('git reset --mixed HEAD~1','Comparem l’alternativa [[mixed]].', [('--mixed','Mou la branca i restaura la preparació a la destinació. Conserva el treball.'),('HEAD~1','Des del punt inicial C, un pas enrere ens torna a B.')],'Main i preparació passen a B, però el treball manté V2. La salutació nova queda sense preparar.','Moure main i HEAD a B; copiar V1 a preparació; deixar V2 al treball.',mode='alternative:mixed'),
 N('La diferència és a la preparació','En tots dos casos la branca torna a B i el fitxer conserva V2. Soft deixa el canvi preparat; mixed el deixa pendent de preparar. C pot continuar com a objecte accessible localment.','Taula de dues files amb B / V2 / V2 per soft i B / V1 / V2 per mixed; etiquetes textuals, a més de colors.',pause=4)],
 summary=['En aquest exemple reset mou la branca local a B.','Soft conserva la preparació; mixed la restaura a B.','Tots dos conserven el treball; les alternatives es comparen des del mateix inici.'],
 practice='Reprodueix cada alternativa en un repositori de pràctiques separat, amb un últim commit no publicat. Compara treball, índex i historial abans de continuar.'),
12: dict(goal='Trobar un commit al reflog i donar-li una branca sense perdre canvis preparats.',
 start='Continuació de reset soft: main i HEAD a B, mentre treball i preparació conserven el contingut de C. Les entrades locals encara existeixen. recuperacio serà una branca nova.',
 stages=[
 N('Un commit fora de la línia actual','C ja no surt al recorregut de main després del reset. Això no vol dir que el seu objecte s’hagi esborrat immediatament. Buscarem una referència local anterior.','Graf A–B amb main a B; C atenuat. Treball i preparació amb el contingut de C.'),
 C('git log --oneline','Consultem la història accessible des de la branca activa.', [('--oneline','Cada commit es resumeix en una línia.')],'Només veiem B i A en aquesta línia. Aquesta consulta no busca tots els moviments locals anteriors.','Ressaltar el camí recorregut des de main; deixar C fora d’aquest recorregut.'),
 C('git reflog','[[git reflog]] mostra moviments locals de la referència consultada; aquí, [[HEAD]].', [],'Hi veiem el reset a B i l’entrada anterior de C. Copiem l’identificador de C, no el del reset.','Ressaltar primer la fila reset i després la fila del commit anterior; hash de mostra c95f4a7.'),
 C('git show c95f4a7 -- helloGit.py','Revisem el commit trobat abans de recuperar-lo.', [('c95f4a7','Substituïm el hash de mostra pel que hem copiat del nostre reflog.'),('helloGit.py','Consultem el canvi del programa en aquell commit.')],'La diferència correspon a la salutació personalitzada que buscàvem. La consulta no modifica els fitxers.','Diff de C i editor actual visibles alhora.'),
 C('git branch recuperacio c95f4a7','Creem una branca que torni a donar accés a C.', [('recuperacio','És el nom de la branca nova: recuperació.'),('c95f4a7','Indica el commit on situem la nova etiqueta.')],'Recuperació apunta a C. Main continua a B i segueix sent la branca activa; no hem canviat de branca.','Afegir només l’etiqueta recuperacio a C. Conservar HEAD unit a main.'),
 C('git log --oneline --decorate --all','Comprovem les referències de les dues branques.', [('--decorate','Mostra els noms de les referències al costat dels commits.'),('--all','Inclou les branques que no són l’activa.')],'C torna a ser visible a través de recuperació. Els canvis preparats i els fitxers continuen com abans.','Main a B, recuperacio a C i preparació intacta.'),
 T('El canvi que havia deixat reset soft continua preparat. Crear la branca no l’ha descartat.'),
 N('Una ajuda local amb límits','El reflog és local i les entrades poden caducar. Ajuda a recuperar referències a commits disponibles; no desa qualsevol edició que no hàgim confirmat.','Icona LOCAL, rellotge i distinció COMMIT EXISTENT / EDICIÓ SENSE CONFIRMAR.')],
 summary=['Log recorre l’historial accessible des d’una referència.','Reflog permet investigar moviments locals anteriors.','Crear una branca al commit trobat no canvia automàticament el treball ni la branca activa.'],
 practice='Després d’un reset soft de pràctiques, localitza el commit al reflog, revisa’l i crea una branca de recuperació sense canviar-hi amb feina pendent.'),
13: dict(goal='Ignorar fitxers generats i distingir fitxers nous dels que Git ja seguia.',
 start='Exemple independent: helloGit.py i app.log ja seguits. app.log té una edició sense preparar. debug.log i __pycache__/ són nous. Encara no hi ha .gitignore.',
 stages=[
 N('Separar el codi dels fitxers generats','Volem versionar el codi i les regles del projecte. Els registres d’execució i la memòria cau nous no han d’entrar a cada commit.','Quatre targetes amb estat: codi seguit, app.log seguit, debug.log nou i __pycache__/ nou.'),
 T('El registre nou i la memòria cau apareixen com a fitxers no seguits. El registre antic també apareix, però com a fitxer seguit modificat.'),
 N('Escrivim les regles al projecte',['Creem el fitxer punt [[gitignore]]. Escrivim una regla per línia. Asterisc punt [[log]] selecciona noms acabats en aquesta extensió.','La regla de memòria cau acaba en barra i selecciona aquestes carpetes. El fitxer de regles també es pot confirmar perquè el projecte comparteixi els criteris.'],'Editor .gitignore amb dues línies literals: *.log i __pycache__/. Ressaltar primer l’asterisc i després la barra.'),
 T('El registre nou i la memòria cau ja no apareixen. El fitxer de regles sí, perquè encara és nou. El registre antic continua modificat.',False),
 C('git check-ignore -v debug.log','Investiguem la regla que afecta el registre nou.', [('-v','El guionet ve demana informació detallada de la regla.'),('debug.log','Aquest argument indica el fitxer nou que estem consultant.')],'La sortida identifica el fitxer de regles, la línia i el patró que coincideix.','Separar visualment .gitignore, número de línia, *.log i debug.log. La locució diu registre o punt log; no interpreta l’extensió com logaritme.'),
 N('Una regla no deixa de seguir un fitxer','El registre antic ja formava part dels commits. La regla filtra fitxers no seguits, però no en retira automàticament un que ja estava versionat.','Conservar app.log ressaltat com SEGUIT i debug.log com NO SEGUIT IGNORAT.'),
 C('git rm --cached app.log','Decidim deixar de versionar el registre antic, conservant-ne la còpia local.', [('--cached','Aquesta opció retira el fitxer de la preparació sense esborrar-lo del disc.'),('app.log','És el registre que ja estava seguit. En aquest exemple la seva còpia preparada coincidia amb l’últim commit.')],'Queda preparada la retirada del fitxer del repositori. La còpia local continua existint.','Retirar app.log de l’índex; mantenir-lo al treball. Mostrar una D preparada, sense animació d’esborrat al disc.'),
 A('Preparem també les regles noves. La retirada del registre ja era preparada.','.gitignore'),
 M('Ignora fitxers generats','El commit enregistra les regles i la retirada del registre. La còpia local del registre es conserva i ara queda ignorada com a fitxer no seguit.')],
 summary=['Gitignore filtra fitxers no seguits que coincideixen amb les regles.','Les regles també es poden compartir amb un commit.','Retirar un fitxer ja versionat és una decisió separada; cached conserva la còpia local.'],
 practice='En un projecte de pràctiques, crea un registre nou i una regla per ignorar-lo. Comprova la coincidència i contrasta el resultat amb un fitxer que ja estigui seguit.'),
})

LESSONS.update({
14: dict(goal='Marcar una entrega amb una etiqueta anotada i compartir-la explícitament.',
 start='Main i origin/main són a B, amb el treball net i el programa provat. Encara no existeix v1.0. Exemple independent de les altres lliçons.',
 stages=[
 N('Un nom per a una entrega concreta','Hem acabat una entrega i volem reconèixer aquest punt quan el projecte continuï canviant. Una etiqueta identifica un commit concret de l’historial.','Graf A–B; main a B. Targeta ENTREGA amb el programa original provat.'),
 T('No hi ha canvis pendents. L’etiqueta assenyalarà el commit existent; una edició sense confirmar no hi entraria.'),
 C('git tag -a v1.0 -m "Primera entrega"','Creem una etiqueta amb [[git tag]].', [('-a','El guionet a crea una etiqueta anotada, amb informació pròpia sobre l’etiqueta.'),('v1.0','Aquest és el nom de l’entrega: versió u punt zero.'),('-m','El guionet ema introdueix el missatge de l’etiqueta.'),('"Primera entrega"','El missatge descriu què representa aquest punt del projecte.')],'L’etiqueta apunta a B. L’etiqueta anotada té informació pròpia, però no afegeix un commit a la línia de main.','Afegir una etiqueta v1.0 al costat de B sense crear un node de commit addicional.'),
 C('git show v1.0','Revisem l’etiqueta creada.', [('v1.0','El nom permet consultar la informació de l’etiqueta i el commit associat.')],'Hi veiem les dades de l’etiqueta anotada i el commit B. Això identifica l’entrega que acabem de marcar.','Separar DADES DE L’ETIQUETA i COMMIT ASSOCIAT a la sortida.'),
 N('Continuem treballant després de l’entrega','Editem i desem la salutació nova. Preparem el fitxer i confirmem el canvi. La branca avançarà amb aquest commit; l’etiqueta no es mourà.','Editor amb print("Hola, Anna!") abans de mostrar add i commit.'),
 A('La salutació nova queda seleccionada per al següent commit.'),M('Canvia missatge','Main avança a C. La versió u punt zero continua assenyalant B.'),
 C('git show v1.0:helloGit.py','Llegim el contingut d’aquella entrega sense canviar el treball.', [('v1.0','Abans dels dos punts indiquem la versió.'),('helloGit.py','Després dels dos punts indiquem el camí del fitxer dins d’aquella versió.')],'La consulta mostra la salutació original de B. L’editor actual conserva la salutació nova de C.','Dos panells: CONSULTA DE V1.0 / FITXER ACTUAL. Cap fletxa que sobreescrigui el treball.'),
 P('La branca main queda publicada amb C. Ara compartirem l’etiqueta amb una ordre explícita.'),
 C('git push origin v1.0','Publiquem l’etiqueta al remot.', [('origin','És el remot del projecte.'),('v1.0','Especifiquem l’etiqueta que volem enviar, en lloc d’una branca.')],'El remot també pot identificar B amb el nom de l’entrega. Això no crea per si sol una publicació de tipus [[Release]] a GitHub.','Mostrar main a C i v1.0 a B tant al local com al remot.')],
 summary=['Una branca pot avançar; l’etiqueta conserva el punt de l’entrega.','L’etiqueta anotada té informació pròpia sense afegir un commit.','En aquest exemple publiquem l’etiqueta explícitament.'],
 practice='Marca una entrega provada amb una etiqueta anotada. Fes un commit posterior i consulta el fitxer de l’etiqueta sense modificar l’editor actual.'),
15: dict(goal='Reaplicar una correcció independent a una altra branca sense integrar la feina anterior.',
 start='Main a B amb un error. Salutacio té C, que afegeix notes d’una funcionalitat pendent, i D, que corregeix només el programa. Treball net; el canvi de D no depèn de C.',
 stages=[
 N('Una correcció útil dins d’una altra feina','La branca de prova conté una funcionalitat pendent i una correcció que necessitem a main. Portarem només el canvi de la correcció, després de comprovar que sigui independent.','Graf main a B; salutacio a D amb C entremig. C: notes.md; D: correcció de helloGit.py.'),
 C('git log --oneline salutacio','Identifiquem el commit de la correcció.', [('--oneline','Mostra el resum de cada commit.'),('salutacio','Consultem la història d’aquesta branca, sense canviar-hi.')],'Copiem l’identificador de D. El hash d04f7a2 és una mostra; en un projecte propi copiem el real.','Ressaltar D i deixar C visible com FEINA PENDENT.'),
 C('git show d04f7a2 -- helloGit.py','Revisem què modifica D.', [('d04f7a2','És el commit seleccionat.'),('helloGit.py','La consulta es limita al fitxer del programa, després del separador de camins.')],'La correcció no necessita les notes de C. Aquest exemple permet aplicar-la independentment.','Diff de D amb només la correcció; panell notes.md exclòs.'),
 T('No hi ha feina local pendent que es barregi amb l’operació.'),W('main','La correcció s’aplicarà a main, que és la branca activa.'),
 C('git cherry-pick d04f7a2','[[git cherry-pick]] reaplica el canvi del commit indicat a la branca activa.', [('d04f7a2','Indiquem D, no el seu pare C ni tota la branca de salutació.')],'Es crea E a main amb pare B. El seu identificador és nou; D continua a la branca original amb pare C.','Conservar C i D. Crear E com a fill de B i dibuixar una relació conceptual de canvi D → E, diferent d’una relació de pare.'),
 C('python3 helloGit.py','Comprovem la correcció aplicada.', [],'El programa funciona a main i les notes de C no hi han entrat. Aplicar un canvi concret no substitueix la prova del resultat.','Sortida vàlida i llista de fitxers sense notes.md a main.'),
 N('Camí condicional: resoldre o abandonar','Si l’aplicació s’atura per un conflicte, revisem el fitxer, escrivim el resultat correcte, el provem i el preparem. Després podem continuar l’operació pendent.','Panell condicional amb passos editor → prova → git add helloGit.py, separats i amb espera.'),
 C('git cherry-pick --continue','Reprenem una aplicació pausada després de preparar la resolució.', [('--continue','Continua el cherry-pick pendent; no inicia una segona selecció de commits.')],'La correcció queda confirmada amb la resolució revisada.','Només camí CONTINUAR del cas conflictiu.',mode='conditional:conflict'),
 C('git cherry-pick --abort','En lloc de continuar, podem abandonar l’operació pendent.', [('--abort','Recupera el punt de partida d’aquest cherry-pick.')],'No s’aplica la correcció en aquest camí alternatiu.','Bifurcació AVORTAR des del conflicte, sense executar-la després de continue.',mode='alternative:abort')],
 summary=['Seleccionem un canvi concret i en revisem les dependències.','La branca activa rep un commit nou amb un pare diferent.','La branca original es conserva i cal provar el resultat reaplicat.'],
 practice='En un repositori de pràctiques, prepara una correcció independent d’un altre canvi. Reaplica només la correcció a main i comprova els fitxers de les dues branques.'),
16: dict(goal='Publicar una branca, obrir una proposta, revisar-la i incorporar la versió acordada.',
 start='Projecte ja clonat, main actualitzada i treball net. Tenim permís per publicar branques al mateix repositori i una altra persona revisarà la proposta.',
 stages=[
 N('Una proposta abans d’integrar','Una [[pull request]] proposa incorporar canvis entre branques i ofereix un espai per revisar-los. Publicar una branca i integrar-la són passos diferents.','Esquema main / salutacio / PROPOSTA. Encara no moure main.'),
 T('Comencem amb main al dia i sense canvis pendents.'),W('salutacio','Treballarem en una branca pròpia perquè es pugui revisar per separat.',True),
 N('Mostrem el canvi abans de confirmar','Editem el programa per personalitzar la salutació i el provem. L’edició visible és la que després seleccionarem per al commit.','Editor print("Hola, Anna") i execució amb sortida coincident.'),
 A('La salutació personalitzada queda preparada.'),M('Millora la salutacio','El canvi és un commit local de salutació; main continua al punt inicial.'),P('La branca ja és al remot i es pot comparar amb main. Encara no l’hi hem integrat.','salutacio'),
 N('Triem origen i destinació',['A la interfície obrim una proposta amb [[main]] com a branca de destinació. La branca de comparació és salutació, que conté el nostre canvi.','Escrivim un títol, expliquem la millora i indiquem com l’hem provat. Revisem el diff abans de crear la proposta.'],'Esquema de formulari: base main; compare salutacio. Subratllar primer destinació, després origen. Text complet d’exemple: Personalitza la salutació; prova: python3 helloGit.py.',pause=3.5),
 N('La revisió concreta el resultat','La persona revisora proposa afegir una exclamació. Editem la mateixa branca, desem, provem la salutació amb exclamació i preparem el canvi.','Comentari docent simulat i editor print("Hola, Anna!"). No simular una aprovació anterior com si cobrís automàticament aquesta nova versió.'),
 A('La millora demanada queda preparada.'),M('Completa la salutacio','El commit nou completa la mateixa branca de la proposta.'),P('La mateixa pull request incorpora el commit nou. No cal obrir una proposta diferent.'),
 N('Revisem la versió actualitzada','Després de revisar l’actualització i complir els requisits del repositori, una persona amb permís pot integrar-la. En aquest exemple es crea un commit de merge.','Interfície esquemàtica amb nova revisió i Create a merge commit. Graf remot amb M i dos pares. No actuar sobre cap servei real.'),
 W('main','La nostra branca local main encara ha d’incorporar la fusió del remot.'),
 C('git pull --ff-only','Actualitzem la còpia local de main.', [('--ff-only','L’avançament directe és possible perquè el main local no ha divergit.')],'Main local incorpora M i el programa mostra el resultat revisat.','Fer coincidir el mateix M al remot i al local; executar la prova final.')],
 summary=['La branca publicada permet comparar la proposta.','Un push a la mateixa branca actualitza la proposta existent.','Revisió i integració són passos explícits; després actualitzem el main local.'],
 practice='Amb un repositori de pràctiques i una persona col·laboradora, publica una branca, revisa la diferència i actualitza la mateixa proposta amb una millora petita.'),
17: dict(goal='Investigar una línia amb blame i comprovar la causa amb show i el context.',
 start='Historial A–B–C. B canvia la definició salutacio per missatge, però deixa l’ús antic. C només afegeix espais a la línia d’impressió. Treball net; hashes il·lustratius.',
 stages=[
 N('Una línia que falla té un context','El programa imprimeix una variable que ja no està definida amb aquell nom. Investigarem les línies relacionades i els commits que les han modificat.','Editor amb línies numerades: 1 comentari; 2 missatge = "Hola, Anna!"; 3 print( salutacio ).'),
 C('python3 helloGit.py','Reproduïm el problema amb la mateixa prova.', [],'La terminal mostra un error de nom a la línia tres. La línia de l’error orienta la investigació, però encara no identifica la causa històrica.','Ressaltar NameError i línia 3 sense atribuir responsabilitats.'),
 C('git blame helloGit.py','[[git blame]] associa les línies a commits de l’historial consultat.', [('helloGit.py','Consultem les línies del programa actual.')],'La línia tres s’associa a C. Això indica una modificació de la línia, no una demostració que C introduís l’error.','Separar columnes hash, autoria, data i contingut. La columna d’autoria es mostra com a context, sense llenguatge de culpabilitat.'),
 C('git blame -L 3,3 helloGit.py','Limitem la consulta a la línia de l’error.', [('-L','El guionet ela limita la consulta a un rang de línies.'),('3,3','El primer número és l’inici i el segon el final; aquí consultem només la línia tres.')],'Copiem l’identificador de C per revisar què hi va canviar.','Subratllar -L, després el rang i després la fila de la sortida.'),
 C('git show c95f4a7 -- helloGit.py','Comprovem el canvi concret de C.', [('c95f4a7','És el commit de mostra atribuït a la línia tres.')],'C només hi havia afegit espais. La variable ja era incorrecta abans d’aquell retoc.','Diff C amb print(salutacio) → print( salutacio ). Destacar els espais com a canvi de format.'),
 C('git blame -L 2,2 helloGit.py','Seguim la dependència: la línia que defineix la variable.', [('2,2','Ara consultem només la línia dos, on es defineix el nom utilitzat pel programa.')],'Aquesta línia ens porta a B. El nom definit i el nom imprès no coincideixen.','Unir amb una fletxa missatge de la línia 2 i salutacio de la línia 3.'),
 C('git show b62d8e1 -- helloGit.py','Revisem el canvi de B.', [('b62d8e1','És el commit que modificava la definició de la variable.')],'B va canviar el nom sense actualitzar-ne l’ús. Ja tenim una explicació del canvi que introdueix la regressió.','Diff B amb la definició anterior i la nova; mantenir la línia d’impressió visible.')],
 summary=['Blame orienta cap a modificacions de línies.','Show explica què canviava el commit concret.','Cal seguir el context i les dependències abans d’atribuir l’origen d’un error.'],
 practice='Investiga dues línies relacionades d’un fitxer de pràctiques. Revisa els commits amb show i anota el canvi funcional, separant-lo dels retocs de format.'),
18: dict(goal='Localitzar el primer commit que falla amb una prova repetible i sortir de la cerca.',
 start='Historial lineal A–H, main a H i treball net. La mateixa prova funciona a v1.0, situada a A, i falla a H. D introdueix l’error i aquest persisteix fins a H.',
 stages=[
 N('Acotar una regressió amb una prova','Coneixem una versió que funciona i una que falla. [[Bisect]] tria versions intermèdies per reduir el tram que investiguem. La prova ha de ser la mateixa a cada pas.','Graf A–H; A FUNCIONA, H FALLA. Prova fixa: python3 helloGit.py.'),
 T('No hi ha canvis locals que es puguin barrejar amb els canvis temporals de versió.'),
 C('git bisect start','Iniciem la sessió de cerca.', [('start','Aquesta subordre inicia la investigació; encara hem d’indicar els dos límits.')],'La sessió queda oberta, pendent de classificar els extrems.','Indicador CERCA ACTIVA. Main encara és a H.'),
 C('git bisect bad','Classifiquem l’extrem actual com a fallada coneguda.', [('bad','Indica que la prova falla en el commit actual, que és H.')],'H es converteix en el límit que falla.','Ressaltar H amb etiqueta FALLA, a més del color.'),
 C('git bisect good v1.0','Indiquem la versió que ja hem provat com a correcta.', [('good','Indica que aquesta versió supera la mateixa prova.'),('v1.0','L’etiqueta assenyala A, l’extrem conegut que funciona.')],'En aquest historial Git selecciona D per provar-lo. Main continua a H; canvia temporalment la versió de treball.','HEAD separat a D, main quieta a H. No presentar sempre D com la selecció de qualsevol projecte.'),
 C('python3 helloGit.py','Executem exactament la mateixa prova a D.', [],'La prova falla amb l’error de nom. Comuniquem aquest resultat a la cerca.','Terminal amb error i interval A–D ressaltat.'),
 C('git bisect bad','Marquem D com a versió que falla.', [],'Git redueix el tram i, en aquest exemple, selecciona C.','HEAD separat passa a C; main continua a H.'),
 C('python3 helloGit.py','Provem C de la mateixa manera.', [],'La salutació funciona. Ara classifiquem aquesta versió com a correcta.','Sortida Hello Git!, sense canviar la prova.'),
 C('git bisect good','Marquem el resultat correcte de C.', [],'C i D són consecutius: D és el primer que falla dins del tram investigat. Això localitza un canvi per revisar; encara no l’hem corregit.','Ressaltar D com a RESULTAT. Conservar HEAD a C, que és l’últim commit provat en aquesta seqüència.'),
 C('git show d04f7a2 -- helloGit.py','Revisem el canvi identificat.', [('d04f7a2','Substituïm el hash de mostra pel que ha trobat la nostra cerca.')],'El diff mostra la variable sense definir introduïda a D. La consulta no modifica la versió seleccionada.','Diff de D al costat del resultat de la prova.'),
 C('git bisect reset','Tanquem la cerca i recuperem el punt de partida.', [('reset','En aquesta subordre de bisect, reset finalitza la sessió i torna al punt inicial; no és git reset.')],'Tornem a main H. No s’ha creat cap commit ni s’ha arreglat encara el programa.','Retirar CERCA ACTIVA i tornar HEAD a main H.')],
 summary=['Cal una prova repetible i dos extrems coneguts.','Provem cada versió abans de classificar-la.','Bisect localitza la regressió; reset tanca la cerca i després queda corregir-la.'],
 practice='En un historial de pràctiques amb una fallada persistent, identifica un extrem correcte i un de fallit. Mantén la mateixa prova i acaba la sessió amb bisect reset.'),
19: dict(goal='Completar l’últim commit propi amb un fitxer oblidat i entendre la substitució del commit.',
 start='Main a C, últim commit propi no publicat. notes.md és nou i havia de formar part de C. No hi ha altres canvis locals ni preparats.',
 stages=[
 N('Completar l’últim canvi abans de publicar','Hem confirmat la salutació però hem oblidat les notes. [[Amend]] crea un commit nou que substitueix l’últim a la branca, amb el contingut preparat que indiquem.','Graf A–B–C i notes.md NOU al treball. Etiqueta NO PUBLICAT a C.'),
 T('Només les notes són pendents. Comprovem aquesta premissa abans de substituir el commit.'),
 A('Les notes queden preparades. La resta del contingut preparat continua coincidint amb C.','notes.md'),
 C('git diff --staged --stat','Revisem què hem seleccionat.', [('--staged','Consulta els canvis preparats respecte de l’últim commit.'),('--stat','Mostra un resum dels fitxers afectats; per llegir les línies completes podem consultar el diff preparat sense aquesta opció.')],'El resum només mostra les notes noves. No afegirem altres feines per accident.','Mostrar notes.md al resum i una comprovació del seu contingut.'),
 C('git commit --amend --no-edit','Substituïm l’últim commit amb [[git commit]].', [('--amend','Crea un commit nou amb el mateix pare que l’anterior, incorporant el contingut preparat.'),('--no-edit','Conserva el missatge anterior sense obrir l’editor.')],'Main passa a C prima, amb pare B i identificador nou. El missatge i l’autoria es conserven; les notes ja hi són incloses.','Atenuar C fora de la línia actual i crear C′ des de B. No dibuixar C′ com un fill de C.'),
 C('git show --stat HEAD','Comprovem el commit resultant.', [('--stat','Resumeix els fitxers del commit consultat.'),('HEAD','Assenyala el nou commit actual en aquest exemple.')],'La salutació i les notes formen part del mateix canvi complet. L’estat del treball queda net.','Mostrar missatge conservat i fitxer de notes inclòs; main a C′.'),
 N('Alternativa: canviar només el missatge','En un cas independent tornem a C amb la preparació sense diferències. Podem substituir només el missatge, conservant el contingut i el pare.','Separador CAS INDEPENDENT; recuperar C amb índex igual a C, sense les notes preparades del camí anterior.'),
 C('git commit --amend -m "Personalitza el missatge"','Escrivim un altre missatge per a l’últim commit.', [('--amend','Substitueix l’últim commit a la branca.'),('-m','Introdueix el missatge nou.'),('"Personalitza el missatge"','Aquest és el text nou. En aquest cas no hem preparat cap canvi de contingut.')],'Es crea un altre identificador, amb el mateix arbre i pare B. És una alternativa al cas anterior.','Comparar arbre igual / missatge diferent / hash diferent.',mode='alternative:message')],
 summary=['Amend substitueix l’últim commit a la branca; no n’afegeix un fill.','Revisem el contingut preparat abans de fer-lo.','En aquesta lliçó només reescrivim l’últim commit propi encara no publicat.'],
 practice='En un repositori de pràctiques sense publicar, afegeix un fitxer oblidat a l’últim commit. Compara el pare, el missatge, els fitxers i l’identificador abans i després.'),
})

LESSONS.update({
20: dict(goal='Descarregar, comparar i integrar novetats en tres passos explícits.',
 start='Main local i origin/main a B, treball net. El servidor origin ja té C. La història és lineal i main segueix origin/main.',
 stages=[
 N('La referència local no és una vista en directe','El servidor pot haver avançat sense que el nostre ordinador ho sàpiga. [[origin/main]] és una referència local de l’última consulta; encara apunta a B.','Tres elements separats: main LOCAL B; origin/main LOCAL B; main SERVIDOR C.'),
 T('No hi ha canvis locals pendents. Podem observar amb claredat què modifica cada pas.'),
 C('git fetch origin','[[git fetch]] descarrega les novetats i actualitza les referències de seguiment.', [('origin','Indica el remot que consultem. És el servidor del projecte.')],'C ja existeix al repositori local i origin/main apunta a C. Main, preparació i treball continuen a B.','Animar descàrrega C i actualització de origin/main. No moure main ni canviar el text de l’editor.'),
 C('git log --oneline main..origin/main','Consultem els commits que la branca local encara no conté.', [('--oneline','Mostra un resum de cada commit.'),('main..origin/main','El rang mostra commits accessibles des d’origin/main que no són accessibles des de main.')],'En aquest exemple només apareix C. La consulta tampoc integra el canvi.','Subratllar primer main, després els dos punts i després origin/main; representar conjunts amb el mateix C.'),
 C('git diff main origin/main -- helloGit.py','Comparem el contingut de les dues versions.', [('main','El primer punt de comparació és la nostra branca local.'),('origin/main','El segon és l’estat descarregat del remot.'),('--','Separa les versions del camí de fitxer.'),('helloGit.py','Limitem la comparació al programa.')],'Veiem la salutació nova de C, mentre el fitxer del treball encara té l’original de B.','Diff i editor actual visibles alhora; cap fletxa de sobreescriptura.'),
 C('git merge --ff-only origin/main','Després de revisar, decidim incorporar el canvi.', [('--ff-only','Només permet avançar main directament; amb divergències l’ordre s’aturaria.'),('origin/main','És la referència local actualitzada que volem incorporar.')],'Main avança a C i el treball s’actualitza. Aquest és el pas que integra la novetat.','Moure main fins a C i actualitzar l’editor després de l’execució.'),
 C('python3 helloGit.py','Provem la versió incorporada.', [],'El programa executa la salutació de C. Hem separat descarregar, llegir i integrar.','Sortida Hola, Anna! i graf local coincident amb el servidor.')],
 summary=['Fetch actualitza les referències de seguiment, sense integrar a main.','Log i diff permeten revisar el que hem descarregat.','La integració és posterior; pull combina descàrrega i intent d’integració.'],
 practice='Amb dos clons de pràctiques, publica una novetat en un i fes fetch a l’altre. Compara main i origin/main abans d’integrar amb el treball net.'),
21: dict(goal='Relacionar original, fork i clon local, i proposar una contribució a l’original.',
 start='Projecte original a GitHub que admet contribucions. Crearem un fork propi i el clonarem. Les adreces entre angles són marcadors, no text per executar literalment.',
 stages=[
 N('Tres repositoris amb funcions diferents','L’original és el projecte al qual volem contribuir. El [[fork]] és un repositori al nostre compte. El clon és la còpia de treball que tindrem a l’ordinador.','Tres caixes persistents: ORIGINAL, FORK PROPI i CLON LOCAL. No presentar el fork com una carpeta local.'),
 N('Creem el fork al nostre compte','A la interfície del projecte creem el fork i triem el nostre compte com a destinació. El repositori propi queda al servidor; encara falta copiar-lo a l’ordinador.','Esquema de creació de fork amb comptes ficticis; cap publicació real durant la producció del vídeo.'),
 C('git clone <URL-del-fork> hello-git','Clonem el repositori del nostre compte.', [('<URL-del-fork>','Posem l’adreça real del fork, sense els angles del marcador.'),('hello-git','Aquest és el nom de la carpeta local que es crearà.')],'La carpeta conté el projecte i origin apunta al nostre fork.','Fletxa FORK → LOCAL; etiqueta origin vinculada al fork.'),
 C('cd hello-git','Entrem a la còpia local.', [('hello-git','Les ordres següents s’executen dins d’aquesta carpeta.')],'La terminal queda al projecte local.','Ruta visible a la terminal.'),
 C('git remote add upstream <URL-original>','Afegim una segona connexió amb [[git remote add]].', [('upstream','És el nom que donem al remot de l’original. És una convenció de l’exemple.'),('<URL-original>','Aquí posem l’adreça del projecte original, diferent de la del fork.')],'Origin continua apuntant al fork i upstream apunta a l’original. Afegir el remot no descarrega encara les novetats.','Dues connexions amb noms i adreces diferenciades.'),
 C('git remote -v','Comprovem les connexions.', [('-v','El guionet ve mostra les adreces configurades per consultar i publicar.')],'Llegim quin servidor correspon a cada nom. No confonem origin amb upstream.','Taula amb nom, adreça i direcció d’ús; ressaltar una fila cada vegada.'),
 N('L’original incorpora una novetat','L’original avança a C mentre el nostre fork i main local continuen a B. Amb el treball net i sense divergències, primer actualitzarem la còpia local i després el fork.','Original C; fork B; local B. La novetat és a README.md i no toca la salutació.'),
 C('git fetch upstream','Descarreguem de l’original.', [('upstream','Consultem l’original, no el fork propi.')],'La referència upstream/main local apunta a C. Main local encara és a B.','Actualitzar només la referència de seguiment.'),
 C('git merge --ff-only upstream/main','Incorporem la novetat a main local.', [('--ff-only','La integració només continua si pot ser un avançament directe.'),('upstream/main','És l’estat de main que acabem de descarregar de l’original.')],'Main local avança a C. El fork encara és a B.','Moure només main local.'),
 C('git push origin main','Enviem la branca actualitzada al nostre fork.', [('origin','La destinació és el fork propi.'),('main','Publiquem la seva branca main.')],'Original, fork i còpia local coincideixen a C.','Fletxa LOCAL → FORK; no enviar aquesta ordre a upstream.'),
 W('salutacio','Creem la branca de la contribució des de la base actualitzada.',True),
 N('Editem la contribució','Personalitzem la salutació i la provem. Després preparem el fitxer i confirmem la millora a la nostra branca.','Editor i prova python3 helloGit.py abans de preparar el canvi.'),
 A('La contribució queda preparada.'),M('Personalitza la salutacio','El commit D és a salutació local; l’original continua a C.'),P('La branca de la contribució es publica al fork propi.','salutacio'),
 N('Proposem el canvi a l’original','A la pull request triem main de l’original com a destinació i salutació del nostre fork com a origen. Descrivim la millora i com l’hem provat. La revisió encara queda pendent.','Formulari amb repositori i branca en tots dos costats. No representar una fusió ni una aprovació que encara no s’han produït.')],
 summary=['Fork és un repositori remot propi; clon és una còpia local.','Origin i upstream connecten amb repositoris diferents en aquest exemple.','Publiquem al fork i proposem la contribució a l’original.'],
 practice='Amb un projecte de pràctiques, identifica les dues adreces remotes i dibuixa el recorregut original, fork i local abans de preparar una contribució.'),
22: dict(goal='Agrupar tres commits relacionats no publicats i conservar el contingut final.',
 start='Salutacio activa a E amb C, D i E propis no publicats sobre B. Main a B; treball net. C personalitza, D retoca la puntuació i E documenta la mateixa millora.',
 stages=[
 N('Una millora explicada en tres commits','La feina és una mateixa millora repartida en tres commits. Abans de publicar-los, els agruparem perquè l’historial expliqui el resultat de manera coherent.','Graf A–B–C–D–E; etiqueta NO PUBLICATS sobre C–E i main a B.'),
 T('Comencem sense canvis locals pendents. Conservem l’identificador real d’E per comparar després el contingut final.'),
 C('git log -3 --oneline','Revisem els tres commits que volem agrupar.', [('-3','Limita la consulta als tres últims commits.'),('--oneline','Permet llegir-ne els identificadors i els missatges en un resum.')],'Confirmem que els tres canvis són propis, relacionats i encara no publicats.','Distingir ordre del log, més recent primer, de l’ordre que tindrà l’editor interactiu.'),
 C('git rebase -i HEAD~3','Obrim una reescriptura interactiva d’aquest tram.', [('-i','El guionet i obre una llista editable d’operacions.'),('HEAD~3','La base és B, tres passos enrere des d’E. La llista inclou els commits posteriors: C, D i E.')],'L’editor mostra els commits del més antic al més recent. Encara falta editar, desar i tancar.','Editor amb pick C Personalitza, pick D Puntuacio, pick E Documenta. No representar la reescriptura com a acabada.'),
 N('Escollim les operacions',['Deixem [[pick]] al primer commit. Als altres dos canviem l’acció a [[squash]], que els agrupa amb l’anterior.','Desem i tanquem l’editor de la llista. Aquesta acció permet que Git continuï; escriure la llista sense desar-la no completa el pas.'],'Llista final: pick C Personalitza; squash D Puntuacio; squash E Documenta. Subratllar cada acció per separat.',pause=3.5),
 N('Escrivim el missatge conjunt','A continuació s’obre l’editor del missatge. Escrivim Personalitza la salutació i documenta el canvi. Desem i tanquem també aquest editor.','Missatge conjunt complet visible; dos indicadors diferents LLISTA DESADA i MISSATGE DESAT.'),
 N('Un node nou amb el mateix resultat','La branca de salutació apunta a S, amb pare B i un identificador nou. Main continua a B. Els antics C, D i E queden fora de la línia de la branca, sense esborrar-se immediatament.','Graf abans/després amb C–E atenuats i S nou; contingut final igual al d’E.'),
 C('git diff e18a3b6 HEAD --','Comparem els fitxers finals amb l’antic E.', [('e18a3b6','És el hash de mostra de l’antic E; fem servir el que havíem conservat.'),('HEAD','És el nou commit S.'),('--','Tanquem la llista de versions sense restringir-la a un fitxer.')],'La sortida buida indica que no hi ha diferències de contingut en aquesta comparació. Provem també el programa per comprovar-ne el comportament.','Sortida buida amb llegenda CONTINGUT IGUAL; terminal de prova separat.'),
 N('Si l’operació s’atura','En un cas amb conflictes, editem la resolució, la provem i fem add del fitxer. Després podem continuar; també podem abandonar l’operació pendent.','Panell condicional separat amb editor → prova → git add helloGit.py.'),
 C('git rebase --continue','Reprenem el rebase pausat després de preparar la resolució.', [('--continue','Continua l’operació en curs; pot demanar més resolucions.')],'La reescriptura avança fins al resultat revisat.','Només camí CONTINUAR.',mode='conditional:conflict'),
 C('git rebase --abort','Podem optar per abandonar el rebase pendent.', [('--abort','Recupera l’estat de partida d’aquesta operació.')],'Aquest camí alternatiu conserva la història inicial.','Camí AVORTAR des de l’aturada, mai després de completar continue.',mode='alternative:abort')],
 summary=['Agrupem només els commits relacionats del tram seleccionat.','Cal desar i tancar tant la llista com el missatge conjunt.','L’historial canvia i els identificadors són nous; comprovem que el contingut final es conservi.'],
 practice='En una branca local de pràctiques no publicada, agrupa tres commits relacionats. Conserva el hash final antic i compara els continguts després de la reescriptura.'),
23: dict(goal='Preparar una part d’un fitxer i deixar l’altra edició pendent al treball.',
 start='helloGit.py ja seguit, sense canvis preparats. Modifiquem salutació i comiat, prou separats perquè apareguin en dos blocs independents de diff.',
 stages=[
 N('Dues edicions, dos canvis separables','Hem personalitzat la salutació i canviat el comiat. Volem confirmar només la salutació, conservant el comiat com a feina pendent.','Editor amb les dues edicions ressaltades i les funcions intermèdies sense canvis. No presentar dos blocs garantits per a qualsevol fitxer.'),
 C('git diff -- helloGit.py','Revisem el contingut abans de seleccionar-lo.', [('--','Separa les opcions del camí de fitxer.'),('helloGit.py','Consultem els dos blocs del mateix fitxer.')],'El primer bloc modifica la salutació i el segon, el comiat. Els signes de diff no formen part del codi que editem.','Dos blocs clarament separats i numerats BLOC 1 / BLOC 2.'),
 C('git add -p helloGit.py','Entrem a la preparació interactiva.', [('-p','El guionet pe permet seleccionar blocs de canvi.'),('helloGit.py','Limitem la sessió al fitxer del programa.')],'Git mostra el primer bloc i espera una resposta. Encara no introduïm una altra comanda de terminal.','Terminal en mode INTERACTIU, primer bloc de salutació i opcions de resposta.'),
 C('y','Responem i grega, de [[yes]], per preparar el primer bloc.', [],'La salutació passa a la preparació. La mateixa sessió continua amb el segon bloc.','Moure només el bloc de salutació del treball a l’índex.',input_kind='interactive'),
 C('n','Responem ena per deixar fora el segon bloc.', [],'El comiat continua al treball i no entra a la preparació. La sessió acaba en aquest exemple de dos blocs.','Conservar el comiat al treball. Tornar a mostrar el prompt normal de la terminal.',input_kind='interactive'),
 C('git diff --staged','Comprovem què hem preparat.', [('--staged','Compara la preparació amb l’últim commit.')],'Només hi ha la salutació nova. Aquesta és la selecció que enregistrarem.','Fletxa ÚLTIM COMMIT → PREPARACIÓ; comiat antic a les dues zones.'),
 C('git diff','Comprovem què queda pendent.', [],'Només apareix el comiat nou. La salutació ja coincideix entre treball i preparació.','Fletxa PREPARACIÓ → TREBALL; destacar el comiat sense preparar.'),
 M('Personalitza la salutacio','El commit nou incorpora la salutació. L’edició del comiat continua al treball; el commit no l’ha eliminada.'),
 T('El fitxer encara apareix modificat sense preparar pel canvi de comiat.'),
 N('El bloc és la unitat de selecció d’aquest exemple','Aquí les edicions formen dos blocs independents. Si Git les agrupa en un sol bloc, cal revisar com dividir-lo o ajustar la selecció; no assumim que cada línia es presenta separadament.','Comparació conceptual DOS BLOCS SEPARATS / UN BLOC CONJUNT, sense introduir noves respostes interactives en aquesta lliçó.')],
 summary=['L’opció p permet preparar blocs concrets.','Les respostes y i n pertanyen a la sessió interactiva.','El commit enregistra la selecció i conserva la resta d’edicions al treball.'],
 practice='En un fitxer de pràctiques amb dues edicions separades, prepara un bloc i rebutja l’altre. Compara els dos diffs abans de confirmar.'),
24: dict(goal='Fer una correcció en una altra carpeta de treball conservant la feina pendent original.',
 start='Carpeta projecte a salutacio amb una edició sense preparar. Main a B no està activa en cap altre worktree. La carpeta auxiliar encara no existeix.',
 stages=[
 N('Dues carpetes, preparacions separades','Volem corregir main sense interrompre la salutació pendent. Un [[worktree]] afegeix una carpeta de treball vinculada al mateix repositori, amb el seu índex i la seva branca activa.','Dos espais diferenciats; ORIGINAL a salutacio amb canvi pendent i AUXILIAR encara inexistent.'),
 C('git worktree add -b correccio ../projecte-correccio main','Creem una altra carpeta per a la correcció.', [('-b','El guionet be crea una branca nova per al worktree.'),('correccio','És el nom de la branca de la correcció.'),('../projecte-correccio','És el camí de la nova carpeta, al costat de l’original.'),('main','És el punt de partida; la correcció comença a la versió de main.')],'L’auxiliar comença neta a correcció. La carpeta original conserva l’edició pendent a salutació.','Crear la segona carpeta i índex; conservar el text de l’editor original sense moviments.'),
 C('git worktree list','Consultem les carpetes vinculades.', [],'La llista relaciona camins i branques actives. Encara estem treballant des de la carpeta original.','Dues files amb ruta completa i branca, i un indicador AQUÍ SOM.'),
 C('cd ../projecte-correccio','Entrem a la carpeta auxiliar.', [('../projecte-correccio','El camí ens porta al directori nou, no canvia la branca de la carpeta original.')],'La terminal queda a la correcció amb el treball net.','Moure AQUÍ SOM a l’auxiliar; conservar l’editor original com a referència.'),
 N('Editem només la correcció','Afegim una coma a la salutació original, desem i provem el programa. Aquest retoc es fa al worktree auxiliar.','Editor auxiliar print("Hello, Git!") i prova. L’original continua amb print("Hola, Anna!") sense confirmar.'),
 A('La correcció queda preparada només a l’índex de la carpeta auxiliar.'),M('Corregeix la puntuacio','D és un commit de correcció. La feina pendent de salutació queda fora d’aquest commit.'),
 W('main','Canviem a main dins de l’auxiliar. Això és possible perquè main no està activa en cap altre worktree.'),
 C('git merge --ff-only correccio','Incorporem la correcció a main.', [('--ff-only','Només permet l’avançament directe d’aquest exemple.'),('correccio','És la branca de la correcció que acabem de confirmar.')],'Main avança a D. L’original continua a salutació B amb l’edició pendent intacta.','Main i correccio a D; salutacio a B; dos índexs encara separats.'),
 C('git -C ../projecte status --short','Consultem la carpeta original sense abandonar encara l’auxiliar.', [('-C','El guionet ce majúscula indica la carpeta des d’on Git executarà la consulta.'),('../projecte','És el directori original.'),('--short','Mostra l’estat breu del treball d’aquella carpeta.')],'L’original continua amb la salutació modificada sense preparar. L’auxiliar és neta després de la correcció.','Mostrar la consulta identificada com ORIGINAL, diferenciada de l’estat local de l’auxiliar.'),
 C('cd ../projecte','Tornem a la carpeta original.', [('..','Els dos punts formen part del camí relatiu per pujar al directori pare.')],'Tornem a treballar a salutació. La correcció confirmada ja és a main.','Ruta original i editor pendent intacte.'),
 C('git worktree remove ../projecte-correccio','Retirem la carpeta auxiliar des de fora.', [('../projecte-correccio','La carpeta ha d’estar neta en aquest exemple. La retirem sense forçar.')],'Desapareix el directori auxiliar. Main, correcció i el commit D continuen al repositori.','Retirar només la icona de carpeta, sense esborrar les etiquetes ni el node del graf.')],
 summary=['Els worktrees comparteixen historial i branques.','Cada carpeta té treball, índex i branca activa propis.','Retirar una carpeta auxiliar neta conserva els commits i les branques.'],
 practice='En un repositori de pràctiques, deixa una edició pendent i crea un worktree auxiliar per a una correcció petita. Comprova els dos estats abans de retirar l’auxiliar neta.'),
25: dict(goal='Entendre un control local pre-commit que comprova la sintaxi de la versió preparada.',
 start='Repositori de pràctiques ordinari amb .git i sense hooks actius ni core.hooksPath personalitzat. Git i python3 disponibles; entorn compatible amb shebang i chmod. El programa ja està seguit.',
 stages=[
 N('Comprovar abans de crear el commit','Un [[hook]] és un programa que Git pot executar en un moment concret. Prepararem un control local de tipus [[pre-commit]] per revisar la sintaxi abans de crear el commit.','Línia temporal ADD → HOOK → COMMIT. El control s’interposa abans de crear el node, no després.'),
 N('El control llegeix la preparació','El control ha de comprovar el que entrarà al commit. Per això llegim el programa des de l’índex, encara que l’editor tingui una altra versió.','Editor complet a .git/hooks/pre-commit:\n```python\n#!/usr/bin/env python3\nimport subprocess\n\nsource = subprocess.check_output(\n    ["git", "show", ":helloGit.py"], text=True\n)\ncompile(source, "helloGit.py", "exec")\n```\nRessaltar primer la ruta i després :helloGit.py.'),
 N('Dues parts del codi','La consulta amb [[git show]] i els dos punts llegeix el contingut preparat. La funció [[compile]] comprova que el text tingui sintaxi vàlida; aquí no executa el programa ni prova la seva lògica.','Mantenir el codi complet. Subratllar la lectura de l’índex i després compile. Si no es pot llegir el fitxer obligatori, el control també falla.'),
 C('chmod +x .git/hooks/pre-commit','En aquest entorn fem executable el control.', [('+x','Afegeix el permís d’execució.'),('.git/hooks/pre-commit','És el fitxer que acabem de desar al repositori de pràctiques.')],'Git executarà aquest control local en intentar confirmar. No l’hem afegit com un fitxer versionat del projecte.','Ruta completa visible, fitxer desat i indicador EXECUTABLE. No donar per fet que tots els entorns gestionen permisos igual.'),
 N('Preparem deliberadament una sintaxi incorrecta','Traiem el parèntesi final de la salutació i desem el fitxer. Aquesta és la versió incorrecta que prepararem per comprovar el control.','Editor print("Hola, Anna!" sense el parèntesi final. Etiqueta PROVA DEL CONTROL.'),
 A('La versió sense parèntesi entra a la preparació.'),
 C('git commit -m "Personalitza la salutacio"','Intentem confirmar el contingut preparat.', [('-m','Aquest argument introdueix el missatge del commit; el control encara pot impedir-ne la creació.'),('"Personalitza la salutacio"','El missatge descriu la personalització de la salutació. Les cometes el mantenen en un sol argument.')],'El hook falla amb un error de sintaxi. Git atura l’operació i no crea cap commit nou.','Node C encara inexistent. Terminal amb error i panell ÍNDEX: INCORRECTE.'),
 N('Corregim només el treball','Reposem el parèntesi i desem a l’editor. Encara no hem preparat la correcció: el treball és correcte, però l’índex conserva el text anterior.','Dos panells amb el parèntesi present al treball i absent a la preparació.'),
 C('git commit -m "Personalitza la salutacio"','Tornem a intentar confirmar abans de preparar la correcció.', [],'El control continua fallant perquè llegeix la preparació. Corregir l’editor per si sol no canvia el contingut seleccionat.','Fletxa HOOK → ÍNDEX, no cap a l’editor; cap node nou.'),
 A('Ara la preparació rep la versió amb sintaxi correcta.'),M('Personalitza la salutacio','El control acaba correctament i Git crea el commit. Treball, preparació i historial coincideixen amb el text corregit.'),
 N('Un control concret, amb un abast concret','Aquest control comprova sintaxi, no que el programa faci el que volem. És local, no s’instal·la als altres ordinadors amb un push i es pot ometre. Els controls compartits necessiten una configuració acordada.','Etiquetes SINTAXI / LOCAL / NO DISTRIBUÏT PEL PUSH. No presentar-lo com una garantia general de qualitat.')],
 summary=['El pre-commit s’executa abans de crear el commit.','El control de l’exemple comprova el contingut de l’índex.','Cal preparar la correcció perquè la comprovi; continua sent una ajuda local de sintaxi.'],
 practice='En un repositori de pràctiques separat, instal·la el codi mostrat i compara un intent amb sintaxi incorrecta, un altre corregint només l’editor i el final després d’add.'),
})

# Fer explícits els passos de prova i els recorreguts condicionals.
def run_program(result, mode='main'):
    return C('python3 helloGit.py','Executem el programa per comprovar el contingut desat.',
             [('helloGit.py','És el fitxer de la còpia de treball que acabem d’editar.')],
             result,'Mostrar la sortida real del programa al costat de l’editor.',mode=mode)


def insert_after(number,title,stages):
    items=LESSONS[number]['stages'];index=next(i for i,s in enumerate(items) if s['title']==title)
    items[index+1:index+1]=stages


insert_after(2,'Editem i provem la funcionalitat',[run_program('La salutació personalitzada funciona. El canvi encara no s’ha preparat ni confirmat.')])
insert_after(16,'Mostrem el canvi abans de confirmar',[run_program('Veiem la salutació personalitzada encara sense exclamació. Aquesta és la primera versió que proposem.')])
insert_after(16,'La revisió concreta el resultat',[run_program('La salutació ara acaba en exclamació. Prepararem aquesta correcció a la mateixa branca.')])
insert_after(21,'Editem la contribució',[run_program('La salutació nova funciona a la branca de contribució. Encara no l’hem confirmada ni publicada.')])
insert_after(24,'Editem només la correcció',[run_program('La sortida és Hello, Git! a la carpeta auxiliar. La feina de l’original continua al seu lloc.')])

items=LESSONS[4]['stages'];items[-1:]=[
 N('Continuem des de casa','Editem i desem una altra millora a casa, ja actualitzada. Aquesta vegada el commit nou naixerà a la còpia de casa.','Editor i ruta CASA visibles. Classe continua a B.'),
 run_program('La millora funciona a casa i encara és feina pendent.'),
 A('Seleccionem la millora de casa.'),M('Millora des de casa','C és un commit local de casa. El servidor i classe continuen a B.'),P('El servidor incorpora C. Encara falta actualitzar classe.'),
 N('Tornem a l’ordinador de classe','A classe encara tenim B. Abans de començar a editar, comprovem l’estat i actualitzem aquesta còpia amb la feina publicada des de casa.','Canvi clar de context: ruta CLASSE. No reutilitzar el prompt de casa.'),
 T('No hi ha canvis pendents a classe; en aquest exemple la història és lineal.'),
 C('git pull --ff-only','Descarreguem i incorporem el commit que havíem publicat des de casa.',[('--ff-only','Només avancem directament. Una divergència s’hauria de revisar com un cas diferent.')],'Classe arriba a C. Les tres còpies comparteixen el mateix commit.','Classe B → C; servidor i casa ja eren a C.')]

for n,title in [(7,'Cas condicional: apareix un conflicte'),(15,'Camí condicional: resoldre o abandonar'),(22,'Si l’operació s’atura')]:
    prepare=A('La resolució revisada queda preparada per continuar l’operació pendent.')
    prepare['mode']='conditional:conflict'
    insert_after(n,title,[run_program('La resolució funciona amb la prova d’aquest exemple.',mode='conditional:conflict'),prepare])

# La mateixa correcció d’execució queda representada com a pas propi.
insert_after(14,'Un nom per a una entrega concreta',[run_program('La salutació original de B funciona. Marcarem aquesta versió confirmada com a entrega.')])
insert_after(22,'Un node nou amb el mateix resultat',[run_program('El programa conserva el resultat final després d’agrupar els commits.')])

# Els vídeos mostren el codi necessari, sense dependències de guies externes.
from pathlib import Path as _Path
_SOURCE_ROOT = _Path(__file__).resolve().parents[1]
_before = (_SOURCE_ROOT/'23-add-interactiu/exemples/helloGit-abans.py').read_text().strip()
_edited = (_SOURCE_ROOT/'23-add-interactiu/exemples/helloGit-editat.py').read_text().strip()
LESSONS[23]['stages'][0]['visual'] += '\nCodi inicial complet:\n```python\n'+_before+'\n```\nCodi editat complet:\n```python\n'+_edited+'\n```\nMostrar les dues funcions modificades per torns; conservar les intermèdies sense canvis com a context.'
LESSONS[23]['stages'][0]['speech'] = [
    'El programa té una funció de salutació i una de comiat, separades per altres funcions que no canviem. Mostrem el contingut inicial abans d’editar.',
    'Canviem la salutació a Hola, Anna! i el comiat a Adeu! Volem confirmar només la salutació i conservar el comiat com a feina pendent.']
_setup=next(s for s in LESSONS[25]['stages'] if s['title']=='El control llegeix la preparació')
_setup['speech']=[
    'Creem el fitxer de control a la ruta que veus a la pantalla i hi desem el codi complet.',
    _setup['speech']]
