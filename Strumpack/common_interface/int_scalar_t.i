
/*
int_scalar_t wraps the following 

virtual void set_csr_matrix(integer_t N, integer_t* row_ptr, integer_t* col_ind, scalar_t* values, bool symmetric_pattern=false);
virtual params::returnCode solve(scalar_t* b, scalar_t* x, bool use_initial_guess=false);

*/
%define int_scalar_t_wrap(T, A)
%typemap(in)  (T *A){
  if (PyArray_Check($input)){
    $1 = (T *) PyArray_DATA((PyArrayObject *)$input);
  }
  else {
    return NULL;
  }
}
%typemap(typecheck ) (T *A){
   if (PyArray_Check($input)){
      $1 = 1;
   } else {
      $1 = 0;
   }
}
%enddef

int_scalar_t_wrap(float, values)
int_scalar_t_wrap(double, values)
int_scalar_t_wrap(std::complex<float>, values)
int_scalar_t_wrap(std::complex<double>, values)
int_scalar_t_wrap(float, b)
int_scalar_t_wrap(double, b)
int_scalar_t_wrap(std::complex<float>, b)
int_scalar_t_wrap(std::complex<double>, b)
int_scalar_t_wrap(float, x)
int_scalar_t_wrap(double, x)
int_scalar_t_wrap(std::complex<float>, x)
int_scalar_t_wrap(std::complex<double>, x)
int_scalar_t_wrap(int, row_ptr)
int_scalar_t_wrap(int, col_ind)
