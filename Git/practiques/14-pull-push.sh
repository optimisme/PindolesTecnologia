#!/usr/bin/env bash
# Píndoles de Git · Lliçó 14 · Pull i push: dues còpies al dia
#
# Crea el punt de partida del vídeo en una carpeta nova. A Windows, executa-ho des de Git Bash.
#     bash 14-pull-push.sh            # crea la carpeta practica-14-pull-push
#     bash 14-pull-push.sh una-altra   # o la carpeta que indiquis
# Els remots són carpetes .git locals que fan el paper de GitHub; no cal connexió.
# Generat per Git/eines/practiques.py a partir de 14-pull-push/llico.yaml. No l’editeu a mà.
set -euo pipefail

DESTI="${1:-practica-14-pull-push}"
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
git clone -q "$ARREL/origin.git" "$ARREL/classe/HelloGit"
cd "$ARREL/classe/HelloGit"
cat > helloGit.py <<'FI_DEL_FITXER'
print("Hello Git!")
FI_DEL_FITXER
git add helloGit.py
git commit -q -m 'Afegeix la salutacio inicial'
COMMIT_A=$(git rev-parse --short HEAD)
git push -q -u origin main
git clone -q "$ARREL/origin.git" "$ARREL/casa/HelloGit"
cat > helloGit.py <<'FI_DEL_FITXER'
print("Hola des de classe!")
FI_DEL_FITXER
git commit -q -am "Practica de classe"
COMMIT_B=$(git rev-parse --short HEAD)
git push -q
cd "$ARREL/casa/HelloGit"

cd "$ARREL/casa/HelloGit"
echo "Punt de partida preparat a: $PWD"
if git rev-parse -q --verify HEAD >/dev/null 2>&1; then
  git log --oneline --graph --all
  git status --short
fi
