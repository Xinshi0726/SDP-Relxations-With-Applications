# MLOPT U9 - SDP Relaxations with Applications

## Background

Linear programming is a common constrained optimization problems with uses in several fields including math, computer science, economics, and buisness.
Seveal real world problems can be modelled as a set of linear contraints, making linear programming a ubiquitous construct.
We are able to find solutions to a linear program in polynomial time.

Semidefinite programming (SDP) expands on the ideas used within linear programming and generalizes them so that they can be applied to more problems, including nonlinear optimization problems. SDPs are widely used for combinatorial optimization - a class of problems that are of abundance in network science.

The notorious NP-Hard problems can be approximated quite well with SDPs.
The flexibility and speed of finding solutions of what can be represented as a SDP problem is what gives it its power. 

We show how to relax the [Traveling Salesman (Hamilton Cycle)](https://github.com/Xinshi0726/SDP-Relxations-With-Applications/tree/main/TSPSolver) and [Max Cut](https://github.com/Xinshi0726/SDP-Relxations-With-Applications/tree/main/max-cut), both NP-Complete Problem to a SDP as well as [matrix completion](https://github.com/Xinshi0726/SDP-Relxations-With-Applications/tree/main/matrix-completetion). 


## Experiments

We use the covex optimization solver [CVXPY](https://www.cvxpy.org/) to solve SDP. 

It is recommened to set up a virtual environmnet (conda or venu)

Here are commands set up a new conda env and install necessary packages
```
conda create  --n <SDP> python=3.10.10  
conda activate <SDP>  
conda install -c conda-forge cvxpy  
conda install pytorch torchvision -c pytorch 
```

[CVXPY](https://www.cvxpy.org/install/) is a convex py solver. Installing it will automatically install the following dependencies
- Python >= 3.7
- OSQP >= 0.4.1
- ECOS >= 2
- SCS >= 1.1.6
- NumPy >= 1.15
- SciPy >= 1.1.0
