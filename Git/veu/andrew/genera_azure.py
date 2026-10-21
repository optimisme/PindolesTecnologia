"""Genera la prova SSML amb l’SDK oficial Azure Speech, sense desar claus."""
import argparse
import getpass
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from urllib.parse import urlparse
import wave

from prepara import ROOT,prepare,variant_suffix
sys.path.insert(0,str(ROOT.parents[2]))
from motor.credencials import load_speech_environment


def save_result(data):
    suffix=variant_suffix(data.get('language_switch_pause_ms',0),data.get('language_rates'))
    (ROOT/f'resultat{suffix}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')


def connection_options(target):
    if target.startswith('https://'):
        parsed=urlparse(target)
        if (not parsed.hostname or not parsed.hostname.endswith('.cognitiveservices.azure.com')
                or parsed.username or parsed.password or parsed.query or parsed.fragment
                or parsed.path not in ('','/') or parsed.port not in (None,443)):
            raise ValueError('Cal l’endpoint base de Speech: https://nom.cognitiveservices.azure.com/; no el Project endpoint ni l’Azure OpenAI endpoint.')
        return {'endpoint':f'https://{parsed.hostname}/'}
    if re.fullmatch(r'[a-z0-9-]+',target):
        return {'region':target}
    raise ValueError('Indica l’endpoint base HTTPS de Speech o el codi de regió.')


def main():
    load_speech_environment()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--configura',action='store_true',help='Demana la clau oculta; utilitza l’endpoint de Speech configurat')
    parser.add_argument('--pausa-ms',type=int,default=0,help='Pausa SSML a cada canvi d’idioma, en mil·lisegons; crea una variant separada')
    args=parser.parse_args()
    if args.pausa_ms<0:parser.error('--pausa-ms ha de ser igual o superior a zero')
    if args.configura and not sys.stdin.isatty():
        print('Executa --configura en un terminal interactiu per introduir la clau de manera oculta.',file=sys.stderr)
        return 2
    config,ssml=prepare(args.pausa_ms)
    suffix=variant_suffix(args.pausa_ms,config.get('language_rates'))
    key=os.environ.get('AZURE_SPEECH_KEY') or os.environ.get('SPEECH_KEY')
    target=(os.environ.get('AZURE_SPEECH_ENDPOINT') or os.environ.get('SPEECH_ENDPOINT')
            or os.environ.get('AZURE_SPEECH_REGION') or os.environ.get('SPEECH_REGION')
            or config.get('speech_endpoint'))
    if args.configura:
        try:
            target=target or input('Endpoint base de Speech o codi de regió: ').strip()
        except (EOFError,KeyboardInterrupt):
            print('\nConfiguració cancel·lada.',file=sys.stderr)
            return 2
    report={'voice':config['voice'],'transport':'azure-speech-sdk',
            'ssml_sha256':hashlib.sha256(ssml.encode()).hexdigest(),
            'languages':['ca-ES','en-US'],'production_changed':False,
            'language_switch_pause_ms':args.pausa_ms}
    if config.get('language_rates'):
        report['language_rates']=config['language_rates']
    else:
        report['rate']=config['rate']
    if not target:
        save_result({**report,'status':'missing_speech_endpoint','audio_generated':False})
        print('Falta l’endpoint o la regió de Speech.',file=sys.stderr)
        return 2
    try:
        options=connection_options(target)
    except ValueError as error:
        print(error,file=sys.stderr)
        return 2
    if args.configura:
        print('Connexió Speech:',target)
        print('Veu:',config['voice'],'· SSML explícit ca-ES / en-US')
        print('Pausa a cada canvi d’idioma:',args.pausa_ms,'ms')
        if config.get('language_rates'):
            print('Velocitats: català',config['language_rates']['ca-ES'],'· anglès',config['language_rates']['en-US'])
        try:
            key=key or getpass.getpass('Clau del recurs de Speech (entrada oculta): ').strip()
        except (EOFError,KeyboardInterrupt):
            print('\nConfiguració cancel·lada.',file=sys.stderr)
            return 2
    if not key:
        save_result({**report,'status':'missing_azure_speech_key','connection':options,'audio_generated':False})
        print('Falta la clau: executa amb --configura o configura AZURE_SPEECH_KEY al mateix terminal.',file=sys.stderr)
        return 2
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
        print('Cal ffmpeg i ffprobe.',file=sys.stderr)
        return 2
    try:
        import azure.cognitiveservices.speech as speechsdk
    except ImportError:
        print('Instal·la les dependències opcionals: python -m pip install -r veu/andrew/requirements.txt',file=sys.stderr)
        return 2
    speech_config=speechsdk.SpeechConfig(subscription=key.strip(),**options)
    speech_config.speech_synthesis_voice_name=config['voice']
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
    synthesizer=speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=None)
    result=synthesizer.speak_ssml_async(ssml).get()
    if result.reason!=speechsdk.ResultReason.SynthesizingAudioCompleted:
        details=result.cancellation_details
        message=re.sub(re.escape(key.strip()),'[REDACTED]',details.error_details or '',flags=re.I)
        save_result({**report,'connection':options,'status':'azure_synthesis_canceled','audio_generated':False,
                     'error_code':str(details.error_code),'details':message[:1500]})
        print('Azure ha cancel·lat la síntesi:',details.error_code,file=sys.stderr)
        print(message[:1500],file=sys.stderr)
        return 1
    output=ROOT/'output';output.mkdir(exist_ok=True)
    temporary=output/f'andrew-idiomes-explicits{suffix}.partial.wav'
    temporary.write_bytes(bytes(result.audio_data))
    try:
        with wave.open(str(temporary),'rb') as source:
            assert source.getframerate()==24000 and source.getnframes()>0
    except (wave.Error,EOFError,AssertionError):
        temporary.unlink(missing_ok=True)
        save_result({**report,'status':'invalid_audio_response','audio_generated':False})
        print('Azure no ha retornat un WAV vàlid.',file=sys.stderr)
        return 1
    wav=output/f'andrew-idiomes-explicits{suffix}.wav';temporary.replace(wav)
    mp3=output/f'andrew-idiomes-explicits{suffix}.mp3'
    subprocess.run(['ffmpeg','-y','-v','error','-i',str(wav),'-af','loudnorm=I=-18:TP=-2:LRA=7',
        '-ar','48000','-ac','2','-c:a','libmp3lame','-q:a','2',str(mp3)],check=True)
    subprocess.run(['ffmpeg','-v','error','-i',str(mp3),'-f','null','-'],check=True)
    duration=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration',
        '-of','csv=p=0',str(mp3)],text=True))
    save_result({**report,'status':'audio_generated','audio_generated':True,'connection':options,
        'duration':duration,'audio_sha256':hashlib.sha256(mp3.read_bytes()).hexdigest(),'output':str(mp3)})
    print(mp3)
    return 0


if __name__=='__main__':sys.exit(main())
