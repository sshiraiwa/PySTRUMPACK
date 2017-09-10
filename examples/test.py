from __future__ import print_function

import numpy as np
from scipy.sparse import csr_matrix
from Strumpack import Sp

A = csr_matrix([[1,1,0,],[0, 2,1], [0, 1, 0]], dtype=np.float)

s = Sp()
s.set_csr_matrix(A)
print(s.solve(np.array([1,2,3.], dtype=float)))

