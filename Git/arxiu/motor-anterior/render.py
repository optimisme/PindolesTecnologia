#!/usr/bin/env python3
"""Guió JSON -> veu catalana -> animacions -> MP4, àudio i subtítols.

No modifica ni publica cap repositori Git. Les interfícies són esquemes didàctics.
"""
import argparse
import asyncio
import html
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import wave

import edge_tts
from PIL import Image, ImageDraw, ImageFont
from lesson_visuals import draw_lesson
from opening import prepare_opening, opening_frame, opening_metadata
from pronunciation import spoken_text, original_words, profile_metadata, voice_signature, cached_voice_matches

W, H = 1280, 720
BG, PANEL, BORDER = "#0D1422", "#151F31", "#2C3A50"
WHITE, MUTED, ORANGE, MINT, PURPLE = "#F5F7FC", "#AAB8CD", "#FF845E", "#71E2B6", "#B8A0FF"
FONT_DIR = Path("/System/Library/Fonts/Supplemental")


def run(args):
    subprocess.run([str(a) for a in args], check=True)


def probe(path):
    return float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)
    ], text=True).strip())


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
     "hero": font(82, True), "code": font(23, mono=True), "tinycode": font(18, mono=True)}


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
    d.line((start, end), fill=color, width=width)
    a = math.atan2(end[1] - start[1], end[0] - start[0])
    d.polygon([end, (end[0] - 12 * math.cos(a - .45), end[1] - 12 * math.sin(a - .45)),
               (end[0] - 12 * math.cos(a + .45), end[1] - 12 * math.sin(a + .45))], fill=color)


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
    text(d, (106, 36), config.get('series', 'Git en un minut i escaig').upper(), "label", WHITE)
    episode = config.get("episode_number", 1)
    topic = config.get("short_title", "INTRODUCCIÓ")
    text(d, (1216, 36), f"{episode:02}  /  {topic}     ·     {index+1:02}/{total:02}", "small", MUTED, "rt")
    text(d, (64, 91), scene["label"], "label", ORANGE)
    text(d, (64, 126), scene["title"], "title")
    return im


