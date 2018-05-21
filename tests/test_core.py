from tdk import TurkishWord
from tdk.exceptions import WordNotFoundException

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class CoreTests(unittest.TestCase):

    def test_query_meaining(self):
        term = 'Atatürk'

        word = TurkishWord(term)
        word.query()
        self.assertIn("Türklerin atası", word.meaning)
        self.assertIn("Gazi Mustafa Kemal Paşa", word.meaning)

    def test_invalid_word(self):
        term = 'zabaluba'

        word = TurkishWord(term)
        word.query()

        with self.assertRaises(WordNotFoundException):
            result = word.meaning
