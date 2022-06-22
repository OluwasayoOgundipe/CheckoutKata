import checkout    # The code to test
import unittest   # The test framework

class TestcheckoutValue(unittest.TestCase):
    def testCaseOne(self):
        self.assertEqual(checkout.checkoutKata("CCC"), 0.75)

    def testCaseTwo(self):
        self.assertEqual(checkout.checkoutKata("AAC"), 1.25)    

if __name__ == '__main__':
    unittest.main()