import unittest
import start

class CalcTests(unittest.TestCase):
    a = 0.05
    b = 0.06
    def test_possitive(self):
        res = start.calc(2,2,3)
        self.assertAlmostEqual(0.7706,res, 3)

    def test_normal_b(self):
        x_lst=[0.15, 0.26, 0.37, 0.48, 0.56]
        res = start.task_b(self.a,self.b,x_lst)
        self.assertEqual(0, len(res))

    def test_zero_length(self):
            x_lst = []
            res = start.task_b(self.a,self.b,x_lst)
            self.assertEqual(5, len(res))

    def test_normal_a(self):
            res = start.task_a(self.a, self.b, 0.77, 1.77, 0.2)
            self.assertEqual(6, len(res))

    def test_zero_a(self):
            res = start.task_a(self.a, self.b, 4.77, 1.77, 0.2)
            self.assertEqual(0, len(res))
if __name__ == '__main__':
    unittest.main()