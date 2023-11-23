from MatrixModule import Matrix, Vector
import numpy as np

if __name__=="__main__":
    m = [[1., 2.],[3., 4.]]
    m2 = [[7., 4.],[-2., 2.]]
    v = [[2., 3.]]
    v2 = [[5., 7.]]
    print(type(Matrix(m)))
    print(type(Vector(v)))
    print(f"\n<--addition-->\n")
    mod = Matrix(m) + Matrix(m2)
    nump = np.array(m) + np.array(m2)
    dif = True
    for row in range(nump.shape[0]):
        for column in range(nump.shape[1]):
            if nump[row][column] != mod[row][column]:
                dif = False
    print("Matrix:", dif)
    mod = Vector(v) + Vector(v2)
    nump = np.array(v) + np.array(v2)
    dif = True
    for row in range(nump.shape[0]):
        for column in range(nump.shape[1]):
            if nump[row][column] != mod[row][column]:
                dif = False
    print("vector:", dif)
    print(f"\n<--substraction-->\n")
    mod = Matrix(m) - Matrix(m2)
    nump = np.array(m) - np.array(m2)
    dif = True
    for row in range(nump.shape[0]):
        for column in range(nump.shape[1]):
            if nump[row][column] != mod[row][column]:
                dif = False
    print("Matrix:", dif)
    mod = Vector(v) - Vector(v2)
    nump = np.array(v) - np.array(v2)
    dif = True
    for row in range(nump.shape[0]):
        for column in range(nump.shape[1]):
            if nump[row][column] != mod[row][column]:
                dif = False
    print("vector:", dif)
    print(f"\n<--scalar-->\n")
    mod = Matrix(m) * 2
    nump = np.array(m) * 2
    dif = True
    for row in range(nump.shape[0]):
        for column in range(nump.shape[1]):
            if nump[row][column] != mod[row][column]:
                dif = False
    print("Matrix:", dif)
    mod = Vector(v) * 2
    nump = np.array(v) * 2
    dif = True
    for row in range(nump.shape[0]):
        for column in range(nump.shape[1]):
            if nump[row][column] != mod[row][column]:
                dif = False
    print("vector:", dif)
