from MatrixModule import Vector
from cross_product import cross_product

if __name__=="__main__":
    print(cross_product(Vector([[0,0,1]]),Vector([[1,0,0]])))
    print(cross_product(Vector([[1,2,3]]),Vector([[4,5,6]])))
    print(cross_product(Vector([[4,2,-3]]),Vector([[-2,-5,16]])))