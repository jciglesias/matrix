from ._class import Matrix
from copy import deepcopy

def row_echelon(self):
    mat = deepcopy(self.data)
    for i in range(self.shape[0]):
        pivot = abs(mat[i][i])
        pivot_row = i
        for j in range(i + 1, self.shape[0]):
            if abs(mat[j][i]) > pivot and pivot != 1:
                pivot = abs(mat[j][i])
                pivot_row = j
            if pivot_row != i:
                mat[i], mat[pivot_row] = mat[pivot_row], mat[i]
        for j in range(i + 1, self.shape[0]):
            if mat[i][i] != 0 :
                factor = mat[j][i] / mat[i][i]
            else:
                for row in range(self.shape[0]):
                    if mat[row][i] != 0 and row != j:
                        factor = mat[j][i] / mat[row][i]
                        
            for k in range(i, self.shape[1]):
                mat[j][k] -= factor * mat[i][k]
    return type(self)(mat)

def inverse(self):
    det = self.determinant()
    if det != 0:
        pass
    return self.adjoint() / det

def adjoint(self):
    return Matrix([[1]]) if self.shape[0] == 1 else self.cofactor().T()

def cofactor(self):
    return Matrix([[self.minor(row, column).determinant() * [1,-1][(row + column) % 2] for column in range(self.shape[1])] for row in range(self.shape[0])])

def minor(self, i, j):
    if isinstance(i, int) and isinstance(j, int) and i < self.shape[0] and j < self.shape[1]:
        return Matrix([[self.data[row][column] for column in range(self.shape[1]) if row != i and column != j] for row in range(self.shape[0]) if row != i])

 