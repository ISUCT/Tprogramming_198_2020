import unittest
import pig

class ClassTests(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(True)

    def test_creation(self):
        tst = pig.Pig("pig")
        self.assertEqual("pig",tst.name)

    def test_weight(self):
        tst = pig.Pig("pig")
        self.assertEqual("pig",tst.name)
        tst.weight = 5
        self.assertEqual(5, tst.weight)

    def test_wrong_weight(self):
        tst = pig.Pig("pig")
        self.assertEqual("pig",tst.name)
        tst.weight = -5
        self.assertEqual(0, tst.weight)

    def test_wrong_type_weight(self):
        tst = pig.Pig("pig")
        self.assertEqual("pig",tst.name)
        tst.weight = "5 кг"
        self.assertEqual(0, tst.weight)


if __name__ == '__main__':
    unittest.main()