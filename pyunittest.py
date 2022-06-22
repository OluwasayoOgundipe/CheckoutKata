import checkout    # The code to test
import unittest   # The test framework

class TestcheckoutValue(unittest.TestCase):
    def test_value(self):
        self.assertEqual(checkout.checkoutKata("CCC"), 0.75)

if __name__ == '__main__':
    unittest.main()