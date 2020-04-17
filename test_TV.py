import unittest
import TV

class ClassTests(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(True)

    def test_creation(self):
        tst = TV.TV("TV")
        self.assertEqual("TV", tst.name)

    def test_chanel_change(self):
        tst = TV.TV("TV")
        self.assertEqual("TV", tst.name)
        tst.chanel = 5
        self.assertEqual(5, tst.chanel)

    def test_wrong_chanel_change(self):
        tst = TV.TV("TV")
        self.assertEqual("TV", tst.name)
        tst.chanel = -5
        self.assertEqual(0, tst.chanel)

    def test_wrong_type_chanel_change(self):
        tst = TV.TV("TV")
        self.assertEqual("TV", tst.name)
        tst.chanel = "10 chanels"
        self.assertEqual(0, tst.chanel)
    
    def test_wrong_name_change(self):
        tst = TV.TV("TV")
        self.assertEqual("TV", tst.name)
        tst.name = "ld"
        self.assertEqual("ld", tst.name)

    
if __name__ =='__main__':
    unittest.main()   
    
    
