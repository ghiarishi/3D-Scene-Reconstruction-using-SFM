from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """ YOUR CODE HERE
        """

        # go through the sample indices and add the selected 8 random samples to the lists X1 and X2
        new_X1 = X1[sample_indices] # sample x1s
        new_X2 = X2[sample_indices] # sample x2s

        # find E through LSE
        E = least_squares_estimation(new_X1, new_X2)

        e3_hat = [[0, -1, 0], 
                  [1, 0, 0], 
                  [0, 0, 0]]

        count = 0 # keep count of the number of inliers


        # go through the sample indices and add the selected 8 random samples to the lists X1 and X2
        X1_test = X1[test_indices] # test x1s
        X2_test = X2[test_indices] # test x2s

        inliers_indices = [] # store the indices of the inlier points

        i = 0
        for x1, x2 in zip(X1_test, X2_test):
            dist_1 = ((x2.T @ E @ x1)/np.linalg.norm(e3_hat @ E @ x1))**2
            dist_2 = ((x1.T @ E.T @ x2)/np.linalg.norm(e3_hat @ E.T @ x2))**2
            total_dist = dist_1 + dist_2 # "norm" distance of the points from the E matrix essentially. 

            # if this distance is less than the acceptable error margin, the point is classified as an inlier
            if total_dist < eps: 
                count += 1
                # append the index of the inlier to the list
                inliers_indices.append(test_indices[i])
            i += 1

        # if the new set of points is has more inliers than ever before, then we: 
        if count > best_num_inliers:
            best_num_inliers = count # update the best number of inliers

            # create an array of the sample indices, and the inlier indices
            best_inliers = np.array(inliers_indices, dtype = int) 
            best_inliers = np.append(sample_indices, best_inliers)
            
            # update the best E to the current E
            best_E = E

        """ END YOUR CODE
        """
    return best_E, best_inliers