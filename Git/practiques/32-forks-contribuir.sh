#!/usr/bin/env bash
# Píndoles de Git · Lliçó 32 · Forks: contribueix al projecte original
#
# Crea el punt de partida del vídeo en una carpeta nova. A Windows, executa-ho des de Git Bash.
#     bash 32-forks-contribuir.sh            # crea la carpeta practica-32-forks-contribuir
#     bash 32-forks-contribuir.sh una-altra   # o la carpeta que indiquis
# Els remots són carpetes .git locals que fan el paper de GitHub; no cal connexió.
# Generat per Git/eines/practiques.py a partir de 32-forks-contribuir/llico.yaml. No l’editeu a mà.
set -euo pipefail

DESTI="${1:-practica-32-forks-contribuir}"
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

nou_repositori --bare "$ARREL/original.git"
git clone -q "$ARREL/original.git" "$ARREL/.preparacio"
cd "$ARREL/.preparacio"
cat > helloGit.py <<'FI_DEL_FITXER'
print("Hello Git!")
FI_DEL_FITXER
git add helloGit.py
git commit -q -m 'Afegeix la salutacio inicial'
COMMIT_B=$(git rev-parse --short HEAD)
cat > README.md <<'FI_DEL_FITXER'
Projecte HelloGit
FI_DEL_FITXER
git add README.md
git commit -q -m 'Afegeix el README'
COMMIT_C=$(git rev-parse --short HEAD)
git push -q -u origin main
cd "$ARREL"
rm -rf .preparacio && git clone -q --bare original.git fork.git
git clone -q "$ARREL/fork.git" "$ARREL/HelloGit"
cd "$ARREL/HelloGit"
git remote add upstream ../original.git && git fetch -q upstream

cd "$ARREL/HelloGit"
echo "Punt de partida preparat a: $PWD"
if git rev-parse -q --verify HEAD >/dev/null 2>&1; then
  git log --oneline --graph --all
  git status --short
fi
