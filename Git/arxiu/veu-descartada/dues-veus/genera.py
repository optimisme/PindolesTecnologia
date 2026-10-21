"""Prova aïllada: Enric per al context català i Guy per als termes anglesos.

Sintetitza la frase catalana completa per conservar-ne la prosòdia i substitueix
els trams anglesos amb les marques WordBoundary. No modifica els vídeos.
"""
import asyncio
from array import array
import hashlib
import html
import json
import math
from pathlib import Path
import re
import subprocess
import wave

import edge_tts

ROOT = Path(__file__).resolve().parent
RATE = 48000
LIMIT = asyncio.Semaphore(3)


def run(args):
    subprocess.run([str(arg) for arg in args], check=True)


def normal(text):
    return ''.join(char.casefold() for char in text if char.isalnum())


async def synthesize(text, voice, rate):
    signature = hashlib.sha256(json.dumps([text, voice, rate], ensure_ascii=False).encode()).hexdigest()
    mp3 = ROOT/'cache'/f'{signature}.mp3'
    metadata = mp3.with_suffix('.json')
    if mp3.exists() and metadata.exists():
        return mp3, json.loads(metadata.read_text())['words']
    async with LIMIT:
        for attempt in range(3):
            try:
                words = []
                communicate = edge_tts.Communicate(text, voice=voice, rate=rate,
                    boundary='WordBoundary', receive_timeout=30)
                with mp3.open('wb') as output:
                    async for chunk in communicate.stream():
                        if chunk['type'] == 'audio':
                            output.write(chunk['data'])
                        elif chunk['type'] == 'WordBoundary':
                            words.append({'start':chunk['offset']/10_000_000,
                                'end':(chunk['offset']+chunk['duration'])/10_000_000,
                                'text':html.unescape(chunk['text'])})
                if not words or mp3.stat().st_size < 1000:
                    raise RuntimeError('Resposta TTS incompleta')
                metadata.write_text(json.dumps({'text':text,'voice':voice,'rate':rate,
                    'words':words}, ensure_ascii=False, indent=2))
                return mp3, words
            except Exception:
                if attempt == 2:
                    raise
                await asyncio.sleep(1)


def pcm(path):
    data = subprocess.check_output(['ffmpeg','-v','error','-i',str(path),
        '-ar',str(RATE),'-ac','1','-f','s16le','-'])
    result = array('h')
    result.frombytes(data)
    return result


def save_pcm(path, samples):
    with wave.open(str(path),'wb') as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(RATE)
        output.writeframes(samples.tobytes())


def active_rms(samples):
    active = [value for value in samples if abs(value) > 100]
    return math.sqrt(sum(value*value for value in active)/max(1,len(active)))


def join(parts):
    # Solapament de 4 ms per evitar clics, sense pauses afegides entre idiomes.
    output = array('h')
    for part in parts:
        if not part:
            continue
        count = min(round(.004*RATE),len(output),len(part))
        for index in range(count):
            alpha = (index+1)/(count+1)
            output[len(output)-count+index] = round(
                output[len(output)-count+index]*(1-alpha) + part[index]*alpha)
        output.extend(part[count:])
    return output


async def example(item, config):
    aliases = {key.casefold():value for key,value in config['catalan_aliases'].items()}
    pattern = re.compile(r'\b('+'|'.join(map(re.escape,aliases))+r')\b',re.I)
    spoken = pattern.sub(lambda match:aliases[match.group().casefold()],item['text'])
    tokens = spoken.split()
    english = {term.casefold() for term in config['english_terms']}
    groups = []
    index = 0
    while index < len(tokens):
        if normal(tokens[index]) not in english:
            index += 1
            continue
        end = index+1
        while end < len(tokens) and normal(tokens[end]) in english:
            end += 1
        groups.append((index,end,' '.join(tokens[index:end])))
        index = end
    base_result, *english_results = await asyncio.gather(
        synthesize(spoken,config['catalan_voice'],config['rate']),
        *[synthesize(text,config['english_voice'],config['rate']) for _,_,text in groups])
    base_path, base_words = base_result
    # Aquesta mostra usa tokens senzills: una marca per cada mot original.
    assert [normal(token) for token in tokens] == [normal(word['text']) for word in base_words], spoken
    base = pcm(base_path)
    target_rms = active_rms(base)
    cursor = 0
    parts, replacements = [], []
    for (start,end,text),(english_path,english_words) in zip(groups,english_results):
        assert [normal(token) for token in text.split()] == [normal(word['text']) for word in english_words], text
        start_time, end_time = base_words[start]['start'],base_words[end-1]['end']
        start_sample,end_sample = round(start_time*RATE),round(end_time*RATE)
        parts.append(base[cursor:start_sample])
        english_pcm = pcm(english_path)
        trim_start = max(0,round((english_words[0]['start']-.012)*RATE))
        trim_end = min(len(english_pcm),round((english_words[-1]['end']+.012)*RATE))
        replacement = english_pcm[trim_start:trim_end]
        gain = min(1.58,max(.63,target_rms/max(1,active_rms(replacement))))
        replacement = array('h',(max(-32768,min(32767,round(value*gain))) for value in replacement))
        parts.append(replacement)
        replacements.append({'text':text,'voice':config['english_voice'],
            'base_start':start_time,'base_end':end_time,
            'replacement_duration':len(replacement)/RATE,'gain_db':round(20*math.log10(gain),2)})
        cursor = end_sample
    parts.append(base[cursor:])
    mixed = join(parts)
    wav_path = ROOT/'output'/f"{item['id']}.wav"
    save_pcm(wav_path,mixed)
    mp3 = wav_path.with_suffix('.mp3')
    run(['ffmpeg','-y','-v','error','-i',wav_path,'-af','loudnorm=I=-18:TP=-2:LRA=7',
         '-ar',str(RATE),'-ac','2','-c:a','libmp3lame','-q:a','2',mp3])
    report = {'original_text':item['text'],'spoken_catalan_text':spoken,
        'catalan_voice':config['catalan_voice'],'english_voice':config['english_voice'],
        'english_segments':replacements,'duration_before_normalization':len(mixed)/RATE}
    mp3.with_suffix('.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(mp3,flush=True)
    return wav_path,report


async def main():
    config = json.loads((ROOT/'mostra.json').read_text())
    for name in ('cache','output'):
        (ROOT/name).mkdir(exist_ok=True)
    examples = await asyncio.gather(*[example(item,config) for item in config['examples']])
    combined = array('h')
    for index,(path,_) in enumerate(examples):
        if index:
            combined.extend(array('h',[0])*round(.8*RATE))
        with wave.open(str(path),'rb') as source:
            part = array('h')
            part.frombytes(source.readframes(source.getnframes()))
            combined.extend(part)
    path = ROOT/'output/prova-mixta.wav'
    save_pcm(path,combined)
    run(['ffmpeg','-y','-v','error','-i',path,'-af','loudnorm=I=-18:TP=-2:LRA=7',
        '-ar',str(RATE),'-ac','2','-c:a','libmp3lame','-q:a','2',path.with_suffix('.mp3')])
    print('Prova completa:',path.with_suffix('.mp3'),flush=True)


if __name__ == '__main__':
    asyncio.run(main())
