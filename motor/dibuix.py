"""Primitives de dibuix comunes: paleta, fonts, panells, terminal, nodes i subtítols."""
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from motor.alineacio import original_words

W, H = 1280, 720
BG, PANEL, BORDER = "#0D1422", "#151F31", "#2C3A50"
WHITE, MUTED, ORANGE, MINT, PURPLE = "#F5F7FC", "#AAB8CD", "#FF845E", "#71E2B6", "#B8A0FF"
FONT_DIR = Path("/System/Library/Fonts/Supplemental")


def font(size, bold=False, mono=False):
    candidates = ([Path("/System/Library/Fonts/Menlo.ttc"),
                   Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")]
                  if mono else [FONT_DIR / ("Arial Bold.ttf" if bold else "Arial.ttf"),
                   Path("/usr/share/fonts/truetype/dejavu") / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")])
    for p in candidates:
        if p.exists():
            return ImageFont.truetype(str(p), size)
    raise RuntimeError("Cal instal·lar Arial o DejaVu Sans per renderitzar els textos.")


F = {"small": font(16), "label": font(17, True), "body": font(24),
     "caption": font(24), "h2": font(31, True), "title": font(47, True),
     "hero": font(82, True), "code": font(23, mono=True), "tinycode": font(18, mono=True),
     "lead": font(29), "leadcode": font(27, mono=True)}


def clamp(t):
    return max(0.0, min(1.0, t))


def ease(t):
    t = clamp(t)
    return 1 - (1 - t) ** 3


def text(d, pos, content, style="body", color=WHITE, anchor=None):
    d.text(pos, content, font=F[style], fill=color, anchor=anchor)


def panel(d, box, fill=PANEL, outline=BORDER, radius=20):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=2)


def pill(d, x, y, content, color=MINT, fill="#1E3A35"):
    width = d.textlength(content, font=F["label"]) + 30
    d.rounded_rectangle((x, y, x + width, y + 33), 12, fill=fill)
    text(d, (x + 15, y + 7), content, "label", color)


def arrow(d, start, end, color=MINT, width=4):
    """Fletxa geomètrica: tija recta i punta triangular plena, en una sola forma suavitzada.

    Es dibuixa a 4× sobre una màscara i es redueix, perquè les vores diagonals no
    quedin dentades.
    """
    scale = 4
    a = math.atan2(end[1] - start[1], end[0] - start[0])
    length = math.hypot(end[0] - start[0], end[1] - start[1])
    head = min(width * 3.5, length * .6)
    half_head, half_shaft = width * 2.2, width / 2
    # Contorn en coordenades locals (eix x al llarg de la fletxa), de l’inici a la punta.
    outline = [(0, -half_shaft), (length - head, -half_shaft), (length - head, -half_head), (length, 0),
               (length - head, half_head), (length - head, half_shaft), (0, half_shaft)]
    cos, sin = math.cos(a), math.sin(a)
    points = [(start[0] + x * cos - y * sin, start[1] + x * sin + y * cos) for x, y in outline]
    left, top = math.floor(min(x for x, _ in points)) - 2, math.floor(min(y for _, y in points)) - 2
    right, bottom = math.ceil(max(x for x, _ in points)) + 2, math.ceil(max(y for _, y in points)) + 2
    mask = Image.new('L', ((right - left) * scale, (bottom - top) * scale), 0)
    ImageDraw.Draw(mask).polygon([((x - left) * scale, (y - top) * scale) for x, y in points], fill=255)
    mask = mask.resize((right - left, bottom - top), Image.Resampling.LANCZOS)
    d._image.paste(color, (left, top, right, bottom), mask)


def node(d, x, y, label=None, color=ORANGE, scale=1):
    r = max(1, int(19 * scale))
    d.ellipse((x-r-7, y-r-7, x+r+7, y+r+7), fill=PANEL, outline=BORDER, width=2)
    d.ellipse((x-r, y-r, x+r, y+r), fill=color)
    if label:
        text(d, (x, y+40), label, "tinycode", MUTED, "mt")


def wrap(d, content, max_width, style="caption"):
    lines = []
    current = ""
    for word in content.split():
        candidate = f"{current} {word}".strip()
        if current and d.textlength(candidate, font=F[style]) > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def type_text(content, p):
    return content[:int(len(content) * clamp(p))]


def terminal(d, box, title="TERMINAL"):
    x, y, right, bottom = box
    panel(d, box, "#080F1C", BORDER, 16)
    for i,color in enumerate(("#F17878", "#EEC36E", MINT)):
        d.ellipse((x+18+i*20, y+15, x+27+i*20, y+24), fill=color)
    text(d, (x+90, y+12), title, "small", MUTED)
    d.line((x+1, y+38, right-1, y+38), fill=BORDER, width=1)


def command(d, x, y, content, reveal=1):
    text(d, (x, y), "$", "code", MINT)
    text(d, (x+28, y), type_text(content, reveal), "code")


def base(scene, index, total, config=None):
    config = config or {}
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # Una trama discreta manté el fons coherent entre tots els episodis.
    for x in range(24, W, 36):
        for y in range(22, H, 36):
            d.ellipse((x, y, x+1, y+1), fill="#202B3C")
    d.rounded_rectangle((64, 31, 92, 59), 7, fill=ORANGE)
    d.line((72, 38, 84, 50), fill=BG, width=3)
    d.ellipse((70, 36, 75, 41), fill=BG)
    d.ellipse((81, 47, 86, 52), fill=BG)
    text(d, (106, 36), config.get("series", "Píndoles").upper(), "label", WHITE)
    episode = config.get("episode_number", 1)
    topic = config.get("short_title", "INTRODUCCIÓ")
    text(d, (1216, 36), f"{episode:02}  /  {topic}     ·     {index+1:02}/{total:02}", "small", MUTED, "rt")
    text(d, (64, 91), scene["label"], "label", ORANGE)
    # Els títols llargs (ordres amb missatges) es redueixen fins que hi caben.
    title, size = scene["title"], 47
    while size > 26 and d.textlength(title, font=font(size, True)) > W-128:
        size -= 1
    d.text((64, 126+(47-size)*.6), title, font=font(size, True), fill=WHITE)
    return im


def run(args):
    subprocess.run([str(a) for a in args], check=True)


def probe(path):
    return float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)
    ], text=True).strip())


def subtitles_from_words(words, narration):
    # Els subtítols recuperen sempre l'ortografia del guió.
    words = original_words(words, narration)
    cues, group = [], []
    def flush():
        if group:
            cues.append({"start": group[0]["start"], "end": group[-1]["end"]+.12,
                         "text": " ".join(w["text"] for w in group)})
            group.clear()
    for word in words:
        proposed = " ".join(w["text"] for w in group + [word])
        if group and (len(proposed) > 76 or word["start"]-group[0]["start"] > 3.5):
            flush()
        group.append(word)
        if word["text"].endswith((".", "?", "!", ":")) or (word["text"].endswith(",") and len(group) >= 4):
            flush()
    flush()
    for a,b in zip(cues, cues[1:]):
        a["end"] = min(a["end"], b["start"])
    return cues


def srt_time(t):
    ms = round(t*1000)
    return f"{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}"