def draw_visual(d, scene, t, duration):
    sid = scene["id"]
    if sid.startswith('i_'):
        from intro_revisada import draw_intro
        return draw_intro(d, scene, t, sys.modules[__name__])
    if sid.startswith('g_'):
        from general_intro import draw_general
        return draw_general(d, scene, t, sys.modules[__name__])
    commands = scene.get("commands", [])
    p = clamp(t / duration)
    if sid == "problema":
        for x, before in [(64, True), (666, False)]:
            color = MINT if before else ORANGE
            panel(d, (x, 240, x+550, 460))
            text(d, (x+26, 261), "ABANS · FUNCIONA" if before else "ARA · ERROR", "label", color)
            text(d, (x+26, 307), 'salutacio = "Hola!"' if before else type_text('missatge = "Hola!"', t/1.5), "code", color)
            text(d, (x+26, 353), "print(salutacio)", "code")
            if before or p > .22:
                text(d, (x+26, 411), "→ Hola!" if before else "NameError: salutacio", "tinycode", color)
        arrow(d, (629, 351), (653, 351), MUTED, 3)
        if p > .5:
            pill(d, 64, 505, "QUÈ HAS TOCAT? CONSULTA L'HISTORIAL.", MINT)
    elif sid == "git":
        pill(d, 64, 222, "CONTROL DE VERSIONS", MINT)
        xs = [210, 640, 1070]
        end = 210 + 860*ease(t/4)
        d.line((210, 308, end, 308), fill=BORDER, width=6)
        names = ["Inici del projecte", "Primer missatge", "Millora del missatge"]
        hashes = ["a31b2c4", "b62d8e1", "c95f4a7"]
        for i,x in enumerate(xs):
            s = ease((t-i*1.25)/.6)
            if s > 0:
                node(d, x, 308, hashes[i], scale=s)
                text(d, (x, 378), names[i], "body", WHITE, "mt")
        terminal(d, (64, 426, 1216, 573), "TERMINAL · CONSULTAR L'HISTORIAL")
        command(d, 90, 477, commands[0], (t-2.2)/1.5)
        if p > .48:
            for i,line in enumerate(("c95f4a7 Millora del missatge", "b62d8e1 Primer missatge", "a31b2c4 Inici del projecte")):
                text(d, (606, 475+i*27), line, "tinycode", MUTED)
    elif sid == "github":
        for x,title,sub,tag,col in [(64,"Git","L'historial al teu ordinador","LOCAL",ORANGE),
                                   (738,"GitHub","Repositoris a internet","REMOT",PURPLE)]:
            panel(d, (x, 242, x+478, 540))
            text(d, (x+32, 270), tag, "label", col)
            text(d, (x+32, 324), title, "hero", col)
            text(d, (x+32, 448), sub, "body")
            text(d, (x+32, 492), "Versions i canvis" if x == 64 else "Compartir i col·laborar", "small", MUTED)
        if p > .3:
            arrow(d, (566, 392), (714, 392), MINT)
    elif sid == "editar":
        panel(d, (64, 241, 618, 540))
        text(d, (90, 263), "helloGit.py", "code", MUTED)
        d.line((65, 309, 617, 309), fill=BORDER, width=2)
        text(d, (90, 351), "1", "code", MUTED)
        text(d, (128, 351), type_text('print("Hello Git!")', t/2.3), "code", MINT)
        terminal(d, (650, 241, 1216, 552), "TERMINAL · PREPARAR ELS CANVIS")
        command(d, 676, 311, commands[0], (p-.15)/.16)
        if p > .33:
            text(d, (704, 355), "?? helloGit.py", "tinycode", ORANGE)
        if p > .49:
            command(d, 676, 412, commands[1], (p-.49)/.15)
        if p > .69:
            pill(d, 676, 482, "PREPARAT PER AL COMMIT")
        arrow(d, (625, 389), (642, 389), MUTED, 3)
    elif sid == "commit":
        terminal(d, (64, 241, 824, 441), "TERMINAL · DESAR UN COMMIT LOCAL")
        command(d, 90, 310, commands[0], t/2.7)
        pressed = p > .34
        panel(d, (64, 459, 824, 568))
        text(d, (90, 480), "HISTORIAL LOCAL", "label", ORANGE)
        if pressed:
            text(d, (118, 357), "[main (root-commit) b62d8e1] Primer missatge", "tinycode", MINT)
            arrow(d, (350, 499), (581, 499), ORANGE)
            node(d, 650, 499, "b62d8e1", scale=ease((p-.34)/.08))
        text(d, (90, 405), "GitHub Desktop: Commit to main", "small", MUTED)
        panel(d, (860, 241, 1216, 568))
        text(d, (890, 263), "REMOT  /  GitHub", "label", PURPLE)
        d.ellipse((1009, 357, 1063, 411), outline=BORDER, width=3)
        text(d, (1038, 453), "Encara pendent", "body", MUTED, "mt")
        text(d, (1038, 491), "d'enviar", "body", MUTED, "mt")
    elif sid == "publicar":
        panel(d, (64, 230, 546, 429))
        panel(d, (734, 230, 1216, 429))
        text(d, (96, 250), "LOCAL", "label", ORANGE)
        text(d, (766, 250), "REMOT", "label", PURPLE)
        text(d, (96, 290), "El teu ordinador", "h2")
        text(d, (766, 290), "GitHub / HelloGit", "h2")
        node(d, 300, 357, "b62d8e1")
        arrow(d, (552, 357), (728, 357), MINT)
        travel = ease((p-.26)/.24)
        if p > .26:
            node(d, 300+670*travel, 357, "b62d8e1" if travel == 1 else None, MINT)
        terminal(d, (64, 450, 1216, 573), "TERMINAL · PUBLICAR ELS COMMITS")
        first = p < .69
        command(d, 90, 510, commands[0] if first else commands[1], (p-.04)/.16 if first else (p-.69)/.1)
        text(d, (740, 508), "Primer enviament · Publish branch" if first else "Propers enviaments · Push origin", "small", MUTED)
        if p > .51:
            pill(d, 903, 245, "COMMIT COMPARTIT", MINT)
    elif sid == "cicle":
        labels = ["Editar", "Seleccionar", "Commit", "Push"]
        colors = [WHITE, PURPLE, ORANGE, MINT]
        step = min(3, int(p*5))
        for i, label in enumerate(labels):
            x = 64 + i*296
            active = i <= step
            panel(d, (x, 245, x+264, 383), PANEL, colors[i] if active else BORDER)
            text(d, (x+24, 282), f"0{i+1}", "label", colors[i] if active else MUTED)
            text(d, (x+132, 345), label, "h2", colors[i] if active else MUTED, "mm")
            if i < 3:
                arrow(d, (x+271, 333), (x+289, 333), MUTED, 3)
        terminal(d, (64, 407, 1216, 574), "TERMINAL · LES COMANDES DEL DIA A DIA")
        for i,cmd in enumerate(commands):
            if p > .16+i*.19:
                command(d, 90, 458+i*33, cmd, (p-(.16+i*.19))/.12)
    elif sid == "resum":
        cards = [("Git", "Guarda l'historial", ORANGE),
                 ("Commit", "Desa una versió local", PURPLE),
                 ("Push", "Envia els commits", MINT)]
        for i,(title,sub,color) in enumerate(cards):
            x = 64+i*392
            rise = int(24*(1-ease((t-i*.55)/.7)))
            panel(d, (x, 264+rise, x+368, 483+rise))
            text(d, (x+24, 293+rise), f"0{i+1}", "label", color)
            text(d, (x+24, 337+rise), title, "title", color)
            text(d, (x+24, 421+rise), sub, "body")
        if p > .65:
            text(d, (640, 542), "EL TEU PROJECTE JA TÉ HISTÒRIA.", "label", MINT, "mt")
    else:
        draw_lesson(d, scene, t, duration, sys.modules[__name__])


