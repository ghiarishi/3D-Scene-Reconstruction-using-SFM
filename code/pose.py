import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """
  # SVD on E
  [U, S, Vt] = np.linalg.svd(E)

  # Calculate translation matrices, as the last column of U (and minus that)
  T = U[:, 2]
  T_minus = -T

  # The z roatation matrix for Pi/2
  Rz1 = np.array([[0, -1, 0], 
        [1, 0, 0], 
        [0, 0, 1]])
  
  # The z roatation matrix for -Pi/2
  Rz2 = np.array([[0, 1, 0], 
         [-1, 0, 0], 
         [0, 0, 1]])

  # Calculate the rotation matrices
  R1 = U @ Rz1.T @ Vt

  R2 = U @ Rz2.T @ Vt

  R3 = U @ Rz1.T @ Vt

  R4 = U @ Rz2.T @ Vt

  # put all values in a dictionary
  transform_candidates = [{'T':T,'R':R1}, {'T':T,'R':R2}, {'T':T_minus,'R':R3}, {'T':T_minus,'R':R4}]

  """ END YOUR CODE
  """
  return transform_candidates