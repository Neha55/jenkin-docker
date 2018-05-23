import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper_1(self):
        print("test_upper...1")
        self.assertEqual('foo', 'FOO')
    def test_upper_2(self):
        print("test_upper...2")
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()