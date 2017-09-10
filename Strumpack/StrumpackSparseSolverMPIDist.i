%module StrumpackSparseSolverMPIDist
%{
#include "numpy/arrayobject.h"
#include "StrumpackSparseSolverMPIDist.hpp"
%}

%init %{
import_array();
%}

%include "StrumpackSparseSolverMPIDist.hpp"
