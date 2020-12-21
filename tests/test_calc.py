from pytest_workshop.calc import Calc


def test_add_two_numbers():
    c = Calc()
    res = c.add(4, 5)
    assert res == 9


def test_add_three_numbers():
    c = Calc()
    res = c.add(4, 5, 6)
    assert res == 15


def test_add_many_numbers():
    c = Calc()
    s = range(100)
    res = c.add(*s)
    assert res == 4950


def test_sub_two_numbers():
    c = Calc()
    res = c.sub(10, 3)
    assert res == 7


def test_multiply_two_numbers():
    c = Calc()
    res = c.mul(6, 4)
    assert res == 24


def test_multiply_many_numbers():
    s = range(1, 10)
    assert Calc().mul(*s) == 362880


def test_divide_two_numbers():
    assert Calc().div(22, 2) == 11


def test_divide_returns_floats():
    assert Calc().div(11, 2) == 5.5


def test_divide_by_zero_returns_inf():
    assert Calc().div(5, 0) == "inf"
