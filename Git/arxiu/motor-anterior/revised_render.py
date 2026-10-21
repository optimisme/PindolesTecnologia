"""Muntatge revisat amb Andrew, passos lligats a la parla i pauses de lectura."""
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import wave
from array import array

from PIL import Image, ImageDraw
import render as r
import caption_styles
from azure_voice import generate_voice, identity_words, make_ssml, profile_metadata
from intro_revisada import prepare_demo
from opening import prepare_opening, opening_frame, opening_metadata

run, probe = r.run, r.probe


def subtitles_from_words(words, narration):
    return r.subtitles_from_words(words, narration, transform=lambda token: token)


def verify_revised(root, decode=False, output=None):
    output = output or root/'output'
    config = json.loads((root/'episodi.json').read_text())
    prod = json.loads((output/'produccio.json').read_text())
    video = output/config['output_name']
    streams = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams',
        '-show_format','-of','json',str(video)]))
    visual, sound = streams['streams']
    duration = float(streams['format']['duration'])
    assert (visual['codec_name'],visual['width'],visual['height'],visual['r_frame_rate']) == ('h264',1280,720,'24/1')
    assert (sound['codec_name'],sound['sample_rate'],sound['channels']) == ('aac','48000',2)
    assert abs(float(visual['duration'])-float(sound['duration'])) < .05
    assert abs(duration-prod['duration']) < .05
    assert prod['voice'] == config['voice'] == 'en-US-AndrewMultilingualNeural'
    assert prod['pronunciation'] == profile_metadata(config)
    assert prod['source_sha256'] == hashlib.sha256((root/'episodi.json').read_bytes()).hexdigest()
    assert prod['opening']['music_duration'] == 4
    def seconds(value):
        h,m,s=value.replace(',','.').split(':')
        return int(h)*3600+int(m)*60+float(s)
    cues=[]
    for index,block in enumerate((output/f'{root.name}.ca.srt').read_text().strip().split('\n\n'),1):
        lines=block.splitlines();assert int(lines[0])==index
        start,end=[seconds(v) for v in lines[1].split(' --> ')]
        assert 4 <= start < end <= duration
        if cues:assert cues[-1]['end'] <= start+.001
        cues.append({'start':start,'end':end,'text':caption_styles.plain_srt(' '.join(lines[2:]))})
    expected=' '.join([config['intro']['narration'],*[s['narration'] for s in config['scenes']]])
    assert ' '.join(c['text'] for c in cues).split()==caption_styles.plain_srt(expected).split()
    plain=(output/f'{root.name}.ca-original.srt').read_text().strip().split('\n\n')
    assert ' '.join(' '.join(block.splitlines()[2:]) for block in plain).split()==expected.split()
    for scene in [{'id':'entrada',**config['intro']},*config['scenes']]:
        meta=json.loads((root/'audio'/f"{scene['id']}.json").read_text())
        assert meta['narration']==scene['narration']
        assert meta['pronunciation']==profile_metadata(config)
        assert meta['ssml_sha256']==hashlib.sha256(make_ssml(scene,config).encode()).hexdigest()
        assert meta['audio_sha256']==hashlib.sha256((root/'audio'/f"{scene['id']}.wav").read_bytes()).hexdigest()
        restored=identity_words(meta['words'],scene['narration'])
        assert all(w['start']<w['end'] for w in restored)
    assert not any(s.get('reflection') for s in prod['scenes']), 'No s’han de generar preguntes'
    pauses=[beat['reading_pause'] for s in prod['scenes'] for beat in s['beats'] if beat.get('reading_pause')]
    assert pauses and all(p['requested_seconds']>=1 for p in pauses)
    for pause in pauses:
        start,end=pause['start'],pause['end']
        assert end-start >= pause['requested_seconds']-.4
        assert not any(c['start']<end and c['end']>start for c in cues)
        with wave.open(str(root/'build/narracio-revisada.wav'),'rb') as audio:
            middle=(start+end)/2
            audio.setpos(round((middle-.15)*audio.getframerate()))
            samples=array('h',audio.readframes(round(.3*audio.getframerate())))
            assert samples and max(map(abs,samples)) <= 128, 'La pausa conté àudio massa fort'
    if decode:
        for medium in (video,output/'narracio.mp3'):
            run(['ffmpeg','-v','error','-i',medium,'-f','null','-'])
    return {'episode':root.name,'duration':duration,'subtitles':len(cues),
            'video_sha256':hashlib.sha256(video.read_bytes()).hexdigest(),
            'music_sha256':hashlib.sha256((root/'build/sintonia.wav').read_bytes()).hexdigest(),
            'render_profile_sha256':prod['pronunciation']['sha256'],
            'voice':config['voice'],'reflection_seconds':0,
            'reading_pause_seconds':sum(p['requested_seconds'] for p in pauses),'full_decode':decode}


