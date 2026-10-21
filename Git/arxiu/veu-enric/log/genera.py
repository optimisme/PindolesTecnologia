"""Prova aïllada de lòg i lògs per evitar la lectura logaritme."""
import asyncio
import importlib.util
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('tts_sample',ROOT.parent/'genera_mostra.py')
sample=importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample)
sample.ROOT=ROOT

async def main():
    config={'voice':'ca-ES-EnricNeural','rate':'+12%'}
    text='El fitxer acaba en punt lòg. Aquests lògs guarden informació. Amb Guit lòg consultem els còmits.'
    (ROOT/'output').mkdir(exist_ok=True)
    path=await sample.voice('log-accentuat',text,config)
    final=ROOT/'output'/'prova-log.mp3'
    subprocess.run(['ffmpeg','-y','-v','error','-i',str(path),'-af','loudnorm=I=-18:TP=-2:LRA=7',
        '-ar','48000','-ac','2','-c:a','libmp3lame','-q:a','2',str(final)],check=True)
    subprocess.run(['ffmpeg','-v','error','-i',str(final),'-f','null','-'],check=True)
    (ROOT/'mostra.json').write_text(json.dumps({**config,'written_text':'El fitxer acaba en punt log. Aquests logs guarden informació. Amb git log consultem els commits.','tts_text':text,'status':'prova pendent d’escoltar; no aplicada a producció'},ensure_ascii=False,indent=2)+'\n')
    print(final,flush=True)

if __name__=='__main__':asyncio.run(main())
