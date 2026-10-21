#!/usr/bin/env python3
"""Valida els guions sense sintetitzar i comprova que els mitjans són intactes."""
import hashlib
import json
from pathlib import Path
import re
import shlex
import sys
import xml.etree.ElementTree as ET
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from azure_voice import make_ssml
from caption_styles import decorate, plain_srt


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as source:
        for block in iter(lambda: source.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def main():
    records = json.loads((ROOT/'guions/revisio.json').read_text())
    assert {int(r['episode'][:2]) for r in records['episodes']} == set(range(2, 26))
    words = beats = 0
    for record in records['episodes']:
        folder = ROOT/record['episode']
        path = folder/'guio-revisat.json'
        config = json.loads(path.read_text())
        assert sha(path) == record['script_sha256']
        assert config['questions'] is False
        assert config['voice'] == 'en-US-AndrewMultilingualNeural'
        assert config['language_rates'] == {'ca-ES': '+5%', 'en-US': '+0%'}
        assert config['language_switch_pause_ms'] == 500
        ids, known_options = set(), set()
        markdown = (folder/'guio-revisat.md').read_text()
        for scene in config['scenes']:
            # Serialitzar SSML no invoca synthesize ni carrega credencials.
            ET.fromstring(make_ssml(scene, config))
            assert scene['narration'] == ' '.join(b['narration'] for b in scene['beats'])
            all_words = scene['narration'].split()
            cues = [{'text': ' '.join(all_words[i:i+10])} for i in range(0, len(all_words), 10)]
            decorate(cues, scene)
            assert ' '.join(plain_srt(c['srt_text']) for c in cues) == scene['narration']
            for b in scene['beats']:
                assert b['id'] not in ids
                ids.add(b['id'])
                assert b['narration'] == ''.join(s['text'] for s in b['segments'])
                assert all(s['lang'] in ['ca-ES', 'en-US'] and s['text'] for s in b['segments'])
                assert '?' not in b['narration']
                assert not re.search(r'\b(?:salutacio|correccio|recuperacio)\b', b['narration'])
                assert not re.search(r'\bguia\b|acompanya el vídeo|material extern', b['narration'], re.I)
                assert 1.5 <= b['pause_after'] <= 4
                assert b['narration'] in markdown
                if b.get('highlight'):
                    assert b['highlight'] in b['command_display']
                words += len(b['narration'].split())
                beats += 1
            if scene.get('input_kind'):
                executions = [b for b in scene['beats'] if b.get('event') == 'execute']
                outcomes = [b for b in scene['beats'] if b.get('event') == 'result']
                assert len(executions) == len(outcomes) == 1
                execution = executions[0]
                command = execution['commands'][0]
                assert scene['beats'].index(execution) < scene['beats'].index(outcomes[0])
                tokens = shlex.split(command)
                highlights = [b['highlight'] for b in scene['beats'] if b.get('highlight')]
                options = [t for t in tokens if t.startswith('-') and t != '--']
                for option in options:
                    assert option in highlights or option in known_options, (record['episode'], command, option)
                    known_options.add(option)
                if '-m' in highlights:
                    values = [h for h in highlights if h.startswith('"') and h.endswith('"')]
                    assert values and highlights.index('-m') < highlights.index(values[0])
        assert config['scenes'][-2]['title'] == 'Resum final'
        assert len(config['scenes'][-2]['beats']) == 3
        assert config['scenes'][-1]['title'] == 'Pràctica final'
    before = json.loads((ROOT/'guions/mitjans-abans.json').read_text())
    current = set()
    for episode in ROOT.glob('[0-9][0-9]-*'):
        if not episode.is_dir():
            continue
        current.update(str(p) for name in ['audio', 'output'] for p in (episode/name).rglob('*') if p.is_file())
        current.update(str(p) for p in [episode/'episodi.json', episode/'guio.md'] if p.is_file())
    current.update(str(p) for p in (Path.home()/'Desktop/PindolesTecnologia/Git').glob('*.mp4'))
    assert current == set(before), {'added': sorted(current-set(before)), 'removed': sorted(set(before)-current)}
    changed = [name for name, digest in before.items() if not Path(name).is_file() or sha(Path(name)) != digest]
    assert not changed, changed
    for doc in [ROOT/'README.md', ROOT/'REVISIO_DIDACTICA.md', ROOT/'guions/README.md',
                *ROOT.glob('[0-9][0-9]-*/guio-revisat.md')]:
        for link in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
            if '://' in link or link.startswith('#'):
                continue
            assert (doc.parent/unquote(link.split('#')[0])).exists(), (str(doc), link)
    proof = dict(episodes=24, beats=beats, words=words, questions=0,
                 protected_files_unchanged=len(before), protected_inventory_unchanged=True, new_audio_generated=False,
                 new_video_generated=False, ssml_serialization_valid=True,
                 captions_restore_original_text=True, command_option_explanations_valid=True)
    records['verification'] = proof
    (ROOT/'guions/revisio.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(proof, ensure_ascii=False))


if __name__ == '__main__':
    main()
