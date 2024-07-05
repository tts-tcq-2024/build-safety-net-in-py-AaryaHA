import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):


    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("C"), "C000")
        self.assertEqual(generate_soundex("l"), "L000")

    def test_multiple_charaters(self):
        self.assertEqual(generate_soundex("water"), "W360")
        self.assertEqual(generate_soundex("Lee"), "L000")
        self.assertEqual(generate_soundex("Johnson"), "J525")
    
    def test_non_alphabetic_characters(self):
        self.assertEqual(generate_soundex("O'Conner"), "O256")
        self.assertEqual(generate_soundex("McDonald"), "M235")
        self.assertEqual(generate_soundex("D'Angelo"), "D524")

    def test_name_with_repetition(self):
        self.assertEqual(generate_soundex("monsoon"), "M525")

if __name__ == '__main__':
    unittest.main()
