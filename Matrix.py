class Matrix:
    def T(self):
        """Transpose the matrix"""
        m = []
        for i in range(self.shape[1]):
            m.append([])
            for j in range(self.shape[0]):
                m[i].append(self.data[j][i])
        return type(self)(m)

    def __init__(self, arg):
        """Init with a tuple or a list of lists"""
        if isinstance(arg, list):
            if not arg or not len(arg) or not isinstance(arg[0], list):
                raise TypeError("Argument must be a list of lists")
            self.data = arg
            self.shape = (len(arg), len(arg[0]))
            for row in self.data:
                if not isinstance(row, list):
                    raise TypeError("Argument must be a list of lists")
                if len(row) != self.shape[1]:
                    raise TypeError("Bad dimentions for matrix")
        elif isinstance(arg, tuple):
            self.shape = arg
            self.data = []
            for i in range(self.shape[0]):
                self.data.append([])
                for j in range(self.shape[1]):
                    self.data[i].append(0)
        else:
            raise TypeError("Argument must be of type List of Lists or tuple.")
    #add:only matrices of same dimensions.
    def __add__(self, m):
        """Sum of matrix and matrix"""
        if not (isinstance(self, (Matrix, Vector)) and isinstance(m, (Matrix, Vector))) or self.shape != m.shape or type(self) != type(m):
            return NotImplemented
        ret = []
        for y in range(m.shape[0]):
            ret.append([])
            for x in range(m.shape[1]):
                ret[y].append(self.data[y][x] + m.data[y][x])
        return type(self)(ret)
    def __radd__(self, m):
        """Reverse sum of matrix and matrix"""
        if not (isinstance(self, (Matrix, Vector)) and isinstance(m, (Matrix, Vector))) or self.shape != m.shape or type(self) != type(m):
            return NotImplemented
        ret = []
        for y in range(m.shape[0]):
            ret.append([])
            for x in range(m.shape[1]):
                ret[y].append(m.data[y][x] + self.data[y][x])
        return type(self)(ret)
    #sub:only matrices of same dimensions.
    def __sub__(self, m):
        """Substraction of matrix and matrix"""
        if not (isinstance(self, (Matrix, Vector)) and isinstance(m, (Matrix, Vector))) or self.shape != m.shape or type(self) != type(m):
            return NotImplemented
        ret = []
        for y in range(m.shape[0]):
            ret.append([])
            for x in range(m.shape[1]):
                ret[y].append(self.data[y][x] - m.data[y][x])
        return type(self)(ret)
    def __rsub__(self, m):
        """reverse substraction of matrix and matrix"""
        if not (isinstance(self, (Matrix, Vector)) and isinstance(m, (Matrix, Vector))) or self.shape != m.shape or type(self) != type(m):
            return NotImplemented
        ret = []
        for y in range(m.shape[0]):
            ret.append([])
            for x in range(m.shape[1]):
                ret[y].append(m.data[y][x] - self.data[y][x])
        return type(self)(ret)
    #div:only scalars.
    def __truediv__(self, scal):
        """Division of matrix and scalar"""
        if not (isinstance(self, (Matrix, Vector)) and isinstance(scal, (int, float))):
            return NotImplemented
        ret = []
        for row in range(self.shape[0]):
            ret.append([])
            for column in range(self.shape[1]):
                ret[row].append(self.data[row][column] / scal)
        return type(self)(ret)
    def __rtruediv__(self, scal):
        """Reverse division of matrix and scalar"""
        if not (isinstance(self, (Matrix, Vector)) and isinstance(scal, (int, float))):
            return NotImplemented
        ret = []
        for row in range(self.shape[0]):
            ret.append([])
            for column in range(self.shape[1]):
                ret[row].append(scal / self.data[row][column])
        return type(self)(ret)
    #mul:scalars,vectors and matrices,can have errors with vectors and matrices,
    #returns a Vector if we perform Matrix * Vector mutliplication.
    def __mul__(self, m):
        """Multiplication of matrix and matrix or scalar"""
        if type(self) != type(m) and isinstance(m, (int, float)):
            ret = []
            for row in range(self.shape[0]):
                ret.append([])
                for column in range(self.shape[1]):
                    ret[row].append(self.data[row][column] * m)
            return type(self)(ret)
        elif isinstance(self, Vector) and isinstance(m, Vector):
            return self.dot(m)
        elif isinstance(self, Matrix) and isinstance(m, Vector) and self.shape[1] in m.shape:
            vshape = 1 if m.shape[0] > 1 else 0
            ret = [[0 for _ in range(m.shape[1])] for _ in range(m.shape[0])]
            for row in range(m.shape[0]):
                for column in range(m.shape[1]):
                    if not vshape:
                        for i in self.data:
                            ret[row][column] += i[column] * m.data[row][column]
                    else:
                        for i in self.data:
                            ret[row][column] += i[row] * m.data[row][column]
            return Vector(ret)
        elif type(self) == type(m) and (self.shape[0] == m.shape[1] or self.shape[1] == m.shape[0]):
            size = self.shape[0] if self.shape[0] == m.shape[1] and (self.shape[1] != m.shape[0] or self.shape[0] < self.shape[1]) else self.shape[1]
            p = self.shape[0] if self.shape[0] != size else self.shape[1] if self.shape[1] > m.shape[0] else m.shape[0]
            ret = [[0 for _ in range(size)] for _ in range(size)]
            for row in range(size):
                for column in range(size):
                    for i in range(p):
                        if self.shape[0] == size:
                            ret[row][column] += self.data[row][i] * m.data[i][column]
                        else:
                            ret[row][column] += self.data[i][column] * m.data[row][i]
            return type(self)(ret)
        return NotImplemented
    def __rmul__(self, m):
        """Reverse multiplication of matrix and matrix or scalar"""
        if type(self) != type(m) and isinstance(m, (int, float)):
            ret = []
            for row in range(self.shape[0]):
                ret.append([])
                for column in range(self.shape[1]):
                    ret[row].append(self.data[row][column] * m)
            return type(self)(ret)
        elif isinstance(self, Vector) and isinstance(m, Vector):
            return self.dot(m)
        elif isinstance(self, Matrix) and isinstance(m, Vector) and self.shape[1] in m.shape:
            vshape = 1 if m.shape[0] > 1 else 0
            ret = [[0 for _ in range(m.shape[1])] for _ in range(m.shape[0])]
            for row in range(m.shape[0]):
                for column in range(m.shape[1]):
                    if not vshape:
                        for i in self.data:
                            ret[row][column] += i[column] * m.data[row][column]
                    else:
                        for i in self.data:
                            ret[row][column] += i[row] * m.data[row][column]
            return Vector(ret)
        elif type(self) == type(m) and (self.shape[0] == m.shape[1] or self.shape[1] == m.shape[0]):
            size = self.shape[0] if self.shape[0] == m.shape[1] and (self.shape[1] != m.shape[0] or self.shape[0] < self.shape[1]) else self.shape[1]
            p = self.shape[0] if self.shape[0] != size else self.shape[1] if self.shape[1] > m.shape[0] else m.shape[0]
            ret = [[0 for _ in range(size)] for _ in range(size)]
            for row in range(size):
                for column in range(size):
                    for i in range(p):
                        if self.shape[0] == size:
                            ret[row][column] += self.data[row][i] * m.data[i][column]
                        else:
                            ret[row][column] += self.data[i][column] * m.data[row][i]
            return type(self)(ret)
        return NotImplemented
    def __repr__(self) -> str:
        """Print dev version"""
        return f"{type(self).__name__}.data({self.data})"
    def __str__(self) -> str:
        return f"{type(self).__name__}({self.data})"

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
