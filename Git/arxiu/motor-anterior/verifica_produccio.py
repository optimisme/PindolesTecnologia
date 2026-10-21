#!/usr/bin/env python3
"""Verifica mitjans, perfil de pronunciació i fidelitat dels subtítols."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

from pronunciation import DIGEST, original_words, spoken_text, voice_signature

ROOT = Path(__file__).resolve().parent


def seconds(timestamp):
    h, m, s = timestamp.replace(",", ".").split(":")
    return int(h)*3600 + int(m)*60 + float(s)


def verify(episode, decode):
    config = json.loads((episode/"episodi.json").read_text())
    if config.get('format_version') == 2:
        from revised_render import verify_revised
        result = verify_revised(episode, decode)
        print(f"OK {episode.name}: {result['duration']:.3f} s, Andrew i pauses de lectura verificats", flush=True)
        return result
    output = episode/"output"
    production = json.loads((output/"produccio.json").read_text())
    video = output/config.get("output_name", f"{episode.name}.mp4")
    metadata = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(video)]))
    visual, audio = metadata["streams"]
    duration = float(metadata["format"]["duration"])
    assert (visual["codec_name"], visual["width"], visual["height"], visual["r_frame_rate"]) == ("h264", 1280, 720, "24/1")
    assert (audio["codec_name"], audio["sample_rate"], audio["channels"]) == ("aac", "48000", 2)
    assert abs(float(visual["duration"])-float(audio["duration"])) < .05
    assert abs(duration-production["duration"]) < .05
    assert production["voice"] == "ca-ES-EnricNeural"
    generation_digest = production["pronunciation"]["sha256"]
    assert production["opening"]["music_duration"] == 4
    assert abs(production["scenes"][0]["start"]-production["opening"]["duration"]) < .001

    srt = (output/f"{episode.name}.ca.srt").read_text()
    cues = [block.splitlines() for block in srt.strip().split("\n\n")]
    previous_end = 4
    for number, cue in enumerate(cues, 1):
        assert int(cue[0]) == number
        start, end = [seconds(timestamp) for timestamp in cue[1].split(" --> ")]
        assert previous_end-.001 <= start < end <= duration
        previous_end = end
    expected = " ".join([config['intro']['narration'], *[scene['narration'] for scene in config['scenes']]])
    actual = " ".join(" ".join(cue[2:]) for cue in cues)
    assert actual.split() == expected.split(), "Els subtítols han de conservar tot el text original"

    script = (episode/"guio.md").read_text()
    scenes = [{"id": "entrada", "narration": config["intro"]["narration"]}, *config["scenes"]]
    for scene in scenes:
        assert scene["narration"] in script
        for command in scene.get("commands", []):
            assert command in script
        cache = json.loads((episode/"audio"/f"{scene['id']}.json").read_text())
        assert cache["narration"] == scene["narration"]
        # Un perfil anterior és vàlid si tots els fragments encara coincideixen
        # amb el text efectiu actual. Això evita refer vídeos no afectats.
        assert cache["tts_text"] == spoken_text(scene["narration"]), f"{scene['id']}: text TTS pendent d'actualitzar"
        assert cache["signature"] == voice_signature(scene["narration"], cache["tts_text"], config["voice"], config["rate"])
        assert cache["pronunciation"]["sha256"] == generation_digest
        restored = original_words(cache["words"], scene["narration"])
        assert " ".join(word["text"] for word in restored).split() == scene["narration"].split()
        assert all(word["start"] < word["end"] for word in restored)
    if decode:
        for medium in (video, output/"narracio.mp3"):
            subprocess.run(["ffmpeg", "-v", "error", "-i", str(medium), "-f", "null", "-"], check=True)
    print(f"OK {episode.name}: {duration:.3f} s, {len(cues)} subtítols originals, text TTS vigent", flush=True)
    return {"episode": episode.name, "duration": duration, "subtitles": len(cues),
            "voice": production["voice"],
            "video_sha256": hashlib.sha256(video.read_bytes()).hexdigest(),
            "music_sha256": hashlib.sha256((episode/"build/sintonia.wav").read_bytes()).hexdigest(),
            "render_profile_sha256": generation_digest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decode", action="store_true", help="Descodifica íntegrament MP4 i MP3")
    parser.add_argument("episodes", nargs="*")
    args = parser.parse_args()
    episodes = ([ROOT/name for name in args.episodes] if args.episodes else
                sorted(path.parent for path in ROOT.glob("[0-9][0-9]-*/episodi.json")))
    results = [verify(episode, args.decode) for episode in episodes]
    assert len({result["music_sha256"] for result in results}) == 1, "La sintonia ha de ser comuna"
    report = {"legacy_pronunciation_sha256": DIGEST, "full_decode": args.decode,
              "render_profiles": sorted({result["render_profile_sha256"] for result in results}),
              "episodes": results}
    logs = ROOT/"registres-pronuncia"
    logs.mkdir(exist_ok=True)
    (logs/"verificacio.json").write_text(json.dumps(report, indent=2))
    print(f"Verificats {len(results)} vídeos; sintonia comuna idèntica.")


if __name__ == "__main__":
    main()
