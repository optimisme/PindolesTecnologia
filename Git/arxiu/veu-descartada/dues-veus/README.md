# Dues veus: variant descartada

Document històric. La veu escollida per a la nova versió és
[Andrew amb SSML explícit](../../../veu/andrew/README.md).

**Descartada per l’usuari:** la combinació de veus no resulta natural. Es manté
la segona mostra amb una sola veu catalana Enric i es busquen altres grafies
per a GitHub.

Prova aïllada i descartada; no s’ha integrat al renderitzador. La producció
manté Enric i la variant escollida [Guit Hàb](../../veu-enric/github-enric/README.md).

- Català: veu masculina `ca-ES-EnricNeural`.
- Anglès: veu masculina `en-US-GuyNeural`.
- Mateixa velocitat: `+12%`.

Es genera la frase completa amb Enric per conservar el ritme del català, i es
reemplacen únicament els trams anglesos amb Guy. Les marques WordBoundary
delimiten cada substitució. Els mots anglesos s’envien amb l’ortografia original,
sense grafies aproximades. Es normalitza el volum i s’aplica un solapament de
4 ms als enllaços per evitar clics. El canvi de timbre entre veus pot ser audible;
aquesta prova permet valorar-lo abans d’aplicar el mètode a les lliçons.

Els identificadors `salutacio`, `correccio` i `recuperacio` tenen equivalències
catalanes `salutació`, `correcció` i `recuperació` per al sintetitzador. No es
converteixen en anglès. Les frases de la mostra són:

1. A GitHub publiquem els commits de la branca salutació.
2. Creem la branca correcció des de main i fem un commit.
3. Amb git fetch revisem els canvis abans de fer merge.

[Escoltar les tres frases](output/prova-mixta.mp3). Cada exemple també té el seu
MP3 i un JSON que identifica els trams anglesos, les veus i els textos enviats.
`mostra.json` configura la prova, amb independència del glossari de producció.

Per regenerar des de la carpeta vids:

```bash
.venv/bin/python arxiu/veu-descartada/dues-veus/genera.py
```
