import unittest,gamescript

class Test(unittest.TestCase):
    def setUp(self) :
        print("testing")
    def test_guess(self):
        r=1
        q=1
        result=gamescript.guess(r,q)
        self.assertTrue(result)
        r=+1
    def test_guess_incorrect(self):
        r=1
        q=5
        result=gamescript.guess(r,q)
        self.assertFalse(result)
    def test_overexceed(self):
        r=55
        q=10
        result=gamescript.guess(r,q)
        self.assertEqual(result,"number between 0,10")
    def testVal(self):
        r="weew"
        q="10"
        result=gamescript.guess(r,q)
        self.assertIsInstance(result,ValueError)
unittest.main()