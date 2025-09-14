import unittest

def add(a,b):
   return a + b


class TestMathFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2,5), 7)

    def test_add_nagative_numbers(self):
        self.assertEqual(add(-1000,-4),-1004)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2,4),2)

if __name__=='__main__':
    unittest.main()