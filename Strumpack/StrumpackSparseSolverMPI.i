%module StrumpackSparseSolverMPI
%{
#include "numpy/arrayobject.h"
#include "StrumpackSparseSolverMPI.hpp"
%}

%init %{
import_array();
%}

%include "StrumpackSparseSolverMPI.hpp"
