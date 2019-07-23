from __future__ import print_function

import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from STRUMPACK import *

A = csr_matrix([[1,1,0,],[0, 2,1], [0, 1, 0]], dtype=np.float)
size = 5
# prepare test matrix and rhs
A = lil_matrix((size, size), dtype = np.float64)
for k in range(size):
    A[k, k] = 2
    if k > 0: A[k, k-1] = 1
A = A.tocsr()
print(A.todense())
s = Sp()
s.set_csr_matrix(A)
print(s.solve(np.array(np.zeros(size)+1, dtype=float)))

