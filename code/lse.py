import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """

  # slice the input matrices to include just the first 8 points 
  # X1 = X1[0:8,:] # 8x3 matrix
  # X2 = X2[0:8,:] # 8x3 matrix

  X1 = np.array(X1, dtype = np.float32)
  X2 = np.array(X2, dtype = np.float32)

  # compute the A matrix by multiplying the columns of X1 individually with X2, then stacking them
  c1 = (X2.T * X1[:,0]).T
  c2 = (X2.T * X1[:,1]).T
  c3 = (X2.T * X1[:,2]).T

  A = np.column_stack((c1, c2, c3)) # 8x9 matrix
  
  # perform SVD on A
  [U, S, Vt] = np.linalg.svd(A)

  # the last row of V Transpose will be F
  F = Vt[8,:]

  # slice F to get the 3x3 matrix form of E'
  E_nullspace = np.column_stack((F[:3], F[3:6], F[6:9])) # 3x3 matrix from 9x1 matrix

  # perform SVD on E'
  [U, S, Vt] = np.linalg.svd(E_nullspace)

  # compute E = U @ Diag Matrix @ Vt
  E = U @ np.diag([1, 1, 0]) @ Vt

  """ END YOUR CODE
  """
  return E

X1 = np.array([[1, 2, 1], [4, 5, 1], [7, 8, 1], [10, 11, 1], [14, 15, 1], [17, 36, 1], [20, 21, 1], [23, 24, 1]])
X2 = np.array([[5, 4, 1], [6, 8, 1], [11, 13, 1], [17, 18, 1], [21, 9, 1], [14, 2, 1], [24, 3, 1],[19,28,1]])

least_squares_estimation(X1, X2)