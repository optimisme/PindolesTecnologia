# Pronunciació de GitHub

La variant **B: `Guit jab`** es va escollir inicialment, però després
l’usuari l’ha descartada perquè no s’assembla prou a la pronunciació anglesa.
La prova de dues veus també s’ha descartat. Finalment s’ha escollit
[la segona variant amb Enric, Guit Hàb](../github-enric/README.md).

- [A: text original GitHub](output/01-original.mp3)
- [B: aproximació Guit jab — descartada](output/02-jab.mp3)
- [Variant addicional Guit hàb](output/03-hab.mp3)
- [Referència anglesa, veu Guy](output/04-angles.mp3)

La referència anglesa només és una mostra. La producció continua amb Enric.
En anglès, `hub` té hac aspirada i vocal /ʌ/:
[Cambridge](https://dictionary.cambridge.org/pronunciation/english/hub).
`Guit jab` és una aproximació pràctica per al sintetitzador català.

Per regenerar aquestes mostres des de la carpeta vids:

```bash
.venv/bin/python arxiu/veu-enric/genera_github.py
```
