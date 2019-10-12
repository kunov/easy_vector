from math import sqrt

class Vector:

    def __init__(self, *args):
        self.vector = args

    # iterable & subscriptable

    def __len__(self):
        return len(self.vector)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index <= len(self.vector):
            result = self.vector[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.vector[index]
    
    # printable

    def __repr__(self):
        return f"Vector{self.vector}"

    def __str__(self):
        return str(self.vector)

    # vector operations

    def __add__(self, other_vector):
        result = tuple(x + y for x, y in zip(self.vector, other_vector))
        return Vector(*result)

    def __sub__(self, other_vector):
        result = tuple(x - y for x, y in zip(self.vector, other_vector))
        return Vector(*result)

    def __eq__(self, other):
        return self.vector == other.vector

    def __mul__(self, other):
    
        # dot product
        if isinstance(other, Vector):
            result_tuple = tuple(x * y for x, y in zip(self.vector, other.vector))
            result = sum(result_tuple)

            return result

        result = tuple(other * x for x in self.vector)
        return Vector(*result)

    def __rmul__(self, other):
      
        result = tuple(other * x for x in self.vector)
        return Vector(*result)

    @property
    def norm(self):
        squared = tuple(x * x for x in self.vector)
        sum_of_squares = sum(squared)
        return sqrt(sum_of_squares)

    @property
    def unit(self):
        result = tuple(x/self.norm for x in self.vector)
        return Vector(*result)
