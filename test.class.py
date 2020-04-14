import unittest
import Dog

class ClassTests(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(True)

    def test_creation(self):
        tst = Dog.Dog("Dog")
        self.assertEqual("Dog", tst.name)

    def test_age_change(self):
        tst = Dog.Dog("Dog")
        self.assertEqual ("Dog",tst.name)       
        tst.age =  5 
        self.assertEqual(5, tst.age)

    def test_wrong_age_change(self):
        tst = Dog.Dog("Dog")
        self.assertEqual ("Dog",tst.name)       
        tst.age =  -5 
        self.assertEqual(0, tst.age)

    def test_wronge_type_age_change(self):
        tst = Dog.Dog("Dog")
        self.assertEqual ("Dog",tst.name)       
        tst.age =  "5 vears"
        self.assertEqual(0, tst.age)

if __name__ == '__main__':
    unittest.main()
