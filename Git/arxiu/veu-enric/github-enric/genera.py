"""Audició de grafies de GitHub, exclusivament amb la veu catalana Enric."""
import asyncio
import importlib.util
import json
from pathlib import Path
import subprocess
import wave

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('tts_sample',ROOT.parent/'genera_mostra.py')
sample=importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample)
sample.ROOT=ROOT

async def main():
    config=json.loads((ROOT/'mostra.json').read_text())
    output=ROOT/'output';output.mkdir(exist_ok=True)
    semaphore=asyncio.Semaphore(3)
    async def synthesize(name,text):
        async with semaphore:
            return await sample.voice(name,text,config)
    requests=[]
    for variant in config['variants']:
        requests.append((variant['id'],variant['label']+' '+config['template'].format(github=variant['spelling'])))
    requests.append(('05-accents',config['catalan_check']))
    paths=await asyncio.gather(*[synthesize(name,text) for name,text in requests])
    wavs=[]
    for index,path in enumerate(paths):
        wav=output/f'tram-{index:02}.wav'
        subprocess.run(['ffmpeg','-y','-v','error','-i',str(path),'-af',
            'silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.1,areverse,apad=pad_dur=0.5',
            '-ar','48000','-ac','2','-c:a','pcm_s16le',str(wav)],check=True)
        wavs.append(wav)
    joined=output/'comparacio-enric.wav'
    with wave.open(str(joined),'wb') as dest:
        for index,path in enumerate(wavs):
            with wave.open(str(path),'rb') as source:
                if index==0:dest.setparams(source.getparams())
                dest.writeframes(source.readframes(source.getnframes()))
    subprocess.run(['ffmpeg','-y','-v','error','-i',str(joined),'-af','loudnorm=I=-18:TP=-2:LRA=7',
        '-ar','48000','-ac','2','-c:a','libmp3lame','-q:a','2',str(output/'comparacio-enric.mp3')],check=True)
    (output/'textos.json').write_text(json.dumps({'voice':config['voice'],'rate':config['rate'],'requests':requests},ensure_ascii=False,indent=2))
    print(output/'comparacio-enric.mp3',flush=True)

if __name__=='__main__':asyncio.run(main())
