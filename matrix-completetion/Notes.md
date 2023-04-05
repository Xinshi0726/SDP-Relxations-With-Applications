```
https://dl.acm.org/doi/pdf/10.1145/2184319.2184343

there's plenty of code for solvers specifically for matrix completion, e.g. https://github.com/travisbrady/py-soft-impute 
```

Images can be well-represented by low rank matrices (well known fact)
Low rank matrices can be recovered from sparse sampling of their entries (i.e we can grab a subset and recover the iamges)
- Note that this is not true for general low rank matrices,
but feasible for our input. For now, we will assume most of the entries are non-zero. Can we recover "original" matrix given a sampling of it's entries
- To be able to infer other elemenets froma sampling, need a at least one per row and one per column. Let $\omega$ be set of locations in matrix. How large does $n = \omega$ need to be so we have a large probability of recovering the original matrix.
- explain how rank can be approximated with nuclear norm
- norms are convex, and can thus be optimized efficietly via semidefinite programming


each channel carries different sementic paper

Install Instructions
```
python -m venv SDP  
source SDP/bin/activate  
pip install numpy  
pip install cvxpy  
```

```
conda create --name myenv
conda activate myenv
conda install numpy scipt  
conda install -c conda-forge cvxpy
```