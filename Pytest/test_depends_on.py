import pytest
import math_func



@pytest.mark.parametrize("x,y,result",[(2,3,5)])
@pytest.mark.run(order=3)
def test_add(x,y,result):
    assert math_func.add(x,y)==result


@pytest.mark.parametrize("x,y,result",[(2,3,6)])
@pytest.mark.run(order=1)
def test_product(x,y,result):
    assert math_func.multiply(x,y)==result

@pytest.mark.run(order=2)
def test_method1():
    assert math_func.add(10,15)==25
