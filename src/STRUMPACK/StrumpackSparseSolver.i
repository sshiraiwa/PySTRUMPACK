%module(package="STRUMPACK") StrumpackSparseSolver
%{
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <cmath>    
#include <complex> 
#include "numpy/arrayobject.h"

  //#include "StrumpackConfig.hpp"
  //#include "StrumpackConfig.hpp"
#include "../../strumpack_solve/strumpack_solve.hpp"  
%}

%init %{
import_array();
%}

%include mpi4py/mpi4py.i
%mpi4py_typemap(Comm, MPI_Comm);

/* these two methods are declared but not implemented anywhere in STRUMPACK??? */
//%ignore  STRUMPACK_get_gmres_restart;
//%ignore  use_HSS;

%import "common_interface/pointer_array.i"

%pythoncode %{
import numpy as np
def make_set_csr_matrix(mat_type, int_type):
 '''
  mat_type = np.float32, np.float64, np.complex64, np.complex128
  int_type = np.int32, np.int64
 '''
 def set_csr_matrix(self, A, symmetric=0, mat_type=mat_type):
  if A.dtype != mat_type:
    assert False, ("input data type is not correct "+str(mat_type) +
                   " is expected. " + str(A.dtype) + " is given")
  
  N = A.shape[0]
  values = A.data
  row_ptr = A.indptr.astype(int_type, copy=False)
  col_ind = A.indices.astype(int_type, copy=False)
	      
  return self.set_csr_matrix0(int_type(N), row_ptr, col_ind, values, symmetric)
 return set_csr_matrix

def make_set_distributed_csr_matrix(mat_type, int_type):
 '''
  mat_type = np.float32, np.float64, np.complex64, np.complex128
  int_type = np.int32, np.int64
 '''
 def set_distributed_csr_matrix(self, A,  symmetric=0, mat_type=mat_type):
  if A.dtype != mat_type:
    assert False, ("input data type is not correct "+str(mat_type) +
                   " is expected. " + str(A.dtype) + " is given")
  
  local_rows = int_type(A.shape[0])
  values = A.data
  row_ptr = A.indptr.astype(int_type, copy=False)
  col_ind = A.indices.astype(int_type, copy=False)

  from mpi4py import MPI
  dist = np.hstack(([int_type(0)], np.cumsum(MPI.COMM_WORLD.allgather(local_rows)))).astype(int_type, copy=False)
  return self.set_distributed_csr_matrix0(local_rows, row_ptr, col_ind, values, dist, symmetric)
 return set_distributed_csr_matrix
%}

%include "../../strumpack_solve/strumpack_solve.hpp"


