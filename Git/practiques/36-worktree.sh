#!/usr/bin/env bash
# Píndoles de Git · Lliçó 36 · Worktree: corregeix main sense interrompre la feina
#
# Crea el punt de partida del vídeo en una carpeta nova. A Windows, executa-ho des de Git Bash.
#     bash 36-worktree.sh            # crea la carpeta practica-36-worktree
#     bash 36-worktree.sh una-altra   # o la carpeta que indiquis
# No cal cap connexió: tot passa al teu ordinador.
# Generat per Git/eines/practiques.py a partir de 36-worktree/llico.yaml. No l’editeu a mà.
set -euo pipefail

DESTI="${1:-practica-36-worktree}"
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

nou_repositori "$ARREL/projecte"
cd "$ARREL/projecte"
cd "$ARREL/projecte"
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
git switch -q -c salutacio
cat > helloGit.py <<'FI_DEL_FITXER'
print("Hola, Ermessenda!")
FI_DEL_FITXER

cd "$ARREL/projecte"
echo "Punt de partida preparat a: $PWD"
if git rev-parse -q --verify HEAD >/dev/null 2>&1; then
  git log --oneline --graph --all
  git status --short
fi
