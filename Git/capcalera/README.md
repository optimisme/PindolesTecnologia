# Capçalera comuna

Quatre segons per identificar la sèrie i presentar la lliçó: graf de commits que es
construeix, número, títol i subtítol, amb una sintonia original. El generador és
[motor/capcalera.py](../../motor/capcalera.py) i la integració als vídeos,
[motor/obertura.py](../../motor/obertura.py). Els títols i subtítols de cada lliçó són
al camp `capcalera` del seu `llico.yaml`.

| Temps | Imatge | So |
| --- | --- | --- |
| 0–0,5 s | Entren els nodes i es dibuixen les connexions | Primeres notes electròniques |
| 0,5–1 s | Apareixen número, títol i subtítol | Petita escala de sintetitzador |
| 1–3,65 s | El títol es manté llegible; avança una línia menta | Motiu melòdic i percussió suau |
| 3,65–4 s | La targeta es dissol sobre el fons dels episodis | Resolució i sortida de la música |

Després de la música, la veu anuncia «Vuitena lliçó. Branques.» i el títol es manté fins
que acaba la presentació. La música no continua sota la locució.

La sintonia és una composició original sintetitzada (FM, baix, acords i percussió), de
quatre segons, estèreo i a −18 LUFS. No incorpora cap fragment d’àudio extern.

Per generar una mostra de capçalera d’una lliçó (escriu a `capcalera/output/`):

```bash
.venv/bin/python -m motor.capcalera Git --llico 8
```

La mostra anterior (`output/capcalera-02.mp4`, `titols.jpg`) correspon a la numeració antiga.
