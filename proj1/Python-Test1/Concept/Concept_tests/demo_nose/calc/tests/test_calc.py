from nose import with_setup
from nose.tools import assert_raises
from demo_nose.calc import calc

def setup_module(module):
    print("")
    print("Module setup")

def teardown_module(module):
    print("")
    print("Module teardown")

def setup_func():
    print("")
    print("Function set up")

def teardown_func():
    print("")
    print("Function tear down")

@with_setup(setup_func(), teardown_func())
def test_add():
    assert calc.add(10, 5) == 15

@with_setup(setup_func(), teardown_func())
def test_subtract():
    assert calc.subtract(10, 5) == 5

@with_setup(setup_func(), teardown_func())
def test_multiply():
    assert calc.multiply(10, 2) == 20

@with_setup(setup_func(), teardown_func())
def test_divide():
    assert calc.divide(10, 2) == 5

    with assert_raises(ZeroDivisionError):
        calc.divide(10, 0)

    with assert_raises(ValueError):
        calc.divide(10, -1)




