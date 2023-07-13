import unittest
import main


class Testmain(unittest.TestCase):
    def setUp(self):
        print("about to test")
    def test(self):
        test_param=10
        result=main.add(test_param)
        self.assertEqual(result,15)
    def test1(self):
        test_param="estrgtrghr"
        result=main.add(test_param)
        self.assertIsInstance(result,ValueError)
    def test2(self):
        test_param=None
        result=main.add(test_param)
        self.assertEqual(result, 'enter a number')
    def test3(self):
        test_param=2
        result=main.check(test_param)
        self.assertTrue(result)
    def test4(self):
        test_param="estrgtrghr"
        result=main.check(test_param)
        self.assertIsInstance(result,ValueError)   
    def test5(self):
        test_param=''
        result=main.add(test_param)
        self.assertEqual(result, 'enter a number')     
    def test6(self):
        test_param=23
        result=main.check(test_param)
        self.assertFalse(result)

    def tearDown(self):
        print("cleaning")
if __name__=="__main__":  #only run if its the main file
    unittest.main()
