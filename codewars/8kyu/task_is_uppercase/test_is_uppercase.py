import unittest
from .solution import is_uppercase


class TestIsUppercase(unittest.TestCase):
    def test_is_uppercase(self):
        self.assertTrue(is_uppercase("C"))
        self.assertFalse(is_uppercase("c"))
        self.assertTrue(is_uppercase("HELLO I AM DONALD"))
        self.assertFalse(is_uppercase("hello I AM DONALD"))
        self.assertFalse(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ"))
        self.assertTrue(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ"))
        self.assertTrue(is_uppercase("@!33@!@#!*&"))



if __name__ == "__main__":
    unittest.main()
