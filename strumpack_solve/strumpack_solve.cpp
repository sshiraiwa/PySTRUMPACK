#include "StrumpackSparseSolver.h"
#include "strumpack_solve.hpp"

namespace libstrumpack_solve{
  
template <STRUMPACK_PRECISION T1, typename T2>
StrumpackSolver<T1, T2>::~StrumpackSolver()
{
  if (success) {
     STRUMPACK_destroy(spss);
  }
}


template <STRUMPACK_PRECISION T1, typename T2>
void StrumpackSolver<T1, T2>::set_csr_matrix0(int N,
					      int *row_ptr,
					      int *col_ind,
					      T2 *values,
					      int symmetric_pattern){
   STRUMPACK_set_csr_matrix(*spss,  &N, (void*) row_ptr,(void*) col_ind,
		(void*) values, symmetric_pattern);
}


template <STRUMPACK_PRECISION T1, typename T2>
void StrumpackSolver<T1, T2>::set_distributed_csr_matrix0(int local_rows,
							  const int* row_ptr,
							  const int* col_ind,
							  const T2 *values,
							  const int* dist,
							  int symmetric_pattern){

  STRUMPACK_set_distributed_csr_matrix(*spss,
		       &local_rows, (const void*) row_ptr,
		       (const void*) col_ind, (const void*) values,
		       (const void*) dist, symmetric_pattern);
}



template <STRUMPACK_PRECISION T1, typename T2>
STRUMPACK_RETURN_CODE StrumpackSolver<T1, T2>::solve(T2 *b, T2 *x, int use_initial_guess){
   return STRUMPACK_solve(*spss, (const void*) b, (void*) x, use_initial_guess);
}
  
} /* end of namespace */
