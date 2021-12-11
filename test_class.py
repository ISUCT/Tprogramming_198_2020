import unittest
import Fish

class ClassTests(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(True)
    
    def test_creation(self):
        tst = Fish.Fish("Fish")
        self.assertEqual("Fish", tst.name)

    def test_age_change(self):
        tst = Fish.Fish("Fish")
        self.assertEqual("Fish", tst.name)
        tst.age = 5
        self.assertEqual(5, tst.age)

    def test_wrong_age_change(self):
        tst = Fish.Fish("Fish")
        self.assertEqual("Fish", tst.name)
        tst.age = -5
        self.assertEqual(0, tst.age)

    def test_wrong_type_age_change(self):
        tst = Fish.Fish("Fish")
        self.assertEqual("Fish", tst.name)
        tst.age = "5 years"
        self.assertEqual(0, tst.age)

if __name__ == '__main__':
    unittest.main()