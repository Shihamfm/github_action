from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(5,3) == 8
    assert add(2,2) == 4

def test_sub():
    assert sub(2,3) == -1
    assert sub(4,3) == 1
    assert sub(3,3) == 0