%extend libstrumpack_solve::StrumpackSolver{
  libstrumpack_solve::StrumpackSolver(bool verbose){
    int argc = 0;
    char name[8] = "program";
    char *argv[1];
    argv[0] = &(name[0]);

    libstrumpack_solve::StrumpackSolver<T1, T2, T3> *solver;
    solver = new libstrumpack_solve::StrumpackSolver<T1, T2, T3>(argc, argv, verbose);
    return solver;
  }
  libstrumpack_solve::StrumpackSolver(MPI_Comm comm, bool verbose){
    int argc = 0;
    char name[8] = "program";
    char *argv[1];    
    argv[0] = &(name[0]);
    
    libstrumpack_solve::StrumpackSolver<T1, T2, T3> *solver;
    solver = new libstrumpack_solve::StrumpackSolver<T1, T2, T3>(comm, argc, argv, verbose);
    return solver;
  }
    
  libstrumpack_solve::StrumpackSolver(PyObject *options, bool verbose){
    /*
    This method is wrapped to recived tuple or list to create
    Array object
    */
    libstrumpack_solve::StrumpackSolver<T1, T2, T3> *solver;

    if (!PyList_Check(options)) {
      throw "Expecting a list";
    }
    int argc = PyList_Size(options);
    char **argv;
    argv = (char **) calloc((argc+1), sizeof(char *));
    argv[0] = (char *)malloc(sizeof(char) * 8);
    strcpy(argv[0], "program");
       
    for (int i = 0; i < argc; i++) {
       PyObject *s = PyList_GetItem(options, i);
       if ( ! PyUnicode_Check(s)) {
          throw "List items must be strings";
       }
       PyObject *ss = PyUnicode_AsUTF8String(s);
       argv[i+1] = (char *)malloc(sizeof(char) * strlen(PyString_AsString(ss))+1);
       strcpy(argv[i+1], PyString_AsString(ss));
      //std::cout << argv[i+1] << "\n";
    }
    
    solver = new libstrumpack_solve::StrumpackSolver<T1, T2, T3>(argc, argv, verbose);
    
    //for (int i = 0; i < argc; i++) {
    //  free(argv[i]);
    //}
    //free(argv);
    return solver;
  }

  libstrumpack_solve::StrumpackSolver(MPI_Comm comm, PyObject *options, bool verbose){
    /*
    This method is wrapped to recived tuple or list to create
    Array object
    */
    libstrumpack_solve::StrumpackSolver<T1, T2, T3> *solver;

    if (!PyList_Check(options)) {
      throw "Expecting a list";
    }
    int argc = PyList_Size(options);

    char **argv;
    argv = (char **) calloc((argc+1), sizeof(char *));
    argv[0] = (char *)malloc(sizeof(char) * 8);
    strcpy(argv[0], "program");
       
    for (int i = 0; i < argc; i++) {
       PyObject *s = PyList_GetItem(options, i);
       if ( ! PyUnicode_Check(s)) {
          throw "List items must be strings";
       }
       PyObject *ss = PyUnicode_AsUTF8String(s);
       argv[i+1] = (char *)malloc(sizeof(char) * strlen(PyString_AsString(ss))+1);
       strcpy(argv[i+1], PyString_AsString(ss));
      //std::cout << argv[i+1] << "\n";
    }
     
    solver = new libstrumpack_solve::StrumpackSolver<T1, T2, T3>(comm, argc, argv, verbose);
    
    //for (int i = 0; i < argc; i++) {
    //  free(argv[i]);
    //}
    //free(argv);
    return solver;
  }
}



%template(SStrumpackSolver) libstrumpack_solve::StrumpackSolver<STRUMPACK_FLOAT, float, int32_t>;
%template(DStrumpackSolver) libstrumpack_solve::StrumpackSolver<STRUMPACK_DOUBLE, double, int32_t>;
%template(CStrumpackSolver) libstrumpack_solve::StrumpackSolver<STRUMPACK_FLOATCOMPLEX, std::complex<float>, int32_t>;
%template(ZStrumpackSolver) libstrumpack_solve::StrumpackSolver<STRUMPACK_DOUBLECOMPLEX, std::complex<double>, int32_t>;
%template(S64StrumpackSolver) libstrumpack_solve::StrumpackSolver<STRUMPACK_FLOAT_64, float, int64_t>;
%template(D64StrumpackSolver) libstrumpack_solve::StrumpackSolver<STRUMPACK_DOUBLE_64, double, int64_t>;
%template(C64StrumpackSolver) libstrumpack_solve::StrumpackSolver<STRUMPACK_FLOATCOMPLEX_64, std::complex<float>, int64_t>;
%template(Z64StrumpackSolver) libstrumpack_solve::StrumpackSolver<STRUMPACK_DOUBLECOMPLEX_64, std::complex<double>, int64_t>;



%pythoncode %{
SStrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.float32, np.int32)
DStrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.float64, np.int32)
CStrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.complex64, np.int32)
ZStrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.complex128, np.int32)
      
SStrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.float32, np.int32)
DStrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.float64, np.int32)
CStrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.complex64, np.int32)
ZStrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.complex128, np.int32)

S64StrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.float32, np.int64)
D64StrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.float64, np.int64)
C64StrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.complex64, np.int64)
Z64StrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.complex128, np.int64)
      
S64StrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.float32, np.int64)
D64StrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.float64, np.int64)
C64StrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.complex64, np.int64)
Z64StrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.complex128, np.int64)

%}

// include enum in header
%rename("$ignore", %$isfunction) "";
%rename("$ignore", %$isclass) "";
%include "StrumpackSparseSolver.h"



  