def subtitles_from_words(words, narration, transform=None):
    # Els subtítols recuperen sempre l'ortografia del guió, també quan un
    # terme anglès es pronuncia amb diversos mots fonètics.
    words = (original_words(words, narration) if transform is None else
             original_words(words, narration, transform=transform))
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


async def generate_voice(scene, config, folder):
    audio = folder / f"{scene['id']}.mp3"
    metadata = audio.with_suffix(".json")
    tts_text = spoken_text(scene["narration"])
    signature = voice_signature(scene["narration"], tts_text, config["voice"], config["rate"])
    if audio.exists() and metadata.exists():
        cached = json.loads(metadata.read_text())
        if audio.stat().st_size >= 1000 and cached_voice_matches(
                cached, scene["narration"], tts_text, config["voice"], config["rate"]):
            original_words(cached["words"], scene["narration"])
            cached.update(signature=signature, pronunciation=profile_metadata())
            metadata.write_text(json.dumps(cached, ensure_ascii=False, indent=2))
            return audio, cached["words"]
    print(f"Veu: {scene['id']} ({config['voice']})", flush=True)
    for attempt in range(3):
        words = []
        try:
            communicate = edge_tts.Communicate(tts_text, voice=config["voice"],
                                              rate=config["rate"], boundary="WordBoundary",
                                              receive_timeout=30)
            with audio.open("wb") as f:
                async for chunk in communicate.stream():
                    if chunk["type"] == "audio":
                        f.write(chunk["data"])
                    elif chunk["type"] == "WordBoundary":
                        words.append({"start": chunk["offset"]/10_000_000,
                                      "end": (chunk["offset"]+chunk["duration"])/10_000_000,
                                      "text": html.unescape(chunk["text"])})
            if not words or audio.stat().st_size < 1000:
                raise RuntimeError("El servei TTS no ha retornat àudio i marques de temps.")
            # Verifica l'alineació abans de donar l'àudio per vàlid a la memòria cau.
            original_words(words, scene["narration"])
            metadata.write_text(json.dumps({"signature": signature, "narration": scene["narration"],
                "tts_text": tts_text, "pronunciation": profile_metadata(), "words": words}, ensure_ascii=False, indent=2))
            return audio, words
        except Exception:
            if attempt == 2:
                raise
            await asyncio.sleep(1)


