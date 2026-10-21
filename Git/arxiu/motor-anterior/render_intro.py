#!/usr/bin/env python3
"""Mostra independent de capçalera. No modifica els episodis existents."""
import argparse
from array import array
import math
from pathlib import Path
import random
import subprocess
import sys
import wave

from PIL import Image, ImageDraw, ImageFont

# Primitives independents per reutilitzar la capçalera des del renderitzador.
BG, BORDER, WHITE, MUTED = '#0D1422', '#2C3A50', '#F5F7FC', '#AAB8CD'
ORANGE, MINT, PURPLE = '#FF845E', '#71E2B6', '#B8A0FF'


def font(size, bold=False):
    for path in (Path('/System/Library/Fonts/Supplemental')/('Arial Bold.ttf' if bold else 'Arial.ttf'),
                 Path('/usr/share/fonts/truetype/dejavu')/('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')):
        if path.exists():
            return ImageFont.truetype(str(path),size)
    raise RuntimeError('Cal Arial o DejaVu Sans.')


def clamp(t):
    return max(0.0,min(1.0,t))


def ease(t):
    return 1-(1-clamp(t))**3

W, H, FPS, DURATION, SR = 1280, 720, 24, 4.0, 48000
TITLES = {
    0: ("INTRODUCCIÓ A GIT", "Versions, historial i col·laboració"),
    1: ("EL PRIMER COMMIT", "Preparar, confirmar i publicar"),
    2: ("BRANQUES", "Prova una idea sense tocar main"),
    3: ("ELS TRES ESTATS", "Desar, preparar i confirmar"),
    4: ("SINCRONITZACIÓ", "De classe a casa"),
    5: ("MERGE", "Portem la prova a main"),
    6: ("CONFLICTES", "Dues edicions, una decisió"),
    7: ("REBASE", "Continua sobre una base nova"),
    8: ("STASH", "Aparca la feina pendent"),
    9: ("RESTORE", "Desmarca o descarta un canvi local"),
    10: ("REVERT", "Desfés un commit publicat"),
    11: ("RESET", "Torna enrere un commit local"),
    12: ("REFLOG", "Recupera un commit local"),
    13: ("GITIGNORE", "Deixa fora els fitxers generats"),
    14: ("TAGS", "Identifica una entrega del projecte"),
    15: ("CHERRY-PICK", "Porta una correcció a main"),
    16: ("PULL REQUESTS", "Revisa i integra la feina en equip"),
    17: ("BLAME", "Investiga l’origen d’una línia"),
    18: ("BISECT", "Troba el primer commit que falla"),
    19: ("AMEND", "Completa l’últim commit local"),
    20: ("FETCH", "Consulta els canvis abans d’integrar"),
    21: ("FORKS I UPSTREAM", "Contribueix a un projecte original"),
    22: ("REBASE INTERACTIU", "Agrupa commits abans de publicar"),
    23: ("ADD INTERACTIU", "Prepara només una part del fitxer"),
    24: ("WORKTREE", "Dues carpetes, un historial compartit"),
    25: ("HOOKS", "Comprova la sintaxi abans del commit"),
}


def generate_music(path):
    """Composició original: petits sintetitzadors FM, baix, acords i percussió."""
    left, right = [0.0]*int(SR*DURATION), [0.0]*int(SR*DURATION)
    rng = random.Random(820)

    def add(start, duration, instrument, gain, pan=0):
        first = round(start*SR)
        for i in range(min(round(duration*SR), len(left)-first)):
            t = i/SR
            sample = instrument(t)*gain
            left[first+i] += sample*math.sqrt((1-pan)/2)
            right[first+i] += sample*math.sqrt((1+pan)/2)

    def hz(midi):
        return 440*2**((midi-69)/12)

    def pluck(midi, duration):
        freq = hz(midi)
        def sound(t):
            attack = min(1,t/.006)
            release = clamp((duration-t)/.065)
            envelope = attack*math.exp(-t*9)*release
            phase = 2*math.pi*freq*t
            return envelope*(math.sin(phase+1.3*math.exp(-t*18)*math.sin(phase*2))+.13*math.sin(phase*3))
        return sound

    # Motiu en Re major. Les notes i els instruments es creen aquí, sense samples.
    score = ((.10,74),(.33,78),(.56,81),(.79,85),(1.15,83),(1.38,81),
             (1.61,78),(1.96,81),(2.42,86),(2.88,81),(3.11,86))
    for i,(start,note) in enumerate(score):
        duration = .6 if i==len(score)-1 else .35
        pan = -.25 if i%2 else .25
        instrument = pluck(note,duration)
        add(start,duration,instrument,.23,pan)
        if start+.13+duration < DURATION:
            add(start+.13,duration,instrument,.032,-pan)
    for start,note in ((.08,50),(.99,50),(1.90,55),(2.58,57),(3.05,50)):
        freq=hz(note)
        add(start,.5,lambda t,f=freq: math.sin(2*math.pi*f*t)*min(1,t/.01)*math.exp(-t*9),.20)
    for start,notes,duration in ((.08,(62,66,69),1.7),(1.88,(55,59,62),.65),
                                  (2.55,(57,61,64),.5),(3.04,(62,66,69),.85)):
        frequencies=tuple(hz(n) for n in notes)
        add(start,duration,lambda t,fs=frequencies,dur=duration:
            sum(math.sin(2*math.pi*f*t) for f in fs)/3 * min(1,t/.05)*clamp((dur-t)/.18),.055)
    for start in (.08,.99,1.90,2.81):
        add(start,.19,lambda t:math.sin(2*math.pi*(48*t+.75*(1-math.exp(-t*35))))*math.exp(-t*27),.22)
    for start in (.54,1.45,2.36,3.27):
        add(start,.065,lambda t:(rng.random()*2-1)*math.exp(-t*85),.035,.25)
    peak=max(max(abs(v) for v in left), max(abs(v) for v in right))
    scale=.65/max(peak,.001)
    samples=array('h')
    for i,(l,r) in enumerate(zip(left,right)):
        t=i/SR
        fade=min(1,t/.02)*clamp((3.94-t)/.23)
        samples.extend((round(l*scale*fade*32767),round(r*scale*fade*32767)))
    if sys.byteorder!='little':
        samples.byteswap()
    with wave.open(str(path),'wb') as f:
        f.setparams((2,2,SR,0,'NONE','not compressed'))
        f.writeframes(samples.tobytes())


