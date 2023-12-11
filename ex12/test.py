from MatrixModule import Matrix, Vector
import numpy as np

if __name__ == "__main__":
    mat = [[1,0,0],[0,1,0],[0,0,1]]
    print(Matrix(mat).inverse())
    print("numpy:\n",  np.linalg.inv(np.array(mat)))
    mat = [[2,0,0],[0,2,0],[0,0,2]]
    print(Matrix(mat).inverse())
    print("numpy:\n",  np.linalg.inv(np.array(mat)))
    mat = [[8., 5., -2.],[4., 7., 20.],[7., 6., 1.]]
    print(Matrix(mat).inverse())
    # print(np.linalg.inv(np.array(mat)) * np.array(mat))
    # print(Matrix(mat).inverse() * Matrix(mat))
    print(np.linalg.inv(np.array(mat)))
    mat = [[6, 1 ,1],[4 ,-2 ,5],[2 ,8 ,7]]
    print("matrix:\n", Matrix(mat).inverse())
    print("numpy:\n",  np.linalg.inv(np.array(mat)))