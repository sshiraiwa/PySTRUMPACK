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

include_dirs=["include",
              numpy_include,
              "/opt/local/include/mpich-mp",
              "/Users/shiraiwa/sandbox/include",
              "../scotch_6.0.4/include"]
library_dirs = ["/Users/shiraiwa/sandbox/lib",]
                              
base = "Strumpack"
sp_libraries = ['strumpack_sparse']


ext_modules = [Extension("_StrumpackSparseSolver",
                        [path.join(base,"StrumpackSparseSolver_wrap.cxx"), ],
                         include_dirs = include_dirs,
                         extra_compile_args = ['-std=gnu++0x'],
                         library_dirs = library_dirs,                         
                         libraries = sp_libraries)]


setup(
    name='PyStrumpackSparse',
    version='1.1.0',

    description='PyStrumpackSparse',
    long_description=long_description,
    url='https://github.com/sshiraiwa/PyStrumpackSparse',
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
