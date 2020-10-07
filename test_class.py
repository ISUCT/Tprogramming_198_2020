  
import unittest
import ship

class ClassTests(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(True)

    def test_creation(self):
        tst = ship.Ship("ship")
        self.assertEqual("ship",tst.name)

    def test_weight(self):
        tst = ship.Ship("ship")
        self.assertEqual("ship",tst.name)
        tst.length = 5
        self.assertEqual(5, tst.length)

    def test_wrong_weight(self):
        tst = ship.Ship("ship")
        self.assertEqual("ship",tst.name)
        tst.length = -5
        self.assertEqual(0, tst.length)

    def test_wrong_type_weight(self):
        tst = ship.Ship("ship")
        self.assertEqual("ship",tst.name)
        tst.length = "50 метров"
        self.assertEqual(0, tst.length)


if __name__ == '__main__':
    unittest.main() 
