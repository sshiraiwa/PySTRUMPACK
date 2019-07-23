"""

  Petra-M setuptools based setup module.

"""
import os
from os import path, listdir
from setuptools import setup, find_packages, Extension
# To use a consistent encoding
from codecs import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()
    
import numpy
numpy_include = numpy.get_include()

try:
    import mpi4py
    mpi4py_include = mpi4py.get_include()
except ImportError:
    mpi4py_include = None

strumpackincdir = os.getenv('STRUMPACKINCDIR')
strumpacklnkdir = os.getenv('STRUMPACKLNKDIR')

subs = ['HSS', 'BLR', 'dense', 'misc', 'sparse']
strumpackincsubdirs = [os.path.join(strumpackincdir, x) for x in subs]
include_dirs=([strumpackincdir,] + strumpackincsubdirs + 
              [numpy_include,])
library_dirs = [strumpacklnkdir,]

include_dirs = [x for x in include_dirs if len(x) > 0]
library_dirs = [x for x in library_dirs if len(x) > 0]
print(library_dirs)
print(include_dirs)

base = "STRUMPACK"
modules = ["StrumpackSparseSolver",]

if  mpi4py_include is not None:
    include_dirs.append(mpi4py_include)
#    modules.extend(["StrumpackSparseSolverMPI",
#                    "StrumpackSparseSolverMPIDist",])

 
ext_modules = [Extension("_"+n,
                        [path.join(base, n  + "_wrap.cxx"), ],
                         include_dirs = include_dirs,
                        # extra_compile_args = ['-std=c++11',],
                         extra_link_args = ['-DSWIG_TYPE_TABLE=PySTRUMPACK'],
                         library_dirs = library_dirs,
                         libraries = ['strumpack',])
               for n in modules]

setup(
    name='PySTRUMPACK',
    version='3.1.1',

    description='PySTRUMPACK',
    long_description=long_description,
    url='https://github.com/sshiraiwa/PySTRUMPAKC',
    author='S. Sihraiwa',
    author_email='shiraiwa@psfc.mit.edu',
    license='LGPL-2.1',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Physics'
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='Strumpack Sparse Linear Solver',
    packages=find_packages(),
    install_requires=[],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
    ext_modules = ext_modules,
)
