from MatrixModule import Matrix, Vector
import numpy as np

# Drivers code
if __name__ == "__main__":
	mat = [[6, 1 ,1],[4 ,-2 ,5],[2 ,8 ,7]]
	print("matrix: ", Matrix(mat).determinant())
	print("numpy: ", round( np.linalg.det(mat)))
	mat = [[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 4, -3], [1, 0, 5, 0]]
	print("matrix: ", Matrix(mat).determinant())
	print("numpy: ", round( np.linalg.det(mat)))
	mat = [[2., 0., 0.],[0., 2., 0.],[0., 0., 2.]]
	print("matrix: ", Matrix(mat).determinant())
	print("numpy: ", round( np.linalg.det(mat)))
	mat = [[8., 5., -2.],[4., 7., 20.],[7., 6., 1.]]
	print("matrix: ", Matrix(mat).determinant())
	print("numpy: ", round( np.linalg.det(mat)))
	mat = [[ 8., 5., -2., 4.],[ 4., 2.5, 20., 4.],[ 8., 5., 1., 4.],[28., -4., 17., 1.]]
	print("matrix: ", Matrix(mat).determinant())
	print("numpy: ", round( np.linalg.det(mat)))
	mat = [[1,4,7],[10,0,3],[3,5,20]]
	print("matrix: ", Matrix(mat).determinant())
	print("numpy: ", round( np.linalg.det(mat)))

