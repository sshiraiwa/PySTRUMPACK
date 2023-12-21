#include "StrumpackSparseSolver.h"
#include "strumpack_solve.hpp"

namespace libstrumpack_solve{
  
STRUMPACK_RETURN_CODE StrumpackSolverBase::factor(void){
  return STRUMPACK_factor(*spss);
}
STRUMPACK_RETURN_CODE StrumpackSolverBase::reorder(void){
  return STRUMPACK_reorder(*spss);
}
STRUMPACK_RETURN_CODE StrumpackSolverBase::reorder_regular(int nx, int ny, int nz, int components, int width){
    return STRUMPACK_reorder_regular(*spss, nx, ny, nz, components, width);
  }
void StrumpackSolverBase::set_from_options(void){
  return STRUMPACK_set_from_options(*spss);
}
  //void move_to_gpu(void){return STRUMPACK_move_to_gpu(spss);}
  //void remove_from_gpu(void){return STRUMPACK_remove_from_gpu(spss);}
  //void delete_factors(void){return STRUMPACK_delete_factors(spss);}
  
void StrumpackSolverBase::set_verbose(int v){
  STRUMPACK_set_verbose(*spss, v);
}
void StrumpackSolverBase::set_maxit(int  maxit){
  STRUMPACK_set_maxit(*spss, maxit);
}
void StrumpackSolverBase::set_gmres_restart(int m){
  STRUMPACK_set_gmres_restart(*spss, m);
}
void StrumpackSolverBase::set_rel_tol(double tol){
  STRUMPACK_set_rel_tol(*spss, tol);
}
void StrumpackSolverBase::set_abs_tol(double tol){
  STRUMPACK_set_abs_tol(*spss, tol);
}
void StrumpackSolverBase::set_nd_param(int nd_param){
  STRUMPACK_set_nd_param(*spss, nd_param);
}
void StrumpackSolverBase::set_reordering_method(STRUMPACK_REORDERING_STRATEGY m){
  STRUMPACK_set_reordering_method(*spss, m);
}
void StrumpackSolverBase::set_GramSchmidt_type(STRUMPACK_GRAM_SCHMIDT_TYPE t){
  STRUMPACK_set_GramSchmidt_type(*spss, t);
}
void StrumpackSolverBase::set_matching(STRUMPACK_MATCHING_JOB job){
  STRUMPACK_set_matching(*spss, job);
}
void StrumpackSolverBase::set_Krylov_solver(STRUMPACK_KRYLOV_SOLVER solver_type){
  STRUMPACK_set_Krylov_solver(*spss, solver_type);
}
void StrumpackSolverBase::enable_gpu(){
  STRUMPACK_enable_gpu(*spss);
}
void StrumpackSolverBase::disable_gpu(){
  STRUMPACK_disable_gpu(*spss);
}
void StrumpackSolverBase::set_compression(STRUMPACK_COMPRESSION_TYPE t){
  STRUMPACK_set_compression(*spss, t);
}
void StrumpackSolverBase::set_compression_min_sep_size(int size){
  STRUMPACK_set_compression_min_sep_size(*spss, size);
}
void StrumpackSolverBase::set_compression_min_front_size(int size){
  STRUMPACK_set_compression_min_front_size(*spss, size);
}
void StrumpackSolverBase::set_compression_leaf_size(int size){
  STRUMPACK_set_compression_leaf_size(*spss, size);
}
void StrumpackSolverBase::set_compression_rel_tol(double rctol){
  STRUMPACK_set_compression_rel_tol(*spss, rctol);
}
void StrumpackSolverBase::set_compression_abs_tol(double actol){
  STRUMPACK_set_compression_abs_tol(*spss, actol);
}
void StrumpackSolverBase::set_compression_butterfly_levels(int l){
  STRUMPACK_set_compression_butterfly_levels(*spss, l);
}
int StrumpackSolverBase::get_verbose(void){
  return STRUMPACK_verbose(*spss);
}
int StrumpackSolverBase::get_maxit(void){
  return STRUMPACK_maxit(*spss);
}
  //int gmres_restart(void){return STRUMPACK_get_gmres_restart(spss);}
double StrumpackSolverBase::get_rel_tol(void){
  return STRUMPACK_rel_tol(*spss);
}
double StrumpackSolverBase::get_abs_tol(void){
  return STRUMPACK_abs_tol(*spss);
}
int StrumpackSolverBase::get_nd_param(void){
  return STRUMPACK_nd_param(*spss);
}
STRUMPACK_REORDERING_STRATEGY StrumpackSolverBase::reordering_method(void){
  return STRUMPACK_reordering_method(*spss);
}
STRUMPACK_GRAM_SCHMIDT_TYPE StrumpackSolverBase::GramSchmidt_type(void){
  return STRUMPACK_GramSchmidt_type(*spss);
}
STRUMPACK_MATCHING_JOB StrumpackSolverBase::matching(void){
  return STRUMPACK_matching(*spss);
}
STRUMPACK_KRYLOV_SOLVER StrumpackSolverBase::Krylov_solver(void){
  return STRUMPACK_Krylov_solver(*spss);
}
//bool use_gpu(void){return bool(STRUMPACK_use_gpu(spss));}
STRUMPACK_COMPRESSION_TYPE StrumpackSolverBase::compression(void){
  return STRUMPACK_compression(*spss);
}
int StrumpackSolverBase::compression_min_sep_size(void){
  return STRUMPACK_compression_min_sep_size(*spss);
}
int StrumpackSolverBase::compression_min_front_size(void){
  return STRUMPACK_compression_min_front_size(*spss);
}
int StrumpackSolverBase::compression_leaf_size(void){
  return STRUMPACK_compression_leaf_size(*spss);
}
double StrumpackSolverBase::compression_rel_tol(void){
  return STRUMPACK_compression_rel_tol(*spss);
}
double StrumpackSolverBase::compression_abs_tol(void){
  return STRUMPACK_compression_abs_tol(*spss);
}
int StrumpackSolverBase::compression_butterfly_levels(void){
  return STRUMPACK_compression_butterfly_levels(*spss);
}

int StrumpackSolverBase::its(void){
  return STRUMPACK_its(*spss);
}
int StrumpackSolverBase::rank(void){
  return STRUMPACK_rank(*spss);
}
long StrumpackSolverBase::factor_nonzeros(void){
  return STRUMPACK_factor_nonzeros(*spss);
}
long StrumpackSolverBase::factor_memory(void){
  return STRUMPACK_factor_memory(*spss);
}
  
template <STRUMPACK_PRECISION T1, typename T2, typename T3>
StrumpackSolver<T1, T2, T3>::StrumpackSolver(int argc, char *argv[], bool verbose){
  spss=new STRUMPACK_SparseSolver();  
  STRUMPACK_init_mt(spss, T1, STRUMPACK_MT, argc, argv, verbose);
}

template <STRUMPACK_PRECISION T1, typename T2, typename T3>
StrumpackSolver<T1, T2, T3>::StrumpackSolver(MPI_Comm comm, int argc, char *argv[], bool verbose){
  spss=new STRUMPACK_SparseSolver();    
  STRUMPACK_init(spss, comm, T1, STRUMPACK_MPI_DIST, argc, argv, verbose);
  success = true;
}

template <STRUMPACK_PRECISION T1, typename T2, typename T3>
StrumpackSolver<T1, T2, T3>::~StrumpackSolver()
{
  if (success) {
     STRUMPACK_destroy(spss);
  }
}

template <STRUMPACK_PRECISION T1, typename T2, typename T3>
void StrumpackSolver<T1, T2, T3>::set_csr_matrix0(T3 N,
					      T3 *row_ptr,
					      T3 *col_ind,
					      T2 *values,
					      bool symmetric_pattern){
   STRUMPACK_set_csr_matrix(*spss,  &N, (void*) row_ptr,(void*) col_ind,
		(void*) values, symmetric_pattern);
}

template <STRUMPACK_PRECISION T1, typename T2, typename T3>
void StrumpackSolver<T1, T2, T3>::set_distributed_csr_matrix0(T3 local_rows,
							  const T3* row_ptr,
							  const T3* col_ind,
							  const T2 *values,
							  const T3* dist,
 							  bool symmetric_pattern){

  STRUMPACK_set_distributed_csr_matrix(*spss,
		       &local_rows, (const void*) row_ptr,
		       (const void*) col_ind, (const void*) values,
		       (const void*) dist, symmetric_pattern);
}

template <STRUMPACK_PRECISION T1, typename T2, typename T3>
STRUMPACK_RETURN_CODE StrumpackSolver<T1, T2, T3>::solve(T2 *b, T2 *x, bool use_initial_guess){
   return STRUMPACK_solve(*spss, (const void*) b, (void*) x, use_initial_guess);
}

template class StrumpackSolver<STRUMPACK_FLOAT, float, int32_t>;
template class StrumpackSolver<STRUMPACK_DOUBLE, double, int32_t>;
template class StrumpackSolver<STRUMPACK_FLOATCOMPLEX, std::complex<float>, int32_t>;
template class StrumpackSolver<STRUMPACK_DOUBLECOMPLEX, std::complex<double>, int32_t>;
template class StrumpackSolver<STRUMPACK_FLOAT_64, float, int64_t>;
template class StrumpackSolver<STRUMPACK_DOUBLE_64, double, int64_t>;
template class StrumpackSolver<STRUMPACK_FLOATCOMPLEX_64, std::complex<float>, int64_t>;
template class StrumpackSolver<STRUMPACK_DOUBLECOMPLEX_64, std::complex<double>, int64_t>;
  
} /* end of namespace */
