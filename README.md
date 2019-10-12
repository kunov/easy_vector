# easy_vector
An exercise in "double under" methods: My attempt to augment Python's tuples to behave like mathematical vectors

## Python tuples vs. easy_vector

```python
# tuples
>>> (1, 2, 3) + (1, 2, 3)
(1, 2, 3, 1, 2, 3)

>>> (1, 2, 3) * (1, 2, 3)
...
TypeError: can't multiply sequence by non-int of type 'tuple'
```
```python
# easy_vector
>>> from easy_vector import Vector

# addition
>>> Vector(1, 2, 3) + Vector(1, 2, 3)
Vector(2, 4, 6)

# subtraction
>>> Vector(1, 2, 3, 4) - Vector(1, 2, 3, 0) - Vector(0, 0, 0, 4)
Vector(0, 0, 0, 0)

# scalar multiplication
>>> v = Vector(1, 1, 1, 1)
>>> v * 7
Vector(7, 7, 7, 7)
>>> 7 * v
Vector(7, 7, 7, 7)

# dot product
>>> Vector(1, 2, 3) * Vector(1, 2, 3) # dot product
14 

```

