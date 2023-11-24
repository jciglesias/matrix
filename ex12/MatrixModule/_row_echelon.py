from ._class import Matrix
from copy import deepcopy

def row_echelon(self):
    mat = deepcopy(self.data)
    l_row = self.shape[0]
    l_column = self.shape[1]
    for i in range(l_row):
        pivot = abs(mat[i][i if i < (l_column - 1) else (l_column - 1)])
        pivot_row = i
        for j in range(i + 1, l_row):
            if i < (l_column - 1) and abs(mat[j][i]) > pivot and pivot != 1:
                pivot = abs(mat[j][i])
                pivot_row = j
            if i < (l_column - 1) and pivot_row != i:
                mat[i], mat[pivot_row] = mat[pivot_row], mat[i]
        for j in range(i + 1, self.shape[0]):
            if mat[i][i if i < (l_column - 1) else (l_column - 1)] != 0 :
                factor = mat[j][i if i < (l_column - 1) else (l_column - 1)] / mat[i][i if i < (l_column - 1) else (l_column - 1)]
            else:
                factor = 0
                for row in range(self.shape[0]):
                    if mat[row][i if i < (l_column - 1) else (l_column - 1)] != 0 and row != j:
                        factor = mat[j][i if i < (l_column - 1) else (l_column - 1)] / mat[row][i if i < (l_column - 1) else (l_column - 1)]
            for k in range(i, self.shape[1]):
                mat[j][k] -= factor * mat[i][k]
    return type(self)(mat)

def rank(self):
    mat = self.row_echelon()
    rnk = 0
    for row in mat:
        for column in row:
            if column != 0:
                rnk += 1
                break
    return rnk if rnk < self.shape[0] and rnk < self.shape[1] else self.shape[0] if self.shape[0] < self.shape[1] else self.shape[1]

def inverse(self):
    det = self.determinant()
    if det != 0:
        return self.adjoint() / det

def adjoint(self):
    return Matrix([[1]]) if self.shape[0] == 1 else self.cofactor().T()

def cofactor(self):
    return Matrix([[self.minor(row, column).determinant() * [1,-1][(row + column) % 2] for column in range(self.shape[1])] for row in range(self.shape[0])])

def minor(self, i, j):
    if isinstance(i, int) and isinstance(j, int) and i < self.shape[0] and j < self.shape[1]:
        return Matrix([[self.data[row][column] for column in range(self.shape[1]) if row != i and column != j] for row in range(self.shape[0]) if row != i])

 