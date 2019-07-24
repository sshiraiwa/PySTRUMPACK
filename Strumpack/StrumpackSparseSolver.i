%module(package="STRUMPACK") StrumpackSparseSolver
%{
#include <stdio.h>
#include <stdlib.h> 
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
  
  void set_verbose(int v){STRUMPACK_set_verbose(spss, v);}
  void set_maxit(int  maxit){STRUMPACK_set_maxit(spss, maxit);}
  void set_gmres_restart(int m){STRUMPACK_set_gmres_restart(spss, m);}
  void set_rel_tol(double tol){STRUMPACK_set_rel_tol(spss, tol);}
  void set_abs_tol(double tol){STRUMPACK_set_abs_tol(spss, tol);}
  void set_nd_param(int nd_param){STRUMPACK_set_nd_param(spss, nd_param);}
  void set_reordering_method(STRUMPACK_REORDERING_STRATEGY m){STRUMPACK_set_reordering_method(spss, m);}
  void set_GramSchmidt_type(STRUMPACK_GRAM_SCHMIDT_TYPE t){STRUMPACK_set_GramSchmidt_type(spss, t);}
  void set_mc64job(int job){STRUMPACK_set_mc64job(spss, job);}
  void set_matching(int job){STRUMPACK_set_matching(spss, job);}
  void set_Krylov_solver(STRUMPACK_KRYLOV_SOLVER solver_type){STRUMPACK_set_Krylov_solver(spss, solver_type);}
  void enable_HSS(void){STRUMPACK_enable_HSS(spss);}
  void disable_HSS(void){STRUMPACK_disable_HSS(spss);}
  void set_HSS_min_front_size(int size){STRUMPACK_set_HSS_min_front_size(spss, size);}
  void set_HSS_min_sep_size(int size){STRUMPACK_set_HSS_min_sep_size(spss, size);}
  void set_HSS_max_rank(int max_rank){STRUMPACK_set_HSS_max_rank(spss, max_rank);}
  void set_HSS_leaf_size(int leaf_size){STRUMPACK_set_HSS_leaf_size(spss, leaf_size);}
  void set_HSS_rel_tol(double rctol){STRUMPACK_set_HSS_rel_tol(spss, rctol);}
  void set_HSS_abs_tol(double actol){STRUMPACK_set_HSS_abs_tol(spss, actol);}  
  
  int  get_verbose(void){return STRUMPACK_verbose(spss);}
  int  get_maxit(void){return STRUMPACK_maxit(spss);}
  double get_rel_tol(void){return STRUMPACK_rel_tol(spss);}
  double get_abs_tol(void){return STRUMPACK_abs_tol(spss);}
  int get_nd_param(void){return STRUMPACK_nd_param(spss);}
  STRUMPACK_REORDERING_STRATEGY get_reordering_method(void){return STRUMPACK_reordering_method(spss);}
  int get_mc64job(void){return STRUMPACK_mc64job(spss);}
  int get_matching(void){return STRUMPACK_matching(spss);}
  STRUMPACK_KRYLOV_SOLVER get_Krylov_solver(void){return STRUMPACK_Krylov_solver(spss);}
  int get_HSS_min_front_size(void){return STRUMPACK_HSS_min_front_size(spss);}
  int get_HSS_min_sep_size(void){return STRUMPACK_HSS_min_sep_size(spss);}
  int get_HSS_max_rank(void){return STRUMPACK_HSS_max_rank(spss);}
  int get_HSS_leaf_size(void){return STRUMPACK_HSS_leaf_size(spss);}
  double get_HSS_rel_tol(void){return STRUMPACK_HSS_rel_tol(spss);}
  double get_HSS_abs_tol(void){return STRUMPACK_HSS_abs_tol(spss);}
  int get_its(void){return STRUMPACK_its(spss);}
  int get_rank(void){return STRUMPACK_rank(spss);}
  long get_factor_nonzeros(void){return STRUMPACK_factor_nonzeros(spss);}
  long get_factor_memory(void){return STRUMPACK_factor_memory(spss);}
};
%}

%import "common_interface/pointer_array.i"

%define MakeSolver(PREFIX, TYPE, TYPE_C)
%inline %{

class PREFIX##StrumpackSolver : public StrumpackSolverBase
{
 public:
    PREFIX##StrumpackSolver(){
       char *argv[] = {NULL};
       STRUMPACK_init_mt(&spss, TYPE, STRUMPACK_MT, 1, argv, 0);
    }
    
    PREFIX##StrumpackSolver(MPI_Comm comm){
       char *argv[] = {NULL};      
       STRUMPACK_init(&spss, comm, TYPE, STRUMPACK_MPI_DIST, 0, argv, 0);
    }

    ~PREFIX##StrumpackSolver(){
       STRUMPACK_destroy(&spss);
    }
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
  print(dist)    
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

  
