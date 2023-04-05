'''
forked from https://github.com/JoonyoungYi/MCCO-numpy 
'''
# Import packages
import cvxpy as cp
import numpy as np

def _cp_solver(M, omega):
    """
    M is our original (square) matrix
    Omega is our set
    """
    r, c = M.shape
    W1 = cp.Variable((r,r))
    X = cp.variable((r,c))
    # X.T = (c,r)
    W2 = cp.Variable((c,c))

    # F = cp.vstack((cp.hstack((W1,X)),cp.hstack((X.T, W2))))
    objective = cp.Minimize(cp.trace(W1)+cp.trace(W2))
    constraints = [cp.vstack((cp.hstack((W1,X)),cp.hstack((X.T, W2)))) >> 0]
    for i,j in omega:
        constraints.append(X[i, j] == M[i, j]) 
    prob = cp.Problem(objective, constraints)
    prob.solve()

    # Print result.
    print("The optimal value is", prob.value)
    print("A solution X is")
    print(X.value)

    return X.value

def _generate_omega(r, c, m):
    """ 
    sample m data points from (r x c) matrix
    """
    return np.random.sample(np.array([(i, j) for i in range(r) for j in range(c)]), m)


def mask_image(image, m):
    """ 
    blurs and image
    """
    r,c = image.shape
    omega = _generate_omega(r,c, m)

    # TODO : simplify?
    mask = np.zeros((r,c ))
    for i, j in omega:
        mask[i, j] = 1
    return mask

def mc_solver(image, m=None):
    '''
    takes in an (masked) image 
    and m = size of omega
    '''
    if m is None:
        # TODO: change this to be theoretical value of good omega
        m = 0
    r,c = image.shape
    omega = _generate_omega(r,c, m)
    return _cp_solver(image, omega)