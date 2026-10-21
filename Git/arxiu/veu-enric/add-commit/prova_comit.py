"""Prova sol·licitada: add original i còmit, amb Enric."""
import asyncio
import importlib.util
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('tts_sample',ROOT.parent/'genera_mostra.py')
sample=importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample)
sample.ROOT=ROOT

async def main():
    config={'voice':'ca-ES-EnricNeural','rate':'+12%'}
    (ROOT/'output').mkdir(exist_ok=True)
    path=await sample.voice('03-add-comit-obert',
        'Guit add prepara el canvi; Guit còmit el desa.',config)
    final=ROOT/'output'/'prova-add-comit-obert.mp3'
    subprocess.run(['ffmpeg','-y','-v','error','-i',str(path),
        '-af','loudnorm=I=-18:TP=-2:LRA=7','-ar','48000','-ac','2',
        '-c:a','libmp3lame','-q:a','2',str(final)],check=True)
    subprocess.run(['ffmpeg','-v','error','-i',str(final),'-f','null','-'],check=True)
    print(final,flush=True)

if __name__=='__main__':asyncio.run(main())
