import unittest
from translator import english_to_french, french_to_english  # Change here

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        # Test that 'Hello' is translated to 'Bonjour'
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # Change here

        # Test that 'Bonjour' is not the translation of 'Hello' in English
        self.assertNotEqual(english_to_french('Bonjour'), 'Hello')  # Change here

    def test_french_to_english(self):
        # Test that 'Bonjour' is translated to 'Hello'
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # Change here

        # Test that 'Hello' is not the translation of 'Bonjour' in French
        self.assertNotEqual(french_to_english('Hello'), 'Bonjour')  # Change here

if __name__ == '__main__':
    unittest.main()

