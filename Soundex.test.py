import unittest
from Soundex import generate_soundex
class TestSoundex(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")
    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")
        self.assertEqual(generate_soundex("l"), "L000")

    def test_multiple_characters(self):
        self.assertEqual(generate_soundex("water"), "W360")
        self.assertEqual(generate_soundex("asdfghjk"), "A231")
        self.assertEqual(generate_soundex("qxecyn"), "Q250")
    
    def test_names_with_non_alphabetic_characters(self):
        self.assertEqual(generate_soundex("O'Conner"), "O256")
        self.assertEqual(generate_soundex("McDonald"), "M235")
        self.assertEqual(generate_soundex("D'Angelo"), "D524")

if __name__ == '__main__':
    unittest.main()
