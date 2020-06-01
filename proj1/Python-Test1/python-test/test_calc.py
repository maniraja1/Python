import calc
import unittest

'''
 one way of running this is navigate to the project folder where your test.py is located and run the below
 python -m unittest test_calc.py

 Another way of running this is including if__name=='__main__':unittest.main()

'''
class testcalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(1, -1), 0)
        self.assertEqual(calc.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(1, -1), 2)
        self.assertEqual(calc.subtract(-1, -5), 4)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(1, -1), -1)
        self.assertEqual(calc.multiply(-1, -5), 5)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(1, -1), -1)
        self.assertEqual(calc.divide(-1, -5), 0.2)



if __name__=='__main__':
    unittest.main()
