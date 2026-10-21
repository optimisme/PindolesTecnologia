# Arxiu de la pronunciació guiada amb Enric

Estat: referència històrica del perfil dels 25 MP4 actuals. L’usuari ha aprovat
Andrew amb SSML per a la futura versió, documentat a
[veu/andrew](../../veu/andrew/README.md). La migració dels vídeos està pendent
de revisar-ne el contingut. Les variants d’aquesta carpeta documenten el
recorregut d’Enric; no totes es van escollir.

Mostra de comparació amb la mateixa veu masculina catalana de la sèrie,
`ca-ES-EnricNeural`, a la mateixa velocitat (`+12%`).

- [Comparació amb presentació parlada de cada variant](output/comparacio.mp3)
- [Lectura actual](output/01-original.mp3)
- [Lectura amb pronunciació guiada](output/02-pronuncia-guiada.mp3)
- [Text i glossari editable](mostra.json)

La comparació diu primer «Primera mostra. Lectura actual» i després
«Segona mostra. Pronunciació guiada». En tots dos casos la frase escrita és:

> Amb Git, fem un commit a main. Després fem push i pull. Revisem el canvi abans
> de fer merge o rebase. Amb fetch descarreguem les novetats.

La segona variant transforma només el text que rep el sintetitzador. Les formes
com «guit», «méin» o «ribéis» són instruccions aproximades per a aquesta veu,
no traduccions ni grafies per als apunts. Cal validar-les escoltant-les;
especialment merge requereix trobar un equilibri amb els sons disponibles.
La segona variant s’ha integrat al renderitzador i a les 25 lliçons.
La comparació original es conserva com a referència: posteriorment l’usuari
ha escollit `commit` → `còmit`, `commits` → `còmits`, `add` sense modificar
i `GitHub` → `Guit Hàb`. El glossari de producció inclou aquestes correccions.
El glossari dels MP4 actuals és [`../../pronunciacions.json`](../../pronunciacions.json),
i el procés es documenta a [`../../DESENVOLUPAMENT.md`](../../DESENVOLUPAMENT.md).
Aquesta carpeta conserva la comparació original com a referència; modificar
`mostra.json` només modifica la prova, no el glossari de la sèrie.

El connector actual no admet SSML personalitzat, segons la
[documentació d’edge-tts](https://github.com/rany2/edge-tts#custom-ssml).
La prova utilitza aproximacions ortogràfiques. Si no donen un resultat
satisfactori, es pot valorar un motor que admeti català i pronunciació
multilingüe o control de fonemes, mantenint una sola veu durant les frases.

Per regenerar des de `01-Git/vids`:

```bash
.venv/bin/python arxiu/veu-enric/genera_mostra.py
```

La generació envia al mateix servei TTS només els textos de la mostra i les
dues frases de presentació. L’àudio queda desat a output i es reutilitza si
el text, la veu i la velocitat no han canviat.
