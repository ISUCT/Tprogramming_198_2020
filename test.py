import unittest
import start

def summ(a,b):
    return a + b

class SummTests(unittest.TestCase):

    def test_positive(self):
        res = summ(2,3)
        self.assertEqual(5,res)

    def test_zero(self):
        res = summ(0,0)
        self.assertEqual(0,res)

    def test_one_negative(self):
        res = summ(-2,3)
        self.assertEqual(1,res)

    def test_both_negative(self):
        res = summ(-2,-4)
        self.assertEqual(-6,res)

    def test_one_negative_xero_res(self):
        res = summ(-2,2)
        self.assertEqual(0,res)



if __name__ == '__main__':
    unittest.main()
