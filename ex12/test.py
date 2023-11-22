from MatrixModule import Matrix, Vector
import numpy as np

if __name__ == "__main__":
    mat = [[6, 1 ,1],[4 ,-2 ,5],[2 ,8 ,7]]
    print("matrix: ", Matrix(mat).inverse())
    print("numpy: ",  np.linalg.inv(np.array(mat)))