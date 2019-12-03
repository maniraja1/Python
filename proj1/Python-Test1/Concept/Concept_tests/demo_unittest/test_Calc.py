import unittest
import Calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calc.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(Calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(Calc.multiply(10, 2), 20)

    def test_divide(self):
        self.assertEqual(Calc.divide(10, 2), 5)

        with self.assertRaises(ZeroDivisionError):
            Calc.divide(10, 0)

        with self.assertRaises(ValueError) as valerror:
            Calc.divide(10, -1)


if __name__ == '__main__':
    unittest.main()


