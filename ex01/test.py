from MatrixModule import Matrix, Vector
from linear_combination import linear_combination

if __name__=="__main__":
    v1 = Vector([[1,0,0]])
    v2 = Vector([[0,1,0]])
    v3 = Vector([[0,0,1]])
    # m = Matrix([v1,v2,v3])
    # m2 = Matrix([[1,2,3],[0,10,-100]])
    e1 = [10,-2,0.5]
    e2 = [10,-2]
    print(f"\nlinear combination:\n{[v1,v2,v3]}, {e1} = {linear_combination([v1,v2,v3], e1)}")
    # print(f"m.shape: {m2.shape}, v.shape: {e2.shape}")
    # print(f"{m2} * {e2} = {m2 * e2}")
