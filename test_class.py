import unittest
import document
class ClassTests(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(True)

    def test_creation(self):
        tst = document.Document("document")  
        self.assertEqual("document", tst.type) 

    def test_size_change(self):
        tst = document.Document("document")  
        self.assertEqual("document", tst.type)
        tst.size = 5
        self.assertEqual(5, tst.size)

    def test_wrong_size_change(self):
        tst = document.Document("document")  
        self.assertEqual("document", tst.type)
        tst.size = -5
        self.assertEqual(7, tst.size)

    def test_wrong_type_size_change(self):
        tst = document.Document("document")  
        self.assertEqual("document", tst.type)
        tst.size = "A5"
        self.assertEqual(7, tst.size)

if __name__ == '__main__':
    unittest.main()