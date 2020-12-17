'''

   test program to compare 5x5 matrix inverse with scipy

'''
from __future__ import print_function

import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from STRUMPACK import *

dtype = np.float32

# prepare test matrix
size = 5
A = lil_matrix((size, size),  dtype=dtype)
for k in range(size):
    A[k, k] = 2
    if k > 0: A[k, k-1] = 1
A = A.tocsr()
N = A.shape[0]

from scipy.sparse.linalg import inv

def solve_ln(spss, A, b, x, dtype):
   spss.set_verbose(1)    
   A = A.astype(dtype)

   b = b.astype(dtype)
   x = x.astype(dtype)

   if np.iscomplexobj(A):
       A = A + 0.1*1j*A
       b = b - 0.1*1j*b

   spss.set_csr_matrix(A)
   spss.solve(b, x, 0)
   #print(list(x))
   #print(np.array(np.dot(inv(A.tocsc()).todense(), b)).flatten())
   err = (np.array(np.dot(inv(A.tocsc()).todense(), b)).flatten() - x)
   th = 1e-7 if dtype==np.float32 or dtype==np.complex64 else 1e-16
       
   print("x: ", list(x))
   print("x (ref):", list(np.array(np.dot(inv(A.tocsc()).todense(), b)).flatten()))
   print("err:", np.abs(err))
       
   if np.max(np.abs(err)) > th:
       assert False, "error is too large"
   else:
       print("max err:", np.max(np.abs(err)))
       

b = np.ones(N, dtype=dtype)
x = np.zeros(N, dtype=dtype)

print("float")
spss = SStrumpackSolver()
solve_ln(spss, A, b, x, np.float32)

print("double")
spss = DStrumpackSolver()
solve_ln(spss, A, b, x, np.float64)

print("complex")
spss = CStrumpackSolver()
solve_ln(spss, A, b, x, np.complex64)

print("zcomplex")
spss = ZStrumpackSolver()
solve_ln(spss, A, b, x, np.complex128)
