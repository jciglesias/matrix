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