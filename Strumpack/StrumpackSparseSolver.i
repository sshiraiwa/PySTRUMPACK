%module StrumpackSparseSolver
%{
#include <atomic>
#include <tuple>
#include <vector>
#include <sstream>
#include <new>
#include <cmath>
#include <complex>
#include <iostream>  
#include "numpy/arrayobject.h"
#include "StrumpackSparseSolver.hpp"
#include "CSRMatrixMPI.hpp"
using namespace strumpack;
using namespace strumpack::params; 
%}

%init %{
import_array();
%}

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

// handle int argc, char *argv[] 
%typemap(in) (int argc, char *argv[]) {
  int i;
  if (!PyList_Check($input)) {
    PyErr_SetString(PyExc_ValueError, "Expecting a list");
    SWIG_fail;
  }
  $1 = PyList_Size($input);
  $2 = (char **) malloc(($1+1)*sizeof(char *));
  for (i = 0; i < $1; i++) {
    PyObject *s = PyList_GetItem($input, i);
    if (!PyString_Check(s)) {
      free($2);
      PyErr_SetString(PyExc_ValueError, "List items must be strings");
      SWIG_fail;
    }
    $2[i] = PyString_AsString(s);
  }
  $2[i] = 0;
}

%typemap(freearg) (int argc, char *argv[]) {
  if ($2) free($2);
}

/* Required for C++ method overloading */
%typecheck(SWIG_TYPECHECK_STRING_ARRAY) (int argc, char *argv[]) {
  $1 = PyList_Check($input) ? 1 : 0;
}
// end of int argc, char *argv[]

%include "StrumpackSparseSolver.hpp"

%template(SStrumpackSparseSolver) strumpack::StrumpackSparseSolver<float, float, int>;
%template(DStrumpackSparseSolver) strumpack::StrumpackSparseSolver<double, double, int>;
%template(CStrumpackSparseSolver) strumpack::StrumpackSparseSolver<std::complex<float>, float, int>;
%template(ZStrumpackSparseSolver) strumpack::StrumpackSparseSolver<std::complex<double>, double, int>;




