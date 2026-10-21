# Prova de pronunciació de add i commit

El glossari anterior transformava `add` en `ad` i `commit` en `camít`.
L’usuari ha detectat que Enric diu «Andorra» i «kamit». Després de les proves, s’ha escollit `add` original i `còmit`.
S’actualitza la producció amb aquestes grafies i el plural `còmits`.

[Comparació curta](output/comparacio.mp3), amb la mateixa veu masculina
`ca-ES-EnricNeural`, a `+12%`:

1. Primera: `Guit add prepara el canvi; Guit comít el desa.`
2. Segona: `Guit àdd prepara el canvi; Guit comít el desa.`

A la primera, `add` es conserva com a l’original anglès, sense convertir-lo
en `ad`. A la segona s’utilitza `àdd` per intentar evitar la interpretació
com a abreviatura. Totes dues proven `comít` en lloc de `camít`.
Són mostres per escoltar abans d’escollir les substitucions de producció.
La frase escrita continua sent «Git add prepara el canvi; git commit el desa».

```bash
.venv/bin/python arxiu/veu-enric/add-commit/genera.py
```

## Prova add i còmit

A petició de l’usuari, es prova `add` sense modificar i `còmit` amb accent
obert a la primera síl·laba: «Guit add prepara el canvi; Guit còmit el desa».
[Escoltar la mostra](output/prova-add-comit-obert.mp3).
**Mostra aprovada:** aplicada al glossari compartit de producció.

```bash
.venv/bin/python arxiu/veu-enric/add-commit/prova_comit.py
```
