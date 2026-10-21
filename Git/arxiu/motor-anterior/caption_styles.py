"""Subtítols: anglès entre cometes i cursiva real, sense tocar la locució."""
import html
import re
from pathlib import Path
from PIL import ImageFont

REGULAR = None
ITALIC = None


def decorate(cues, scene):
    narration = scene['narration']
    tokens = list(re.finditer(r'\S+', narration))
    spans, offset = [], 0
    beats = scene.get('beats') or [{'segments': scene['segments']}]
    for i, beat in enumerate(beats):
        if i: offset += 1
        for segment in beat['segments']:
            end = offset + len(segment['text'])
            if segment['lang'] == 'en-US': spans.append((offset, end))
            offset = end
    assert offset == len(narration)
    english = [any(a < t.end() and b > t.start() for a,b in spans) for t in tokens]
    cursor = 0
    for cue in cues:
        words = cue['text'].split()
        assert words == [t.group() for t in tokens[cursor:cursor+len(words)]]
        flags = english[cursor:cursor+len(words)]
        runs, i = [], 0
        while i < len(words):
            flag = flags[i]; j = i+1
            while j < len(words) and flags[j] == flag: j += 1
            text = ' '.join(words[i:j])
            if flag:
                core = text.rstrip('.,;:!?')
                tail = text[len(core):]
                runs.append({'text':'«'+core+'»','italic':True})
                if tail: runs.append({'text':tail,'italic':False})
            else: runs.append({'text':text,'italic':False})
            if j < len(words): runs.append({'text':' ','italic':False})
            i = j
        cue['runs'] = runs
        cue['srt_text'] = ''.join(('<i>'+html.escape(run['text'],quote=False)+'</i>') if run['italic']
                                  else html.escape(run['text'],quote=False) for run in runs)
        cursor += len(words)
    assert cursor == len(tokens)
    return cues


def plain_srt(text):
    return html.unescape(re.sub(r'</?i>', '', text)).replace('«','').replace('»','')


def draw(d, cues, t, r):
    global REGULAR, ITALIC
    cue = next((cue for cue in cues if cue['start'] <= t < cue['end']), None)
    if not cue: return
    if REGULAR is None:
        REGULAR = r.F['caption']
        candidates = [r.FONT_DIR/'Arial Italic.ttf',
                      Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf')]
        path = next((p for p in candidates if p.exists()), None)
        if path is None: raise RuntimeError('Cal una font cursiva per als subtítols en anglès.')
        ITALIC = ImageFont.truetype(str(path), 24)
    if '_layout' not in cue:
        lines, line, width = [], [], 0
        for run in cue['runs']:
            font = ITALIC if run['italic'] else REGULAR
            for part in re.findall(r'\S+|\s+', run['text']):
                size = d.textlength(part, font=font)
                if width+size > 1090 and line and part.strip():
                    lines.append((line,width));line=[];width=0
                if not line and not part.strip():continue
                line.append((part,run['italic']));width+=size
        if line:lines.append((line,width))
        assert 1 <= len(lines) <= 2, 'Subtítol massa llarg'
        cue['_layout'] = lines
    lines = cue['_layout'];top=617 if len(lines)==1 else 601
    # Una mateixa línia de base per a tots els fragments i les dues fonts.
    # L’ancoratge al contorn superior de cada mot desplaça les minúscules,
    # els accents i la cursiva a altures diferents.
    baseline = top + REGULAR.getmetrics()[0]
    d.rounded_rectangle((64,590,1216,680),14,fill='#080D16')
    for i,(parts,width) in enumerate(lines):
        x=640-width/2
        for part,italic in parts:
            font=ITALIC if italic else REGULAR
            d.text((x,baseline+i*31),part,font=font,fill=r.WHITE,anchor='ls')
            x+=d.textlength(part,font=font)
