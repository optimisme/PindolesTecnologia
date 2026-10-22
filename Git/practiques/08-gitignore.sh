#!/usr/bin/env bash
# Píndoles de Git · Lliçó 8 · Gitignore: deixa fora els fitxers generats
#
# Crea el punt de partida del vídeo en una carpeta nova. A Windows, executa-ho des de Git Bash.
#     bash 08-gitignore.sh            # crea la carpeta practica-08-gitignore
#     bash 08-gitignore.sh una-altra   # o la carpeta que indiquis
# No cal cap connexió: tot passa al teu ordinador.
# Generat per Git/eines/practiques.py a partir de 08-gitignore/llico.yaml. No l’editeu a mà.
set -euo pipefail

DESTI="${1:-practica-08-gitignore}"
if [ -e "$DESTI" ]; then
  echo "Ja existeix $DESTI: tria una altra carpeta." >&2
  exit 1
fi
mkdir -p "$DESTI"
cd "$DESTI"
ARREL="$PWD"

# Si encara no has configurat Git (lliçó 1), els commits d’aquest exemple fan servir un nom provisional.
git config user.name >/dev/null || export GIT_AUTHOR_NAME="Alumne" GIT_COMMITTER_NAME="Alumne"
git config user.email >/dev/null || export GIT_AUTHOR_EMAIL="alumne@example.com" GIT_COMMITTER_EMAIL="alumne@example.com"

nou_repositori() {  # git init amb main com a branca inicial, també en versions antigues de Git
  git init -q "$@"
  git -C "${@: -1}" symbolic-ref HEAD refs/heads/main
}

nou_repositori "$ARREL/HelloGit"
cd "$ARREL/HelloGit"
cat > salutacions.py <<'FI_DEL_FITXER'
def saluda():
    return "Hola, Ermessenda!"
FI_DEL_FITXER
cat > helloGit.py <<'FI_DEL_FITXER'
from salutacions import saluda

missatge = saluda()
with open("debug.log", "a") as registre:
    registre.write(missatge + "\n")
print(missatge)
FI_DEL_FITXER
cat > app.log <<'FI_DEL_FITXER'
Registre d’una versió antiga
FI_DEL_FITXER
git add helloGit.py salutacions.py app.log
git commit -q -m 'Afegeix el programa i les salutacions'
COMMIT_A=$(git rev-parse --short HEAD)
cat > .env <<'FI_DEL_FITXER'
CLAU_API=exemple-que-no-es-real
FI_DEL_FITXER
cat > mostra.log <<'FI_DEL_FITXER'
Exemple de registre per a la documentació
FI_DEL_FITXER

cd "$ARREL/HelloGit"
echo "Punt de partida preparat a: $PWD"
if git rev-parse -q --verify HEAD >/dev/null 2>&1; then
  git log --oneline --graph --all
  git status --short
fi
