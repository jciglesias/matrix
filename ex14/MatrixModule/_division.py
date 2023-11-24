from ._class import Matrix, Vector

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