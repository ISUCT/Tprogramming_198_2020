import unittest
import Table
class ClassTests(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(True)

    def test_creation(self):
        tst = Table.Table("Table")
        self.assertEqual("Table", tst.name)



if __name__ == '__main__':
    unittest.main() 