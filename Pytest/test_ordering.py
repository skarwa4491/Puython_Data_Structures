import pytest


@pytest.mark.run(order=2)
def test_foo():
    assert True


@pytest.mark.run(order=1)
def test_bar():
    assert True



@pytest.mark.run(order=3)
def test_disp():
    assert True