from demo_unittest.employee import employee
import unittest
from unittest.mock import patch

class Testemployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass within superclass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass within SuperClass")

    def setUp(self):
        self.emp1=employee('corey','schafer',50000)
        self.emp2=employee('mani','raja',60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        self.assertEqual(self.emp1.email,'corey.schafer@email.com')
        self.assertEqual(self.emp2.email, 'mani.raja@email.com')

        self.emp1.first='john'
        self.emp2.first='jane'

        self.assertEqual(self.emp1.email, 'john.schafer@email.com')
        self.assertEqual(self.emp2.email, 'jane.raja@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname,'corey schafer')
        self.assertEqual(self.emp2.fullname,'mani raja')

        self.emp1.first = 'john'
        self.emp2.first = 'jane'

        self.assertEqual(self.emp1.fullname, 'john schafer')
        self.assertEqual(self.emp2.fullname, 'jane raja')

    def test_apply_raise(self):
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

    def test_monthly_schedule(self):
        with patch ('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok=True
            mocked_get.return_value.text='Success'

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/raja/June')
            self.assertEqual(schedule, 'Bad Response!')




if __name__=='__main__':
    unittest.main()