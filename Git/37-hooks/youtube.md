# YouTube · lliçó 37

Generat per `python -m motor.youtube`. No l’editeu a mà: canvieu el `llico.yaml` o `serie.yaml`.

**Títol** (64/100 caràcters)

```text
Hooks: comprova la sintaxi abans del commit · Píndoles de Git 37
```

**Descripció**

```text
Crear un control local que revisi la sintaxi del contingut preparat abans de cada commit.

Punt de partida: Tenim un projecte de pràctiques amb el programa confirmat. Volem que Git ens avisi si intentem confirmar codi amb errors de sintaxi.

Ordres que surten al vídeo:
  chmod +x .git/hooks/pre-commit
  git add helloGit.py
  git commit -m "Personalitza la salutacio"

Practica-ho: En un repositori de pràctiques, instal·la el control i prova tres intents. Un amb un error preparat, un amb l’error corregit només a l’editor i l’últim després de preparar la correcció.
Script per preparar el mateix punt de partida: Git/practiques/37-hooks.sh

Capítols:
0:00 Capçalera i presentació
0:32 Un control abans del commit
0:51 El control llegeix la preparació
1:13 Dues parts del codi
1:34 $ chmod +x .git/hooks/pre-commit
2:06 Preparem una errada a propòsit
2:17 $ git add helloGit.py
2:34 $ git commit -m "Personalitza la salutacio"
3:12 Corregim només l’editor
3:25 $ git commit -m "Personalitza la salutacio"
3:46 $ git add helloGit.py
4:02 $ git commit -m "Personalitza la salutacio"
4:24 Què fa i què no fa aquest control
4:43 Resum final
5:07 Pràctica final

Lliçó anterior: 36 · Worktree: corregeix main sense interrompre la feina

Llista: Píndoles de Git. Subtítols en català inclosos.
```

**Etiquetes:** git, github, control de versions, programació, català, tutorial, hooks  
**Llista:** Píndoles de Git, posició 38  
**Idioma del vídeo i dels subtítols:** català  
**Vídeo:** `Git/output/37-hooks.mp4`  
**Subtítols:** `37-hooks/output/37-hooks.ca.srt`  
**Miniatura:** `37-hooks/output/portada.png`
