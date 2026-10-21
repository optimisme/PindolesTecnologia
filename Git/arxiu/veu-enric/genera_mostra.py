"""Comparació de lectura actual i pronunciació guiada amb la mateixa veu."""
import asyncio
import hashlib
import json
from pathlib import Path
import re
import subprocess
import wave
import edge_tts

ROOT=Path(__file__).resolve().parent

def run(args):subprocess.run([str(x) for x in args],check=True)

async def voice(name,text,config):
    path=ROOT/'output'/f'{name}.mp3';meta=path.with_suffix('.json')
    signature=hashlib.sha256(json.dumps([text,config['voice'],config['rate']],ensure_ascii=False).encode()).hexdigest()
    if path.exists() and meta.exists() and json.loads(meta.read_text()).get('signature')==signature:return path
    for attempt in range(3):
        try:
            words=[]
            tts=edge_tts.Communicate(text,voice=config['voice'],rate=config['rate'],boundary='WordBoundary',receive_timeout=30)
            with path.open('wb') as f:
                async for chunk in tts.stream():
                    if chunk['type']=='audio':f.write(chunk['data'])
                    elif chunk['type']=='WordBoundary':words.append({'start':chunk['offset']/10_000_000,'end':(chunk['offset']+chunk['duration'])/10_000_000,'text':chunk['text']})
            if path.stat().st_size<1000 or not words:raise RuntimeError('Resposta TTS incompleta')
            meta.write_text(json.dumps({'signature':signature,'tts_text':text,'voice':config['voice'],'rate':config['rate'],'words':words},ensure_ascii=False,indent=2))
            print(name,'preparat',flush=True);return path
        except Exception:
            if attempt==2:raise
            await asyncio.sleep(1)

async def main():
    config=json.loads((ROOT/'mostra.json').read_text());out=ROOT/'output';out.mkdir(exist_ok=True)
    forms={k.casefold():v for k,v in config['pronunciations'].items()}
    pattern=re.compile(r'\b('+'|'.join(re.escape(k) for k in sorted(config['pronunciations'],key=len,reverse=True))+r')\b',re.I)
    guided=pattern.sub(lambda m:forms[m.group().casefold()],config['narration'])
    original=await voice('01-original',config['narration'],config)
    corrected=await voice('02-pronuncia-guiada',guided,config)
    labels=[]
    for name,text in (('etiqueta-original','Primera mostra. Lectura actual.'),('etiqueta-guiada','Segona mostra. Pronunciació guiada.')):labels.append(await voice(name,text,config))
    paths=[]
    for i,path in enumerate((labels[0],original,labels[1],corrected)):
        wav=out/f'tram-{i:02}.wav'
        run(['ffmpeg','-y','-v','error','-i',path,'-af','silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.1,areverse,apad=pad_dur=0.55','-ar','48000','-ac','2','-c:a','pcm_s16le',wav]);paths.append(wav)
    joined=out/'comparacio.wav'
    with wave.open(str(joined),'wb') as dest:
        for i,p in enumerate(paths):
            with wave.open(str(p),'rb') as src:
                if i==0:dest.setparams(src.getparams())
                dest.writeframes(src.readframes(src.getnframes()))
    run(['ffmpeg','-y','-v','error','-i',joined,'-af','loudnorm=I=-18:TP=-2:LRA=7','-ar','48000','-ac','2','-c:a','libmp3lame','-q:a','2',out/'comparacio.mp3'])
    report={'voice':config['voice'],'rate':config['rate'],'written_text':config['narration'],'spoken_original':config['narration'],'spoken_guided':guided,'pronunciations':config['pronunciations']}
    (out/'comparacio.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(out/'comparacio.mp3',flush=True)

if __name__=='__main__':asyncio.run(main())
