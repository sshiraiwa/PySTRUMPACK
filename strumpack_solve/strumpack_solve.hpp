#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <cmath>    
#include <complex> 
#include "StrumpackSparseSolver.h"
#include "StrumpackConfig.hpp"


namespace libstrumpack_solve
{
class StrumpackSolverBase
{
 protected:
  STRUMPACK_SparseSolver *spss;
 public:
  StrumpackSolverBase(){}
  STRUMPACK_RETURN_CODE factor(void);
  STRUMPACK_RETURN_CODE reorder(void);
  STRUMPACK_RETURN_CODE reorder_regular(int nx, int ny, int nz, int components=1, int width=1);

  void set_from_options(void);
  //void move_to_gpu(void){return STRUMPACK_move_to_gpu(spss);}
  //void remove_from_gpu(void){return STRUMPACK_remove_from_gpu(spss);}
  //void delete_factors(void){return STRUMPACK_delete_factors(spss);}
  
  void set_verbose(int v);
  void set_maxit(int  maxit);
  void set_gmres_restart(int m);
  void set_rel_tol(double tol);
  void set_abs_tol(double tol);
  void set_nd_param(int nd_param);
  void set_reordering_method(STRUMPACK_REORDERING_STRATEGY m);
  void set_GramSchmidt_type(STRUMPACK_GRAM_SCHMIDT_TYPE t);
  void set_matching(STRUMPACK_MATCHING_JOB job);
  void set_Krylov_solver(STRUMPACK_KRYLOV_SOLVER solver_type);
  void enable_gpu();
  void disable_gpu();
  void set_compression(STRUMPACK_COMPRESSION_TYPE t);
  void set_compression_min_sep_size(int size);
  void set_compression_min_front_size(int size);
  void set_compression_leaf_size(int size);
  void set_compression_rel_tol(double rctol);
  void set_compression_abs_tol(double actol);
  void set_compression_butterfly_levels(int l);
  
  int  get_verbose(void);
  int  get_maxit(void);
  //int gmres_restart(void){return STRUMPACK_get_gmres_restart(spss);}

  double get_rel_tol(void);
  double get_abs_tol(void);
  int get_nd_param(void);
  STRUMPACK_REORDERING_STRATEGY reordering_method(void);
  STRUMPACK_GRAM_SCHMIDT_TYPE GramSchmidt_type(void);
  STRUMPACK_MATCHING_JOB matching(void);
  STRUMPACK_KRYLOV_SOLVER Krylov_solver(void);
  //bool use_gpu(void){return bool(STRUMPACK_use_gpu(spss));}
  STRUMPACK_COMPRESSION_TYPE compression(void);
  int compression_min_sep_size(void);
  int compression_min_front_size(void);
  int compression_leaf_size(void);
  double compression_rel_tol(void);
  double compression_abs_tol(void);
  int compression_butterfly_levels(void);

  int its(void);
  int rank(void);
  long factor_nonzeros(void);
  long factor_memory(void);
};

template <STRUMPACK_PRECISION T1, typename T2, typename T3>
class StrumpackSolver : public StrumpackSolverBase
{
 private:
    bool success = false;
 public:
  StrumpackSolver(int argc, char *argv[], bool verbose);
  StrumpackSolver(MPI_Comm comm, int argc, char *argv[], bool verbose);
  ~StrumpackSolver();
  bool isValid(void){return success;}

  void set_csr_matrix0(T3 N, T3 *row_ptr, T3 *col_ind, T2 *values, bool symmetric_pattern);

  void set_distributed_csr_matrix0(T3 local_rows, const T3* row_ptr,
                                     const T3* col_ind, const T2 *values,
				     const T3* dist,  bool symmetric_pattern);

  STRUMPACK_RETURN_CODE solve(T2 *b, T2 *x, bool use_initial_guess);
};

} /* end of namespace */
