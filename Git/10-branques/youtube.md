# YouTube · lliçó 10

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (59/100 caràcters)

```text
Branques: prova idees sense tocar main · Píndoles de Git 10
```

**Descripció**

```text
Crear dues branques des de main, confirmar-hi una idea a cadascuna i comparar les tres versions.

Punt de partida: Partim d’un projecte amb dos commits a main. El programa saluda i dona la benvinguda, i no hi ha cap canvi pendent.

Ordres que surten al vídeo:
  git switch -c salutacio
  git add helloGit.py
  git commit -m "Personalitza la salutacio"
  git switch main
  git switch -c comiat
  git commit -m "Afegeix un comiat"
  git log --oneline --graph --all --decorate
  python3 helloGit.py
  git switch salutacio

Practica-ho: En un repositori de pràctiques sense canvis pendents, crea dues branques des de main, confirma un canvi diferent a cadascuna i alterna-les per comparar el fitxer i la sortida del programa.
Script per preparar el mateix punt de partida: Git/practiques/10-branques.sh

Capítols:
0:00 Capçalera i presentació
0:33 Dues idees, dues línies de treball
0:53 Una branca és una etiqueta
1:10 $ git switch -c salutacio
1:50 Primera idea, la salutació
2:15 $ git commit -m "Personalitza la salutacio"
2:39 $ git switch main
3:14 $ git switch -c comiat
3:54 Segona idea, el comiat
4:17 $ git commit -m "Afegeix un comiat"
4:41 $ git log --oneline --graph --all --decorate
5:35 $ python3 helloGit.py
5:53 $ git switch salutacio
6:22 $ python3 helloGit.py
6:42 La branca activa
7:02 Resum final
7:31 Pràctica final

Lliçó anterior: 09 · Finals de línia: Windows, macOS i Linux
Lliçó següent: 11 · Merge: porta les idees a main

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, branques  
**Llista:** Píndoles de Git, posició 11  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/10-branques.mp4`  
**Subtítols:** `10-branques/output/10-branques.ca.srt`  
**Miniatura:** `10-branques/output/portada.png`
