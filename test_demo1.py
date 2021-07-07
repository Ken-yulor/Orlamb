import pytest

def add_function(a,b):
    return a + b

@pytest.mark.parametrize("a,b,expected",[
    (3,5,8),(-1,-2,-3),(1000,1000,2000)
], ids=['int', 'minus', 'bigint'])
def test_one(a,b,expected):
    assert add_function(a,b) == expected
