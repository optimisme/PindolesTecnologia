# Píndoles de Tecnologia

Vídeos educatius curts en català per publicar a YouTube. Cada sèrie té les lliçons
escrites com a dades, unes eines que en comproven el contingut i un motor comú
que en produeix la veu, les animacions i els subtítols.

| Sèrie | Estat |
| --- | --- |
| [Git](Git/README.md) | 38 lliçons amb guió revisat i exemples comprovats; vídeos pendents de produir |
| Docker | Carpeta reservada |
| HTML-CSS | Carpeta reservada |

## Organització

```text
motor/                 Motor comú de totes les sèries
  serie.py             Ordre de la sèrie, numeració i renumeració de carpetes
  guions.py            llico.yaml → guio.json + guio.md, amb revisió del text
  veu.py, credencials.py, alineacio.py   Veu Azure amb SSML, marques temporals
  subtitols.py, dibuix.py, capcalera.py, obertura.py, muntatge.py
  youtube.py           Fitxes de publicació (títol, descripció, capítols)
  proves/              Proves unitàries
Git/                   Sèrie de Git (contingut, eines pròpies i arxiu)
  output/              Vídeos finals del tema Git
Docker/, HTML-CSS/     Temes futurs, cadascun amb la seva carpeta output/
assets/                Imatges de marca
.github/workflows/     Comprovacions automàtiques
```

El que és comú a qualsevol sèrie viu a `motor/`. El que depèn del tema (per exemple,
executar ordres de Git en repositoris temporals o dibuixar un graf de commits) viu a
`<sèrie>/eines/`.

## Preparar l’entorn

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Cal Python 3.11 o posterior, Git i, per produir vídeos, FFmpeg i una clau d’Azure
Speech. Per a les comprovacions n’hi ha prou amb `requirements-comprovacions.txt`.
Copieu `.env.example` a `.env` i ompliu-hi la clau; `.env` no entra mai a Git.

## Flux de treball d’una sèrie

1. Editar el contingut a `<sèrie>/<NN-nom>/llico.yaml` (o l’ordre a `serie.yaml`).
2. Comprovar l’exemple i obtenir sortides reals: `python Git/eines/repeticio.py Git`.
3. Compilar i revisar els guions: `python -m motor.guions Git`.
4. Actualitzar els punts de partida de pràctica: `python Git/eines/practiques.py Git`.
5. Actualitzar les fitxes de YouTube: `python -m motor.youtube Git`.
6. Produir un vídeo quan es decideixi: `python Git/eines/render.py Git/08-branques`
   (el MP4 queda a `Git/output/`).

Els passos 2 a 5 no generen àudio ni vídeo i no necessiten credencials. Les mateixes
comprovacions s’executen a cada `push` amb GitHub Actions.

## Vídeos i mitjans

Cada tema (Git, Docker, HTML-CSS...) té la seva carpeta de vídeos finals: `<tema>/output/` (per exemple,
`Git/output/08-branques.mp4`). Es pot canviar amb `videos` a `serie.yaml`. La resta del que
es produeix per a cada lliçó (subtítols, narració, portada, informes) queda a
`<tema>/NN-nom/output/`.

Els fitxers d’àudio i vídeo no es versionen: `audio/`, `build/` i el contingut de les
carpetes `output/` estan exclosos de Git perquè es poden regenerar i ocupen massa. Els
vídeos es publiquen a YouTube; si cal conservar-ne una còpia versionada, feu servir Git LFS
o un emmagatzematge extern.
