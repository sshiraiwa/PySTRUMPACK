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

%import "common_interface/int_scalar_t.i"
%import "common_interface/argc_argv.i"

%include "StrumpackSparseSolver.hpp"

%template(SStrumpackSparseSolver) strumpack::StrumpackSparseSolver<float, float, int>;
%template(DStrumpackSparseSolver) strumpack::StrumpackSparseSolver<double, double, int>;
%template(CStrumpackSparseSolver) strumpack::StrumpackSparseSolver<std::complex<float>, float, int>;
%template(ZStrumpackSparseSolver) strumpack::StrumpackSparseSolver<std::complex<double>, double, int>;




