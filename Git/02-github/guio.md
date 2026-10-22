# Lliçó 2 · Connectar amb GitHub: accés i primer clon

**Sèrie:** Píndoles de Git · **Capçalera:** CONNECTAR AMB GITHUB — Accés des de la terminal i primer clon  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/02-github.sh`](../practiques/02-github.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Segona lliçó. Connectar amb *GitHub*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a autoritzar la terminal per treballar amb *GitHub* i clonar un repositori buit per començar el projecte. *(pausa 2.5 s)*

Tenim *Git* configurat i un compte de *GitHub*. Ara connectarem la terminal amb aquest compte. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Dues eines, dues funcions

*Git* treballa al nostre ordinador. *GitHub* és un servei on guardem una còpia per compartir-la. *(pausa 3 s)*

Per enviar-hi *commits*, la terminal ha de demostrar qui som. La contrasenya del compte no serveix per a la terminal: necessitem una autorització pròpia. *(pausa 3 s)*

**Visual:** Ordinador amb Git a l’esquerra, núvol de GitHub a la dreta i un cadenat a la fletxa que els uneix.

## Instal·lem GitHub CLI

Farem servir *GitHub CLI*, l’eina oficial de *GitHub* per a la terminal. La instal·lem amb el gestor de paquets del sistema; a la pantalla veus l’ordre per a cada sistema. *(pausa 3 s)*

**Visual:** Tres targetes: macOS · brew install gh / Windows · winget install --id GitHub.cli / Linux · el gestor de paquets de la distribució.

## Terminal · `gh auth login`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `gh auth login` | Amb *gh auth login* iniciem l’autorització. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Responem amb les fletxes i la tecla de retorn: *GitHub* punt com, protocol HTTPS, autoritzar *Git* i iniciar sessió amb el navegador. Copiem el codi que apareix i el confirmem a la pàgina que s’obre. *(pausa 4 s)*

Sortida de mostra:

```text
? Where do you use GitHub? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: 1A2B-3C4D
Press Enter to open https://github.com/login/device in your browser...
```

**Visual:** Sortida de mostra amb les quatre preguntes ressaltades per torns; després, navegador amb el camp del codi d’un sol ús. Codi i compte inventats.

## Terminal · `gh auth status`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `gh auth status` | Comprovem que la terminal ja està autoritzada. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** Indica el compte connectat i que *Git* farà servir HTTPS. El codi d’accés queda desat de manera segura al sistema; no l’hem d’escriure ni compartir. *(pausa 3.5 s)*

Sortida de mostra:

```text
github.com
  ✓ Logged in to github.com account ermessenda-carcassona (keyring)
  - Active account: true
  - Git operations protocol: https
  - Token: gho_************************************
```

**Visual:** Sortida de mostra; ressaltar el nom del compte i la línia del protocol. El token surt amagat amb asteriscos.

## Una alternativa a Windows

A Windows, l’instal·lador de *Git* també inclou un gestor d’accés. El primer cop que enviem *commits*, obre el navegador i desa l’autorització. Qualsevol dels dos camins serveix. *(pausa 3 s)*

**Visual:** Finestra d’inici de sessió del gestor de credencials de Git per a Windows, com a camí alternatiu.

## Creem un repositori buit

A la web de *GitHub*, creem un repositori nou anomenat HelloGit. No hi afegim cap fitxer inicial: el començarem des de l’ordinador. *(pausa 3 s)*

**Visual:** Esquema del formulari New repository: nom HelloGit, opcions README, .gitignore i llicència desmarcades. Botó Code amb l’adreça HTTPS ressaltada.

## Terminal · `git clone <URL-del-repositori> HelloGit`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git clone` | Amb *git clone* creem la còpia local del repositori. | 2.5 s |
| `<URL-del-repositori>` | Substituïm aquest marcador per l’adreça que hem copiat del botó *Code*. No escrivim els signes de menor i major. | 2.5 s |
| `HelloGit` | És el nom de la carpeta nova que es crearà. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *Git* avisa que el repositori és buit. És el que esperàvem: ja tenim la carpeta connectada amb *GitHub*. *(pausa 3.5 s)*

Sortida de mostra:

```text
Cloning into 'HelloGit'...
warning: You appear to have cloned an empty repository.
```

**Visual:** Animació de la carpeta HelloGit que apareix a l’ordinador, unida al repositori de GitHub.

## Terminal · `cd HelloGit`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `cd` | Entrem a la carpeta del projecte amb l’ordre cd. | 2.5 s |
| `HelloGit` | És la carpeta que acabem de crear. Les ordres següents s’executen des de dins. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La terminal mostra que som dins del projecte. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** El camí de la terminal canvia a ~/HelloGit.

## Terminal · `git remote -v`

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git remote` | Comprovem amb quin repositori remot està connectada la carpeta. | 2.5 s |
| `-v` | El guionet ve mostra també les adreces. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** El remot es diu *origin* i apunta al repositori de *GitHub*, tant per descarregar com per enviar. *(pausa 3.5 s)*

Sortida de mostra:

```text
origin	https://github.com/ermessenda-carcassona/HelloGit.git (fetch)
origin	https://github.com/ermessenda-carcassona/HelloGit.git (push)
```

**Visual:** Sortida de mostra; ressaltar el nom origin i l’adreça del compte d’exemple.

## Resum final

La terminal necessita una autorització pròpia per treballar amb *GitHub*. *(pausa 2.5 s)*

*gh auth login* la crea i *gh auth status* la comprova. *(pausa 2.5 s)*

*git clone* crea la carpeta local connectada al remot *origin*. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Autoritza la terminal amb el teu compte, crea un repositori buit de pràctiques a *GitHub* i clona’l en una carpeta nova. Comprova el remot abans de continuar. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
