#!/usr/bin/env bash
# Píndoles de Git · Lliçó 17 · Branques remotes: consultar, seguir i esborrar
#
# Crea el punt de partida del vídeo en una carpeta nova. A Windows, executa-ho des de Git Bash.
#     bash 17-branques-remotes.sh            # crea la carpeta practica-17-branques-remotes
#     bash 17-branques-remotes.sh una-altra   # o la carpeta que indiquis
# Els remots són carpetes .git locals que fan el paper de GitHub; no cal connexió.
# Generat per Git/eines/practiques.py a partir de 17-branques-remotes/llico.yaml. No l’editeu a mà.
set -euo pipefail

DESTI="${1:-practica-17-branques-remotes}"
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
print("Hello Git!")
FI_DEL_FITXER
git add helloGit.py
git commit -q -m 'Afegeix la salutacio inicial'
COMMIT_A=$(git rev-parse --short HEAD)
git push -q -u origin main
git branch proves
git push -q -u origin proves
git clone -q "$ARREL/origin.git" "$ARREL/companya"
cd "$ARREL/companya"
git switch -q -c prova-antiga
cat > prova.md <<'FI_DEL_FITXER'
Prova antiga
FI_DEL_FITXER
git add prova.md
git commit -q -m "Prova antiga"
git push -q -u origin prova-antiga
cd "$ARREL/HelloGit"
git fetch -q
cd "$ARREL/companya"
git push -q origin --delete prova-antiga
git switch -q main
git switch -q -c menu
cat > menu.py <<'FI_DEL_FITXER'
print("1. Saluda  2. Surt")
FI_DEL_FITXER
git add menu.py
git commit -q -m 'Afegeix el menu'
COMMIT_C=$(git rev-parse --short HEAD)
git push -q -u origin menu
cd "$ARREL/HelloGit"

cd "$ARREL/HelloGit"
echo "Punt de partida preparat a: $PWD"
if git rev-parse -q --verify HEAD >/dev/null 2>&1; then
  git log --oneline --graph --all
  git status --short
fi
