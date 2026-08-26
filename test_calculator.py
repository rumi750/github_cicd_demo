from calculator import add, subtract


def test_add():
    assert add(5, 2) == 7


def test_subtract():
    assert subtract(5, 2) == 3
