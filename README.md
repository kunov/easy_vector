# easy_vector
An exercise in "double under" methods - my attempt to augment Python's `tuples` to behave like mathematical vectors

***

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
```
![addition](https://latex.codecogs.com/gif.download?%5Clarge%20%5Cbegin%7Balign*%7D%20%5Cboldsymbol%7B%5Cvec%7Bv%7D%7D%20%26%3D%20%281%2C%202%2C%203%29%20%5C%5C%20%5Cboldsymbol%7B%5Cvec%7Bw%7D%7D%20%26%3D%20%281%2C%202%2C%203%29%20%5C%5C%20%5Cboldsymbol%7B%5Cvec%7Bv%7D%7D%20+%20%5Cboldsymbol%7B%5Cvec%7Bw%7D%7D%20%26%3D%20%282%2C%204%2C%206%29%20%5Cend%7Balign*%7D)

```python
# addition
>>> v = Vector(1, 2, 3)
>>> w = Vector(1, 2, 3)
>>> v + w
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

