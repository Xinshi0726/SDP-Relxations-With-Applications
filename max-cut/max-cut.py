#!/usr/bin/env python3
# Import packages.
import cvxpy as cp
import numpy as np
from scipy.spatial.distance import cdist
# import matplotlib.pyplot as plt


# A * B = trace( A.T @ B )
#
# Generate a list of n points and their corresponding adjacency matrix
n = 20
points = np.random.rand(n, 2)
adj_matrix = cdist(points, points)
W = adj_matrix

# plt.scatter(points[:, 0], points[:, 1])
# plt.show()

# Define and solve the CVXPY problem.
# Create a symmetric matrix variable.
X = cp.Variable((n,n), symmetric=True)
# The operator >> denotes matrix inequality.
constraints = [X >> 0] # PSD
constraints += [
    X[i, i] == 1 for i in range(n)
]
W_sum = W.sum()

prob = cp.Problem(
    cp.Maximize(
        0.25 * (adj_matrix.sum() - cp.trace(adj_matrix @ X))
    ), constraints)
prob.solve()
# print("The optimal value is", prob.value)
# print("A solution X is")
sol = np.sign(X.value)
set1 = sol[1, :] > 0
set2 = ~set1

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(points[set1, 0], points[set1, 1], color = "blue")
ax.scatter(points[set2, 0], points[set2, 1], color = "orange")
ax.set(xticklabels=[], yticklabels = [])  # remove the tick labels
ax.tick_params(bottom = False, left=False)  # remove the ticks
ax.set_title(f"Max Cut: {int(np.round(prob.value))}")

# or skip the previous two lines and plot df directly
# ax = df.plot(x='radians', y='freq: 1x', figsize=(8, 8), legend=False)

plt.show()
# print(set1)
# print(set2)
# sol[sol > 0] = 0
# sol *= -1

# print(sol)
exit()
