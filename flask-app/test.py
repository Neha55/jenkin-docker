import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        print("test_upper...")
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()