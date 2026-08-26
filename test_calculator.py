from calculator import add, subtract


def test_add():
    assert add(5, 2) == 7
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 4) == 6
