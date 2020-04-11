import unittest
import rabbit

class ClassTests(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(True)

    def tes_tcreation(self):
        tst = rabbit.Rabbit("Rabbit")
        self.assertEqual("Rabbit", tst.name)
    
    def test_size_change(self):
        tst = rabbit.Rabbit("Rabbit")
        self.assertEqual("Rabbit", tst.name)
        tst.age = 5
        self.assertEqual(5, tst.age)

    def test_wrong_size_change(self):
        tst = rabbit.Rabbit("Rabbit")
        self.assertEqual("Rabbit", tst.name)
        tst.age = -5
        self.assertEqual(0, tst.age)

    def test_wrong_type_age_change(self):
        tst = rabbit.Rabbit("Rabbit")
        self.assertEqual("Rabbit", tst.name)
        tst.age = "5 vears"
        self.assertEqual(0, tst.age)

if __name__ == '__main__':
    unittest.main()