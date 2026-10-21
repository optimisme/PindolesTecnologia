#!/usr/bin/env bash
# Píndoles de Git · Lliçó 29 · Bisect: troba el primer commit que falla
#
# Crea el punt de partida del vídeo en una carpeta nova. A Windows, executa-ho des de Git Bash.
#     bash 29-bisect.sh            # crea la carpeta practica-29-bisect
#     bash 29-bisect.sh una-altra   # o la carpeta que indiquis
# No cal cap connexió: tot passa al teu ordinador.
# Generat per Git/eines/practiques.py a partir de 29-bisect/llico.yaml. No l’editeu a mà.
set -euo pipefail

DESTI="${1:-practica-29-bisect}"
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
git tag -a v1.0 -m "Primera entrega"
cat > helloGit.py <<'FI_DEL_FITXER'
# Salutació del projecte
print("Hello Git!")
FI_DEL_FITXER
git commit -q -am "Afegeix un comentari"
COMMIT_C=$(git rev-parse --short HEAD)
cat > helloGit.py <<'FI_DEL_FITXER'
# Salutació del projecte
print(salutacio)
FI_DEL_FITXER
git commit -q -am "Prepara la salutacio personalitzada"
COMMIT_D=$(git rev-parse --short HEAD)
cat > notes.md <<'FI_DEL_FITXER'
Idea 1
FI_DEL_FITXER
git add notes.md
git commit -q -m 'Comença les notes'
COMMIT_E=$(git rev-parse --short HEAD)
cat > notes.md <<'FI_DEL_FITXER'
Idea 1, idea 2
FI_DEL_FITXER
git commit -q -am "Amplia les notes"
COMMIT_F=$(git rev-parse --short HEAD)
cat > notes.md <<'FI_DEL_FITXER'
Idea 1, idea 2, idea 3
FI_DEL_FITXER
git commit -q -am "Completa les notes"
COMMIT_G=$(git rev-parse --short HEAD)
cat > notes.md <<'FI_DEL_FITXER'
Idees revisades
FI_DEL_FITXER
git commit -q -am "Revisa les notes"
COMMIT_H=$(git rev-parse --short HEAD)

cd "$ARREL/HelloGit"
echo "Punt de partida preparat a: $PWD"
if git rev-parse -q --verify HEAD >/dev/null 2>&1; then
  git log --oneline --graph --all
  git status --short
fi
