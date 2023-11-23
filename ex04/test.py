from MatrixModule import Vector

if __name__=="__main__":
    v = Vector([[0,0,0]])
    print(v.norm_1(),v.norm(),v.norm_inf())
    v = Vector([[1,2,3]])
    print(v.norm_1(),v.norm(),v.norm_inf())
    v = Vector([[-1,-2]])
    print(v.norm_1(),v.norm(),v.norm_inf())
