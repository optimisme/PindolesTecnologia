"""Prova aïllada d’Andrew: autodetecció, referència Enric i SSML experimental.

No modifica la biblioteca instal·lada, els guions ni el renderitzador. L’SSML
s’injecta només en aquest procés i amb una sola petició. Si el servei el rebutja,
es registra el resultat i es conserven les mostres de text pla.
"""
import asyncio
import html
import importlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

import edge_tts

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[2]))
from pronunciation import spoken_text
spec=importlib.util.spec_from_file_location('tts_sample',ROOT.parents[1]/'veu-enric'/'genera_mostra.py')
sample=importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample)
sample.ROOT=ROOT


def normalize(path,destination):
    subprocess.run(['ffmpeg','-y','-v','error','-i',str(path),'-af','loudnorm=I=-18:TP=-2:LRA=7',
        '-ar','48000','-ac','2','-c:a','libmp3lame','-q:a','2',str(destination)],check=True)
    subprocess.run(['ffmpeg','-v','error','-i',str(destination),'-f','null','-'],check=True)


def make_ssml(config):
    pattern=re.compile(r'\b('+'|'.join(re.escape(term) for term in sorted(config['english_terms'],key=len,reverse=True))+r')\b',re.I)
    spans=[];cursor=0
    for match in pattern.finditer(config['text']):
        if match.start()>cursor:
            spans.append(('ca-ES',config['text'][cursor:match.start()]))
        spans.append(('en-US',match.group()))
        cursor=match.end()
    if cursor<len(config['text']):spans.append(('ca-ES',config['text'][cursor:]))
    body=''.join(f'<lang xml:lang="{language}">{html.escape(text)}</lang>' for language,text in spans)
    ssml=(f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">'
          f'<voice name="{config["voice"]}"><prosody rate="{config["rate"]}" pitch="+0Hz" volume="+0%">'
          f'{body}</prosody></voice></speak>')
    ET.fromstring(ssml)
    (ROOT/'prova.ssml').write_text(ssml+'\n')
    return ssml,spans


async def ssml_trial(config,ssml):
    module=importlib.import_module('edge_tts.communicate')
    original=module.mkssml
    raw=ROOT/'output/03-andrew-ssml-raw.mp3'
    words=[]
    async def request():
        communicate=edge_tts.Communicate(config['text'],voice=config['voice'],rate=config['rate'],
            boundary='WordBoundary',receive_timeout=15,connect_timeout=10)
        with raw.open('wb') as output:
            async for chunk in communicate.stream():
                if chunk['type']=='audio':output.write(chunk['data'])
                elif chunk['type']=='WordBoundary':words.append({'start':chunk['offset']/10_000_000,
                    'end':(chunk['offset']+chunk['duration'])/10_000_000,'text':html.unescape(chunk['text'])})
        if not raw.exists() or raw.stat().st_size<1000:
            raise RuntimeError('No audio returned')
    try:
        module.mkssml=lambda config,text:ssml
        await asyncio.wait_for(request(),timeout=25)
        final=ROOT/'output/03-andrew-ssml.mp3'
        normalize(raw,final)
        final.with_suffix('.json').write_text(json.dumps({'voice':config['voice'],'rate':config['rate'],
            'ssml_file':'../prova.ssml','words':words},ensure_ascii=False,indent=2))
        return {'status':'audio_received','path':str(final),'note':'El servei ha retornat àudio; cal escoltar si respecta els canvis d’idioma.'}
    except Exception as error:
        raw.unlink(missing_ok=True)
        return {'status':'not_available_on_current_connection','error_type':type(error).__name__,
                'http_status':getattr(error,'status',None),'note':'Petició experimental SSML amb lang. No s’ha generat cap àudio SSML vàlid.'}
    finally:
        module.mkssml=original


async def main():
    config=json.loads((ROOT/'mostra.json').read_text())
    (ROOT/'output').mkdir(exist_ok=True)
    andrew_config={'voice':config['voice'],'rate':config['rate']}
    enric_config={'voice':config['reference_voice'],'rate':config['rate']}
    # La referència conserva el glossari actual, Andrew rep l’anglès original.
    enric_text=spoken_text(config['text'])
    andrew,enric=await asyncio.wait_for(asyncio.gather(
        sample.voice('01-andrew-auto-raw',config['text'],andrew_config),
        sample.voice('02-enric-actual-raw',enric_text,enric_config)),timeout=60)
    normalize(andrew,ROOT/'output/01-andrew-auto.mp3')
    normalize(enric,ROOT/'output/02-enric-actual.mp3')
    print('Mostres Andrew automàtic i Enric preparades.',flush=True)
    ssml,spans=make_ssml(config)
    result=await ssml_trial(config,ssml)
    report={'andrew_voice':config['voice'],'reference_voice':config['reference_voice'],'rate':config['rate'],
        'original_text':config['text'],'enric_tts_text':enric_text,'ssml_language_spans':spans,'ssml_trial':result,
        'production_changed':False}
    (ROOT/'resultat.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('SSML:',json.dumps(result,ensure_ascii=False),flush=True)


if __name__=='__main__':asyncio.run(main())
