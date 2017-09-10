import six
import numpy as np
import warnings

from scipy.sparse import csr_matrix

from .StrumpackSparseSolver import SStrumpackSparseSolver, DStrumpackSparseSolver, CStrumpackSparseSolver, ZStrumpackSparseSolver
class Sp():
    def __init__(self, **kwargs):
        self.gstype = 'classical'
        self.Krylov_solver = 'auto'
        self.reordering_method = 'metis'
        self.atol = 1e-10
        self.rtol = 1e-6
        self.rctrol = 0.01
        self.actol = 1e10
        self.maxit = 500
        self.restart = 30
        self.has_front_size = 2500
        self.nd_param = 8
        self.rank_offset = 128
        self.max_rank = 2000
        self.mc64job = 5
        self.print_ranks = ''
        self.q_power = 0
        self.separator_ordering_level = 1
        self.hss = False
        self.rank_pattern = 'adaptive'
        self.rank_factor = 1.0
        self.log_ranks = False
        self.use_METIS_NodeND = False
        self.verbose = True
        self.task_level = 3
        self.random_blocksize = 128
        self.rank_offset = 64
        self.random_distribution = 'normal' 
        self.random_engine = 'minstd_rand'
        self.minpart = 128

        self.solver = None
        self.solver_dtype = None

        for key in kwargs.keys():
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

    def set_solver(self, dtype):
        if self.solver is not None:
            if self.solver_dtype != dtype:
                warnings.warn("differet data type is used, previous solver is discared. prev. solver for " + str(self.solver_dtype) + ": new solver for "+str(dtype), warnings.UserWarning)
        if dtype == np.float32:
            self.solver = SStrumpackSparseSolver([])
        elif dtype == np.float64:
            self.solver = DStrumpackSparseSolver([])
        elif dtype == np.complex64:
            self.solver = CStrumpackSparseSolver([])            
        elif dtype == np.complex128:
            self.solver = ZStrumpackSparseSolver([])
        else:
            assert False, "Not supported data type"

    def set_csr_matrix(self, A, symmetric_pattern = False):
        if not isinstance(A, csr_matrix) and hasattr(A, 'tocsr'):
            try:
                A = A.tocsr()
            except:
                pass
        assert isinstance(A, csr_matrix), "input matrix is not scipy.sparse.csr_matrix"
        self.set_solver(A.dtype)
        self.solver_dtype = A.dtype
        self.matrix_size = A.shape[0]
        self.solver.set_csr_matrix(self.matrix_size,
                                  A.indptr, A.indices, A.data,
                                  symmetric_pattern = symmetric_pattern)
        
    def solve(self, b, initial_guess = None):
        if initial_guess is None:
            use_initila_guess = False
            x = b*0.0
        else:
            use_initila_guess = True
            x = initila_guess
        assert b.shape == x.shape, "b, and x should have the same shape"
        assert b.dtype == self.solver_dtype, "b and matrix should have the same data type"
        assert b.shape[0] == self.matrix_size, "b and matrix should have the same size"        
        returncode = self.solver.solve(b, x)
        return x
    
    def set_gmres_restart(self, m):
        pass
class SparseSolverMPI():
    pass

class SparseSolverMPIDist():
    pass
