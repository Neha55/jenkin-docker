import unittest

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
        
    @classmethod
    def tearDownClass(cls):
        print("I am tear-down")
        
    def test_upper_1(self):
        print("test_upper...1")
        self.assertEqual('FOO', 'FOO')
        
    def test_upper_2(self):
        print("test_upper...2")
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)