from MatrixModule import Matrix, Vector

if __name__=="__main__":
    m = Matrix([[1, 0], [0, 1]])
    v = Vector([[4, 2]])
    print(m * v)

    m = Matrix([[2, 0], [0, 2]])
    print(m * v)

    m = Matrix([[2, -2], [-2, 2]])
    print(m * v)

    m = Matrix([[1, 0], [0, 1]])
    print(m * m)

    m2 = Matrix([[2, 1], [4, 2]])
    print(m * m2)

    m = Matrix([[3, -5], [6, 8]])
    print(m * m2)