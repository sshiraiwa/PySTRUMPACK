//  conversion of Int (can handle numpy int)
%typemap(in) int {
  if ((PyArray_PyIntAsInt($input) == -1) && PyErr_Occurred()) {
    SWIG_exception_fail(SWIG_TypeError, "Input must be integer (numpy_int_typemap-int)");
  };  
  $1 = PyArray_PyIntAsInt($input);
}
%typemap(typecheck,precedence=SWIG_TYPECHECK_INTEGER) int {
  if ((PyArray_PyIntAsInt($input) == -1) && PyErr_Occurred()) {
    PyErr_Clear();
    $1 = 0;
  } else {
    $1 = 1;    
  }
}
%typemap(in) long {
  if ((PyArray_PyIntAsInt($input) == -1) && PyErr_Occurred()) {
    SWIG_exception_fail(SWIG_TypeError, "Input must be integer (numpy_int_typemap-long)");
  };  
  $1 = PyArray_PyIntAsInt($input);
}
%typemap(typecheck,precedence=SWIG_TYPECHECK_INTEGER) long {
  if ((PyArray_PyIntAsInt($input) == -1) && PyErr_Occurred()) {
    PyErr_Clear();
    $1 = 0;
  } else {
    $1 = 1;    
  }
}


