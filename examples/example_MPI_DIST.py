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

def gather_vector(data, root=0):
    '''
    gather vector to root node. 
    B: Vector to be collected 
    '''
    def mpi_dtype(data):
        if data.dtype == np.float32:
           return MPI.FLOAT
        elif data.dtype == np.float64:    
           return MPI.DOUBLE
        elif data.dtype == np.complex64:     
           return MPI.COMPLEX
        elif data.dtype == np.complex128:
           return MPI.DOUBLE_COMPLEX
        else:
           assert False, "unknown type"

    mpi_data_type = mpi_dtype(data)

    myid     = MPI.COMM_WORLD.rank
    rcounts = data.shape[0]
    rcounts = MPI.COMM_WORLD.gather(rcounts, root=root)
    cm = np.hstack((0, np.cumsum(rcounts)))
    disps = list(cm[:-1])
    recvdata = None
    senddata = [data, data.shape[0]]

    if myid ==root:
        length =  cm[-1]
        recvbuf = np.empty([length], dtype=data.dtype)
        recvdata = [recvbuf, rcounts, disps, mpi_data_type]
    else:
        recvdata = [None, rcounts, disps, mpi_data_type]
        recvbuf = None

    MPI.COMM_WORLD.Barrier()
    MPI.COMM_WORLD.Gatherv(senddata, recvdata, root=root)
    if myid == root:
        #print 'collected'
        MPI.COMM_WORLD.Barrier()
        return np.array(recvbuf)
    MPI.COMM_WORLD.Barrier()
    return None

def get_partition(m):
    min_nrows  = m // nprc
    extra_rows = m % nprc
    start_row  = min_nrows * myid + (extra_rows if extra_rows < myid else myid)
    end_row    = start_row + min_nrows + (1 if extra_rows > myid else 0)
    nrows   = end_row - start_row

    return start_row, end_row, nrows

from scipy.sparse import csr_matrix, lil_matrix
from STRUMPACK import *
from STRUMPACK.debug import nicePrint

n = 30

if len(sys.argv) > 1:
    if sys.argv[1] == 'D':
        dtype = np.float64
        spss = DStrumpackSolver(MPI.COMM_WORLD, True)                
    elif sys.argv[1] == 'S':
        dtype = np.float32
        spss = SStrumpackSolver(MPI.COMM_WORLD, True)                
    elif sys.argv[1] == 'C':
        dtype = np.complex64
        spss = CStrumpackSolver(MPI.COMM_WORLD, True)
    elif sys.argv[1] == 'Z':        
        dtype = np.complex128
        spss = ZStrumpackSolver(MPI.COMM_WORLD, True)          
    else:
        assert False, "unknown dtype"
        
    if len(sys.argv) > 2:
        n = int(sys.argv[2])
else:
    dtype = np.float32
    spss = SStrumpackSolver(MPI.COMM_WORLD, True)
    
spss.set_verbose(1)
spss.set_reordering_method(STRUMPACK_GEOMETRIC)
    
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


x = gather_vector(x, root=0)

if myid == 0:
    x = x.reshape((n, n))
    import matplotlib.pyplot as plt
    import matplotlib.tri as tri

    fig1, ax1 = plt.subplots()
    ax1.set_aspect('equal')
    im = ax1.imshow(x)
    fig1.colorbar(im)
    plt.show()