async def render_episode(root, config, audio_only=False):
    audio_dir,build=root/'audio',root/'build'
    stage=build/'revisio-output'
    for path in (audio_dir,build,stage):path.mkdir(parents=True,exist_ok=True)
    source_hash=hashlib.sha256((root/'episodi.json').read_bytes()).hexdigest()
    demo=(prepare_demo(build) if config.get('lesson_kind')!='general' else
          {'verified':False,'scope':'conceptual lesson; no commands executed'})
    fps=config['fps']
    opening=await prepare_opening(root,config,sys.modules[__name__])
    caption_styles.decorate(opening['cues'],config['intro'])
    offset=opening['duration'];cues=list(opening['cues']);wavs=[opening['wav']];timings=[]
    script=[f"# {config['title']}",'',f"Sèrie: {config['series']}",
            f"Veu: {config['voice']} · català +5%, anglès +0%, pauses d’idioma de 500 ms.",'',
            f"Punt de partida: {config['prerequisites']}",'',
            '## Capçalera musical (0:00–0:04)','',
            'Sintonia comuna de quatre segons, sense locució.','',
            f"## Presentació (4,00–{offset:.2f} s)",'',opening['narration'],'']
    for scene in config['scenes']:
        audio,words=await generate_voice(scene,config,audio_dir)
        meta=json.loads((audio_dir/f"{scene['id']}.json").read_text())
        audio_duration=probe(audio)
        reflection=scene.get('reflection');hold=scene.get('hold_after',0)
        frames=math.ceil((.3+audio_duration+.55+hold+(reflection['seconds'] if reflection else 0))*fps)
        duration=frames/fps
        local=subtitles_from_words(words,scene['narration'])
        caption_styles.decorate(local,scene)
        for cue in local:
            cue['start']+=.3;cue['end']+=.3
            cue['end']=min(cue['end'],.3+audio_duration)
            cues.append({**cue,'start':cue['start']+offset,'end':cue['end']+offset})
        timed=[]
        aligned=identity_words(words,scene['narration']);word_cursor=0
        for beat in scene['beats']:
            effect=.3+meta['bookmarks'][beat['id']]+1
            prefix=''
            for segment in beat['segments']:
                if segment['lang']=='en-US':
                    index=word_cursor+len(prefix.split())+len(segment['text'].split())-1
                    effect=.3+aligned[index]['end']+.15
                    break
                prefix+=segment['text']
            word_end=.3+aligned[word_cursor+len(beat['narration'].split())-1]['end']
            if beat.get('effect_after')=='speech':effect=word_end+.15
            timed.append({**beat,'at':.3+meta['bookmarks'][beat['id']],'effect_at':effect,'word_end':word_end})
            word_cursor+=len(beat['narration'].split())
        scene.update(start=offset,duration=duration,frames=frames,cues=local,_timed_beats=timed,_demo=demo)
        info={'id':scene['id'],'start':offset,'duration':duration,'voice_end':offset+.3+audio_duration,
              'beats':[{'id':b['id'],'view':b['view'],'start':offset+b['at'],
                        'effect_at':offset+b['effect_at']} for b in timed]}
        for i,beat in enumerate(timed):
            pause=beat.get('pause_after',0)
            if pause:
                start=beat['word_end']+.15
                end=start+pause-.15
                assert end <= .3+audio_duration+.01
                if i+1<len(timed):assert end <= timed[i+1]['at']+.01
                info['beats'][i]['reading_pause']={'start':offset+start,'end':offset+end,'requested_seconds':pause}
        if reflection:
            begin=.3+audio_duration
            scene['_reflection_start']=begin
            info['reflection']={**reflection,'start':offset+begin,'end':offset+begin+reflection['seconds']}
        timings.append(info)
        wav=build/f"{scene['id']}.wav"
        run(['ffmpeg','-y','-v','error','-i',audio,'-af',
             f'adelay=300,apad,atrim=duration={duration}',
             '-ar','48000','-ac','2','-c:a','pcm_s16le',wav])
        wavs.append(wav)
        script += [f"## {scene['title']} ({offset:.2f}–{offset+duration:.2f} s)",'',
                   '**Animació:** '+scene['visual'],'']
        for i,beat in enumerate(timed):
            end=timed[i+1]['at'] if i+1<len(timed) else .3+audio_duration
            script += [f"### {beat['id']} ({offset+beat['at']:.2f}–{offset+end:.2f} s)",'',
                       '**Locució:** '+beat['narration'],'']
            if beat['commands']:script+=['**Comanda en pantalla:**','', '```bash',*beat['commands'],'```','']
            if beat.get('pause_after'):
                script += [f"**Pausa de lectura i assimilació:** {beat['pause_after']} s; es manté el mateix visual.",'']
        if reflection:
            interval=info['reflection']
            script += [f"**Reflexió sense locució:** {interval['start']:.2f}–{interval['end']:.2f} s. "
                       +reflection['question'],'','La resposta es revela a l’escena següent.','']
        if hold:script += [f'**Temps per assimilar el resultat:** {hold:.1f} s addicionals.','']
        offset+=duration
    narration=build/'narracio-revisada.wav'
    with wave.open(str(narration),'wb') as dest:
        for i,path in enumerate(wavs):
            with wave.open(str(path),'rb') as source:
                if i==0:dest.setparams(source.getparams())
                dest.writeframes(source.readframes(source.getnframes()))
    (stage/f'{root.name}.ca.srt').write_text('\n\n'.join(
        f"{i+1}\n{r.srt_time(c['start'])} --> {r.srt_time(c['end'])}\n{c['srt_text']}" for i,c in enumerate(cues))+'\n')
    (stage/f'{root.name}.ca-original.srt').write_text('\n\n'.join(
        f"{i+1}\n{r.srt_time(c['start'])} --> {r.srt_time(c['end'])}\n{c['text']}" for i,c in enumerate(cues))+'\n')
    (stage/'guio.md').write_text('\n'.join(script))
    production={'format_version':2,'title':config['title'],'series':config['series'],'voice':config['voice'],
                'tts':'Microsoft Azure Speech SDK / SSML explícit','fps':fps,'resolution':[1280,720],
                'duration':offset,'source_sha256':source_hash,'opening':opening_metadata(opening),
                'pronunciation':profile_metadata(config),'scenes':timings,'example_verified':demo['verified'],
                'subtitles':'Anglès entre cometes i cursiva; SRT amb estil i còpia original sense format',
                'questions':False,'reading_pauses':True}
    (stage/'produccio.json').write_text(json.dumps(production,ensure_ascii=False,indent=2))
    run(['ffmpeg','-y','-v','error','-i',narration,'-c:a','libmp3lame','-q:a','2',stage/'narracio.mp3'])
    print(f'Veu i guió revisats: {offset:.1f} s',flush=True)
    if audio_only:return
    silent=build/'animacions-revisades.mp4'
    encoder=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24',
        '-s','1280x720','-r',str(fps),'-i','pipe:0','-an','-c:v','libx264','-preset','fast',
        '-threads','2','-crf','19','-pix_fmt','yuv420p',str(silent)],stdin=subprocess.PIPE)
    sheets=[]
    try:
        for n in range(opening['frames']):
            t=n/fps;im=opening_frame(t,opening)
            caption_styles.draw(ImageDraw.Draw(im),opening['cues'],t,r)
            if n==round(2.1*fps):im.save(stage/'portada.png')
            encoder.stdin.write(im.tobytes())
        for index,scene in enumerate(config['scenes']):
            print(f"Animació revisada {index+1}/{len(config['scenes'])}: {scene['id']}",flush=True)
            background=r.base(scene,index,len(config['scenes']),config)
            for n in range(scene['frames']):
                t=n/fps;im=background.copy();d=ImageDraw.Draw(im)
                r.draw_visual(d,scene,t,scene['duration']);caption_styles.draw(d,scene['cues'],t,r)
                d.rectangle((0,712,1279,719),fill=r.BORDER)
                d.rectangle((0,712,int(1280*(scene['start']+t)/offset),719),fill=r.MINT)
                if n==round(scene['frames']*.78):
                    im.save(build/f'revisada-{index+1:02}.png');sheets.append(im.copy())
                encoder.stdin.write(im.tobytes())
        encoder.stdin.close()
        if encoder.wait()!=0:raise RuntimeError('Ha fallat el render de les animacions revisades.')
    except BaseException:
        encoder.kill();encoder.wait();raise
    final=stage/config['output_name']
    run(['ffmpeg','-y','-v','error','-i',silent,'-i',narration,'-map','0:v','-map','1:a',
         '-c:v','copy','-c:a','aac','-b:a','192k','-metadata:s:a:0','language=cat',
         '-metadata',f"title={config['title']}",'-movflags','+faststart',final])
    sheet=Image.new('RGB',(1280,math.ceil(len(sheets)/2)*360),r.BG)
    for i,im in enumerate(sheets):sheet.paste(im.resize((640,360)),((i%2)*640,(i//2)*360))
    sheet.save(build/'storyboard-revisat.jpg',quality=92)
    report=verify_revised(root,decode=True,output=stage)
    (stage/'verificacio.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    output=root/'output';output.mkdir(exist_ok=True)
    for source in stage.iterdir():
        target=root/'guio.md' if source.name=='guio.md' else output/source.name
        temporary=target.with_name(target.name+'.partial')
        shutil.copy2(source,temporary);temporary.replace(target)
    export=Path.home()/'Desktop/PindolesTecnologia/Git'
    export.mkdir(parents=True,exist_ok=True)
    destination=export/config['output_name'];temporary=destination.with_suffix('.partial')
    shutil.copy2(output/config['output_name'],temporary);temporary.replace(destination)
    assert hashlib.sha256(destination.read_bytes()).hexdigest()==report['video_sha256']
    print(f'Vídeo revisat verificat i copiat a Desktop: {final.name} ({offset:.1f} s)',flush=True)
