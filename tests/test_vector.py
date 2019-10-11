from vector.vector import Vector
import pytest

def test_summation():
    assert Vector(1, 2, 3) + Vector(1, 2, 4) == Vector(2, 4, 7)