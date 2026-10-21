#!/usr/bin/env bash
# Píndoles de Git · Lliçó 2 · Connectar amb GitHub: accés i primer clon
#
# Crea el punt de partida del vídeo en una carpeta nova. A Windows, executa-ho des de Git Bash.
#     bash 02-github.sh            # crea la carpeta practica-02-github
#     bash 02-github.sh una-altra   # o la carpeta que indiquis
# Els remots són carpetes .git locals que fan el paper de GitHub; no cal connexió.
# Generat per Git/eines/practiques.py a partir de 02-github/llico.yaml. No l’editeu a mà.
set -euo pipefail

DESTI="${1:-practica-02-github}"
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

nou_repositori --bare "$ARREL/origin.git"

cd "$ARREL"
echo "Punt de partida preparat a: $PWD"
if git rev-parse -q --verify HEAD >/dev/null 2>&1; then
  git log --oneline --graph --all
  git status --short
fi
