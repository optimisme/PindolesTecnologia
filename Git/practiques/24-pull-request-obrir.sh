#!/usr/bin/env bash
# Píndoles de Git · Lliçó 24 · Pull request: proposa un canvi a l’equip
#
# Crea el punt de partida del vídeo en una carpeta nova. A Windows, executa-ho des de Git Bash.
#     bash 24-pull-request-obrir.sh            # crea la carpeta practica-24-pull-request-obrir
#     bash 24-pull-request-obrir.sh una-altra   # o la carpeta que indiquis
# Els remots són carpetes .git locals que fan el paper de GitHub; no cal connexió.
# Generat per Git/eines/practiques.py a partir de 24-pull-request-obrir/llico.yaml. No l’editeu a mà.
set -euo pipefail

DESTI="${1:-practica-24-pull-request-obrir}"
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
git clone -q "$ARREL/origin.git" "$ARREL/HelloGit"
cd "$ARREL/HelloGit"
cat > helloGit.py <<'FI_DEL_FITXER'
print("Hello Git")
FI_DEL_FITXER
git add helloGit.py
git commit -q -m 'Afegeix la salutacio inicial'
COMMIT_A=$(git rev-parse --short HEAD)
cat > helloGit.py <<'FI_DEL_FITXER'
print("Hello Git!")
FI_DEL_FITXER
git commit -q -am "Afegeix una exclamacio"
COMMIT_B=$(git rev-parse --short HEAD)
git push -q -u origin main

cd "$ARREL/HelloGit"
echo "Punt de partida preparat a: $PWD"
if git rev-parse -q --verify HEAD >/dev/null 2>&1; then
  git log --oneline --graph --all
  git status --short
fi
