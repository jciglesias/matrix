from ._class import Matrix

def trace(self):
    if isinstance(self, Matrix) and self.shape[0] == self.shape[1]:
        ret = 0
        for i in range(self.shape[0]):
            ret += self.data[i][i]
        return ret
    return