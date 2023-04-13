cmake_minimum_required(VERSION 3.20.0)

project(STRUMPACK LANGUAGES CXX C)


option(USE_OPENMP  "Use OpenMP for on-node threading tasking" ON)
option(USE_CUDA    "Use CUDA for NVIDIA GPU acceleration" ON)
option(USE_PARMETIS    "Use Parmetis" ON)
option(USE_PTSCOTCH    "Use PT-Scotch" ON)
option(USE_SLATE    "Use SLATE" ON)
option(USE_BPACK    "Use Butterflypack" ON)
option(USE_ZFP    "Use ZFP" ON)

if(NOT STRUMPACK_PREFIX)
  set(STRUMPACK_PREFIX ${CMAKE_INSTALL_PREFIX})
endif()


list(APPEND CMAKE_PREFIX_PATH "${STRUMPACK_PREFIX}")
list(APPEND CMAKE_MODULE_PATH "${STRUMPACK_PREFIX}/lib/cmake/STRUMPACK")


find_package(BLAS)
find_package(LAPACK)

find_package(STRUMPACK)

message(STATUS OpenMP_FOUND ":" ${OpenMP_FOUND})
message(STATUS MPI_FOUND ":" ${MPI_FOUND})
message(STATUS CUDAToolkitFOUND ":" ${CUDAToolkit_FOUND})

message(STATUS BLAS_FOUND ":" ${BLAS_FOUND})
message(STATUS LAPACK_FOUND ":" ${LAPACK_FOUND})

message(STATUS METIS_FOUND ":" ${METIS_FOUND})
message(STATUS ParMETIS_FOUND ":" ${ParMETIS_FOUND})
message(STATUS SCOTCH_FOUND ":" ${SCOTCH_FOUND})
message(STATUS PTSCOTCH_FOUND ":" ${PTSCOTCH_FOUND})

message(STATUS slate_FOUND ":" ${slate_FOUND})

message(STATUS ZFP_FOUND ":" ${ZFP_FOUND})
message(STATUS ButterflyPACK_FOUND ":" ${ButterflyPACK_FOUND})

message(STATUS MKL_FOUND ":" ${MKL_FOUND})



# make target
add_library(strumpack_solve SHARED strumpack_solve.cpp)
if(USE_MPI)
  if(SCALAPACK_FOUND)
    target_link_libraries(strumpack_solve PUBLIC ${SCALAPACK_LIBRARIES})
  endif()
endif()
if(LAPACK_FOUND)
  target_link_libraries(strumpack_solve PUBLIC ${LAPACK_LIBRARIES})
endif()
if(BLAS_FOUND)
  target_link_libraries(strumpack_solve PUBLIC ${BLAS_LIBRARIES})
endif()

if(MKL_FOUND)
  target_link_libraries(strumpack_solve PUBLIC MKL::MKL)
  # target_link_libraries(strumpack PUBLIC MKL::MKL_DPCPP)
endif()

