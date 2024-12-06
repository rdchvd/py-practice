import unittest
from solution import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Smile elimS"))
        self.assertTrue(is_palindrome("Hello, Olleh!"))
        self.assertTrue(is_palindrome("stoppots"))

        self.assertFalse(is_palindrome("Darynaanyras"))
        self.assertFalse(is_palindrome("game something something else"))
        self.assertFalse(is_palindrome("test"))



if __name__ == "__main__":
    unittest.main()
