import unittest
import start

class CalcTests(unittest.TestCase):
    a = 2.0
    b = 3.0    

    def test_positive(self):
        res = start.calc(2,2,1)
        self.assertAlmostEqual(1.099,res,3)

    def test_normal_b(self):
        x_lst = [0.08,0.26,0.35,0.41,0.53]
        res = start.task_b(self.a,self.b,x_lst)
        self.assertEqual(5, len(res))

    def test_zero_length(self):
        x_lst = []
        res = start.task_b(self.a,self.b,x_lst)
        self.assertEqual(0, len(res))

    def test_normal_a(self):
        res = start.task_a(self.a,self.b,0.11,0.36,0.05)
        self.assertEqual(6, len(res))

    def test_zero_a(self):
        res = start.task_a(self.a,self.b,0.11,0.36,0.05)
        self.assertEqual(0, len(res))        


if __name__ == "__main__":
    unittest.main()        