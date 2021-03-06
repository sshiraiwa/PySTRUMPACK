%module(package="STRUMPACK") StrumpackSparseSolver
%{
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <cmath>    
#include <complex> 
#include "numpy/arrayobject.h"
#include "StrumpackSparseSolver.h"
#include "StrumpackConfig.hpp"
%}

%init %{
import_array();
%}

%include mpi4py/mpi4py.i
%mpi4py_typemap(Comm, MPI_Comm);

/* these two methods are declared but not implemented anywhere in STRUMPACK??? */
%ignore  STRUMPACK_get_gmres_restart;
%ignore  use_HSS;


%inline %{
class StrumpackSolverBase
{
 protected:
  STRUMPACK_SparseSolver spss;
 public:

  STRUMPACK_RETURN_CODE factor(void){return STRUMPACK_factor(spss);}
  STRUMPACK_RETURN_CODE reorder(void){return STRUMPACK_reorder(spss);}
  STRUMPACK_RETURN_CODE reorder_regular(int nx, int ny, int nz){return STRUMPACK_reorder_regular(spss, nx, ny, nz);}

  void set_from_options(void){return STRUMPACK_set_from_options(spss);}
  //void move_to_gpu(void){return STRUMPACK_move_to_gpu(spss);}
  //void remove_from_gpu(void){return STRUMPACK_remove_from_gpu(spss);}
  //void delete_factors(void){return STRUMPACK_delete_factors(spss);}
  
  void set_verbose(int v){STRUMPACK_set_verbose(spss, v);}
  void set_maxit(int  maxit){STRUMPACK_set_maxit(spss, maxit);}
  void set_gmres_restart(int m){STRUMPACK_set_gmres_restart(spss, m);}
  void set_rel_tol(double tol){STRUMPACK_set_rel_tol(spss, tol);}
  void set_abs_tol(double tol){STRUMPACK_set_abs_tol(spss, tol);}
  void set_nd_param(int nd_param){STRUMPACK_set_nd_param(spss, nd_param);}
  void set_reordering_method(STRUMPACK_REORDERING_STRATEGY m){STRUMPACK_set_reordering_method(spss, m);}
  void set_GramSchmidt_type(STRUMPACK_GRAM_SCHMIDT_TYPE t){STRUMPACK_set_GramSchmidt_type(spss, t);}
  void set_matching(STRUMPACK_MATCHING_JOB job){STRUMPACK_set_matching(spss, job);}
  void set_Krylov_solver(STRUMPACK_KRYLOV_SOLVER solver_type){STRUMPACK_set_Krylov_solver(spss, solver_type);}
  void enable_gpu(){STRUMPACK_enable_gpu(spss);}
  void disable_gpu(){STRUMPACK_disable_gpu(spss);}
  void set_compression(STRUMPACK_COMPRESSION_TYPE t){STRUMPACK_set_compression(spss, t);}
  void set_compression_min_sep_size(int size){STRUMPACK_set_compression_min_sep_size(spss, size);}
  void set_compression_min_front_size(int size){STRUMPACK_set_compression_min_front_size(spss, size);}
  void set_compression_leaf_size(int size){STRUMPACK_set_compression_leaf_size(spss, size);}
  void set_compression_rel_tol(double rctol){STRUMPACK_set_compression_rel_tol(spss, rctol);}
  void set_compression_abs_tol(double actol){STRUMPACK_set_compression_abs_tol(spss, actol);}
  void set_compression_butterfly_levels(int l){STRUMPACK_set_compression_butterfly_levels(spss, l);}
  
  int  get_verbose(void){return STRUMPACK_verbose(spss);}
  int  get_maxit(void){return STRUMPACK_maxit(spss);}
  //int gmres_restart(void){return STRUMPACK_get_gmres_restart(spss);}

  double get_rel_tol(void){return STRUMPACK_rel_tol(spss);}
  double get_abs_tol(void){return STRUMPACK_abs_tol(spss);}
  int get_nd_param(void){return STRUMPACK_nd_param(spss);}
  STRUMPACK_REORDERING_STRATEGY reordering_method(void){return STRUMPACK_reordering_method(spss);}
  STRUMPACK_GRAM_SCHMIDT_TYPE GramSchmidt_type(void){return STRUMPACK_GramSchmidt_type(spss);}
  STRUMPACK_MATCHING_JOB matching(void){return STRUMPACK_matching(spss);}
  STRUMPACK_KRYLOV_SOLVER Krylov_solver(void){return STRUMPACK_Krylov_solver(spss);}
  //bool use_gpu(void){return bool(STRUMPACK_use_gpu(spss));}
  STRUMPACK_COMPRESSION_TYPE compression(void){return STRUMPACK_compression(spss);}
  int compression_min_sep_size(void){return STRUMPACK_compression_min_sep_size(spss);}
  int compression_min_front_size(void){return STRUMPACK_compression_min_front_size(spss);}
  int compression_leaf_size(void){return STRUMPACK_compression_leaf_size(spss);}
  double compression_rel_tol(void){return STRUMPACK_compression_rel_tol(spss);}
  double compression_abs_tol(void){return STRUMPACK_compression_abs_tol(spss);}
  int compression_butterfly_levels(void){return STRUMPACK_compression_butterfly_levels(spss);}

  int its(void){return STRUMPACK_its(spss);}
  int rank(void){return STRUMPACK_rank(spss);}
  long factor_nonzeros(void){return STRUMPACK_factor_nonzeros(spss);}
  long factor_memory(void){return STRUMPACK_factor_memory(spss);}

  /*** deprecated ***/
  // void set_mc64job(int job){STRUMPACK_set_mc64job(spss, job);}
  // void enable_HSS(void){STRUMPACK_enable_HSS(spss);}
  // void disable_HSS(void){STRUMPACK_disable_HSS(spss);}
  // void set_HSS_min_front_size(int size){STRUMPACK_set_HSS_min_front_size(spss, size);}
  // void set_HSS_min_sep_size(int size){STRUMPACK_set_HSS_min_sep_size(spss, size);}
  // void set_HSS_max_rank(int max_rank){STRUMPACK_set_HSS_max_rank(spss, max_rank);}
  // void set_HSS_leaf_size(int leaf_size){STRUMPACK_set_HSS_leaf_size(spss, leaf_size);}
  // void set_HSS_rel_tol(double rctol){STRUMPACK_set_HSS_rel_tol(spss, rctol);}
  // void set_HSS_abs_tol(double actol){STRUMPACK_set_HSS_abs_tol(spss, actol);}  
  
};
%}

