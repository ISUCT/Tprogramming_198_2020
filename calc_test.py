import unittest
import start

class CalcTests(unittest.TestCase):
    a = 2.5
    b = 4.6

    def test_normal_b(self):
        x_lst = [1.2, 1.28, 1.36, 1.46, 2.35]
        res = start.task_b(self.a,self.b,x_lst)
        self.assertEqual(5, len(res))

    def test_zero_length(self):
        x_lst = []
        res = start.task_b(self.a,self.b,x_lst)
        self.assertEqual(0, len(res))

    def test_normal_a(self):
        res  = start.task_a(self.a,self.b,1.1,3.6,0.5)
        self.assertEqual(6, len(res))

    def test_zero_a(self):
        res  = start.task_a(self.a,self.b,1.1,3.6,0.5)
        self.assertEqual(6, len(res))


if __name__ == '__main__':
    unittest.main() 
