import math_func
import pytest
import sys


@pytest.mark.parametrize('x ,y, result',
                         [(7,3,10),("Hello ","World","Hello World")])
def test_add_func(x,y,result):
    print("***** test add function ******")
    assert math_func.add(x,y) == result

def test_product():
    print("***** test product ******")
    assert math_func.multiply()==40

def test_strings():
    print("***** test string ******")
    result = math_func.add("Hello ","World")
    assert result=="Hello World"
    assert type(result) is str
    assert "sad" not in result