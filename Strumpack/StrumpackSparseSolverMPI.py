# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_StrumpackSparseSolverMPI')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_StrumpackSparseSolverMPI')
    _StrumpackSparseSolverMPI = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_StrumpackSparseSolverMPI', [dirname(__file__)])
        except ImportError:
            import _StrumpackSparseSolverMPI
            return _StrumpackSparseSolverMPI
        try:
            _mod = imp.load_module('_StrumpackSparseSolverMPI', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _StrumpackSparseSolverMPI = swig_import_helper()
    del swig_import_helper
else:
    import _StrumpackSparseSolverMPI
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SStrumpackSparseSolver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SStrumpackSparseSolver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SStrumpackSparseSolver, name)
    __repr__ = _swig_repr

    def __init__(self, argc, verb=True, root=True):
        this = _StrumpackSparseSolverMPI.new_SStrumpackSparseSolver(argc, verb, root)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _StrumpackSparseSolverMPI.delete_SStrumpackSparseSolver
    __del__ = lambda self: None

    def set_from_options(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_from_options(self)

    def set_from_options_no_warning_unrecognized(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_from_options_no_warning_unrecognized(self)

    def set_matrix(self, A):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_matrix(self, A)

    def set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern=False):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern)

    def reorder(self, nx=1, ny=1, nz=1):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_reorder(self, nx, ny, nz)

    def factor(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_factor(self)

    def solve(self, b, x, use_initial_guess=False):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_solve(self, b, x, use_initial_guess)

    def set_maximum_Krylov_iterations(self, maxit):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_maximum_Krylov_iterations(self, maxit)

    def set_gmres_restart(self, m):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_gmres_restart(self, m)

    def set_relative_Krylov_tolerance(self, tol):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_relative_Krylov_tolerance(self, tol)

    def set_absolute_Krylov_tolerance(self, tol):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_absolute_Krylov_tolerance(self, tol)

    def set_scotch_strategy(self, strat):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_scotch_strategy(self, strat)

    def set_nested_dissection_parameter(self, nd_param):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_nested_dissection_parameter(self, nd_param)

    def set_matrix_reordering_method(self, m):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_matrix_reordering_method(self, m)

    def set_GramSchmidt_type(self, t):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_GramSchmidt_type(self, t)

    def set_mc64job(self, job):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_mc64job(self, job)

    def set_Krylov_solver(self, solver_type):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_Krylov_solver(self, solver_type)

    def set_minimum_HSS_size(self, s):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_minimum_HSS_size(self, s)

    def set_relative_compression_tolerance(self, rctol):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_relative_compression_tolerance(self, rctol)

    def set_absolute_compression_tolerance(self, actol):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_absolute_compression_tolerance(self, actol)

    def set_rank_pattern(self, p):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_rank_pattern(self, p)

    def set_verbose(self, v=True):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_set_verbose(self, v)

    def get_maximum_Krylov_iterations(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_maximum_Krylov_iterations(self)

    def get_gmres_restart(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_gmres_restart(self)

    def get_relative_Krylov_tolerance(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_relative_Krylov_tolerance(self)

    def get_absolute_Krylov_tolerance(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_absolute_Krylov_tolerance(self)

    def get_scotch_strategy(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_scotch_strategy(self)

    def get_nested_dissection_parameter(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_nested_dissection_parameter(self)

    def get_matrix_reordering_method(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_matrix_reordering_method(self)

    def get_GramSchmidt_type(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_GramSchmidt_type(self)

    def get_maximum_rank(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_maximum_rank(self)

    def get_factor_nonzeros(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_factor_nonzeros(self)

    def get_factor_memory(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_factor_memory(self)

    def get_Krylov_iterations(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_Krylov_iterations(self)

    def get_mc64job(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_mc64job(self)

    def use_HSS(self, *args):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_use_HSS(self, *args)

    def get_minimum_HSS_size(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_minimum_HSS_size(self)

    def get_relative_compression_tolerance(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_relative_compression_tolerance(self)

    def get_absolute_compression_tolerance(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_absolute_compression_tolerance(self)

    def get_Krylov_solver(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_Krylov_solver(self)

    def get_rank_pattern(self):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolver_get_rank_pattern(self)
SStrumpackSparseSolver_swigregister = _StrumpackSparseSolverMPI.SStrumpackSparseSolver_swigregister
SStrumpackSparseSolver_swigregister(SStrumpackSparseSolver)

class DStrumpackSparseSolver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DStrumpackSparseSolver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DStrumpackSparseSolver, name)
    __repr__ = _swig_repr

    def __init__(self, argc, verb=True, root=True):
        this = _StrumpackSparseSolverMPI.new_DStrumpackSparseSolver(argc, verb, root)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _StrumpackSparseSolverMPI.delete_DStrumpackSparseSolver
    __del__ = lambda self: None

    def set_from_options(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_from_options(self)

    def set_from_options_no_warning_unrecognized(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_from_options_no_warning_unrecognized(self)

    def set_matrix(self, A):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_matrix(self, A)

    def set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern=False):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern)

    def reorder(self, nx=1, ny=1, nz=1):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_reorder(self, nx, ny, nz)

    def factor(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_factor(self)

    def solve(self, b, x, use_initial_guess=False):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_solve(self, b, x, use_initial_guess)

    def set_maximum_Krylov_iterations(self, maxit):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_maximum_Krylov_iterations(self, maxit)

    def set_gmres_restart(self, m):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_gmres_restart(self, m)

    def set_relative_Krylov_tolerance(self, tol):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_relative_Krylov_tolerance(self, tol)

    def set_absolute_Krylov_tolerance(self, tol):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_absolute_Krylov_tolerance(self, tol)

    def set_scotch_strategy(self, strat):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_scotch_strategy(self, strat)

    def set_nested_dissection_parameter(self, nd_param):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_nested_dissection_parameter(self, nd_param)

    def set_matrix_reordering_method(self, m):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_matrix_reordering_method(self, m)

    def set_GramSchmidt_type(self, t):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_GramSchmidt_type(self, t)

    def set_mc64job(self, job):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_mc64job(self, job)

    def set_Krylov_solver(self, solver_type):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_Krylov_solver(self, solver_type)

    def set_minimum_HSS_size(self, s):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_minimum_HSS_size(self, s)

    def set_relative_compression_tolerance(self, rctol):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_relative_compression_tolerance(self, rctol)

    def set_absolute_compression_tolerance(self, actol):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_absolute_compression_tolerance(self, actol)

    def set_rank_pattern(self, p):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_rank_pattern(self, p)

    def set_verbose(self, v=True):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_set_verbose(self, v)

    def get_maximum_Krylov_iterations(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_maximum_Krylov_iterations(self)

    def get_gmres_restart(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_gmres_restart(self)

    def get_relative_Krylov_tolerance(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_relative_Krylov_tolerance(self)

    def get_absolute_Krylov_tolerance(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_absolute_Krylov_tolerance(self)

    def get_scotch_strategy(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_scotch_strategy(self)

    def get_nested_dissection_parameter(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_nested_dissection_parameter(self)

    def get_matrix_reordering_method(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_matrix_reordering_method(self)

    def get_GramSchmidt_type(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_GramSchmidt_type(self)

    def get_maximum_rank(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_maximum_rank(self)

    def get_factor_nonzeros(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_factor_nonzeros(self)

    def get_factor_memory(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_factor_memory(self)

    def get_Krylov_iterations(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_Krylov_iterations(self)

    def get_mc64job(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_mc64job(self)

    def use_HSS(self, *args):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_use_HSS(self, *args)

    def get_minimum_HSS_size(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_minimum_HSS_size(self)

    def get_relative_compression_tolerance(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_relative_compression_tolerance(self)

    def get_absolute_compression_tolerance(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_absolute_compression_tolerance(self)

    def get_Krylov_solver(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_Krylov_solver(self)

    def get_rank_pattern(self):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolver_get_rank_pattern(self)
DStrumpackSparseSolver_swigregister = _StrumpackSparseSolverMPI.DStrumpackSparseSolver_swigregister
DStrumpackSparseSolver_swigregister(DStrumpackSparseSolver)

class CStrumpackSparseSolver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CStrumpackSparseSolver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CStrumpackSparseSolver, name)
    __repr__ = _swig_repr

    def __init__(self, argc, verb=True, root=True):
        this = _StrumpackSparseSolverMPI.new_CStrumpackSparseSolver(argc, verb, root)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _StrumpackSparseSolverMPI.delete_CStrumpackSparseSolver
    __del__ = lambda self: None

    def set_from_options(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_from_options(self)

    def set_from_options_no_warning_unrecognized(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_from_options_no_warning_unrecognized(self)

    def set_matrix(self, A):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_matrix(self, A)

    def set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern=False):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern)

    def reorder(self, nx=1, ny=1, nz=1):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_reorder(self, nx, ny, nz)

    def factor(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_factor(self)

    def solve(self, b, x, use_initial_guess=False):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_solve(self, b, x, use_initial_guess)

    def set_maximum_Krylov_iterations(self, maxit):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_maximum_Krylov_iterations(self, maxit)

    def set_gmres_restart(self, m):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_gmres_restart(self, m)

    def set_relative_Krylov_tolerance(self, tol):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_relative_Krylov_tolerance(self, tol)

    def set_absolute_Krylov_tolerance(self, tol):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_absolute_Krylov_tolerance(self, tol)

    def set_scotch_strategy(self, strat):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_scotch_strategy(self, strat)

    def set_nested_dissection_parameter(self, nd_param):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_nested_dissection_parameter(self, nd_param)

    def set_matrix_reordering_method(self, m):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_matrix_reordering_method(self, m)

    def set_GramSchmidt_type(self, t):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_GramSchmidt_type(self, t)

    def set_mc64job(self, job):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_mc64job(self, job)

    def set_Krylov_solver(self, solver_type):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_Krylov_solver(self, solver_type)

    def set_minimum_HSS_size(self, s):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_minimum_HSS_size(self, s)

    def set_relative_compression_tolerance(self, rctol):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_relative_compression_tolerance(self, rctol)

    def set_absolute_compression_tolerance(self, actol):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_absolute_compression_tolerance(self, actol)

    def set_rank_pattern(self, p):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_rank_pattern(self, p)

    def set_verbose(self, v=True):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_set_verbose(self, v)

    def get_maximum_Krylov_iterations(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_maximum_Krylov_iterations(self)

    def get_gmres_restart(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_gmres_restart(self)

    def get_relative_Krylov_tolerance(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_relative_Krylov_tolerance(self)

    def get_absolute_Krylov_tolerance(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_absolute_Krylov_tolerance(self)

    def get_scotch_strategy(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_scotch_strategy(self)

    def get_nested_dissection_parameter(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_nested_dissection_parameter(self)

    def get_matrix_reordering_method(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_matrix_reordering_method(self)

    def get_GramSchmidt_type(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_GramSchmidt_type(self)

    def get_maximum_rank(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_maximum_rank(self)

    def get_factor_nonzeros(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_factor_nonzeros(self)

    def get_factor_memory(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_factor_memory(self)

    def get_Krylov_iterations(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_Krylov_iterations(self)

    def get_mc64job(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_mc64job(self)

    def use_HSS(self, *args):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_use_HSS(self, *args)

    def get_minimum_HSS_size(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_minimum_HSS_size(self)

    def get_relative_compression_tolerance(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_relative_compression_tolerance(self)

    def get_absolute_compression_tolerance(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_absolute_compression_tolerance(self)

    def get_Krylov_solver(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_Krylov_solver(self)

    def get_rank_pattern(self):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolver_get_rank_pattern(self)
CStrumpackSparseSolver_swigregister = _StrumpackSparseSolverMPI.CStrumpackSparseSolver_swigregister
CStrumpackSparseSolver_swigregister(CStrumpackSparseSolver)

class ZStrumpackSparseSolver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ZStrumpackSparseSolver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ZStrumpackSparseSolver, name)
    __repr__ = _swig_repr

    def __init__(self, argc, verb=True, root=True):
        this = _StrumpackSparseSolverMPI.new_ZStrumpackSparseSolver(argc, verb, root)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _StrumpackSparseSolverMPI.delete_ZStrumpackSparseSolver
    __del__ = lambda self: None

    def set_from_options(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_from_options(self)

    def set_from_options_no_warning_unrecognized(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_from_options_no_warning_unrecognized(self)

    def set_matrix(self, A):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_matrix(self, A)

    def set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern=False):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern)

    def reorder(self, nx=1, ny=1, nz=1):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_reorder(self, nx, ny, nz)

    def factor(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_factor(self)

    def solve(self, b, x, use_initial_guess=False):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_solve(self, b, x, use_initial_guess)

    def set_maximum_Krylov_iterations(self, maxit):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_maximum_Krylov_iterations(self, maxit)

    def set_gmres_restart(self, m):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_gmres_restart(self, m)

    def set_relative_Krylov_tolerance(self, tol):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_relative_Krylov_tolerance(self, tol)

    def set_absolute_Krylov_tolerance(self, tol):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_absolute_Krylov_tolerance(self, tol)

    def set_scotch_strategy(self, strat):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_scotch_strategy(self, strat)

    def set_nested_dissection_parameter(self, nd_param):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_nested_dissection_parameter(self, nd_param)

    def set_matrix_reordering_method(self, m):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_matrix_reordering_method(self, m)

    def set_GramSchmidt_type(self, t):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_GramSchmidt_type(self, t)

    def set_mc64job(self, job):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_mc64job(self, job)

    def set_Krylov_solver(self, solver_type):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_Krylov_solver(self, solver_type)

    def set_minimum_HSS_size(self, s):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_minimum_HSS_size(self, s)

    def set_relative_compression_tolerance(self, rctol):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_relative_compression_tolerance(self, rctol)

    def set_absolute_compression_tolerance(self, actol):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_absolute_compression_tolerance(self, actol)

    def set_rank_pattern(self, p):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_rank_pattern(self, p)

    def set_verbose(self, v=True):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_set_verbose(self, v)

    def get_maximum_Krylov_iterations(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_maximum_Krylov_iterations(self)

    def get_gmres_restart(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_gmres_restart(self)

    def get_relative_Krylov_tolerance(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_relative_Krylov_tolerance(self)

    def get_absolute_Krylov_tolerance(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_absolute_Krylov_tolerance(self)

    def get_scotch_strategy(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_scotch_strategy(self)

    def get_nested_dissection_parameter(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_nested_dissection_parameter(self)

    def get_matrix_reordering_method(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_matrix_reordering_method(self)

    def get_GramSchmidt_type(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_GramSchmidt_type(self)

    def get_maximum_rank(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_maximum_rank(self)

    def get_factor_nonzeros(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_factor_nonzeros(self)

    def get_factor_memory(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_factor_memory(self)

    def get_Krylov_iterations(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_Krylov_iterations(self)

    def get_mc64job(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_mc64job(self)

    def use_HSS(self, *args):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_use_HSS(self, *args)

    def get_minimum_HSS_size(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_minimum_HSS_size(self)

    def get_relative_compression_tolerance(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_relative_compression_tolerance(self)

    def get_absolute_compression_tolerance(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_absolute_compression_tolerance(self)

    def get_Krylov_solver(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_Krylov_solver(self)

    def get_rank_pattern(self):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_get_rank_pattern(self)
ZStrumpackSparseSolver_swigregister = _StrumpackSparseSolverMPI.ZStrumpackSparseSolver_swigregister
ZStrumpackSparseSolver_swigregister(ZStrumpackSparseSolver)

class SStrumpackSparseSolverMPI(SStrumpackSparseSolver):
    __swig_setmethods__ = {}
    for _s in [SStrumpackSparseSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SStrumpackSparseSolverMPI, name, value)
    __swig_getmethods__ = {}
    for _s in [SStrumpackSparseSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SStrumpackSparseSolverMPI, name)
    __repr__ = _swig_repr

    def __init__(self, mpi_comm, argc, verb=True):
        this = _StrumpackSparseSolverMPI.new_SStrumpackSparseSolverMPI(mpi_comm, argc, verb)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _StrumpackSparseSolverMPI.delete_SStrumpackSparseSolverMPI
    __del__ = lambda self: None

    def set_matrix(self, A):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolverMPI_set_matrix(self, A)

    def set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern):
        return _StrumpackSparseSolverMPI.SStrumpackSparseSolverMPI_set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern)
SStrumpackSparseSolverMPI_swigregister = _StrumpackSparseSolverMPI.SStrumpackSparseSolverMPI_swigregister
SStrumpackSparseSolverMPI_swigregister(SStrumpackSparseSolverMPI)

class DStrumpackSparseSolverMPI(DStrumpackSparseSolver):
    __swig_setmethods__ = {}
    for _s in [DStrumpackSparseSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DStrumpackSparseSolverMPI, name, value)
    __swig_getmethods__ = {}
    for _s in [DStrumpackSparseSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DStrumpackSparseSolverMPI, name)
    __repr__ = _swig_repr

    def __init__(self, mpi_comm, argc, verb=True):
        this = _StrumpackSparseSolverMPI.new_DStrumpackSparseSolverMPI(mpi_comm, argc, verb)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _StrumpackSparseSolverMPI.delete_DStrumpackSparseSolverMPI
    __del__ = lambda self: None

    def set_matrix(self, A):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolverMPI_set_matrix(self, A)

    def set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern):
        return _StrumpackSparseSolverMPI.DStrumpackSparseSolverMPI_set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern)
DStrumpackSparseSolverMPI_swigregister = _StrumpackSparseSolverMPI.DStrumpackSparseSolverMPI_swigregister
DStrumpackSparseSolverMPI_swigregister(DStrumpackSparseSolverMPI)

class CStrumpackSparseSolverMPI(CStrumpackSparseSolver):
    __swig_setmethods__ = {}
    for _s in [CStrumpackSparseSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CStrumpackSparseSolverMPI, name, value)
    __swig_getmethods__ = {}
    for _s in [CStrumpackSparseSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CStrumpackSparseSolverMPI, name)
    __repr__ = _swig_repr

    def __init__(self, mpi_comm, argc, verb=True):
        this = _StrumpackSparseSolverMPI.new_CStrumpackSparseSolverMPI(mpi_comm, argc, verb)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _StrumpackSparseSolverMPI.delete_CStrumpackSparseSolverMPI
    __del__ = lambda self: None

    def set_matrix(self, A):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolverMPI_set_matrix(self, A)

    def set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern):
        return _StrumpackSparseSolverMPI.CStrumpackSparseSolverMPI_set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern)
CStrumpackSparseSolverMPI_swigregister = _StrumpackSparseSolverMPI.CStrumpackSparseSolverMPI_swigregister
CStrumpackSparseSolverMPI_swigregister(CStrumpackSparseSolverMPI)

class ZStrumpackSparseSolverMPI(ZStrumpackSparseSolver):
    __swig_setmethods__ = {}
    for _s in [ZStrumpackSparseSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ZStrumpackSparseSolverMPI, name, value)
    __swig_getmethods__ = {}
    for _s in [ZStrumpackSparseSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ZStrumpackSparseSolverMPI, name)
    __repr__ = _swig_repr

    def __init__(self, mpi_comm, argc, verb=True):
        this = _StrumpackSparseSolverMPI.new_ZStrumpackSparseSolverMPI(mpi_comm, argc, verb)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _StrumpackSparseSolverMPI.delete_ZStrumpackSparseSolverMPI
    __del__ = lambda self: None

    def set_matrix(self, A):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolverMPI_set_matrix(self, A)

    def set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern):
        return _StrumpackSparseSolverMPI.ZStrumpackSparseSolverMPI_set_csr_matrix(self, N, row_ptr, col_ind, values, symmetric_pattern)
ZStrumpackSparseSolverMPI_swigregister = _StrumpackSparseSolverMPI.ZStrumpackSparseSolverMPI_swigregister
ZStrumpackSparseSolverMPI_swigregister(ZStrumpackSparseSolverMPI)

# This file is compatible with both classic and new-style classes.


