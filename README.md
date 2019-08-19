# PySTRUMPACK
   UnderConstruction. Please visit us a few days later. 

# News
  2019/07/23: C-interface SWIG wrapper works in serial mode (tested with Python3.7)
     
# Installation:
##  Prerequisite:

mpi compilers
STRUMPACK installed as a shared library

## Install
     $ export SCALAPACKLINK="-L...."  ### to specify link to scalapack
     $ CC=mpicc CXX=mpicxx python setup.py instal

If include/library files are not in the standard path, you may need to
define enviromental variable. See more detail in Install.txt

## Usage

STRUMPACK.`<PREFIX>`StrumpackSolver where "S", "D", "C", "Z" corresponds to
precision of float32, float64, complex64, complex128, respectively.
     

     from scipy.sparse import lil_matrix
     from STRUMPACK import *
     
     size = 10
     dtype = np.float64
     A = lil_matrix((10, 10),  dtype=dtype)
     
     # fill matrix in somewhy....
     for k in range(size):
         A[k, k] = 2
         if k > 0: A[k, k-1] = 1
     A = A.tocsr()
     b = np.ones(N, dtype=dtype)
     x = np.zeros(N, dtype=dtype)

     spss = SStrumpackSolver()
     spss.set_csr_matrix(A)
     spss.solve(b, x, 0)
     
     
 STRUMPACK.`<PREFIX>`StrumpackSolver has methods to access functions defined in STRUMPACK
 C interface (StrumpackSparseSolver.hpp). For example, 
     
     from STRUMPACK import *
     spss = SStrumpackSolver()
     spss.set_verbose(1)
     spss.set_reordering_method(STRUMPACK_GEOMETRIC)
    
  set verbose mode and reordering method. 
     
