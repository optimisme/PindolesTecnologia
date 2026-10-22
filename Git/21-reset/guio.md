# Lliçó 21 · Reset: torna enrere un commit local

**Sèrie:** Píndoles de Git · **Capçalera:** RESET — Torna enrere un commit local  
**Veu:** en-US-AndrewMultilingualNeural; català +5%, anglès +0%; 500 ms en cada canvi d’idioma.  
**Format:** sense preguntes; pauses de lectura explícites; anglès en cursiva als subtítols.

**Punt de partida reproduïble:** [`practiques/21-reset.sh`](../practiques/21-reset.sh)

## Capçalera i presentació

4 s de música comuna. Després, la veu llegeix:

> Vint-i-unena lliçó. *Reset*.

## Objectiu i punt de partida

En aquesta lliçó aprendrem a comparar *reset soft* i *mixed* sense confondre què passa amb el treball i la preparació. *(pausa 2.5 s)*

L’últim *commit*, encara no publicat, conté la salutació nova. Volem tornar-hi a treballar abans de confirmar-la de nou. *(pausa 3.5 s)*

**Visual:** Objectiu en una frase; esquema general del resultat.

## Reprendre un commit local

Volem continuar treballant en el contingut de l’últim *commit*. Compararem dues formes de *reset* que conserven el fitxer de treball. *(pausa 3 s)*

**Visual:** Graf A, B i C; main i HEAD a C. Panells treball, preparació i historial amb la SALUTACIÓ NOVA.

## On anirà la branca

En aquest exemple, *HEAD* segueix *main*. *HEAD* titlla u vol dir un pas enrere, així que la destinació és el *commit* anterior, el de l’exclamació. *(pausa 3 s)*

**Visual:** Subratllar HEAD i després ~1 a HEAD~1; fletxa conceptual de C a B, sense executar encara.

## Terminal · `git reset --soft HEAD~1`

> **Alternativa soft.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git reset` | Comencem per l’alternativa *soft*. | 2.5 s |
| `--soft` | Mou la branca i conserva la preparació i el treball. | 2.5 s |
| `HEAD~1` | La destinació és el *commit* anterior. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* torna al *commit* anterior. El treball i la preparació conserven la salutació nova, que ara queda preparada respecte d’aquell *commit*. *(pausa 3.5 s)*

Sortida real: *cap línia*.

**Visual:** Moure només main i HEAD. C es queda atenuat fora de la línia, sense esborrar-lo.

## Terminal · `git diff --staged`

> **Alternativa soft.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git diff` | Comprovem el canvi que ha quedat preparat. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** La salutació nova surt com a canvi preparat. Podem retocar-la i confirmar-la de nou. *(pausa 3.5 s)*

Sortida real:

```text
diff --git a/helloGit.py b/helloGit.py
index 52662af..9dfb79d 100644
--- a/helloGit.py
+++ b/helloGit.py
@@ -1 +1 @@
-print("Hello Git!")
+print("Hola, Ermessenda!")
```

**Visual:** Fletxa HISTORIAL → PREPARACIÓ amb la salutació nova.

## Tornem al punt de partida

Tornem al dibuix inicial, amb *main* a l’últim *commit*. L’opció següent és una alternativa: no s’executa després de *soft*. *(pausa 3 s)*

**Visual:** Separador TORNEM AL PUNT DE PARTIDA. Restaurar el dibuix inicial complet.

## Terminal · `git reset --mixed HEAD~1`

> **Alternativa mixed.** Parteix del seu propi punt; no s’encadena amb el camí principal.

| Subratllat | Locució | Pausa |
| --- | --- | ---: |
| `git reset` | Ara provem l’alternativa *mixed*. | 2.5 s |
| `--mixed` | Mou la branca i torna la preparació a la destinació. Conserva el treball. | 2.5 s |
| execució | Executem l’ordre. | 1.5 s |

**Resultat:** *main* i la preparació tornen al *commit* anterior, però el treball manté la salutació nova. El canvi queda sense preparar. *(pausa 3.5 s)*

Sortida real:

```text
Unstaged changes after reset:
M	helloGit.py
```

**Visual:** Moure main i HEAD a B; copiar l’ORIGINAL a la preparació; deixar la SALUTACIÓ NOVA al treball.

## La diferència és la preparació

En tots dos casos la branca torna enrere i el fitxer conserva la salutació nova. *Soft* deixa el canvi preparat; *mixed* el deixa pendent de preparar. *(pausa 4 s)*

**Visual:** Taula de dues files. SOFT · branca B, preparació nova, treball nou. MIXED · branca B, preparació original, treball nou.

## Resum final

En aquest exemple, *reset* fa tornar la branca local un *commit* enrere. *(pausa 2.5 s)*

*Soft* conserva la preparació; *mixed* la torna a la destinació. *(pausa 2.5 s)*

Tots dos conserven el treball; només els fem servir amb *commits* que no hem publicat. *(pausa 2.5 s)*

**Visual:** Tres idees finals; ressaltar només la idea que s’està explicant.

## Pràctica final

Reprodueix cada alternativa en un repositori de pràctiques separat, amb un últim *commit* no publicat. Compara el treball, la preparació i l’historial després de cada una. *(pausa 4 s)*

**Visual:** Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.
