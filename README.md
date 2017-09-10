# PyStrumpackSparse


## install

1) build strumpack as a shared library
cmake .. -DBUILD_SHARED_LIBS=1

ln -s <strumpack source>/src include

2) edit setup.py to add include and library directories

include_dirs=["include",
              numpy_include,
              "/opt/local/include/mpich-mp",
              "/Users/shiraiwa/sandbox/include",
              "../scotch_6.0.4/include"]
library_dirs = ["/Users/shiraiwa/sandbox/lib",]
