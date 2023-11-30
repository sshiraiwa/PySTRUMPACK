"""

  Setup script for PySTRUMPACK 

"""
import sys
import os

import shutil
import subprocess
from subprocess import DEVNULL 

from setuptools import setup, find_packages, Extension
from setuptools.command.install import install as _install
from distutils.command.build import build as _build
from setuptools.command.build_py import build_py as _build_py
from setuptools.command.build_ext import build_ext as _build_ext
from setuptools.command.install_egg_info import install_egg_info as _install_egg_info
from setuptools.command.install_scripts import install_scripts as _install_scripts
from setuptools.command.install_lib import install_lib as _install_lib

# this stops working after setuptools (56)
#try:
#    from setuptools._distutils.command.clean import clean as _clean
#except ImportError:
from distutils.command.clean import clean as _clean

import numpy

try:
    import mpi4py
    has_mpi4py = True
except ImportError:
    has_mpi4py = False


### global variables
is_configured = False
prefix = ''

verbose = -1
swig_only = False
skip_install = False
run_swig = False
clean_swig = False
dry_run = False

cc_command = 'cc' if os.getenv("CC") is None else os.getenv("CC")
cxx_command = 'c++' if os.getenv("CC") is None else os.getenv("CXX")
mpicc_command = 'mpicc' if os.getenv("MPICC") is None else os.getenv("MPICC")
mpicxx_command = 'mpic++' if os.getenv("MPICXX") is None else os.getenv("MPICXX")
cxx11_flag = '-std=c++11' if os.getenv("CXX11FLAG") is None else os.getenv("CXX11FLAG")

strumpackincdir = ''
strumpacklnkdir = ''

extlib_dirs = []
ext_libs = []

### meta data
rootdir = os.path.abspath(os.path.dirname(__file__))
def long_description():
    with open(os.path.join(rootdir, 'README.md'), encoding='utf-8') as f:
        return f.read()
    
platforms = """
Mac OS X
Linux
"""
keywords = """
scientific computing
sparse solver
"""
metadata = {'name':'PySTRUMPACK',
            'version':'7.2.0.0',
            'description'      : __doc__.strip(),
            'long_description' : long_description(),
            'long_description_content_type':"text/markdown",
            'url'              :'https://github.com/sshiraiwa/PySTRUMPAKC',
            'download_url'     :'https://github.com/sshiraiwa/PySTRUMPAKC',
            'classifiers'      :['Development Status :: 4 - Beta',
                                 'Intended Audience :: Developers',
                                 'Topic :: Scientific/Engineering :: Physics',
                                 'License :: OSI Approved :: BSD License',
                                 'Programming Language :: Python :: 3.6',
                                 'Programming Language :: Python :: 3.7',
                                 'Programming Language :: Python :: 3.8',  ],
            'keywords'         : [k for k in keywords.split('\n')    if k],
            'platforms'        : [p for p in platforms.split('\n')   if p],
            'license'          : 'BSD-3',
            'author'           : '',
            'author_email'     : '',
            'maintainer'       : 'S. Shiraiwa',
            'maintainer_email' : 'shiraiwa@princeton.edu',}

##  utilities
def abspath(path):
    return os.path.abspath(os.path.expanduser(path))

def find_command(name):
    from shutil import which
    return which(name)

def make_call(command, target=''):
    '''
    call command
    '''
    if dry_run or verbose:
        print("calling ... " + " ".join(command))
    if dry_run:        
        return
    kwargs = {}
    if not verbose:
        kwargs['stdout'] = DEVNULL
        kwargs['stderr'] = DEVNULL
    p = subprocess.Popen(command, **kwargs)
    p.communicate()
    if p.returncode != 0:
        if target == '':
            target = " ".join(command)
        print("Failed when calling command: " + target)
        raise subprocess.CalledProcessError(p.returncode,
                                            " ".join(command))
    
def chdir(path):
    '''
    change directory
    '''
    pwd = os.getcwd()
    os.chdir(path)
    if verbose:
        print("Moving to a directory : " + path)
    return pwd

def remove_files(files):
    for f in files:
        if verbose:
            print("Removing : " + f)
        if dry_run:
            continue
        os.remove(f)
#
#
#
def print_config():
    print("----configuration----")
    print(" prefix", prefix)
    print(" strumpack include : " + strumpackincdir)
    print(" strumpack lib : " +  strumpacklnkdir)
    print(" generate swig wrapper : " + ("Yes" if swig_only else "No"))
    print(" c compiler : " + cc_command)
    print(" c++ compiler : " + cxx_command)
    print(" mpi-c compiler : " + mpicc_command)
    print(" mpi-c++ compiler : " + mpicxx_command)
    print(" dry-run : " + ("Yes" if dry_run else "No"))
    print("")
    
