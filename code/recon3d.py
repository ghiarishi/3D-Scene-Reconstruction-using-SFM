import numpy as np

def reconstruct3D(transform_candidates, calibrated_1, calibrated_2):
  """This functions selects (T,R) among the 4 candidates transform_candidates
  such that all triangulated points are in front of both cameras.
  """

  best_num_front = -1
  best_candidate = None
  best_lambdas = None
  for candidate in transform_candidates:
    R = candidate['R']
    T = candidate['T']

    lambdas = np.zeros((2, calibrated_1.shape[0]))
    """ YOUR CODE HERE
    """
    # calibrated 1 and 2 are both nx3 matrices

    # iterate through each x1, x2 pair, and calculate lambdas for them
    i = 0
    for x1, x2 in zip(calibrated_1, calibrated_2):

      x1 = x1.reshape(3,1)
      x2 = x2.reshape(3,1)

      A = np.column_stack((x2, -(R @ x1)))
      B = T
      
      # solving for lambda 1, 2 through pseudo inverse of Ax = B
      soln = (np.linalg.inv(A.T @ A) @ A.T @ B).reshape(2,1)

      lambdas[0,i] = soln[0]
      lambdas[1,i] = soln[1]

      i += 1

    """ END YOUR CODE
    """
    num_front = np.sum(np.logical_and(lambdas[0]>0, lambdas[1]>0))

    if num_front > best_num_front:
      best_num_front = num_front
      best_candidate = candidate
      best_lambdas = lambdas
      print("best", num_front, best_lambdas[0].shape)
    else:
      print("not best", num_front)


  P1 = best_lambdas[1].reshape(-1, 1) * calibrated_1
  P2 = best_lambdas[0].reshape(-1, 1) * calibrated_2
  T = best_candidate['T']
  R = best_candidate['R']
  return P1, P2, T, R