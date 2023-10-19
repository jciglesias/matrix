from MatrixModule import Vector
from cross_product import cross_product

if __name__=="__main__":
    v = Vector([[0,0,1]])
    v2 = Vector([[1,0,0]])
    print(cross_product(v,v2))
    print(cross_product(Vector([[1,2,3]]),Vector([[4,5,6]])))
    print(cross_product(Vector([[4,2,-3]]),Vector([[-2,-5,16]])))