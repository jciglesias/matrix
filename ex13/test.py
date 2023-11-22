from MatrixModule import Matrix
import numpy as np
import sympy
if __name__=="__main__":
    mat = [[1,0,0],[0,1,0],[0,0,1]]
    print(Matrix(mat).rank())
    print(np.linalg.matrix_rank(np.array(mat)))
    mat = [[ 1., 2., 0., 0.],[ 2., 4., 0., 0.],[-1., 2., 1., 1.]]
    print(Matrix(mat).rank())
    print(np.linalg.matrix_rank(np.array(mat)))
    mat = [[ 8., 5., -2.],[ 4., 7., 20.],[ 7., 6., 1.],[21., 18., 7.]]
    print(Matrix(mat).rank())
    # print(sympy.Matrix(mat).rank())
    print(np.linalg.matrix_rank(np.array(mat)))