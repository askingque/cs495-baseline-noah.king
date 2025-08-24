import unittest
from utils import normalize_and_count

class Test_Normalize_and_Count(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(normalize_and_count("  Hello   World  ", "hello"),
                         ('hello world', 1))

    def test_caps(self):
        self.assertEqual(normalize_and_count("  Hello   World  ", "HELLO"),
                         ('hello world', 1))

    def test_no_match(self):
        self.assertEqual(normalize_and_count("  Hello   World  ", "goodbye"),
                         ('hello world', 0))

if __name__ == '__main__':
    unittest.main()


