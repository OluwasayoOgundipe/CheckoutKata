from tabnanny import check
import checkout    # The code to test
import unittest   # The test framework

class TestcheckoutValue(unittest.TestCase):
    def testCaseOne(self):
        self.assertEqual(checkout.checkoutKata("CCC"), 0.75)

    def testCaseTwo(self):
        self.assertEqual(checkout.checkoutKata("AAC"), 1.25)  

    def testCaseThree(self):
        self.assertEqual(checkout.checkoutKata("BBB"), 2.00)   

    def testCaseFour(self):
        self.assertEqual(checkout.checkoutKata("CCCC"), 0.75)   

    def testCaseFive(self):
        self.assertEqual(checkout.checkoutKata("BBCCCC"), 2.00)        

if __name__ == '__main__':
    unittest.main()