import unittest
class MyTests(unittest.TestCase):

    def  test_something(self):
        self.assertEquals(1,1+1-1)

    def  test_something_else(self):
        self.assertTrue(9>1)


if __name__=='__main__':
    unittest.main()
