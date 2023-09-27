class Matrix: pass
class Vector: pass

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
