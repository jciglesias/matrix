from MatrixModule import Matrix, Vector

if __name__ == "__main__":
	print(Matrix([[1 ,-1],[-1,1]]).determinant())
	print(Matrix([[2., 0., 0.],[0., 2., 0.],[0., 0., 2.]]).determinant())
	print(Matrix([[8., 5., -2.],[4., 7., 20.],[7., 6., 1.]]).determinant())
	print(Matrix([[ 8., 5., -2., 4.],[ 4., 2.5, 20., 4.],[ 8., 5., 1., 4.],[28., -4., 17., 1.]]).determinant())
