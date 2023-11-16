from ._class import Matrix

def row_echelon(self):
    for i in range(self.shape[0]):
        pivot = abs(self.data[i][i])
        pivot_row = i
        for j in range(i + 1, self.shape[0]):
            if abs(self.data[j][i]) > pivot and pivot != 1:
                pivot = abs(self.data[j][i])
                pivot_row = j
            if pivot_row != i:
                self.data[i], self.data[pivot_row] = self.data[pivot_row], self.data[i]
        for j in range(i + 1, self.shape[0]):
            if self.data[i][i] != 0 :
                factor = self.data[j][i] / self.data[i][i]
            else:
                factor = self.data[j][i] / self.data[0][i]
            for k in range(i, self.shape[1]):
                self.data[j][k] -= factor * self.data[i][k]
    return self

# def gcd(a, b): 
#     if (a == 0): 
#         return b 
#     return gcd(b % a, a) 

# def lcm(a, b):
#     return (a * b) / gcd(a, b) 

# def gauss_elimination(A):
#     """
#     Gauss elimination method [By Bottom Science].
  
#     A - the coefficient matrix (an n x n matrix)
#     b - the right-hand side column vector (an n x 1 matrix)
  
#     """
  
#     n = len(A)
  
#     # Perform Gauss elimination
#     for i in range(n):
#         # Find the pivot element
#         pivot = abs(A[i][i])
#         pivot_row = i
#         for j in range(i+1, n):
#             if abs(A[j][i]) > pivot:
#               pivot = abs(A[j][i])
#               pivot_row = j
  
#         # Swap the pivot row with the current row (if necessary)
#         if pivot_row != i:
#             A[i], A[pivot_row] = A[pivot_row], A[i]
  
#         # Eliminate the current variable from the other equations
#         for j in range(i+1, n):
#             factor = A[j][i] / A[i][i]
#             for k in range(i, n):
#                 A[j][k] -= factor * A[i][k]