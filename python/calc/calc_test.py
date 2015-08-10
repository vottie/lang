import unittest
from calc import Calc

class CalcTest(unittest.TestCase):
    def setUp(self):
        print "Calc Test"
    def test_add(self):
        c = Calc()
        x = 100
        y = 200
        result = 0
        result = c.add(x,y)
        print '{0} + {1} = {2}'.format(x, y, result)
        self.assertEqual(x + y, result)
    def test_add_notint_x(self):
        c = Calc()
        x = "aaa"
        y = "bbb"
        result = 0
        with self.assertRaises(TypeError):
            result = c.add(x,y)
            print '{0} + {1} = {2}'.format(x, y, result)
            # self.assertNotEqual(x + y, result)

if __name__ == '__main__':
    unittest.main()
