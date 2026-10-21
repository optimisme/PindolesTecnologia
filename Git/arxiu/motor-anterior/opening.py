"""Capçalera aprovada: quatre segons de música i presentació de la lliçó."""
import importlib.util
from pathlib import Path
import math
import wave

_path=Path(__file__).parent/'capcalera'/'render_intro.py'
_spec=importlib.util.spec_from_file_location('approved_intro',_path)
visuals=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(visuals)


async def prepare_opening(root,config,r):
    settings=config.get('intro',{})
    if not settings.get('enabled',False):
        return None
    number=config.get('episode_number',1)
    phrase=settings['narration']
    entry={'id':'entrada','narration':phrase}
    if settings.get('segments'):
        entry['segments']=settings['segments']
    audio,words=await r.generate_voice(entry,config,root/'audio')
    music_duration=visuals.DURATION
    # Retallem el silenci de cua del TTS, amb 0,4 s després de l'últim mot.
    frames=math.ceil((words[-1]['end']+.15+.4)*config['fps'])
    voice_duration=frames/config['fps']
    duration=music_duration+voice_duration
    voice_wav=root/'build'/'entrada.wav'
    r.run(['ffmpeg','-y','-v','error','-i',audio,'-af',
           f'adelay=150,apad,atrim=duration={voice_duration},afade=t=in:d=0.01',
           '-ar','48000','-ac','2','-c:a','pcm_s16le',voice_wav])
    raw=root/'build'/'sintonia-original.wav'
    music=root/'build'/'sintonia.wav'
    visuals.generate_music(raw)
    r.run(['ffmpeg','-y','-v','error','-i',raw,'-af','loudnorm=I=-18:TP=-2:LRA=7',
           '-ar','48000','-ac','2','-c:a','pcm_s16le',music])
    # La sintonia i la veu ocupen trams consecutius; mai se superposen.
    cues=r.subtitles_from_words(words,phrase)
    for cue in cues:
        cue['start']+=music_duration+.15
        cue['end']=min(cue['end']+music_duration+.15,duration-.2)
    prefix=root/'build'/'capcalera.wav'
    with wave.open(str(prefix),'wb') as dest:
        for i,path in enumerate((music,voice_wav)):
            with wave.open(str(path),'rb') as src:
                if i==0:
                    dest.setparams(src.getparams())
                dest.writeframes(src.readframes(src.getnframes()))
    return {'duration':duration,'frames':round(duration*config['fps']),
            'music_duration':music_duration,'voice_start':music_duration+.15,
            'voice_duration':voice_duration,'narration':phrase,'episode_number':number,
            'wav':prefix,'cues':cues,'series':config.get('series','Git en un minut i escaig')}


def opening_frame(t,opening):
    return visuals.frame(t,opening['episode_number'],opening['duration'],series=opening['series'])


def opening_metadata(opening):
    if not opening:
        return None
    return {key:opening[key] for key in ('duration','music_duration','voice_start',
                                       'voice_duration','narration','episode_number')}
