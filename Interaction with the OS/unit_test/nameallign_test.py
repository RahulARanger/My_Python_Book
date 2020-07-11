import unittest
from nameallign import align
    
class testing_2(unittest.TestCase):
    def test_basic(self):
        testcase=input('Enter the Input: ')
        expected=input('Expected Output: ')
        print('Testing with the run time input ')
        self.assertEqual(align(testcase),expected)
    def test_with_default_values(self):
        testcase='Rahul,Sai Hanuma'
        expected='Sai Hanuma Rahul'
        print('Testing with the default values')
        self.assertEqual(align(testcase),expected)

unittest.main()        
