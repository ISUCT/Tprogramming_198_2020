import unittest
import Employee
class ClassTests(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(True)

    def test_creation(self):
        tst = Employee.Employee("Employee")
        self.assertEqual("Employee", tst.name)

if __name__ == '__main__':
    unittest.main()