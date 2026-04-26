from app import add, div, sub, mul
import pytest

def test_add():
    assert add(2, 3) == 5

def test_div():
    assert div(6, 3) == 2

def test_sub():
    assert sub(10, 5) == 5 

def test_mul():
    assert mul(5, 3) == 15 

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)