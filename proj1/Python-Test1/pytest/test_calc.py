import calc

'''

'''

def test_add():
    assert calc.add(5, 5) == 10
    assert calc.add(-1, -2) == -3
    assert calc.add(-5, 2) == -3
    assert calc.add(0, 0) == 0
    assert calc.add(0, 2) == 2
    #assert calc.add(5, 2) == 6

def test_subtract():
    assert calc.subtract (5, 5) == 0
    assert calc.subtract(-1, -2) == 1
    assert calc.subtract(-5, 2) == -7
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(0, 2) == -2

def test_multiply():
    assert calc.multiply(5, 5) == 25
    assert calc.multiply(-1, -2) == 2
    assert calc.multiply(-5, 2) == -10
    assert calc.multiply(0, 0) == 0
    assert calc.multiply(0, 2) == 0

def test_divide():
    assert calc.divide(5, 5) == 1
    assert calc.divide(-1, -2) == 0.5
    assert calc.divide(-5, 2) == -2.5
    assert calc.divide(0, 2) == 0


