StrumpackSolver::~StrumpackSolver()
{
  if (success) {
     STRUMPACK_destroy(&spss);
  }
}

void StrumpackSolver::set_csr_matrix0(int N, int *row_ptr, int *col_ind, T2 *values, int symmetric_pattern){
   STRUMPACK_set_csr_matrix(spss,  &N, (void*) row_ptr,(void*) col_ind,
		(void*) values, symmetric_pattern);
}

void StrumpackSolver::set_distributed_csr_matrix0(int local_rows, const int* row_ptr,
                                     const int* col_ind, const T2 *values,
				     const int* dist,   int symmetric_pattern){

  STRUMPACK_set_distributed_csr_matrix(spss,
		       &local_rows, (const void*) row_ptr,
		       (const void*) col_ind, (const void*) values,
		       (const void*) dist, symmetric_pattern);
}
   
STRUMPACK_RETURN_CODE StrunpackSolver::solve(T2 *b, T2 *x, int use_initial_guess){
   return STRUMPACK_solve(spss, (const void*) b, (void*) x, use_initial_guess);
}  

