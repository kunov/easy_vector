class Vector:

    def __init__(self, *args):
        self.vector = args

    # make Vector iterable & subscriptable

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
    
    # make Vector printable

    def __repr__(self):
        return f"Vector{self.vector}"

    def __str__(self):
        return str(self.vector)

    # make Vector perform operations

    def __add__(self, other_vector):
        result = tuple(x + y for x, y in zip(self.vector, other_vector))
        return Vector(*result)

    def __sub__(self, other_vector):
        result = tuple(x - y for x, y in zip(self.vector, other_vector))
        return Vector(*result)

    def __eq__(self, other):
        return self.vector == other.vector