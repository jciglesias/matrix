from MatrixModule._class import Matrix, Vector

def add(self, m):
    """Sum of matrix and matrix"""
    if not (isinstance(self, (Matrix, Vector)) and isinstance(m, (Matrix, Vector))) or self.shape != m.shape or type(self) != type(m):
        return NotImplemented
    ret = []
    for y in range(m.shape[0]):
        ret.append([])
        for x in range(m.shape[1]):
            ret[y].append(self.data[y][x] + m.data[y][x])
    return type(self)(ret)

def radd(self, m):
    """Reverse sum of matrix and matrix"""
    if not (isinstance(self, (Matrix, Vector)) and isinstance(m, (Matrix, Vector))) or self.shape != m.shape or type(self) != type(m):
        return NotImplemented
    ret = []
    for y in range(m.shape[0]):
        ret.append([])
        for x in range(m.shape[1]):
            ret[y].append(m.data[y][x] + self.data[y][x])
    return type(self)(ret)

def iadd(self, item):
    if not (isinstance(self, (Matrix, Vector)) and isinstance(item, (Matrix, Vector))) or self.shape != item.shape or type(self) != type(item):
        print("test")
        return NotImplemented
    ret = []
    for y in range(item.shape[0]):
        ret.append([])
        for x in range(item.shape[1]):
            ret[y].append(self.data[y][x] + item.data[y][x])
    self.data = ret
    return self

def T(self):
    """Transpose the matrix"""
    m = []
    for i in range(self.shape[1]):
        m.append([])
        for j in range(self.shape[0]):
            m[i].append(self.data[j][i])
    return type(self)(m)