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
  StrumpackSolverBase(){
    spss=nullptr;
  }
  STRUMPACK_RETURN_CODE factor(void){return STRUMPACK_factor(*spss);}
  STRUMPACK_RETURN_CODE reorder(void){return STRUMPACK_reorder(*spss);}
  STRUMPACK_RETURN_CODE reorder_regular(int nx, int ny, int nz, int components=1, int width=1){return STRUMPACK_reorder_regular(*spss, nx, ny, nz, components, width);}

  void set_from_options(void){return STRUMPACK_set_from_options(*spss);}
  //void move_to_gpu(void){return STRUMPACK_move_to_gpu(spss);}
  //void remove_from_gpu(void){return STRUMPACK_remove_from_gpu(spss);}
  //void delete_factors(void){return STRUMPACK_delete_factors(spss);}
  
  void set_verbose(int v){STRUMPACK_set_verbose(*spss, v);}
  void set_maxit(int  maxit){STRUMPACK_set_maxit(*spss, maxit);}
  void set_gmres_restart(int m){STRUMPACK_set_gmres_restart(*spss, m);}
  void set_rel_tol(double tol){STRUMPACK_set_rel_tol(*spss, tol);}
  void set_abs_tol(double tol){STRUMPACK_set_abs_tol(*spss, tol);}
  void set_nd_param(int nd_param){STRUMPACK_set_nd_param(*spss, nd_param);}
  void set_reordering_method(STRUMPACK_REORDERING_STRATEGY m){STRUMPACK_set_reordering_method(*spss, m);}
  void set_GramSchmidt_type(STRUMPACK_GRAM_SCHMIDT_TYPE t){STRUMPACK_set_GramSchmidt_type(*spss, t);}
  void set_matching(STRUMPACK_MATCHING_JOB job){STRUMPACK_set_matching(*spss, job);}
  void set_Krylov_solver(STRUMPACK_KRYLOV_SOLVER solver_type){STRUMPACK_set_Krylov_solver(*spss, solver_type);}
  void enable_gpu(){STRUMPACK_enable_gpu(*spss);}
  void disable_gpu(){STRUMPACK_disable_gpu(*spss);}
  void set_compression(STRUMPACK_COMPRESSION_TYPE t){STRUMPACK_set_compression(*spss, t);}
  void set_compression_min_sep_size(int size){STRUMPACK_set_compression_min_sep_size(*spss, size);}
  void set_compression_min_front_size(int size){STRUMPACK_set_compression_min_front_size(*spss, size);}
  void set_compression_leaf_size(int size){STRUMPACK_set_compression_leaf_size(*spss, size);}
  void set_compression_rel_tol(double rctol){STRUMPACK_set_compression_rel_tol(*spss, rctol);}
  void set_compression_abs_tol(double actol){STRUMPACK_set_compression_abs_tol(*spss, actol);}
  void set_compression_butterfly_levels(int l){STRUMPACK_set_compression_butterfly_levels(*spss, l);}
  
  int  get_verbose(void){return STRUMPACK_verbose(*spss);}
  int  get_maxit(void){return STRUMPACK_maxit(*spss);}
  //int gmres_restart(void){return STRUMPACK_get_gmres_restart(spss);}

  double get_rel_tol(void){return STRUMPACK_rel_tol(*spss);}
  double get_abs_tol(void){return STRUMPACK_abs_tol(*spss);}
  int get_nd_param(void){return STRUMPACK_nd_param(*spss);}
  STRUMPACK_REORDERING_STRATEGY reordering_method(void){return STRUMPACK_reordering_method(*spss);}
  STRUMPACK_GRAM_SCHMIDT_TYPE GramSchmidt_type(void){return STRUMPACK_GramSchmidt_type(*spss);}
  STRUMPACK_MATCHING_JOB matching(void){return STRUMPACK_matching(*spss);}
  STRUMPACK_KRYLOV_SOLVER Krylov_solver(void){return STRUMPACK_Krylov_solver(*spss);}
  //bool use_gpu(void){return bool(STRUMPACK_use_gpu(spss));}
  STRUMPACK_COMPRESSION_TYPE compression(void){return STRUMPACK_compression(*spss);}
  int compression_min_sep_size(void){return STRUMPACK_compression_min_sep_size(*spss);}
  int compression_min_front_size(void){return STRUMPACK_compression_min_front_size(*spss);}
  int compression_leaf_size(void){return STRUMPACK_compression_leaf_size(*spss);}
  double compression_rel_tol(void){return STRUMPACK_compression_rel_tol(*spss);}
  double compression_abs_tol(void){return STRUMPACK_compression_abs_tol(*spss);}
  int compression_butterfly_levels(void){return STRUMPACK_compression_butterfly_levels(*spss);}

  int its(void){return STRUMPACK_its(*spss);}
  int rank(void){return STRUMPACK_rank(*spss);}
  long factor_nonzeros(void){return STRUMPACK_factor_nonzeros(*spss);}
  long factor_memory(void){return STRUMPACK_factor_memory(*spss);}

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

template <STRUMPACK_PRECISION T1, typename T2>
class StrumpackSolver : public StrumpackSolverBase
{
 private:
    bool success = false;
 public:
  StrumpackSolver(int argc, char *argv[], bool verbose){
      STRUMPACK_init_mt(spss, T1, STRUMPACK_MT, argc, argv, verbose);
    }

  StrumpackSolver(MPI_Comm comm, int argc, char *argv[], bool verbose){
      STRUMPACK_init(spss, comm, T1, STRUMPACK_MPI_DIST, argc, argv, verbose);
      success = true;
    }
    
  ~StrumpackSolver();
  bool isValid(void){return success;}

  void set_csr_matrix0(int N, int *row_ptr, int *col_ind, T2 *values, int symmetric_pattern);

  void set_distributed_csr_matrix0(int local_rows, const int* row_ptr,
                                     const int* col_ind, const T2 *values,
				     const int* dist,   int symmetric_pattern);

  STRUMPACK_RETURN_CODE solve(T2 *b, T2 *x, int use_initial_guess);
};

template class StrumpackSolver<STRUMPACK_FLOAT, float>;
template class StrumpackSolver<STRUMPACK_DOUBLE, double>;
template class StrumpackSolver<STRUMPACK_FLOATCOMPLEX, std::complex<float>>;
template class StrumpackSolver<STRUMPACK_DOUBLECOMPLEX, std::complex<double>>;

} /* end of namespace */
