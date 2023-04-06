"""
Relaxation of Matrix Completion to SDP as described in
Exact Matrix Completion via Convex Optimization 
    by Emmanuel Candès and Benjamin Recht

M does not have to be either square nor symmetric
"""
import cvxpy as cp
import numpy as np
import random

def mc_solver(M, omega):
    """ Given an (low rank) image M and a sampling a points we would like to fix,
        find a low rank matrix to fill in data points that are not fixed

    Parameters
    ----------
    M : 2d-ndarray
        A 2D numpy matrix representing the image
    Omega : ndarray
        sampling of points we have knowledge about

    Returns
    -------
    X.value
        Our image with missing points filled in
    """
    r, c = M.shape
    W1 = cp.Variable((r,r))
    X = cp.Variable((r,c))
    # X.T = (c,r)
    W2 = cp.Variable((c,c))

    objective = cp.Minimize(cp.trace(W1)+cp.trace(W2))
    # The augmented matrix must be positive semidefinite
    constraints = [cp.vstack((cp.hstack((W1,X)),cp.hstack((X.T, W2)))) >> 0]
    # Fix points we are confident about
    constraints.append(X[omega]==M[omega])
    # for i in range(len(omega[0])):
    #     constraints.append(X[omega[0][i], omega[1][i]] == M[omega[0][i], omega[1][i]]) 
    prob = cp.Problem(objective, constraints)
    prob.solve()

    return X.value

def mask_image(image, p=0):
    """ 
    Parameters
    ----------
    image : 2d-ndarray
        A 2D numpy matrix representing the image
    p : float
        the percent of points to remove

    Returns
    -------
    tuple(masked_image, omega)
        where masked_image has specific points zeroed out
        omega is coordinates of the points zeroed out
    """
    r,c = image.shape
    # randomly generate (r x c) numbers from N(0,1), where N is the normal distribution
    mask = np.random.rand(r, c)
    # [0,p] becomes 0. p percent of data is zeroed out
    mask[mask <= p] = 0
    # (p, 1) becomes 1. 1-p percent of data
    mask[mask > p] = 1
    omega = np.where(mask == 1)
    return mask * image, omega