def srt_time(t):
    ms = round(t*1000)
    return f"{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}"


def draw_captions(d,cues,t):
    caption=next((c['text'] for c in cues if c['start']<=t<c['end']), '')
    if caption:
        lines=wrap(d,caption,1090)
        top=617 if len(lines)==1 else 601
        d.rounded_rectangle((64,590,1216,680),14,fill='#080D16')
        for j,line in enumerate(lines):
            text(d,(640,top+j*31),line,'caption',WHITE,'mt')


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("episode", type=Path, nargs="?", default=Path(__file__).parent/"00-introduccio")
    parser.add_argument("--voice", help="Identificador de veu Edge TTS; per defecte, el del guió")
    parser.add_argument("--audio-only", action="store_true", help="Genera la veu, el guió temporitzat i els subtítols")
    args = parser.parse_args()
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise SystemExit("Cal instal·lar ffmpeg i ffprobe.")
    root = args.episode.resolve()
    config = json.loads((root/"episodi.json").read_text())
    if config.get('format_version') == 2:
        from revised_render import render_episode
        await render_episode(root, config, audio_only=args.audio_only)
        return
    if args.voice:
        config["voice"] = args.voice
    audio_dir, build, output = [root/p for p in ("audio", "build", "output")]
    for folder in (audio_dir, build, output):
        folder.mkdir(exist_ok=True)
    fps = config["fps"]
    opening=await prepare_opening(root,config,sys.modules[__name__])
    offset=opening['duration'] if opening else 0.0
    all_cues=list(opening['cues']) if opening else []
    timings=[]
    wav_files=[opening['wav']] if opening else []
    for scene in config["scenes"]:
        audio, words = await generate_voice(scene, config, audio_dir)
        # Una pausa inicial i una de final deixen respirar cada canvi d'escena.
        nframes = math.ceil((probe(audio)+.85)*fps)
        duration = nframes/fps
        cues = subtitles_from_words(words, scene["narration"])
        for cue in cues:
            cue["start"] += .3
            cue["end"] = min(cue["end"]+.3, duration-.2)
            all_cues.append({**cue, "start": cue["start"]+offset, "end": cue["end"]+offset})
        scene.update(duration=duration, frames=nframes, start=offset, cues=cues)
        wav_path = build/f"{scene['id']}.wav"
        run(["ffmpeg", "-y", "-v", "error", "-i", audio, "-af",
             f"adelay=300,apad,atrim=duration={duration},afade=t=in:d=0.01",
             "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", wav_path])
        wav_files.append(wav_path)
        timings.append({"id": scene["id"], "start": round(offset,3), "duration": duration})
        offset += duration
    narration = build/"narracio.wav"
    with wave.open(str(narration), "wb") as dest:
        for i, path in enumerate(wav_files):
            with wave.open(str(path), "rb") as src:
                if i == 0:
                    dest.setparams(src.getparams())
                dest.writeframes(src.readframes(src.getnframes()))
    subtitle_path = output/f"{root.name}.ca.srt"
    subtitle_path.write_text("\n\n".join(
        f"{i+1}\n{srt_time(c['start'])} --> {srt_time(c['end'])}\n{c['text']}"
        for i,c in enumerate(all_cues))+"\n")
    guio = [f"# {config['title']}", "", f"Veu: `{config['voice']}` · Català · {offset:.1f} segons", "",
            "Format: 1280 × 720, 24 fps. Interfícies esquemàtiques, sense capturar dades personals.", "",
            f"Punt de partida: {config['prerequisites']}", ""]
    if opening:
        guio += ['## Capçalera musical (0,0–4,0 s)','',
                 '**Animació:** graf de commits, número de lliçó, títol i subtítol.',
                 '**Àudio:** sintonia electrònica original. Sense locució durant la música.','',
                 f"## Presentació de la lliçó (4,0–{opening['duration']:.2f} s)",'',
                 f"**Locució:** {opening['narration']}",'',
                 '**Animació:** es manté el títol fins que acaba la presentació; després es dissol.','']
    for scene in config["scenes"]:
        guio += [f"## {scene['title']} ({scene['start']:.1f}–{scene['start']+scene['duration']:.1f} s)",
                 "", f"**Locució:** {scene['narration']}", "", f"**Animació:** {scene['visual']}", ""]
        if scene.get("commands"):
            guio += ["**Comandes en pantalla:**", "", "```bash", *scene["commands"], "```", ""]
    (root/"guio.md").write_text("\n".join(guio))
    (output/"produccio.json").write_text(json.dumps({
        "title": config["title"], "voice": config["voice"], "tts": "Microsoft Edge online TTS via edge-tts",
        "fps": fps, "resolution": [W,H], "duration": offset, "scenes": timings,
        "opening": opening_metadata(opening),
        "pronunciation": profile_metadata(),
        "subtitles": "Incrustats a la imatge i també en un fitxer SRT separat"
    }, ensure_ascii=False, indent=2))
    run(["ffmpeg", "-y", "-v", "error", "-i", narration, "-c:a", "libmp3lame", "-q:a", "2", output/"narracio.mp3"])
    print(f"Guió i veu preparats: {offset:.1f} segons", flush=True)
    if args.audio_only:
        return
    silent = build/"animacions.mp4"
    command = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
               "-s", f"{W}x{H}", "-r", str(fps), "-i", "pipe:0", "-an", "-c:v", "libx264",
               "-preset", "fast", "-threads", "2", "-crf", "19", "-pix_fmt", "yuv420p", str(silent)]
    screenshots = []
    with subprocess.Popen(command, stdin=subprocess.PIPE) as encoder:
        try:
            if opening:
                print(f"Capçalera i presentació: {opening['duration']:.2f} segons",flush=True)
                for n in range(opening['frames']):
                    t=n/fps
                    im=opening_frame(t,opening)
                    draw_captions(ImageDraw.Draw(im),opening['cues'],t)
                    if n==round(2.1*fps):
                        im.save(output/'portada.png')
                    if n==round((opening['voice_start']+.4)*fps):
                        im.save(build/'presentacio.png')
                    encoder.stdin.write(im.tobytes())
            for index,scene in enumerate(config["scenes"]):
                print(f"Animació {index+1}/{len(config['scenes'])}: {scene['id']}", flush=True)
                background = base(scene, index, len(config["scenes"]), config)
                for n in range(scene["frames"]):
                    t = n/fps
                    im = background.copy()
                    d = ImageDraw.Draw(im)
                    draw_visual(d, scene, t, scene["duration"])
                    draw_captions(d,scene['cues'],t)
                    progress = (scene["start"]+t)/offset
                    d.rectangle((0, 712, W, 719), fill=BORDER)
                    d.rectangle((0, 712, int(W*progress), 719), fill=MINT)
                    if n == int(scene["frames"]*.82):
                        path = build/f"escena-{index+1:02}.png"
                        im.save(path)
                        screenshots.append(im.copy())
                        if not opening and index == len(config["scenes"])-1:
                            im.save(output/"portada.png")
                    encoder.stdin.write(im.tobytes())
            encoder.stdin.close()
            if encoder.wait() != 0:
                raise RuntimeError("FFmpeg no ha pogut renderitzar les animacions.")
        except BaseException:
            encoder.kill()
            encoder.wait()
            raise
    final = output/config.get("output_name", f"{root.name}.mp4")
    run(["ffmpeg", "-y", "-v", "error", "-i", silent, "-i", narration,
         "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
         "-metadata:s:a:0", "language=cat", "-metadata", f"title={config['title']}",
         "-movflags", "+faststart", final])
    sheet = Image.new("RGB", (1280, math.ceil(len(screenshots)/2)*360), BG)
    for i,im in enumerate(screenshots):
        sheet.paste(im.resize((640,360), Image.Resampling.LANCZOS), ((i%2)*640, (i//2)*360))
    sheet.save(build/"storyboard.jpg", quality=92)
    print(f"Vídeo complet: {final} ({probe(final):.1f} s)", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
