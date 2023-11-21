from ._class import Matrix, Vector
from copy import deepcopy, copy

def mul(self, m):
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
        for row in range(len(ret)):
            for column in range(len(ret[row])):
                for m_column in range(self.shape[1]):
                    if not vshape:
                        ret[row][column] += self.data[column][m_column] * m.data[0][m_column]
                    else:
                        ret[row][column] += self.data[row][m_column] * m.data[m_column][0]
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

def rmul(self, m):
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

def determinant(self):
    mat = self.row_echelon()
    ret = 1
    for i in range(self.shape[0]):
        ret *= mat[i][i]
    return round(ret)

def linear_combination(self, m):
    pass