%import "common_interface/pointer_array.i"

%define MakeSolver(PREFIX, TYPE, TYPE_C)

%exception PREFIX##StrumpackSolver {
  try {
     $action
  } catch (const char* msg) {
     PyErr_SetString(PyExc_MemoryError, msg);
     return NULL;
  }
}

%inline %{
class PREFIX##StrumpackSolver : public StrumpackSolverBase
{
 private:
    char ** argv = NULL;
    int argc;
    bool success = false;
 public:
    PREFIX##StrumpackSolver(PyObject *options, bool verbose){
      success = proc_options(options);
      STRUMPACK_init_mt(&spss, TYPE, STRUMPACK_MT, argc, argv, verbose);
      //STRUMPACK_set_from_options(spss);
    }

    PREFIX##StrumpackSolver(MPI_Comm comm, PyObject *options, bool verbose){
      success = proc_options(options);
      STRUMPACK_init(&spss, comm, TYPE, STRUMPACK_MPI_DIST, argc, argv, verbose);
      //STRUMPACK_set_from_options(spss);       
    }

    ~PREFIX##StrumpackSolver(){

      if (argv != NULL){
          for (int i = 0; i < argc+1; i++) {
	    if (argv[i] != NULL){
		free(argv[i]);
	    }
	  }
  	 free(argv);
      }

      if (success) {
	STRUMPACK_destroy(&spss);
      }
    }
    bool proc_options(PyObject *options){
       if (!PyList_Check(options)) {
	 throw "Expecting a list";
       }
       argc = PyList_Size(options);	 
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
       return true;
    }
    
    bool isValid(void){return success;}
      
    void set_csr_matrix0(int N, int *row_ptr, int *col_ind, TYPE_C *values, int symmetric_pattern){
       STRUMPACK_set_csr_matrix(spss,  &N, (void*) row_ptr,(void*) col_ind,
				(void*) values, symmetric_pattern);
    }

    void set_distributed_csr_matrix0(int local_rows, const int* row_ptr,
                                     const int* col_ind, const TYPE_C *values,
				     const int* dist,   int symmetric_pattern){

          STRUMPACK_set_distributed_csr_matrix(spss,
					       &local_rows, (const void*) row_ptr,
					       (const void*) col_ind, (const void*) values,
					       (const void*) dist, symmetric_pattern);
     }
    
    STRUMPACK_RETURN_CODE solve(TYPE_C *b, TYPE_C *x, int use_initial_guess){
       return STRUMPACK_solve(spss, (const void*) b, (void*) x, use_initial_guess);
    }  
   };
  
%}
%enddef

MakeSolver(S, STRUMPACK_FLOAT, float)
MakeSolver(D, STRUMPACK_DOUBLE, double)
MakeSolver(C, STRUMPACK_FLOATCOMPLEX, std::complex<float>)
MakeSolver(Z, STRUMPACK_DOUBLECOMPLEX, std::complex<double>)

%pythoncode %{
import numpy as np
def make_set_csr_matrix(mat_type):
 def set_csr_matrix(self, A, symmetric=0, mat_type=mat_type):
  if A.dtype != mat_type:
    assert False, ("input data type is not correct "+str(mat_type) +
                   " is expected. " + str(A.dtype) + " is given")
  
  N = A.shape[0]
  values = A.data
  row_ptr = A.indptr.astype(np.int32, copy=False)
  col_ind = A.indices.astype(np.int32, copy=False)
	      
  return self.set_csr_matrix0(N, row_ptr, col_ind, values, symmetric)
 return set_csr_matrix

def make_set_distributed_csr_matrix(mat_type):
 def set_distributed_csr_matrix(self, A,  symmetric=0, mat_type=mat_type):
  if A.dtype != mat_type:
    assert False, ("input data type is not correct "+str(mat_type) +
                   " is expected. " + str(A.dtype) + " is given")
  
  local_rows = A.shape[0]
  values = A.data
  row_ptr = A.indptr.astype(np.int32, copy=False)
  col_ind = A.indices.astype(np.int32, copy=False)

  from mpi4py import MPI
  dist = np.hstack(([np.int32(0)], np.cumsum(MPI.COMM_WORLD.allgather(local_rows)))).astype(np.int32, copy=False)
  return self.set_distributed_csr_matrix0(local_rows, row_ptr, col_ind, values, dist, symmetric)
 return set_distributed_csr_matrix

SStrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.float32)
DStrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.float64)
CStrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.complex64)      
ZStrumpackSolver.set_csr_matrix = make_set_csr_matrix(np.complex128)
      
SStrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.float32)
DStrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.float64)
CStrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.complex64)      
ZStrumpackSolver.set_distributed_csr_matrix = make_set_distributed_csr_matrix(np.complex128)

%}

// include enum in header
%rename("$ignore", %$isfunction) "";
%rename("$ignore", %$isclass) "";

%include "StrumpackSparseSolver.h"

//%include "StrumpackSparseSolver.h"

  
