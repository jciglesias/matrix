from MatrixModule import Matrix, Vector

if __name__=="__main__":
    m = Matrix([[1],[2]])
    m2 = Matrix([[1,2]])
    v = Vector([[1,2,3]])
    print(type(m))
    print(type(v))
    print(f"\naddition:\n{m} + {m} = {m + m}")
    print(f"{v} + {v} = {v + v}")
    print(f"\nsubstraction:\n{m} - {m} = {m - m}")
    print(f"{v} - {v} = {v - v}")
    print(f"\nscalar:\n{m} * 4 = {m * 4}")
    print(f"{v} * 4 = {v * 4}")