from MatrixModule import Matrix

if __name__=="__main__":
    m = [[1,0,0], [0,1,0], [0,0,1]]
    print(f"first test:\n{Matrix(m).row_echelon()}")
    m = [[1,2], [3,4]]
    print(f"\nsecond test:\n{Matrix(m).row_echelon()}")
    m = [[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]]
    print(f"\nthird test:\n{Matrix(m).row_echelon()}")
