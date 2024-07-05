import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")
        self.assertEqual(generate_soundex("C"), "C000")
        # Test lowercase character
        self.assertEqual(generate_soundex("z"), "Z000")

    def test_basic_soundex_generation(self):
        self.assertEqual(generate_soundex("Washington"), "W252")
        self.assertEqual(generate_soundex("Lee"), "L000")
        self.assertEqual(generate_soundex("Johnson"), "J525")
    
    def test_names_with_non_alphabetic_characters(self):
        self.assertEqual(generate_soundex("O'Conner"), "O256")
        self.assertEqual(generate_soundex("McDonald"), "M235")
        self.assertEqual(generate_soundex("D'Angelo"), "D524")
    

    def test_long_name(self):
        self.assertEqual(generate_soundex("Christopher"), "C623")

    def test_name_with_repeating_consonants(self):
        self.assertEqual(generate_soundex("Johnsonn"), "J525")

    def test_name_with_duplicate_soundex_codes(self):
        self.assertEqual(generate_soundex("Euler"), "E460")
        self.assertEqual(generate_soundex("Eulerh"), "E460")

if __name__ == '__main__':
    unittest.main()
