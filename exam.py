import unittest
import start

def summ(a, b):
    return a + b

class Tests(unittest.TestCase):

    def test_one(self):
        res = summ(6,3)
        self.assertEqual(9,res)

    def test_two(self):
        res = summ(-40,10)
        self.assertEqual(-30,res)
    
    def test_zero(self):
        res = summ(0,0)
        self.assertEqual(0,res)

if __name__ == '__main__':
    unittest.main()
    