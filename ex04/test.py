from MatrixModule import Vector

if __name__=="__main__":
    v = Vector([[1,2,3]])
    print(v.norm())
    print(v.norm_1())
    print(v.norm_inf())
