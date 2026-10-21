# Restore: desmarca o descarta un canvi local

Veu: `ca-ES-EnricNeural` · Català · 83.5 segons

Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.

Punt de partida: HelloGit.py és un fitxer seguit, amb print("Hello Git!") a l'últim commit. L'hem editat a print("Hola, Anna!") i hem fet git add helloGit.py. No hi ha altres canvis. L'exemple usa el nom helloGit.py en minúscula. Restore --staged restaura per defecte l'índex des de HEAD i conserva el directori de treball. Restore sense staged restaura per defecte el directori de treball des de l'índex. Es descarta l'edició local només després d'haver-la revisat i haver decidit que no es vol conservar.

## Capçalera musical (0,0–4,0 s)

**Animació:** graf de commits, número de lliçó, títol i subtítol.
**Àudio:** sintonia electrònica original. Sense locució durant la música.

## Presentació de la lliçó (4,0–6.54 s)

**Locució:** Novena lliçó, Restore.

**Animació:** es manté el títol fins que acaba la presentació; després es dissol.

## Volies preparar aquest fitxer? (6.5–15.4 s)

**Locució:** Has preparat un canvi amb git add, però t'has equivocat de fitxer. Vols treure'l de preparació sense perdre l'edició.

**Animació:** HelloGit.py apareix seleccionat a la preparació, amb el missatge nou. L'objectiu és desmarcar-lo conservant el fitxer editat.

## El missatge nou està preparat (15.4–25.5 s)

**Locució:** Treball i preparació tenen el missatge nou. L'últim commit conserva l'original. Són les tres zones que ja coneixem.

**Animació:** Treball V2, preparació V2 i historial V1. La terminal mostra M a la primera columna perquè el canvi està preparat.

**Comandes en pantalla:**

```bash
git status --short
```

## Desmarcar conserva l'edició (25.5–34.5 s)

**Locució:** Git restore amb l'opció staged i el nom del fitxer el treu de preparació. L'edició del directori de treball es conserva.

**Animació:** L'índex torna de V2 a V1 per còpia de HEAD. Treball conserva V2. La fletxa va d'historial a preparació.

**Comandes en pantalla:**

```bash
git restore --staged helloGit.py
```

## El canvi continua al fitxer (34.5–43.6 s)

**Locució:** Git status ara marca el canvi com a pendent de preparar. Amb git diff podem revisar exactament què continua modificat.

**Animació:** Treball V2, preparació V1 i historial V1. Status té M a la segona columna. El diff mostra la salutació nova respecte de l'original.

**Comandes en pantalla:**

```bash
git status --short
git diff
```

## Aquest canvi local no el volem (43.6–53.2 s)

**Locució:** Després de revisar-lo, decidim que tampoc volem conservar aquest canvi local. Encara no té cap commit: el descartarem del fitxer.

**Animació:** Es compara el missatge editat amb el que es conservarà. Una etiqueta explicita que aquesta edició local es descartarà, sense presentar-ho com una recuperació automàtica.

## Restore copia des de la preparació (53.2–62.2 s)

**Locució:** Fem git restore amb el nom del fitxer. Restaura el treball des de la preparació, que ara coincideix amb l'últim commit.

**Animació:** La fletxa va de preparació a treball i copia V1. L'edició V2 desapareix del fitxer. L'índex i l'historial no canvien.

**Comandes en pantalla:**

```bash
git restore helloGit.py
```

## El missatge original reapareix (62.2–71.7 s)

**Locució:** El missatge original reapareix i git status queda sense canvis pendents. No hem creat ni esborrat cap commit de l'historial.

**Animació:** Les tres zones contenen V1. Status --short no mostra cap línia i els commits no es mouen.

**Comandes en pantalla:**

```bash
git status --short
```

## Desmarcar o descartar? (71.7–83.5 s)

**Locució:** Amb staged, desmarquem i conservem l'edició. Sense staged, restaurem el treball des de la preparació. Tria l'operació segons què vols conservar.

**Animació:** Dos panells distingeixen treure de preparació i descartar una edició de treball. Les comandes estan vinculades a les seves fletxes i efectes.

**Comandes en pantalla:**

```bash
git restore --staged helloGit.py
git restore helloGit.py
```
