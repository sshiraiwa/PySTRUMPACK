'''

   test program to compare 5x5 matrix inverse with scipy

   mpirun -np 2 python -u test_MPI_Dist.py

'''
from __future__ import print_function

import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from mpi4py import MPI

myid = MPI.COMM_WORLD.rank
nprc = MPI.COMM_WORLD.size

from STRUMPACK import *
from STRUMPACK.debug import nicePrint

dtype = np.float32

# prepare test matrix
size = 5
A = lil_matrix((size, size),  dtype=dtype)
for k in range(size):
    A[k, k] = 2
    if k > 0: A[k, k-1] = 1
    
if myid == 0:    
    A1 = A[:2, :]
else:
    A1 = A[2:, :]
       
A1 = A1.tocsr()
N  = A.shape[0]

from scipy.sparse.linalg import inv

def solve_ln(spss, A, A1, b, x, dtype):
   A1 = A1.astype(dtype)

   b = b.astype(dtype)
   x = x.astype(dtype)

   if np.iscomplexobj(A1):
       A1 = A1 + 0.1*1j*A1
       A = A + 0.1*1j*A
       b = b - 0.1*1j*b

   spss.set_distributed_csr_matrix(A1)
   spss.solve(b, x, 0)
   nicePrint(list(x))
   if myid == 0: print(np.array(np.dot(inv(A.tocsc()).todense(), b)).flatten())

b = np.ones(N, dtype=dtype)
x = np.zeros(N, dtype=dtype)

if myid==0: print("float")
spss = SStrumpackSolver(MPI.COMM_WORLD)
solve_ln(spss, A, A1, b, x, np.float32)

print("double")
spss = DStrumpackSolver(MPI.COMM_WORLD)
solve_ln(spss, A, A1, b, x, np.float64)

print("complex")
spss = CStrumpackSolver(MPI.COMM_WORLD)
solve_ln(spss, A, A1, b, x, np.complex64)

print("zcomplex")
spss = ZStrumpackSolver(MPI.COMM_WORLD)
solve_ln(spss, A, A1, b, x, np.complex128)
