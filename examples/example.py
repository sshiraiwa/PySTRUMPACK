'''

  example.py

  python example.py "S"    ==  sexample.c
  python example.py "D"    ==  dexample.c
  python example.py "C"    ==  cexample.c
  python example.py "Z"    ==  zexample.c

'''
from __future__ import print_function

import sys
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from STRUMPACK import *

n = 30


if len(sys.argv) > 1:
    if sys.argv[1] == 'D':
        dtype = np.float64
        spss = DStrumpackSolver()                
    elif sys.argv[1] == 'S':
        dtype = np.float32
        spss = SStrumpackSolver()        
    elif sys.argv[1] == 'C':
        dtype = np.complex64
        spss = CStrumpackSolver()                
    elif sys.argv[1] == 'Z':        
        dtype = np.complex128
        spss = ZStrumpackSolver()                        
    else:
        assert False, "unknown dtype"
        
    if len(sys.argv) > 2:
        n = int(sys.argv[2])
else:
    dtype = np.float32
    spss = SStrumpackSolver(True)
    
spss.set_verbose(1)
spss.set_reordering_method(STRUMPACK_GEOMETRIC)

N = n*n
m = lil_matrix((N,N), dtype = dtype)
nnz = 0

for row in range(n):
    for col in range(n):
        ind =  col + n*row
        m[ind, ind] = 4.0
        if col > 0:   m[ind, ind-1] = -1
        if col < n-1: m[ind, ind+1] = -1
        if row > 0:   m[ind, ind-n] = -1
        if row < n-1: m[ind, ind+n] = -1

A = m.tocsr()        
    
b = np.ones(N, dtype=dtype)
x = np.zeros(N, dtype=dtype)

spss.set_csr_matrix(A)
spss.reorder_regular(n, n, 1)
spss.solve(b, x, 0)

x = x.reshape((n, n))

import matplotlib.pyplot as plt
import matplotlib.tri as tri

fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
im = ax1.imshow(x)
fig1.colorbar(im)
plt.show()
