%module StrumpackSparseSolverMPI
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
#include "StrumpackSparseSolverMPI.hpp"
#include "CSRMatrixMPI.hpp"
%}

%init %{
import_array();
%}

%import "common_interface/int_scalar_t.i"
%import "common_interface/argc_argv.i"
%include "StrumpackSparseSolver.i"

%include "StrumpackSparseSolverMPI.hpp"

%template(SStrumpackSparseSolverMPI) strumpack::StrumpackSparseSolverMPI<float, float, int>;
%template(DStrumpackSparseSolverMPI) strumpack::StrumpackSparseSolverMPI<double, double, int>;
%template(CStrumpackSparseSolverMPI) strumpack::StrumpackSparseSolverMPI<std::complex<float>, float, int>;
%template(ZStrumpackSparseSolverMPI) strumpack::StrumpackSparseSolverMPI<std::complex<double>, double, int>;
