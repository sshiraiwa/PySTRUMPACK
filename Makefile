##   Makefile
##
##   default variable setting
##   
MAKE=$(shell which make)
PYTHON=$(shell which python)
INSTALL_PREFIX=?/usr/local/

# serial compiler
CXX_SER = g++
CC_SER = g++

SWIG=$(shell which swig)
SWIGFLAG = -Wall -c++ -python

#Strumpack
STRUMPACKINCDIR= $(HOME)/sandbox/include
STRUMPACKLNKDIR= $(HOME)/sandbox/lib

#MPI
MPICHINCDIR    = /opt/local/include/mpich-mp
MPICHLNKDIR    = /opt/local/lib/mpich-mp
MPILIB = mpi
MPI4PYINCDIR = $(shell $(PYTHON) -c "import mpi4py;print mpi4py.get_include()")

#numpy
NUMPYINCDIR = $(shell $(PYTHON) -c "import numpy;print numpy.get_include()")

include ./Makefile.local

MPIINC  = -I$(MPIINCDIR)
MPI4PYINC  = -I$(MPI4PYINCDIR)
STRUMPACKINC = -I$(STRUMPACKINCDIR)
INTERFACE = Strumpack
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
%_wrap.cxx: %.i
	$(SWIG) $(SWIGFLAG) $(MPI4PYINC) $(STRUMPACKINC) $(MPIINC) $<

install:
	$(PYTHON) setup.py install --prefix=$(INSTALL_PREFIX)
cleancxx:
	rm -f $(SRC)/*.cxx
clean:
	rm -f $(SRC)/*.o
	rm -f setup_local.py

