from src.math_utils import add, subtract, square

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_square():
    assert square(4) == 16
