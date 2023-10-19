from cosine import angle_cos
from MatrixModule import Vector

if __name__=="__main__":
    v = Vector([[1,0]])
    u = Vector([[0,1]])
    print(angle_cos(v, v))
    print(angle_cos(v,u))
    v = Vector([[-1,1]])
    u = Vector([[1,-1]])
    print(angle_cos(v,u))
    v = Vector([[2,1]])
    u = Vector([[4,2]])
    print(angle_cos(v,u))
    v = Vector([[1,2,3]])
    u = Vector([[4,5,6]])
    print(angle_cos(v, u))