"""Recupera els mots originals del guió sobre les marques temporals del TTS."""
from bisect import bisect_left, bisect_right


def normalized(text):
    return "".join(char.casefold() for char in text if char.isalnum())


def original_words(words, narration, transform=lambda token: token):
    """Projecta mots originals sobre marques TTS, incloent canvis 1:N i N:1.

    Les marques poden separar apòstrofs o guionets. S'alineen els caràcters
    pronunciats sense espais ni puntuació i es recuperen els tokens del guió.
    Si el servei modifica el text, aturem el procés en lloc de publicar
    subtítols desincronitzats.
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
