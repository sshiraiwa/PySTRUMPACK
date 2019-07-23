from __future__ import print_function

import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from STRUMPACK import *

spss = SStrumpackSolver()
spss.set_verbose(0)
spss.set_maxit(10)

print(spss.get_verbose())
print(spss.get_maxit())
