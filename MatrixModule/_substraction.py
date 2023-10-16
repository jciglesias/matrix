from ._class import Matrix, Vector

def sub(self, m):
    """Substraction of matrix and matrix"""
    if type(self) != type(m) or self.shape != m.shape or not isinstance(self, (Matrix, Vector)):
        print(f"{type(self) != type(m)} or {self.shape != m.shape} or {not isinstance(self, (Matrix, Vector))}")
        return NotImplemented
    ret = []
    for y in range(m.shape[0]):
        ret.append([])
        for x in range(m.shape[1]):
            ret[y].append(self.data[y][x] - m.data[y][x])
    return type(self)(ret)
def rsub(self, m):
    """reverse substraction of matrix and matrix"""
    if not (isinstance(self, (Matrix, Vector)) and isinstance(m, (Matrix, Vector))) or self.shape != m.shape or type(self) != type(m):
        return NotImplemented
    ret = []
    for y in range(m.shape[0]):
        ret.append([])
        for x in range(m.shape[1]):
            ret[y].append(m.data[y][x] - self.data[y][x])
    return type(self)(ret)
