##   Makefile
##
##   default variable setting
##   
MAKE ?= $(shell which make)
PYTHON ?= $(shell which python)
INSTALL_PREFIX ?= /usr/local/

# serial compiler
#CXX_SER = g++
#CC_SER = g++

SWIG=$(shell which swig)
SWIGFLAG = -Wall -c++ -python

#
CC = ?= gcc
CXX = ?= g++
OMPCXXFLAG ?= -fopenmp

#Strumpack
STRUMPACKINCDIR ?= /usr/local/include
STRUMPACKLNKDIR ?= /usr/local/lib

#MPI
MPIINCDIR    ?= /usr/local/include/mpich
MPILNKDIR    ?= /usr/local/lib/mpich

MPI4PYINCDIR = $(shell $(PYTHON) -c "import mpi4py;print(mpi4py.get_include())")

# overwrite everything if you need to
include ./Makefile.local

MPI4PYINC  = -I$(MPI4PYINCDIR)
STRUMPACKINC = -I$(STRUMPACKINCDIR)

INTERFACE = STRUMPACK
# export everything so that it is avaialbe in setup.py
IFILE = $(wildcard $(INTERFACE)/*.i)
ALLCXX = $(IFILE:.i=_wrap.cxx)

.PHONEY:clean cxx clean install

all: so
so: 
	$(PYTHON) setup.py build
debug:
	@echo $(ALLCXX)
cxx: $(ALLCXX)
	@echo $(ALLCXX)
STRUMPACK/%_wrap.cxx: STRUMPACK/%.i
	$(SWIG) $(SWIGFLAG) $(MPI4PYINC) $(STRUMPACKINC)  $<

install:
	$(PYTHON) setup.py install --prefix=$(INSTALL_PREFIX)
cleancxx:
	rm -f STRUMPACK/*.cxx
clean:
	rm -f STRUMPACK/*.o
	rm -rf build
	rm -rf dist

