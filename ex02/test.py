from MatrixModule import Matrix, Vector
from lerp import lerp

if __name__=="__main__":
    print(lerp(0,1,0))
    print(lerp(0,1,1))
    print(lerp(0,1,0.5))
    print(lerp(21,42,0.3))
    v = Vector([[2,1]])
    v2 = Vector([[4,2]])
    print(lerp(v, v2, 0.3))
    m = Matrix([[2., 1.], [3., 4.]])
    m2 = Matrix([[20.,10.], [30., 40.]])
    print(lerp(m, m2, 0.5))