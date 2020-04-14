import unittest
import start

class CalcTests(unittest.TestCase):

    def test_positive (self):
        res= start.calc(2,2,1)
        self.assertAlmostEqual (1.009, res,3)

if __name__ == '__nain__':
    unitest.main()
