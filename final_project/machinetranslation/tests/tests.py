import unittest

from ..translator import english_to_french, french_to_english


class TestF2E(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def testCase2(self):
        self.assertEqual(french_to_english('bière'), 'beer')


class TestE2F(unittest.TestCase):
    def testCase(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def testCase2(self):
        self.assertEqual(english_to_french('beer'), 'bière')


if __name__ == '__main__':
    unittest.main()
