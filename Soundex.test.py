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

    def test_longer_than_4(self):
        self.assertEqual(generate_soundex("friday"), "F630")
        self.assertEqual(generate_soundex("umbrella"), "U516")
    
    def vowels(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("E"), "E000")
        self.assertEqual(generate_soundex("I"), "I000")
        self.assertEqual(generate_soundex("O"), "O000")
        self.assertEqual(generate_soundex("U"), "U000")

    def special_chars(self):
        self.assertEqual(generate_soundex("L_@#$"), "L000")
        self.assertEqual(generate_soundex("Q.&*^"), "Q000")

    def repeating_letters(self):
        self.assertEqual(generate_soundex("monsoon"), "M525")
        self.assertEqual(generate_soundex("book"), "B200")

if __name__ == '__main__':
    unittest.main()
