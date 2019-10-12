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
![addition](<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;\begin{align*}&space;\boldsymbol{\vec{v}}&space;&=&space;(1,&space;2,&space;3)&space;\\&space;\boldsymbol{\vec{w}}&space;&=&space;(1,&space;2,&space;3)&space;\\&space;\boldsymbol{\vec{v}}&space;&plus;&space;\boldsymbol{\vec{w}}&space;&=&space;(2,&space;4,&space;6)&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\large&space;\begin{align*}&space;\boldsymbol{\vec{v}}&space;&=&space;(1,&space;2,&space;3)&space;\\&space;\boldsymbol{\vec{w}}&space;&=&space;(1,&space;2,&space;3)&space;\\&space;\boldsymbol{\vec{v}}&space;&plus;&space;\boldsymbol{\vec{w}}&space;&=&space;(2,&space;4,&space;6)&space;\end{align*}" title="\large \begin{align*} \boldsymbol{\vec{v}} &= (1, 2, 3) \\ \boldsymbol{\vec{w}} &= (1, 2, 3) \\ \boldsymbol{\vec{v}} + \boldsymbol{\vec{w}} &= (2, 4, 6) \end{align*}" /></a>)

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

