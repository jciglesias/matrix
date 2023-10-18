from MatrixModule import Matrix, Vector
from lerp import lerp

if __name__=="__main__":
    print(lerp(10, 20, 0.25))
    v = Vector([[10,10,10]])
    v2 = Vector([[20,20,20]])
    print(lerp(v, v2, 0.25))
    m = Matrix([[10,10],[10,10],[10,10]])
    m2 = Matrix([[20,20],[20,20],[20,20]])
    print(lerp(m, m2, 0.25))