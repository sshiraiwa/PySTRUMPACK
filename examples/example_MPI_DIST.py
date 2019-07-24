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

from mpi4py import MPI

myid = MPI.COMM_WORLD.rank
nprc = MPI.COMM_WORLD.size

from scipy.sparse import csr_matrix, lil_matrix
from STRUMPACK import *
from STRUMPACK.debug import nicePrint

n = 30


if len(sys.argv) > 1:
    if sys.argv[1] == 'D':
        dtype = np.float64
        spss = DStrumpackSolver(MPI.COMM_WORLD)                
    elif sys.argv[1] == 'S':
        dtype = np.float32
        spss = SStrumpackSolver(MPI.COMM_WORLD)                
    elif sys.argv[1] == 'C':
        dtype = np.complex64
        spss = CStrumpackSolver(MPI.COMM_WORLD)
    elif sys.argv[1] == 'Z':        
        dtype = np.complex128
        spss = ZStrumpackSolver(MPI.COMM_WORLD)          
    else:
        assert False, "unknown dtype"
        
    if len(sys.argv) > 2:
        n = int(sys.argv[2])
else:
    dtype = np.float32
    spss = SStrumpackSolver(MPI.COMM_WORLD)
    
spss.set_verbose(1)
spss.set_reordering_method(STRUMPACK_GEOMETRIC)

def get_partition(m):
    min_nrows  = m // nprc
    extra_rows = m % nprc
    start_row  = min_nrows * myid + (extra_rows if extra_rows < myid else myid)
    end_row    = start_row + min_nrows + (1 if extra_rows > myid else 0)
    nrows   = end_row - start_row

    return start_row, end_row, nrows
    
N = n*n
start_row, end_row, nrows = get_partition(N)

m = lil_matrix((nrows,N), dtype = dtype)
nnz = 0

for row in range(n):
    for col in range(n):
        ind =  col + n*row
        ind0 = ind - start_row
        if ind0 < 0: continue
        if ind0 >= nrows: continue        
        m[ind0, ind] = 4.0
        if col > 0:   m[ind0, ind-1] = -1
        if col < n-1: m[ind0, ind+1] = -1
        if row > 0:   m[ind0, ind-n] = -1
        if row < n-1: m[ind0, ind+n] = -1

A = m.tocsr()        
    
b = np.ones(nrows, dtype=dtype)
x = np.zeros(nrows, dtype=dtype)

spss.set_distributed_csr_matrix(A)
spss.reorder_regular(n, n, 1)
spss.solve(b, x, 0)

nicePrint(x[:15])
