# pyhss

## A python package for hierarchically semiseparable matrix representation

Hierarchically semiseparable (HSS) matrix representation is a subclass of hierarchical matrices (H-matrices), which allows fast matrix multiplication, Cholesky decomposition, and other matrix computations. The HSS matrix representation is a hierarchical representation that is based on a recursive row and column partitioning of the matrix. Each k-level HSS representation is associated with k+1 level HSS tree on which all blocks of HSS matrices including the whole matrix can be represented.  This package allows Python user to transform their matrix into HSS matrix representation seamlessly. 

### Install

Install pyhss simply by

```bash
pip install pyhss
```


### Usage

For b = Ax we can implement

```Python
from pyhss import hss
from pyhss import hss_matmul

A = np.random.randn(100, 100)
x = np.random.randn(100, 1)

hss_mat = hss(maxdepth=10).build(A)
b = hss_matmul(A, x)
print(LA.norm(b - np.dot(A, x), 2))
```
