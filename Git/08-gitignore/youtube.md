# YouTube · lliçó 08

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (63/100 caràcters)

```text
Gitignore: deixa fora els fitxers generats · Píndoles de Git 08
```

**Descripció**

```text
Escriure un fitxer de regles per ignorar fitxers generats i secrets, i distingir-los dels que [[Git]] ja seguia.

Punt de partida: El programa fa servir un segon fitxer amb les salutacions i deixa un registre de cada execució. També tenim un fitxer amb una clau privada i un registre de mostra per a la documentació. Fa temps, vam confirmar per error un registre antic.

Ordres que surten al vídeo:
  python3 helloGit.py
  git status --short
  git status --short --ignored
  git check-ignore -v debug.log
  git rm --cached app.log
  git add .gitignore mostra.log
  git commit -m "Ignora els fitxers generats i els secrets"

Practica-ho: En un projecte de pràctiques, genera un registre executant el programa i escriu un punt gitignore amb una regla i una excepció. Comprova-ho amb git status doble guionet ignored i amb git check-ignore. Els fitxers propis de l’editor es poden ignorar només al teu ordinador, amb el fitxer exclude de la carpeta punt git.
Script per preparar el mateix punt de partida: Git/practiques/08-gitignore.sh

Capítols:
0:00 Capçalera i presentació
0:40 $ python3 helloGit.py
1:02 $ git status --short
1:30 Un fitxer de regles, línia a línia
2:47 $ git status --short --ignored
3:28 $ git check-ignore -v debug.log
4:03 $ git rm --cached app.log
5:06 $ git add .gitignore mostra.log
5:28 $ git commit -m "Ignora els fitxers generats i els secrets"
5:56 Resum final
6:26 Pràctica final

Lliçó anterior: 07 · Add interactiu: prepara només una part del fitxer
Lliçó següent: 09 · Finals de línia: Windows, macOS i Linux

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, gitignore  
**Llista:** Píndoles de Git, posició 9  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/08-gitignore.mp4`  
**Subtítols:** `08-gitignore/output/08-gitignore.ca.srt`  
**Miniatura:** `08-gitignore/output/portada.png`
