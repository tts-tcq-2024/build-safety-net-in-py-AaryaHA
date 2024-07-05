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
        self.assertEqual(generate_soundex("assignment"), "A225")
        self.assertEqual(generate_soundex("umbrella"), "U516")
    
    def test_special_characters(self):
        self.assertEqual(generate_soundex("_abc"), "A120")

if __name__ == '__main__':
    unittest.main()
