"""Text fonètic per al TTS i recuperació del text original amb els seus temps."""
from bisect import bisect_left, bisect_right
import hashlib
import json
from pathlib import Path
import re

GLOSSARY_PATH = Path(__file__).with_name("pronunciacions.json")
PROFILE = json.loads(GLOSSARY_PATH.read_text())
FORMS = {key.casefold(): value for key, value in PROFILE["pronunciations"].items()}
PATTERN = re.compile(r"\b(" + "|".join(
    re.escape(key) for key in sorted(FORMS, key=len, reverse=True)
) + r")\b", re.IGNORECASE)
# La versió inclou també el contracte d'alineació dels subtítols.
VERSION = "original-token-spans-v1"
DIGEST = hashlib.sha256(json.dumps(
    [VERSION, PROFILE], ensure_ascii=False, sort_keys=True
).encode()).hexdigest()


def spoken_text(narration):
    return PATTERN.sub(lambda match: FORMS[match.group().casefold()], narration)


def voice_signature(narration, tts_text, voice, rate):
    return hashlib.sha256(json.dumps([
        narration, tts_text, voice, rate, "effective-speech-v1", VERSION
    ]).encode()).hexdigest()


def cached_voice_matches(cached, narration, tts_text, voice, rate):
    if cached.get("signature") == voice_signature(narration, tts_text, voice, rate):
        return True
    # Migració de fragments anteriors: només es poden reutilitzar si la
    # signatura antiga prova que text, veu i velocitat continuen sent els mateixos.
    old_digest = cached.get("pronunciation", {}).get("sha256")
    if not old_digest:
        return False
    old_signature = hashlib.sha256(json.dumps([
        narration, tts_text, voice, rate, old_digest
    ]).encode()).hexdigest()
    return cached.get("signature") == old_signature


def normalized(text):
    return "".join(char.casefold() for char in text if char.isalnum())


def original_words(words, narration, transform=spoken_text):
    """Projecta mots originals sobre marques TTS, incloent canvis 1:N i N:1.

    Les marques poden separar apostrofs, guionets o «Guit Hàb». S'alineen els
    caràcters pronunciats sense espais/puntuació i es recuperen els tokens del
    guió. Si el servei modifica el text, aturem el procés en lloc de publicar
    subtítols fonètics o desincronitzats.
    """
    source = narration.split()
    spoken = [normalized(transform(token)) for token in source]
    boundaries = [(word, normalized(word["text"])) for word in words]
    boundaries = [(word, token) for word, token in boundaries if token]
    if "".join(spoken) != "".join(token for _, token in boundaries):
        raise ValueError(f"Les marques TTS no coincideixen amb el text pronunciat: {narration!r}")
    starts, ends, cursor = [], [], 0
    for _, token in boundaries:
        starts.append(cursor)
        cursor += len(token)
        ends.append(cursor)

    def time_at(position, end=False):
        index = (bisect_left(ends, position) if end else bisect_right(ends, position))
        index = min(index, len(boundaries)-1)
        word, token = boundaries[index]
        fraction = (position-starts[index])/len(token)
        return word["start"] + fraction*(word["end"]-word["start"])

    restored, cursor, prefix = [], 0, ""
    for token, spoken in zip(source, spoken):
        if not spoken:
            if restored:
                restored[-1]["text"] += " " + token
            else:
                prefix += token + " "
            continue
        restored.append({"text": prefix + token, "start": time_at(cursor),
                         "end": time_at(cursor+len(spoken), end=True)})
        prefix = ""
        cursor += len(spoken)
    return restored


def profile_metadata():
    return {"profile": PROFILE["profile"], "sha256": DIGEST,
            "glossary": GLOSSARY_PATH.name, "alignment": VERSION}
