import unittest
import start

class CalcTests(unittest.TestCase):
    a = 0.8
    b = 0.4

    def test_normal_b(self):
        x_lst = [1.88, 2.26, 3.84, 4.55, -6.21]
        res = start.task_b(self.a,self.b,x_lst)
        self.assertEqual(5, len(res))
    
    def test_zero_length(self):
        x_lst = []
        res = stark.task_b(self.a,self.b,x_lst)
        self.assertEqual(0, len(res))
    
    def test_normal_a(self):
        res  = start.task_a(self.a,self.b,1.23,7.23,1.2)
        self.assertEqual(6, len(res))

    def test_zero_a(self):
        res  = start.task_a(self.a,sekf.b,1.23,7.23,1.2)
        self.assertEqual(0, len(res))


if __name__ == '__main__':
    unittest.main()