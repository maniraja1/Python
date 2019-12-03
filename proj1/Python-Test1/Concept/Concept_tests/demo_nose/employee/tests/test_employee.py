from demo_nose.employee import employee
import mock
class testemployee:

    def setup(self):
        print("")
        print("setup() before each test method")
        self.emp1 = employee('mani', 'shankar', 10000)
        self.emp2 = employee('jane', 'doe', 5000)


    def teardown(self):
        print("")
        print("teardown() after each test method")


    @classmethod
    def setup_class(cls):
        print("")
        print("setup_class() before any methods in this class")


    @classmethod
    def teardown_class(cls):
        print("")
        print("teardown_class() after any methods in this class")

    def testemail(self):
        assert self.emp1.email == 'mani.shankar@email.com'
        assert self.emp2.email == 'jane.doe@email.com'

    def testfullname(self):
        assert self.emp1.fullname == 'mani.shankar'
        assert self.emp2.fullname == 'jane.doe'

    def testapplyraise(self):
        assert self.emp1.apply_riase() == 11000
        assert self.emp2.apply_riase() == 5500

    @mock.patch('employee.requests.get')
    def testschedule(self,mocked_get):
        mocked_get.return_value.ok = True
        mocked_get.return_value.text = 'Success'

        schedule = self.emp1.monthly_schedule('May')
        mocked_get.assert_called_with('http://company.com/shankar/May')
        assert schedule == 'Success'


        mocked_get.return_value.ok = False

        schedule = self.emp2.monthly_schedule('June')
        mocked_get.assert_called_with('http://company.com/doe/June')
        assert schedule == 'Bad Response!'
