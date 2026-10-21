"""La marca d’idioma guia el format i conserva el text dels subtítols."""
import unittest

from PIL import Image, ImageChops, ImageDraw
import caption_styles
import render
from caption_styles import decorate, plain_srt


class CaptionStylesTest(unittest.TestCase):
    def test_sentence_punctuation_stays_outside_english_quotes(self):
        scene = {
            'narration': 'Fem git commit, després continuem.',
            'segments': [
                {'lang': 'ca-ES', 'text': 'Fem '},
                {'lang': 'en-US', 'text': 'git commit'},
                {'lang': 'ca-ES', 'text': ', després continuem.'},
            ],
        }
        cue = decorate([{'text': scene['narration']}], scene)[0]
        self.assertEqual(cue['srt_text'], 'Fem <i>«git commit»</i>, després continuem.')
        self.assertEqual(plain_srt(cue['srt_text']), scene['narration'])

    def test_only_explicit_english_span_is_styled(self):
        scene = {
            'narration': 'main main',
            'segments': [
                {'lang': 'ca-ES', 'text': 'main '},
                {'lang': 'en-US', 'text': 'main'},
            ],
        }
        cue = decorate([{'text': scene['narration']}], scene)[0]
        self.assertEqual(cue['srt_text'], 'main <i>«main»</i>')

    def test_english_split_across_cues_has_balanced_format_and_exact_text(self):
        scene = {
            'narration': 'Ara git push origin main. Després esperem.',
            'beats': [
                {'segments': [
                    {'lang': 'ca-ES', 'text': 'Ara '},
                    {'lang': 'en-US', 'text': 'git push origin main'},
                    {'lang': 'ca-ES', 'text': '.'},
                ]},
                {'segments': [{'lang': 'ca-ES', 'text': 'Després esperem.'}]},
            ],
        }
        cues = decorate([{'text': 'Ara git push'}, {'text': 'origin main. Després esperem.'}], scene)
        self.assertEqual(cues[0]['srt_text'], 'Ara <i>«git push»</i>')
        self.assertEqual(cues[1]['srt_text'], '<i>«origin main»</i>. Després esperem.')
        self.assertEqual(' '.join(plain_srt(cue['srt_text']) for cue in cues), scene['narration'])

    def assert_caption_matches_unfragmented_runs(self, runs):
        actual = Image.new('RGB', (1280, 720), render.BG)
        cue = {'start': 0, 'end': 1, 'runs': runs}
        caption_styles.draw(ImageDraw.Draw(actual), [cue], .5, render)
        expected = Image.new('RGB', actual.size, render.BG)
        drawing = ImageDraw.Draw(expected)
        drawing.rounded_rectangle((64, 590, 1216, 680), 14, fill='#080D16')
        fonts = [caption_styles.ITALIC if run['italic'] else caption_styles.REGULAR for run in runs]
        widths = [drawing.textlength(run['text'], font=font) for run, font in zip(runs, fonts)]
        x = 640 - sum(widths) / 2
        baseline = 617 + caption_styles.REGULAR.getmetrics()[0]
        # Dibuixar cada frase sencera evita alinear els contorns dels mots
        # individualment: és la referència visual d’una línia de base comuna.
        for run, font, width in zip(runs, fonts, widths):
            drawing.text((x, baseline), run['text'], font=font, fill=render.WHITE, anchor='ls')
            x += width
        self.assertIsNone(ImageChops.difference(actual, expected).getbbox())

    def test_word_baselines_match_a_sentence_drawn_as_one_piece(self):
        self.assert_caption_matches_unfragmented_runs([
            {'text': 'Aquesta ordre ens informa; no confirma ni envia cap', 'italic': False},
        ])

    def test_accents_and_english_italics_share_the_same_baseline(self):
        self.assert_caption_matches_unfragmented_runs([
            {'text': 'Àudio amb ', 'italic': False},
            {'text': '«git push»', 'italic': True},
            {'text': ' i més explicacions.', 'italic': False},
        ])


if __name__ == '__main__':
    unittest.main()
