from MatrixModule import Matrix, Vector

if __name__=="__main__":
    m = Matrix([[1],[2]])
    v = Vector([[1,2,3]])
    print(type(m))
    print(type(v))
    print(m + m)
    print(v * v)