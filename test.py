import unittest
from rope import Rope


class TestRopeMethods(unittest.TestCase):
    def test_that_the_string_initialises_as_expected(self):
        testStr = "the quick brown fox jumped over the lazy dog"
        testRope = Rope(testStr, 10, 5, 15)
        self.assertEqual(str(testRope), testStr)
        self.assertEqual(testRope.leftLength, 22)
        self.assertEqual(testRope.left.leftLength, 11)
        self.assertEqual(testRope.left.left.value, "the quick b")
    
    def test_that_inserts_happen_as_expected_and_rebalances(self):
        testStr = "the quick brown fox jumped over the lazy dog"
        testRope = Rope(testStr, 10, 5, 15)
        testRope.insert(4, "not so ")
        testRope.insert(27, "almost ")

        self.assertEqual(str(testRope), "the not so quick brown fox almost jumped over the lazy dog")

    def test_that_deletes_happen_as_expected_and_rebalances(self):
        testStr = "the not so quick brown fox almost jumped over the lazy dog"
        testRope = Rope(testStr, 10, 5, 15)
        testRope.delete(27, 7)
        testRope.delete(4, 7)

        self.assertEqual(str(testRope), "the quick brown fox jumped over the lazy dog")
    
    def test_that_the_rope_works_with_small_strings(self):
        testStr = "Hi"
        testRope = Rope(testStr)
        self.assertEqual(str(testRope), testStr)
        testRope.insert(1, "i, what's your name? My name is Benj")
        self.assertEqual(str(testRope), "Hi, what's your name? My name is Benji")
    
if __name__ == '__main__':
    unittest.main()