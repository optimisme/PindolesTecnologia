"""Idiomes, plantilles i revisions del compilador de guions."""
from pathlib import Path
import unittest

from motor.alineacio import original_words
from motor.guions import Compiler, Language, ScriptError, expand
from motor.serie import load_series, spoken_number

SERIE = Path(__file__).resolve().parents[2]/'Git'
CONFIG = {'termes_angles': ['git commit', 'commits', 'commit', 'main', 'Git', 'GitHub', 'cherry-pick'],
          'formes_parlades': {'salutacio': 'salutació'}}


class LanguageTest(unittest.TestCase):
    def setUp(self):
        self.language = Language(CONFIG)

    def test_terms_are_english_and_longest_first(self):
        text, segments = self.language.segments('Fem git commit a main amb GitHub.')
        self.assertEqual(text, 'Fem git commit a main amb GitHub.')
        self.assertEqual([s['text'] for s in segments if s['lang'] == 'en-US'], ['git commit', 'main', 'GitHub'])

    def test_explicit_markup_and_hyphenated_terms(self):
        _, segments = self.language.segments('[[Cherry-pick]] porta un canvi; cherry-pick també.')
        self.assertEqual([s['text'] for s in segments if s['lang'] == 'en-US'], ['Cherry-pick', 'cherry-pick'])

    def test_terms_inside_other_words_stay_catalan(self):
        _, segments = self.language.segments('El remitent i la mainada.')
        self.assertEqual(segments, [{'lang': 'ca-ES', 'text': 'El remitent i la mainada.'}])

    def test_identifiers_recover_catalan_accents(self):
        text, _ = self.language.segments('La branca salutacio.')
        self.assertEqual(text, 'La branca salutació.')

    def test_explicit_only_mode_keeps_approved_segments(self):
        _, segments = self.language.segments('Primer commit de [[Git]].', explicit_only=True)
        self.assertEqual([s['lang'] for s in segments], ['ca-ES', 'en-US', 'ca-ES'])
        self.assertEqual(self.language.untagged(segments), ['commit'])


class TemplateTest(unittest.TestCase):
    def test_commit_template_fills_message_and_keeps_overrides(self):
        templates = load_series(SERIE)['config']['plantilles']
        stage = expand({'plantilla': 'commit', 'missatge': 'Canvia la salutacio', 'resultat': 'Fet.'}, templates)
        self.assertEqual(stage['ordre'], 'git commit -m "Canvia la salutacio"')
        self.assertEqual(stage['resultat'], 'Fet.')
        self.assertIn('Canvia la salutacio', list(stage['parts'][1].values())[0])


class SeriesTest(unittest.TestCase):
    def test_ordinals(self):
        self.assertEqual(spoken_number(0), 'Lliçó zero')
        self.assertEqual(spoken_number(21), 'Vint-i-unena lliçó')
        self.assertEqual(spoken_number(31), 'Trenta-unena lliçó')

    def test_all_lessons_compile_and_reject_spoken_hashes(self):
        series = load_series(SERIE)
        compiler = Compiler(series)
        for item in series['lessons']:
            compiler.compile(item)
        broken = dict(series['lessons'][8])
        broken['data'] = dict(broken['data'], inici_parlat='El commit 2e4c08d té la salutació.')
        with self.assertRaises(ScriptError):
            Compiler(series).compile(broken)

    def test_subtitle_alignment_keeps_original_spelling(self):
        words = [{'text': 'Fem', 'start': 0, 'end': .2}, {'text': 'git', 'start': .3, 'end': .4},
                 {'text': 'commit', 'start': .4, 'end': .7}]
        restored = original_words(words, 'Fem git commit.')
        self.assertEqual([w['text'] for w in restored], ['Fem', 'git', 'commit.'])


if __name__ == '__main__':
    unittest.main()
