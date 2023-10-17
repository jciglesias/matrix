from MatrixModule import Vector
from linear_combination import linear_combination

if __name__=="__main__":
    v1 = Vector([[1,0,0]])
    v2 = Vector([[0,1,0]])
    v3 = Vector([[0,0,1]])
    v4 = Vector([[1,2,3]])
    v5 = Vector([[0,10,-100]])
    e1 = [10,-2,0.5]
    e2 = [10,-2]
    print(f"\nlinear combination:\n{[v1,v2,v3]}, {e1} = {linear_combination([v1,v2,v3], e1)}")
    print(f"{[v4,v5]}, {e2} = {linear_combination([v4,v5], e2)}")
