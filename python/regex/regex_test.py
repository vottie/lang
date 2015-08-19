import unittest
from regex import RegEx

class RexExTest(unittest.TestCase):
    def setUp(self):
        print('Test Started')

    def test_regex(self):
        string = 'hello'
        r = RegEx(string)
        r.search()
        self.assertTrue(r)

if __name__ == '__main__':
    unittest.main()
