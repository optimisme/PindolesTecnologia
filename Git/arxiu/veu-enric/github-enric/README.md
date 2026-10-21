# Noves grafies de GitHub amb una sola veu catalana

Totes les mostres utilitzen `ca-ES-EnricNeural`, a `+12%`, sense fragments
anglesos d’una altra veu. Es manté el criteri de la segona mostra inicial.
L’usuari ha escollit la **segona variant, `Guit Hàb`**, per al glossari de producció.

[Escoltar la comparació](output/comparacio-enric.mp3). L’ordre és:

1. **Primera:** `Guit Hub`, mantenint el mot anglès Hub.
2. **Segona — escollida:** `Guit Hàb`, amb vocal accentuada.
3. **Tercera:** `Guit Hahb`, una altra grafia per intentar induir la consonant.
4. **Quarta:** `Guit Khàb`, una aproximació alternativa al so aspirat.
5. Comprovació catalana: «La branca salutació i la branca correcció conserven
   els noms en català.»

La frase comuna és «Publiquem la branca salutació a GitHub».
Els MP3 individuals i les metadades del TTS es desen també a `output/`.
`mostra.json` és independent del glossari de producció; les proves no
modifiquen els vídeos. Es descarten `Guit jab` i la barreja de dues veus.

Per regenerar des de la carpeta vids:

```bash
.venv/bin/python arxiu/veu-enric/github-enric/genera.py
```
