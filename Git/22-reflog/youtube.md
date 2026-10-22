# YouTube · lliçó 22

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (53/100 caràcters)

```text
Reflog: recupera un commit local · Píndoles de Git 22
```

**Descripció**

```text
Trobar un commit al [[reflog]] i tornar-hi a donar accés amb una branca, sense perdre els canvis preparats.

Punt de partida: Continuem on ho vam deixar amb reset soft. La branca ha tornat enrere i el commit de la salutació ja no apareix a l’historial de main.

Ordres que surten al vídeo:
  git log --oneline
  git reflog
  git show 46a3283 -- helloGit.py
  git branch recuperacio 46a3283
  git log --oneline --decorate --all
  git status --short

Practica-ho: Després d’un reset soft de pràctiques, troba el commit al reflog, revisa’l i crea-hi una branca de recuperació sense canviar de branca.
Script per preparar el mateix punt de partida: Git/practiques/22-reflog.sh

Capítols:
0:00 Capçalera i presentació
0:38 Un commit fora de la línia actual
0:52 $ git log --oneline
1:14 $ git reflog
1:42 $ git show 46a3283 -- helloGit.py
2:15 $ git branch recuperacio 46a3283
2:53 $ git log --oneline --decorate --all
3:27 $ git status --short
3:48 Una ajuda local amb límits
4:05 Resum final
4:31 Pràctica final

Lliçó anterior: 21 · Reset: torna enrere un commit local
Lliçó següent: 23 · Revert: desfés un commit publicat

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, reflog  
**Llista:** Píndoles de Git, posició 23  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/22-reflog.mp4`  
**Subtítols:** `22-reflog/output/22-reflog.ca.srt`  
**Miniatura:** `22-reflog/output/portada.png`
