#!/usr/bin/env bash
# Píndoles de Git · Lliçó 21 · Rebase: continua sobre una base nova
#
# Crea el punt de partida del vídeo en una carpeta nova. A Windows, executa-ho des de Git Bash.
#     bash 21-rebase.sh            # crea la carpeta practica-21-rebase
#     bash 21-rebase.sh una-altra   # o la carpeta que indiquis
# No cal cap connexió: tot passa al teu ordinador.
# Generat per Git/eines/practiques.py a partir de 21-rebase/llico.yaml. No l’editeu a mà.
set -euo pipefail

DESTI="${1:-practica-21-rebase}"
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
print("Hola, Anna!")
FI_DEL_FITXER
git commit -q -am "Personalitza la salutacio"
COMMIT_C=$(git rev-parse --short HEAD)
cat > notes.md <<'FI_DEL_FITXER'
La salutació es personalitza per a l’Anna.
FI_DEL_FITXER
git add notes.md
git commit -q -m 'Documenta la salutacio'
COMMIT_E=$(git rev-parse --short HEAD)
git switch -q main
cat > README.md <<'FI_DEL_FITXER'
Projecte HelloGit
FI_DEL_FITXER
git add README.md
git commit -q -m 'Afegeix el README'
COMMIT_D=$(git rev-parse --short HEAD)

cd "$ARREL/HelloGit"
echo "Punt de partida preparat a: $PWD"
if git rev-parse -q --verify HEAD >/dev/null 2>&1; then
  git log --oneline --graph --all
  git status --short
fi
