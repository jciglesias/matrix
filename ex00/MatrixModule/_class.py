class Matrix:
    from ._constructor import initMatrix as __init__
    def T():pass

class Vector(Matrix):
    def __init__(self, arg):
        super().__init__(arg)
        if not (self.shape[0] != 1) ^ (self.shape[1] != 1):
            raise TypeError("Argument is not a Vector")
    
    def dot(self, v):
        """Dot product of 2 vectors"""
        if not isinstance(v, Vector):
            raise TypeError("Argument must be of type Vector.")
        if self.shape[0] != 1 and (v.shape[0] != self.shape[0] and v.shape[0] != self.shape[1]) or (v.shape[0] != self.shape[1] and v.shape[1] != self.shape[1]):
            raise TypeError("Vectors are not of the same dimension")
        size = v.shape[0] if v.shape[0] > v.shape[1] else v.shape[1]
        ret = 0
        for i in range(size):
            ret += (self.data[i][0] if self.shape[0] > self.shape[1] else self.data[0][i]) * (v.data[i][0] if v.shape[0] > v.shape[1] else v.data[0][i])
        return ret