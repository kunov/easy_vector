from easy_vector.easy_vector import Vector
import pytest

@pytest.fixture
def inp():
    result = {
        'v': Vector(5, 6),
        'w': Vector(23, 3)
    }
    return result

def test_summation(inp):
    assert inp['v'] + inp['w'] == Vector(28, 9)
    assert inp['w'] + inp['v'] == Vector(28, 9)

def test_subtraction(inp):
    assert inp['v'] - inp['w'] == Vector(-18, 3)
    assert inp['w'] - inp['v'] == Vector(18, -3)

def test_scalar_mult(inp):
    assert inp['v'] * 2 == 2 * inp['v'] == Vector(10, 12)
    assert inp['v'] * 1.5 == Vector(7.5, 9)

def test_dot_product(inp):
    assert inp['v'] * inp['w'] == 133