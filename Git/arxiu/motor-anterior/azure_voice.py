"""SSML multilingüe, marques temporals reals i memòria cau sense credencials."""
import asyncio
import hashlib
import json
import subprocess
import wave
import xml.etree.ElementTree as ET

from pronunciation import original_words
from speech_settings import credentials

SYNTH = 'http://www.w3.org/2001/10/synthesis'
XML = 'http://www.w3.org/XML/1998/namespace'
VERSION = 'andrew-explicit-beats-v1'


def profile_metadata(config):
    settings = {key: config[key] for key in ('voice', 'language_rates', 'language_switch_pause_ms')}
    digest = hashlib.sha256(json.dumps([VERSION, settings], sort_keys=True).encode()).hexdigest()
    return {'profile': VERSION, 'sha256': digest, **settings}


def make_ssml(scene, config):
    ET.register_namespace('', SYNTH)
    root = ET.Element(f'{{{SYNTH}}}speak', {'version': '1.0', f'{{{XML}}}lang': 'en-US'})
    voice = ET.SubElement(root, f'{{{SYNTH}}}voice', {'name': config['voice']})
    previous = None
    beats = scene.get('beats') or [{'id': 'speech', 'segments': scene['segments']}]
    assert len({beat['id'] for beat in beats}) == len(beats)
    assert ' '.join(''.join(s['text'] for s in b['segments']) for b in beats) == scene['narration']
    for beat in beats:
        ET.SubElement(voice, f'{{{SYNTH}}}bookmark', {'mark': beat['id']})
        for segment in beat['segments']:
            lang = segment['lang']
            assert lang in ('ca-ES', 'en-US') and segment['text']
            if previous and previous != lang:
                ET.SubElement(voice, f'{{{SYNTH}}}break', {'time': f"{config['language_switch_pause_ms']}ms"})
            node = ET.SubElement(voice, f'{{{SYNTH}}}lang', {f'{{{XML}}}lang': lang})
            ET.SubElement(node, f'{{{SYNTH}}}prosody', {'rate': config['language_rates'][lang]}).text = segment['text']
            previous = lang
        pause = float(beat.get('pause_after', 0))
        assert 0 <= pause <= 10
        if pause:
            ET.SubElement(voice, f'{{{SYNTH}}}break', {'time': f'{round(pause*1000)}ms'})
    ET.SubElement(voice, f'{{{SYNTH}}}bookmark', {'mark': 'speech_end'})
    return ET.tostring(root, encoding='unicode')


def identity_words(words, narration):
    return original_words(words, narration, transform=lambda token: token)


def synthesize(scene, config, folder):
    import azure.cognitiveservices.speech as sdk
    folder.mkdir(parents=True, exist_ok=True)
    audio, metadata = folder / f"{scene['id']}.wav", folder / f"{scene['id']}.json"
    ssml = make_ssml(scene, config)
    signature = hashlib.sha256((VERSION + ssml).encode()).hexdigest()
    if audio.exists() and metadata.exists():
        cached = json.loads(metadata.read_text())
        if (cached.get('signature') == signature
                and hashlib.sha256(audio.read_bytes()).hexdigest() == cached.get('audio_sha256')):
            identity_words(cached['words'], scene['narration'])
            return audio, cached['words']
    key, options = credentials(config.get('speech_endpoint'))
    speech = sdk.SpeechConfig(subscription=key, **options)
    speech.speech_synthesis_voice_name = config['voice']
    speech.set_speech_synthesis_output_format(sdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
    speech.set_property(sdk.PropertyId.SpeechServiceResponse_RequestWordBoundary, 'true')
    speech.set_property(sdk.PropertyId.SpeechServiceResponse_RequestPunctuationBoundary, 'false')
    synth = sdk.SpeechSynthesizer(speech_config=speech, audio_config=None)
    words, bookmarks = [], {}

    def boundary(event):
        if event.boundary_type != sdk.SpeechSynthesisBoundaryType.Word:
            return
        duration = event.duration
        length = duration.total_seconds() if hasattr(duration, 'total_seconds') else duration / 10_000_000
        if length > 0:
            start = event.audio_offset / 10_000_000
            words.append({'text': event.text, 'start': start, 'end': start + length})

    synth.synthesis_word_boundary.connect(boundary)
    synth.bookmark_reached.connect(lambda event: bookmarks.update({event.text: event.audio_offset / 10_000_000}))
    print(f"Veu Azure: {scene['id']}", flush=True)
    try:
        result = synth.speak_ssml_async(ssml).get()
        if result.reason != sdk.ResultReason.SynthesizingAudioCompleted:
            details = result.cancellation_details
            message = (details.error_details or '').replace(key, '[REDACTED]')
            raise RuntimeError(f'Síntesi cancel·lada: {details.error_code}. {message[:500]}')
    except Exception as error:
        raise RuntimeError(str(error).replace(key, '[REDACTED]')) from None
    words.sort(key=lambda word: word['start'])
    aligned = identity_words(words, scene['narration'])
    # El darrer bookmark pot no arribar si no hi ha més parla després.
    # Vinculem cada pas a la primera paraula real, que també inclou les pauses.
    beat_times, cursor = {}, 0
    for beat in scene.get('beats') or [{'id': 'speech', 'narration': scene['narration']}]:
        beat_times[beat['id']] = aligned[cursor]['start']
        cursor += len(beat['narration'].split())
    assert cursor == len(aligned)
    temporary = audio.with_suffix('.partial.wav')
    temporary.write_bytes(bytes(result.audio_data))
    with wave.open(str(temporary), 'rb') as source:
        assert source.getframerate() == 24000 and source.getnframes() > 0
    normalized = audio.with_suffix('.normalized.wav')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', str(temporary), '-af',
                    'loudnorm=I=-18:TP=-2:LRA=7', '-ar', '48000', '-ac', '2',
                    '-c:a', 'pcm_s16le', str(normalized)], check=True)
    normalized.replace(audio)
    temporary.unlink()
    (folder / f"{scene['id']}.ssml").write_text(ssml + '\n')
    metadata.write_text(json.dumps({'signature': signature, 'narration': scene['narration'],
        'words': words, 'bookmarks': beat_times, 'service_bookmarks': bookmarks,
        'beat_timing_source': 'first-aligned-word-boundary', 'pronunciation': profile_metadata(config),
        'ssml_sha256': hashlib.sha256(ssml.encode()).hexdigest(),
        'audio_sha256': hashlib.sha256(audio.read_bytes()).hexdigest()}, ensure_ascii=False, indent=2))
    return audio, words


async def generate_voice(scene, config, folder):
    return await asyncio.to_thread(synthesize, scene, config, folder)
