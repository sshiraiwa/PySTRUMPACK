import six
import numpy as np
import warnings

from scipy.sparse import csr_matrix

Sp_attrs = ['hss', 'hss_front_size', 'rctol', 'actol', 'mc64job']

class Sp():
    def __init__(self, **kwargs):
        self.gstype = 'classical'
        self.Krylov_solver = 'auto'
        self.reordering_method = 'metis'
        self.atol = 1e-10
        self.rtol = 1e-6
        self.rctol = 0.01
        self.actol = 1e10
        self.maxit = 500
        self.restart = 30
        self.hss_front_size = 2500
        self.nd_param = 8
        self.rank_offset = 128
        self.max_rank = 2000
        self.mc64job = 0
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

    @classmethod            
    def generate_sp_solver(cls, dtype):
        from .StrumpackSparseSolver import SStrumpackSparseSolver, DStrumpackSparseSolver, CStrumpackSparseSolver, ZStrumpackSparseSolver        
        if dtype == np.float32:
            return SStrumpackSparseSolver([])
        elif dtype == np.float64:
            return DStrumpackSparseSolver([])
        elif dtype == np.complex64:
            return CStrumpackSparseSolver([])            
        elif dtype == np.complex128:
            return ZStrumpackSparseSolver([])
        else:
            assert False, "Not supported data type"

    def set_solver(self, dtype):
        if self.solver is not None:
            if self.solver_dtype != dtype:
                warnings.warn("differet data type is used, previous solver is discared. prev. solver for " + str(self.solver_dtype) + ": new solver for "+str(dtype), warnings.UserWarning)
        self.solver = self.generate_sp_solver(dtype)                

    def set_param(self, name, value):
        setattr(self, name, value)
        
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
        self.indptr = np.ascontiguousarray(A.indptr, dtype=np.int32)
        self.indices = np.ascontiguousarray(A.indices, dtype=np.int32)
        self.data = np.ascontiguousarray(A.data)
        self.solver.set_csr_matrix(self.matrix_size,
                                   self.indptr,
                                   self.indices,
                                   self.data,
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

        self.solver.use_HSS(self.hss)
        self.solver.set_minimum_HSS_size(self.hss_front_size)
        self.solver.set_relative_compression_tolerance(self.rctol)
        self.solver.set_absolute_compression_tolerance(self.actol)
        self.solver.set_mc64job(self.mc64job)
        
        returncode = self.solver.solve(b, x)
        return returncode, x
    
    def set_gmres_restart(self, m):
        pass
    
class SpMPI(Sp):
    @classmethod            
    def generate_sp_solver(cls, dtype):
        from mpi4py import MPI        
        from .StrumpackSparseSolverMPI import SStrumpackSparseSolverMPI, DStrumpackSparseSolverMPI, CStrumpackSparseSolverMPI, ZStrumpackSparseSolverMPI
        
        comm = MPI.COMM_WORLD
        
        if dtype == np.float32:
            return SStrumpackSparseSolverMPI(comm, [])
        elif dtype == np.float64:
            return DStrumpackSparseSolverMPI(comm, [])
        elif dtype == np.complex64:
            return CStrumpackSparseSolverMPI(comm, [])            
        elif dtype == np.complex128:
            return ZStrumpackSparseSolverMPI(comm, [])
        else:
            assert False, "Not supported data type"

class SpMPIDist(SpMPI):
    @classmethod            
    def generate_sp_solver(cls, dtype):
        from mpi4py import MPI                
        from .StrumpackSparseSolverMPIDist import SStrumpackSparseSolverMPIDist, DStrumpackSparseSolverMPIDist, CStrumpackSparseSolverMPIDist, ZStrumpackSparseSolverMPIDist
        comm = MPI.COMM_WORLD
        
        if dtype == np.float32:
            return SStrumpackSparseSolverMPIDist(comm, [])
        elif dtype == np.float64:
            return DStrumpackSparseSolverMPIDist(comm, [])
        elif dtype == np.complex64:
            return CStrumpackSparseSolverMPIDist(comm, [])            
        elif dtype == np.complex128:
            return ZStrumpackSparseSolverMPIDist(comm, [])
        else:
            assert False, "Not supported data type"


    def set_distributed_csr_matrix(self, A, symmetric_pattern = False):
        if not isinstance(A, csr_matrix) and hasattr(A, 'tocsr'):
            try:
                A = A.tocsr()
            except:
                pass
        assert isinstance(A, csr_matrix), "input matrix is not scipy.sparse.csr_matrix"
        
        from mpi4py import MPI                
        comm = MPI.COMM_WORLD        
        self.set_solver(A.dtype)

        rows = comm.allgather(A.shape[0])
        assert np.sum(rows) == A.shape[1], "input matrix is not diagonal"
        
        dist = np.hstack((0, np.cumsum(rows)))
        self.solver_dtype = A.dtype
        self.matrix_size = A.shape[0]
        self.indptr = np.ascontiguousarray(A.indptr, dtype=np.int32)
        self.indices = np.ascontiguousarray(A.indices, dtype=np.int32)
        self.data = np.ascontiguousarray(A.data)
        self.dist = np.ascontiguousarray(dist, dtype=np.int32)
        self.solver.set_distributed_csr_matrix(self.matrix_size,
                                               self.indptr,
                                               self.indices,
                                               self.data,
                                               self.dist,
                                           symmetric_pattern = symmetric_pattern)
            
