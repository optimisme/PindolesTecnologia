# Hooks: comprova la sintaxi abans del commit

Veu: `ca-ES-EnricNeural` · Català · 100.1 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: Exemple independent en un repositori ordinari amb carpeta .git, main a B i helloGit.py ja seguit amb print("Hello Git!"). No hi ha core.hooksPath personalitzat ni hooks actius. Git i python3 són disponibles al PATH, en un entorn amb execució per shebang i chmod. Es crea .git/hooks/pre-commit executable amb l’script Python d’exemples/pre-commit: check_output de git show :helloGit.py llegeix la versió de l’índex i compile(..., "exec") comprova la sintaxi sense executar el programa ni generar memòria cau. El fitxer és obligatori en aquest exemple; si git show falla, el hook també falla. Es prepara una versió de helloGit.py amb print("Hola, Anna!" sense el parèntesi final i el commit falla abans de crear cap C. Es corregeix només l’arbre de treball; un altre commit encara falla perquè l’índex conserva la sintaxi incorrecta. Després d’add, el commit C es crea i l’arbre queda net. El hook és local i no és un fitxer versionat. No s’instal·la cap hook al repositori real; es proporciona un exemple revisable a exemples/pre-commit i les proves s’executen en repositoris temporals. La prova només comprova sintaxi, no errors d’execució ni la correcció funcional.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.71 s)

**Locució:** Vint-i-cinquena lliçó, Hooks.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Un error de sintaxi pot aturar el commit (6.7–18.8 s)

**Locució:** Has oblidat un parèntesi al programa. Un hook de tipus pre commit pot comprovar la sintaxi abans que Git creï el commit. Prepararem aquest petit control local.

**Animació:** Editor amb print("Hola, Anna!" sense el parèntesi de tancament. Un control de sintaxi se situa abans del nou commit.

## Comprovem el contingut de l’índex (18.8–31.5 s)

**Locució:** Creem el fitxer pre commit dins de punt git, hooks. L’script llegeix hello Git des de l’índex i en comprova la sintaxi amb Python. Així revisa la versió que entrarà al commit.

**Animació:** Editor de `.git/hooks/pre-commit`. Exemple complet disponible a [exemples/pre-commit](exemples/pre-commit).

```python
#!/usr/bin/env python3
import subprocess

source = subprocess.check_output(
    ["git", "show", ":helloGit.py"], text=True
)
compile(source, "helloGit.py", "exec")
```

## El hook ha de ser executable (31.5–42.2 s)

**Locució:** En aquest entorn, donem permís d’execució al fitxer amb chmod. A partir d’ara, Git executarà aquest hook local quan intentem fer un commit.

**Animació:** Fitxer .git/hooks/pre-commit passa de no executable a executable. Es pressuposa el directori de hooks per defecte.

**Comandes en pantalla:**

```bash
chmod +x .git/hooks/pre-commit
```

## El hook rebutja la sintaxi incorrecta (42.2–54.7 s)

**Locució:** Preparem el fitxer amb l’error i intentem confirmar-lo. La comprovació falla amb un error de sintaxi. Git atura l’operació i l’historial encara no té cap commit nou.

**Animació:** Add prepara el contingut incorrecte; commit executa el hook i mostra SyntaxError. Main continua a B.

**Comandes en pantalla:**

```bash
git add helloGit.py
git commit -m "Personalitza la salutacio"
```

## L’índex encara conserva l’error (54.7–64.5 s)

**Locució:** Corregim el fitxer a l’editor, però encara no fem add. Un altre intent continua fallant: el hook revisa la preparació, que conserva la versió amb l’error.

**Animació:** Treball amb print("Hola, Anna!") correcte; índex amb print("Hola, Anna!" incorrecte. Segon intent de commit també falla.

**Comandes en pantalla:**

```bash
git commit -m "Personalitza la salutacio"
```

## Ara la comprovació passa (64.5–74.1 s)

**Locució:** Tornem a preparar el fitxer corregit i fem commit. L’índex ja té sintaxi correcta, el hook acaba bé i Git crea el commit C.

**Animació:** Add actualitza l’índex i el hook permet crear C, fill de B. Treball, índex i HEAD coincideixen.

**Comandes en pantalla:**

```bash
git add helloGit.py
git commit -m "Personalitza la salutacio"
```

## El hook és local i comprova sintaxi (74.1–86.5 s)

**Locució:** Comprovem que no quedin canvis pendents. Aquest hook només valida la sintaxi, no el funcionament del programa. A més, no es comparteix automàticament amb un push.

**Animació:** Status sense sortida. Dues targetes: .git/hooks/pre-commit local i helloGit.py versionat. No es representa cap publicació.

**Comandes en pantalla:**

```bash
git status --short
```

## Preparar, comprovar i confirmar (86.5–100.1 s)

**Locució:** El hook revisa la preparació abans del commit. Si volem compartir aquest control, cal distribuir l’script i configurar-lo a cada entorn. És una ajuda local per detectar errors aviat.

**Animació:** Tres targetes: índex, comprovació i commit. Recordatori de distribuir i instal·lar l’script als entorns on es vulgui utilitzar.
