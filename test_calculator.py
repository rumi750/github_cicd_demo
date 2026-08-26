def add(a, b):
    return a + b


def subtract(a, b):
    return a - b  # <-- Fix operator here (+ to -)


def test_add():
    assert add(5, 2) == 7


def test_subtract():
    assert subtract(5, 2) == 3
