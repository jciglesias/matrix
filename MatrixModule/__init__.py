class Matrix:
    from ._constructor import initMatrix as __init__
    from ._addition import add
    __add__ = classmethod(add)
    # def __add__(self, m):
    #     """Sum of matrix and matrix"""
    #     if not (isinstance(self, (Matrix, Vector)) and isinstance(m, (Matrix, Vector))) or self.shape != m.shape or type(self) != type(m):
    #         return NotImplemented
    #     ret = []
    #     for y in range(m.shape[0]):
    #         ret.append([])
    #         for x in range(m.shape[1]):
    #             ret[y].append(self.data[y][x] + m.data[y][x])
    #     return type(self)(ret)
    from MatrixModule._addition import radd as __radd__
    from MatrixModule._addition import T
    from MatrixModule._substraction import __rsub__, __sub__
    from MatrixModule._print import __repr__, __str__

class Vector(Matrix):
    def initVector(self, arg):
        super().__init__(arg)
        if not (self.shape[0] != 1) ^ (self.shape[1] != 1):
            raise TypeError("Argument is not a Vector")