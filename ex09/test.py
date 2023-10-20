from MatrixModule import Matrix

if __name__=="__main__":
    m = Matrix([[1, 0], [0, 1]])
    print(m.T())
    m = Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]])
    print(m.T())
    m = Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]])
    print(m.T())