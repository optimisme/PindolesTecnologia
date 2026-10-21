# Andrew automàtic: variant descartada

Aquest document conserva el resultat de l’experiment inicial amb Edge.
Posteriorment s’ha aprovat [Andrew amb SSML explícit](../../../veu/andrew/README.md)
a Azure Speech. La detecció automàtica d’aquesta carpeta continua descartada.

**Valoració de l’usuari:** es descarta Andrew amb detecció automàtica perquè
barreja fragments en francès. Enric es percep més robòtic, però pronuncia molt
millor. La producció es manté amb Enric i el glossari validat. No s’ha aprovat
cap canvi de veu ni s’han regenerat els vídeos arran d’aquesta prova.
L’SSML amb Azure continua sense validar, perquè no hi ha l’accés configurat.
La valoració es conserva independentment a `avaluacio-usuari.json`.

Prova aïllada. Els 25 vídeos i les còpies de l’escriptori continuen amb Enric.

## Mostres

- [AndrewMultilingual, text original i detecció automàtica](output/01-andrew-auto.mp3).
- [Enric, amb el glossari actual](output/02-enric-actual.mp3).

Mateix contingut i mateixa velocitat `+12%`. Volum normalitzat a -18 LUFS.
Andrew rep l’anglès original: GitHub, git add, git commit, main, fetch, merge,
rebase i log. Les paraules catalanes salutació i correcció porten els accents
correctes. Enric rep les equivalències actuals de `pronunciacions.json`.

La disponibilitat efectiva d’`en-US-AndrewMultilingualNeural` s’ha comprovat
amb la llista del servei Edge, desada a `veus-disponibles.json`.
Microsoft documenta català i anglès entre les llengües autodetectades d’Andrew:
[veus multilingües i control d’idioma](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice).

## Resultat de la prova SSML

S’ha generat `prova.ssml` amb una sola veu Andrew i etiquetes `<lang>` que
alternen `ca-ES` i `en-US`. El document és XML vàlid. També s’ha enviat una
petició experimental al servei actual, només en el procés de la prova.
No s’ha modificat la biblioteca instal·lada ni el renderitzador.

**Resultat:** `NoAudioReceived`. La connexió actual no ha retornat àudio vàlid
per a aquesta petició SSML. No hi ha cap MP3 de SSML per comparar; el MP3
Andrew disponible és només el de text pla amb detecció automàtica.

Això concorda amb la [limitació documentada d’edge-tts](https://github.com/rany2/edge-tts#custom-ssml):
no admet SSML personalitzat amb etiquetes addicionals. L’API Azure Speech sí
que ofereix `<lang>` per a aquestes veus. No hi ha una clau i regió d’Azure
Speech configurades en aquest procés; per comprovar l’SSML amb aquella API
cal configurar-ne l’accés. No s’han escrit credencials en cap fitxer.

`resultat.json` conserva els textos, els trams d’idioma i el resultat exacte.
`genera.py` restaura la funció original del connector en acabar la petició,
incloent el cas d’error. Les dues mostres de text pla es conserven.

Per regenerar des de la carpeta vids:

```bash
.venv/bin/python arxiu/veu-descartada/andrew-automatic/genera.py
```

La mostra aprovada amb l’API Azure, els idiomes explícits i les instruccions de
configuració és a [veu/andrew](../../../veu/andrew/README.md). S’ha generat i
aprovat després d’aquest experiment inicial.
