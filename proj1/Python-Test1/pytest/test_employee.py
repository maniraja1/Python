from employee import employee
import pytest
from unittest.mock import patch

@pytest.fixture
def employee1Setup():
    return employee('corey','schafer',50000)

@pytest.fixture
def employee2Setup():
    return employee('mani','raja',60000)


def test_email(employee1Setup, employee2Setup):
    assert employee1Setup.email == 'corey.schafer@email.com'
    assert employee2Setup.email == 'mani.raja@email.com'

    employee1Setup.first = 'john'
    assert employee1Setup.email == 'john.schafer@email.com'

    employee2Setup.last = 'iyer'
    assert employee2Setup.email == 'mani.iyer@email.com'


def test_full_name(employee1Setup, employee2Setup):
    assert employee1Setup.fullname == 'corey schafer'
    assert employee2Setup.fullname == 'mani raja'

    employee1Setup.first = 'john'
    assert employee1Setup.fullname == 'john schafer'

    employee2Setup.last = 'iyer'
    assert employee2Setup.fullname == 'mani iyer'

def test_raise(employee1Setup, employee2Setup):
    employee1Setup.apply_raise()
    employee2Setup.apply_raise()

    assert employee1Setup.pay == 52500
    assert employee2Setup.pay == 63000

def test_Schedule(employee1Setup, employee2Setup):
    with patch('employee.requests.get') as mocked_get:
        mocked_get.return_value.ok = True
        mocked_get.return_value.text = 'Success'

        schedule = employee1Setup.monthly_schedule('May')
        mocked_get.assert_called_with('http://company.com/schafer/May')
        assert schedule == 'Success'

        mocked_get.return_value.ok = False

        schedule = employee2Setup.monthly_schedule('June')
        mocked_get.assert_called_with('http://company.com/raja/June')
        assert schedule == 'Bad Response!'



