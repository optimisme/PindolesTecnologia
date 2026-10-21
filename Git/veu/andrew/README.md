# Andrew: veu amb català i anglès explícits

Configuració actual: **en-US-AndrewMultilingualNeural**, català **+5%**,
anglès **+0%**, amb **500 ms en tots dos sentits** quan canvia l’idioma.
És la veu de totes les lliçons de la sèrie (`serie.yaml`). Els vídeos anteriors
de les lliçons 0 i 1 (ara 0 i 3) ja en fan servir aquest ajust. La [guia d’estil](../../README.md#guia-destil)
regula també les pauses de lectura i el subratllat de comandes.

- [Lliçó 0: introducció](../../arxiu/produccio-anterior/00-introduccio/output/00-introduccio.mp4) (vídeo anterior).
- [Antiga lliçó 1, ara 3: primer commit](../../arxiu/produccio-anterior/01-primer-commit/output/01-primer-commit.mp4) (vídeo anterior).
- [Configuració de les noves mostres](mostra.json).
- [Estat de selecció](estat.json).

## Idiomes i velocitats

Cada fragment porta `<lang xml:lang="ca-ES">` o `<lang xml:lang="en-US">`
i un únic `<prosody>` amb la velocitat de l’idioma. `language_rates` té
prioritat sobre el camp global `rate`. Les comandes es llegeixen com un
fragment coherent, sense introduir pauses entre les seves paraules.
La síntesi utilitza `speak_ssml_async`; no depèn de detectar l’idioma.

Les pauses de lectura entre explicacions són independents dels 500 ms de
canvi d’idioma i es defineixen a cada pas dels episodis revisats.

## Generar una mostra

Des de la carpeta `Git`, amb l’entorn preparat a l’arrel:

```bash
../.venv/bin/python veu/andrew/genera_azure.py --pausa-ms 500
```

El generador carrega automàticament la configuració privada local, com es
concreta al [README de l’arrel](../../../README.md#preparar-lentorn).
`--configura` permet introduir la clau de manera oculta si falta; no cal
fer-ho cada vegada. L’accés correspon a Azure Speech i al seu endpoint base
`.cognitiveservices.azure.com`, sense Project endpoint ni Azure OpenAI endpoint.

Els noms de sortida incorporen les velocitats i la pausa perquè cada
comparació es conservi. Canviar `mostra.json` no regenera els vídeos: cada
lliçó pren la configuració de `serie.yaml`.

## Mostres històriques

La [mostra amb català +8% i anglès +0%](output/andrew-idiomes-explicits-pauses-500ms-ca8-en0.mp3)
va ser acceptada abans de reduir el català a +5%. El seu
[SSML](prova-pauses-500ms-ca8-en0.ssml) i [informe](resultat-pauses-500ms-ca8-en0.json)
conserven l’ajust original. Les demos amb velocitat global +12% també es
conserven com a comparacions anteriors. No representen la configuració actual.
La detecció automàtica i el muntatge de dues veus descartats són a `../../arxiu/`.
