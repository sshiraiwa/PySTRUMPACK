%module StrumpackSparseSolverMPIDist
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
#include "StrumpackSparseSolverMPIDist.hpp"
#include "CSRMatrixMPI.hpp"
%}

%init %{
import_array();
%}

%import "common_interface/int_scalar_t.i"
%import "common_interface/argc_argv.i"
%include "StrumpackSparseSolver.i"
%include "StrumpackSparseSolverMPI.i"

%include "StrumpackSparseSolverMPIDist.hpp"

%template(SStrumpackSparseSolverMPIDist) strumpack::StrumpackSparseSolverMPIDist<float, float, int>;
%template(DStrumpackSparseSolverMPIDist) strumpack::StrumpackSparseSolverMPIDist<double, double, int>;
%template(CStrumpackSparseSolverMPIDist) strumpack::StrumpackSparseSolverMPIDist<std::complex<float>, float, int>;
%template(ZStrumpackSparseSolverMPIDist) strumpack::StrumpackSparseSolverMPIDist<std::complex<double>, double, int>;