def frame(t, episode, total_duration=DURATION, series='Git en un minut i escaig'):
    title, subtitle = TITLES[episode]
    im = Image.new('RGB',(W,H),BG)
    d=ImageDraw.Draw(im)
    for x in range(24,W,36):
        for y in range(22,H,36):
            d.ellipse((x,y,x+1,y+1),fill='#202B3C')
    d.rounded_rectangle((96,112,1184,580),radius=28,fill='#111B2C',outline=BORDER,width=2)
    d.text((130,140),series.upper(),font=font(21,True),fill=MUTED)
    d.text((1150,140),'MINI LLIÇONS',font=font(17,True),fill=MUTED,anchor='rt')
    d.line((130,185,1150,185),fill=BORDER,width=1)
    # Quatre nodes i una bifurcació: el símbol es construeix en mig segon.
    a,b,c,branch=(165,367),(240,367),(315,367),(315,286)
    for start,end,delay,color in ((a,b,0,ORANGE),(b,c,.13,ORANGE),(b,branch,.26,MINT)):
        p=ease((t-delay)/.34)
        if p>0:
            endpoint=(start[0]+(end[0]-start[0])*p,start[1]+(end[1]-start[1])*p)
            d.line((*start,*endpoint),fill=color,width=7)
    for i,((x,y),color) in enumerate(((a,ORANGE),(b,ORANGE),(c,ORANGE),(branch,MINT))):
        p=ease((t-.11*i)/.28)
        if p>0:
            radius=round(13*p)
            d.ellipse((x-radius-6,y-radius-6,x+radius+6,y+radius+6),fill='#1D293D',outline=BORDER,width=2)
            d.ellipse((x-radius,y-radius,x+radius,y+radius),fill=color)
    # Aparició amb un petit desplaçament i transparència, sense locució.
    layer=Image.new('RGBA',(W,H),(0,0,0,0))
    ld=ImageDraw.Draw(layer)
    p=ease((t-.38)/.5)
    shift=round(22*(1-p))
    alpha=round(255*p)
    def rgba(hex_color):
        return tuple(int(hex_color[i:i+2],16) for i in (1,3,5))+(alpha,)
    ld.rounded_rectangle((418,224+shift,565,259+shift),radius=10,fill=(30,58,53,alpha))
    ld.text((434,232+shift),f'LLIÇÓ {episode:02}',font=font(18,True),fill=rgba(MINT))
    size=68
    while ld.textlength(title,font=font(size,True))>720:
        size-=1
    ld.text((416,291+shift),title,font=font(size,True),fill=rgba(WHITE))
    ld.text((420,391+shift),subtitle,font=font(30),fill=rgba(MUTED))
    im=Image.alpha_composite(im.convert('RGBA'),layer).convert('RGB')
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((130,525,1150,529),radius=2,fill=BORDER)
    progress=ease((t-.8)/2.6)
    if progress>0:
        d.rounded_rectangle((130,525,130+1020*progress,529),radius=2,fill=MINT)
    # En la versió integrada es manté el títol mentre s'anuncia la lliçó.
    if t>total_duration-.35:
        im=Image.blend(im,Image.new('RGB',(W,H),BG),ease((t-total_duration+.35)/.35))
    return im


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--episode',type=int,choices=TITLES,default=2)
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    build,output=root/'build',root/'output'
    build.mkdir(exist_ok=True); output.mkdir(exist_ok=True)
    raw=build/'sintonia-original.wav'
    music=output/'sintonia.wav'
    generate_music(raw)
    subprocess.run(['ffmpeg','-y','-v','error','-i',str(raw),'-af','loudnorm=I=-18:TP=-2:LRA=7',
                    '-ar',str(SR),'-c:a','pcm_s16le',str(music)],check=True)
    silent=build/f'intro-{args.episode:02}-sense-audio.mp4'
    command=['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}',
             '-r',str(FPS),'-i','pipe:0','-an','-c:v','libx264','-threads','2','-crf','18',
             '-pix_fmt','yuv420p',str(silent)]
    with subprocess.Popen(command,stdin=subprocess.PIPE) as process:
        for i in range(round(DURATION*FPS)):
            process.stdin.write(frame(i/FPS,args.episode).tobytes())
        process.stdin.close()
        if process.wait():
            raise RuntimeError('Ha fallat el render de la capçalera.')
    final=output/f'capcalera-{args.episode:02}.mp4'
    subprocess.run(['ffmpeg','-y','-v','error','-i',str(silent),'-i',str(music),'-map','0:v','-map','1:a',
                    '-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart',str(final)],check=True)
    sheet=Image.new('RGB',(1280,math.ceil(len(TITLES)/2)*360),BG)
    for i,episode in enumerate(TITLES):
        sheet.paste(frame(2.1,episode).resize((640,360),Image.Resampling.LANCZOS),((i%2)*640,(i//2)*360))
    sheet.save(output/'titols.jpg',quality=94)
    frame(2.1,args.episode).save(output/'portada.png')
    print(final)


if __name__=='__main__':
    main()
