## easy_vector
An exercise in "double under" methods - my attempt to augment Python's `tuples` to behave like mathematical vectors

***

#### 1. regular tuples don't behave like vectors

```python
>>> (1, 2, 3) + (1, 2, 3)
(1, 2, 3, 1, 2, 3)

>>> (1, 2, 3) * (1, 2, 3)
...
TypeError: can't multiply sequence by non-int of type 'tuple'
```

#### 2. easy_vector

```python
# easy_vector
>>> from easy_vector import Vector
>>> v = Vector(1, 2, 3)
>>> w = Vector(1, 2, 3)
```

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;\boldsymbol{\vec{v}}&space;&=&space;(1,&space;2,&space;3)&space;\\&space;\boldsymbol{\vec{w}}&space;&=&space;(1,&space;2,&space;3)&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\boldsymbol{\vec{v}}&space;&=&space;(1,&space;2,&space;3)&space;\\&space;\boldsymbol{\vec{w}}&space;&=&space;(1,&space;2,&space;3)&space;\end{align*}" title="\begin{align*} \boldsymbol{\vec{v}} &= (1, 2, 3) \\ \boldsymbol{\vec{w}} &= (1, 2, 3) \end{align*}" /></a>



##### 2.1 addition

```python
>>> v + w
Vector(2, 4, 6)
```

##### 2.2 subtraction

```python
>>> v - w
Vector(0, 0, 0)
```
##### 2.3 scalar multiplication

```python
>>> 7 * v
Vector(7, 14, 21)
>>> v * 7
Vector(7, 14, 21)
```

##### 2.4 dot product

```python
>>> v * w
14
```

##### 2.5 unit vector

```python
>>> v.unit
Vector(0.2672612419124244, 0.5345224838248488, 0.8017837257372732)
```

##### 2.6 magnitude of a vector (Euclidian norm)

```python
>>> v.norm
3.7416573867739413
>>> v.unit.norm == 1
True
```
























