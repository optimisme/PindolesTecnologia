"""Comprovacions del text pronunciat i dels subtítols amb l'ortografia original."""
import json
import hashlib
from pathlib import Path
import unittest

from pronunciation import original_words, spoken_text, voice_signature, cached_voice_matches


class PronunciationTests(unittest.TestCase):
    def test_initial_sample_except_later_commit_correction(self):
        sample = json.loads((Path(__file__).parent/"arxiu/veu-enric/mostra.json").read_text())
        for term, pronunciation in sample["pronunciations"].items():
            if term.casefold() == "commit":
                continue
            self.assertEqual(spoken_text(term), pronunciation)

    def test_selected_add_commit_and_plural(self):
        self.assertEqual(spoken_text("Git add prepara; git commit desa els commits."),
                         "Guit add prepara; Guit còmit desa els còmits.")

    def test_boundaries_and_punctuation(self):
        self.assertEqual(spoken_text("d'upstream, commits; MAIN!"), "d'apstrím, còmits; méin!")
        self.assertEqual(spoken_text("legítim, compromís, principal"), "legítim, compromís, principal")

    def test_catalan_identifiers_keep_catalan_pronunciation(self):
        self.assertEqual(spoken_text("Salutacio, correccio i recuperacio."),
                         "salutació, correcció i recuperació.")
        self.assertEqual(spoken_text("projecte-correccio; d'una salutacio"),
                         "projecte-correcció; d'una salutació")
        self.assertEqual(spoken_text("La salutació i la correcció."),
                         "La salutació i la correcció.")
        restored = original_words([
            {"text": "salutació", "start": 0, "end": .5},
            {"text": "correcció", "start": .6, "end": 1.1}
        ], "salutacio, correccio.")
        self.assertEqual([word["text"] for word in restored], ["salutacio,", "correccio."])

    def test_one_written_token_multiple_spoken_words(self):
        boundaries = [{"text": "Guit", "start": 0, "end": .3},
                      {"text": "Hàb", "start": .4, "end": .7},
                      {"text": "còmit", "start": .9, "end": 1.3}]
        restored = original_words(boundaries, "GitHub, commit.")
        self.assertEqual(restored, [{"text": "GitHub,", "start": 0, "end": .7},
                                    {"text": "commit.", "start": .9, "end": 1.3}])

    def test_selected_github_variant_preserves_accent(self):
        self.assertEqual(spoken_text("A GitHub."), "A Guit Hàb.")

    def test_log_extension_command_and_plural_keep_original_captions(self):
        self.assertEqual(spoken_text("Git log: fitxers .log i logs; reflog."),
                         "Guit lòg: fitxers .lòg i lògs; rèflog.")
        restored = original_words([
            {"text": "lòg", "start": 0, "end": .3},
            {"text": "lògs", "start": .4, "end": .8}
        ], "log, logs.")
        self.assertEqual([word["text"] for word in restored], ["log,", "logs."])

    def test_apostrophes_hyphens_and_merged_boundary(self):
        restored = original_words([
            {"text": "d", "start": 0, "end": .1},
            {"text": "apstrím", "start": .1, "end": .6},
            {"text": "txèri", "start": .7, "end": 1},
            {"text": "pic", "start": 1, "end": 1.3},
            {"text": "notèdit", "start": 1.4, "end": 2.1},
        ], "d'upstream, cherry-pick, not edit.")
        self.assertEqual([word['text'] for word in restored], ["d'upstream,", "cherry-pick,", "not", "edit."])
        self.assertLessEqual(restored[-2]['end'], restored[-1]['start'])

    def test_mismatched_service_text_fails(self):
        with self.assertRaises(ValueError):
            original_words([{"text": "altra", "start": 0, "end": .5}], "Git.")

    def test_cache_reuses_only_identical_speech(self):
        args = ("Git a salutacio.", "Guit a salutacio.", "ca-ES-EnricNeural", "+12%")
        old_digest = "glossari-anterior"
        legacy = {"signature": hashlib.sha256(json.dumps([*args, old_digest]).encode()).hexdigest(),
                  "pronunciation": {"sha256": old_digest}}
        current = {"signature": voice_signature(*args)}
        for cached in (legacy, current):
            self.assertTrue(cached_voice_matches(cached, *args))
            for position, replacement in [(1, "Guit a salutació."), (2, "altra-veu"), (3, "+0%")]:
                changed = list(args)
                changed[position] = replacement
                self.assertFalse(cached_voice_matches(cached, *changed))


if __name__ == "__main__":
    unittest.main()
