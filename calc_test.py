import unittest
import start

class CalcTests(unittest.TestCase):
    a = 0.4
    b = 0.8 

    def test_positive(self):
        res = start.calc(1, 1, 0)
        self.assertAlmostEqual(0,res,3)
 
    def test_normal_b(self):
        x_lst = [4.48, 3.56, 2.78, 5.28, 3.21]
        res = start.task_b(self.a,self.b,x_lst)
        self.assertEqual(5, len(res))
    
    def test_zero_lengt(self):
        x_lst = []
        res = start.task_b(self.a,self.b,x_lst)
        self.assertEqual(0, len(res))

    def test_normal_a(self):
        res = start.task_a(self.a, self.b, 0.77, 1.77, 0.2)
        self.assertEqual(6, len(res))

    def test_zero_a(self):
        res = start.task_a(self.a, self.b, 4.77, 1.77, 0.2)
        self.assertEqual(0, len(res))
        
if __name__ == '__main__':
    unittest.main()