def configure_install(self):
    global prefix, dry_run
    global strumpackincdir, strumpacklnkdir
    global extlib_dirs, ext_libs
    global cc_command, cxx_command, mpicc_command, mpicxx_command
    global swig_only

    if hasattr(self, 'prefix'):
        prefix = self.prefix
    if hasattr(self, 'dry_run'):        
        dry_run = bool(self.dry_run)

    if self.strumpack_prefix == '':
        self.strumpack_prefix = self.prefix
        
    strumpackincdir = os.path.join(self.strumpack_prefix, 'include')
    strumpacklnkdir = os.path.join(self.strumpack_prefix, 'lib')

    extlib_dirs = []
    ext_libs = []

    #ext_libs = self.externals.split(',')    
    #extralib_dirs = [os.path.dirname(x) for x in ext_libs]
    #extralibs = [os.path.basename(x) for x in ext_libs]    
    if self.CC != '':
        cc_command = self.CC
    if self.CXX != '':
        cxx_command = self.CXX
    if self.MPICC != '':
        mpicc_command = self.MPICC
    if self.MPICXX != '':
        mpicxx_command = self.MPICXX

    if self.swig:
        swig_only = True
    global is_configured
    is_configured = True
        
def generate_wrapper(self):
    '''
    run swig.
    '''
    if dry_run or verbose:
        print("generating SWIG wrapper")
    def ifiles():
        ifiles = os.listdir()
        ifiles = [x for x in ifiles if x.endswith('.i')]
        ifiles = [x for x in ifiles if not x.startswith('#')]
        ifiles = [x for x in ifiles if not x.startswith('.')]                
        return ifiles

    def check_new(ifile):
        wfile = ifile[:-2]+'_wrap.cxx'
        if not os.path.exists(wfile):
            return True
        return os.path.getmtime(ifile) > os.path.getmtime(wfile)

    swig_command = find_command('swig')
    if swig_command is None:
        assert False, "SWIG is not installed"

    pwd = chdir(os.path.join(rootdir, 'src', 'STRUMPACK'))

    #swigflag = '-Wall -c++ -python -fastproxy -DSWIGWORDSIZE32 -olddefs -keyword'.split(' ')
    swigflag = '-Wall -c++ -python -fastproxy -DSWIGWORDSIZE64 -olddefs -keyword'.split(' ')

    stflag = ['-I'+ strumpackincdir]

    if has_mpi4py:
        stflag.append('-I'+ mpi4py.get_include())

    for file in ifiles():
        #if not check_new(file):
        #    continue
        command = [swig_command] + swigflag + stflag + [file]
        make_call(command)

    os.chdir(pwd)


def clean_wrapper(self):

    pwd = chdir(os.path.join(rootdir, 'src','STRUMPACK'))
    
    wfiles = [x for x in os.listdir() if x.endswith('_wrap.cxx')]
    remove_files(wfiles)
    chdir(pwd)

def clean_so(self):
    pass

class Install(_install):
    '''
    called when pyton setup.py install
    '''
    user_options = _install.user_options + [
        ('swig', None, 'Run Swig'),
        ('strumpack-prefix', None, 'prefix of strumpack'),
        #('externals', None, 'extenral libraries to be linked'),
        ('CC=', None, 'c compiler'),
        ('CXX=', None, 'c++ compiler'),
        ('MPICC=', None, 'mpic compiler'),
        ('MPICXX=', None, 'mpic++ compiler'),
    ]

    def initialize_options(self):
        _install.initialize_options(self)

        self.swig = True
        self.external_libs = ''
        self.CC = ''
        self.CXX = ''
        self.MPICC = ''
        self.MPICXX = ''
        self.strumpack_prefix = ''
        if os.getenv('STRUMPACK_PREFIX') is not None:
            self.strumpack_prefix = os.getenv('STRUMPACK_PREFIX')
            
    def finalize_options(self):
        _install.finalize_options(self)
        if not is_configured:
            configure_install(self)
            print_config()

        if swig_only:
            generate_wrapper(self)
        #else:
        #    #self.run_command("build_py")
        #    #self.do_egg_install()
        #    _install.run(self)
        
#    def run(self):

class BuildPy(_build_py):
    def run(self):
        self.run_command("build_ext")
        return _build_py.run(self)
    
