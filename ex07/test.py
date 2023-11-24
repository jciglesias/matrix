from MatrixModule import Matrix, Vector

if __name__=="__main__":
    m = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[2, 1], [4, 2]])

    print(Matrix([[1, 0], [0, 1]]) * Vector([[4, 2]]))

    print("\n", Matrix([[2, 0], [0, 2]]) * Vector([[4, 2]]))

    print("\n", Matrix([[2, -2], [-2, 2]]) * Vector([[4, 2]]))

    print("\n", m * m)

    print("\n", m * m2)

    print("\n", Matrix([[3, -5], [6, 8]]) * m2)