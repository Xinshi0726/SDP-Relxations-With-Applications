# Matrix Completetion
It is recommened to set up a virtual environmnet (conda or venu)

Here are commands set up a new conda env and install necessary packages
```
conda create  --n <SDP_Matrix_Completetion> python=3.10.10  
conda activate <SDP_Matrix_Completetion>  
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


**mc_tools.py** contains operations to mask an image and approximate a partial image.

**MC.ipynb** contains experimential results using **mc_tools.py** 

Run `conda deactivate` to deactivate the environment

