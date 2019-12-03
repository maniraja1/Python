import unittest
from employee import employee
from unittest.mock import patch

class testemployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print(f"One time setup for all test cases")

    @classmethod
    def tearDownClass(cls) -> None:
        print("One time teardown for all test cases")

    def setUp(self) -> None:
        print("Set up executed per test case")
        self.emp1 = employee('mani', 'shankar', 10000)
        self.emp2 = employee('jane', 'doe', 5000)

    def tearDown(self) -> None:
        print("Tear down executed per test case")

    def test_email(self):
        self.assertEqual(self.emp1.email, 'mani.shankar@email.com')
        self.assertEqual(self.emp2.email, 'jane.doe@email.com')

    def test_apply_raise(self):
        self.assertEqual(self.emp1.apply_riase(), 11000)
        self.assertEqual(self.emp2.apply_riase(), 5500)

    def test_monthly_schedule(self):
        # parameter passed to patch should be passed exactly as shown below
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/shankar/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/doe/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()
