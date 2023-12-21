
/*
pointer_array_wrap wraps the following 

virtual void set_csr_matrix(integer_t N, integer_t* row_ptr, integer_t* col_ind, scalar_t* values, bool symmetric_pattern=false);
virtual params::returnCode solve(scalar_t* b, scalar_t* x, bool use_initial_guess=false);

*/
%define pointer_array_wrap(T, A)
  %typemap(in)  (T *A)  (PyArrayObject* tempobj = 0) {
  if (PyArray_Check($input)){
    tempobj =  (PyArrayObject *) PyArray_GETCONTIGUOUS( (PyArrayObject *) $input);  
    $1 = (T *) PyArray_DATA( (PyArrayObject *)tempobj);
  }
  else {
    return NULL;
  }
}

%typemap(freearg)  (T *A){
  if (tempobj$argnum){Py_DECREF(tempobj$argnum);}
}  
%typemap(typecheck ) (T *A){c
   if (PyArray_Check($input)){
      $1 = 1;
   } else {
      $1 = 0;
   }
}
%enddef

pointer_array_wrap(float, values)
pointer_array_wrap(double, values)
pointer_array_wrap(std::complex<float>, values)
pointer_array_wrap(std::complex<double>, values)
pointer_array_wrap(float, b)
pointer_array_wrap(double, b)
pointer_array_wrap(std::complex<float>, b)
pointer_array_wrap(std::complex<double>, b)
pointer_array_wrap(float, x)
pointer_array_wrap(double, x)
pointer_array_wrap(std::complex<float>, x)
pointer_array_wrap(std::complex<double>, x)
pointer_array_wrap(int, row_ptr)
pointer_array_wrap(int, col_ind)
pointer_array_wrap(int, dist)  
pointer_array_wrap(long, row_ptr)
pointer_array_wrap(long, col_ind)
pointer_array_wrap(long, dist)  