class BuildExt(_build_ext):
    user_options = _build_ext.user_options + [
        ('swig', None, 'Run Swig and exit'),
        ('build-only', None, 'Skip final install stage to prefix'),
        ('strumpack-prefix=', None, 'prefix of strumpack'),
        #('externals', None, 'extenral libraries to be linked'),
        ('CC=', None, 'c compiler'),
        ('CXX=', None, 'c++ compiler'),
        ('MPICC=', None, 'mpic compiler'),
        ('MPICXX=', None, 'mpic++ compiler'),
    ]

    def initialize_options(self):
        _build_ext.initialize_options(self)

        self.swig = False
        self.build_only = False
        self.external_libs = ''
        self.CC = ''
        self.CXX = ''
        self.MPICC = ''
        self.MPICXX = ''
        self.strumpack_prefix = ''
        if os.getenv('STRUMPACK_PREFIX') is not None:
            self.strumpack_prefix = os.getenv('STRUMPACK_PREFIX')

    def finalize_options(self):
        _build_ext.finalize_options(self)
        

        if not is_configured:
            configure_install(self)
            print_config()
        
        numpy_include = [numpy.get_include()]
        if has_mpi4py:
            mpi4py_include = [mpi4py.get_include()]
        else:
            mpi4py_include = []
        
        subs = ['HSS', 'HODLR', 'BLR', 'dense', 'misc', 'sparse', 'clustering']
        strumpackincsubdirs = [os.path.join(strumpackincdir, x) for x in subs]
        include_dirs=([strumpackincdir,] + strumpackincsubdirs + 
                      numpy_include + mpi4py_include)
        
        library_dirs = [strumpacklnkdir] + extlib_dirs

        include_dirs = [x for x in include_dirs if len(x) > 0]
        library_dirs = [x for x in library_dirs if len(x) > 0]
        #libraries = ['strumpack', 'stdc++']
        libraries = []

        sclpk = os.getenv("SCALAPACKLINK")
        if sclpk is not None:
            print("SCALAPAK flag is given:" + sclpk)
            for x in sclpk.split():
                if x.startswith('-L'): 
                    library_dirs.append(x[2:])
                elif x.startswith('-l'):
                    libraries.append(x[2:])
                else:
                    assert False, "unsupported option :" + x

        for x in self.extensions:
            x.include_dirs.extend(include_dirs)
            x.library_dirs.extend(library_dirs)
            x.libraries.extend(libraries)

        #os.environ['CC'] = mpicc_command
        os.environ['CC'] = mpicxx_command
        os.environ['CXX'] = mpicxx_command

        self.inplace = 0
        
        #_build_ext.run(self)
        
class InstallEggInfo(_install_egg_info):
    def run(self):
        if not dry_run:
            _install_egg_info.run(self)
        else:
            print("skipping regular install_egg_info")

class InstallScripts(_install_scripts):
    def run(self):
        if not dry_run:
            _install_scripts.run(self)
        else:
            print("skipping regular install_scripts")

class InstallLib(_install_lib):
    def run(self):
        _install_lib.run(self)
        
class Clean(_clean):
    '''
    Called when python setup.py clean
    '''
    user_options = _clean.user_options + [
        ('swig', None,  'clean swig'),        
        ]

    def initialize_options(self):
        _clean.initialize_options(self)
        self.swig = False

    def run(self):
        global dry_run, verbose
        dry_run = self.dry_run
        verbose = bool(self.verbose)
        
        if self.swig or self.all:
            clean_wrapper(self)

        clean_so(self)
        
        os.chdir(rootdir)
        _clean.run(self)
            

def run_setup():
    setup_args = metadata.copy()

    base = "STRUMPACK"    
    modules = ["StrumpackSparseSolver",]

    extra_link_args = ["-lstrumpack_solve"]
    #extra_link_args = []
    ext_modules = [Extension("STRUMPACK."+"_"+n,
                             [os.path.join('src', base, n  + "_wrap.cxx"), ],
                             extra_compile_args = ['-std=c++11',],
                             extra_link_args=['-DSWIG_TYPE_TABLE=PySTRUMPACK'] + extra_link_args,
                             include_dirs=[],                             
                             library_dirs=[],
                             libraries=[])
                   for n in modules]

    setup(
        cmdclass = {'build_ext': BuildExt,
                    'build_py': BuildPy,
                    'install': Install,
                    'install_egg_info': InstallEggInfo,
                    'install_scripts': InstallScripts,
                    'install_lib': InstallLib,                    
                    'clean': Clean},
        
        install_requires=["numpy"],
        packages=find_packages('src'),
        package_dir={'': 'src'},        
        extras_require={},
        #data_files=[('data', datafiles)],
        entry_points={},
        #py_modules = ["StrumpackSparseSolver",],
        ext_modules = ext_modules,        
        **setup_args)

def main():
    run_setup()

if __name__ == '__main__':
    main()

