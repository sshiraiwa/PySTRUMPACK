cmake_minimum_required(VERSION 3.20.0)

project(STRUMPACK LANGUAGES CXX C Fortran)

option(USE_MPI     "Build with MPI support" ON)
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

if(USE_MPI)
  find_package(MPI)
  if(NOT MPI_FOUND)
    set(USE_MPI OFF)
    message(WARNING "Configuring without MPI support.")
  endif()
endif()

if(DEFINED TPL_BLAS_LIBRARIES)
    set(BLAS_LIBRARIES ${TPL_BLAS_LIBRARIES})
    set(BLAS_FOUND TRUE)
else()
   find_package(BLAS)
   if(NOT BLAS_FOUND)
      message(WARNING
        "Could not find a BLAS library.\n"
        "This causes problem if BLAS is implicity linked by the compiler(wrapper)")
   endif()
endif()

if(DEFINED TPL_LAPACK_LIBRARIES)
    set(LAPACK_LIBRARIES ${TPL_LAPACK_LIBRARIES})
    set(LAPACK_FOUND TRUE)
else()
  find_package(LAPACK)
  if(NOT LAPACK_FOUND)
     message(WARNING
        "Could not find a LAPACK library.\n"
        "This causes problem if LAPACK is implicity linked by the compiler(wrapper)")
  endif()
endif()

if(DEFINED TPL_SCALAPACK_LIBRARIES)
  set(SCALAPACK_FOUND TRUE)
  set(SCALAPACK_LIBRARIES ${TPL_SCALAPACK_LIBRARIES})
else()
  find_package(SCALAPACK)
  if(NOT SCALAPACK_FOUND)
     message(WARNING
       "Could not find a SCALAPACK library.\n"
       "This causes problem if SCALAPACK is implicity linked by the compiler(wrapper)")
  else()
     set(SCALAPACK_LIBRARIES scalapack)
  endif()
endif()   
find_package(STRUMPACK)

message(STATUS OpenMP_FOUND ":" ${OpenMP_FOUND})
message(STATUS MPI_FOUND ":" ${MPI_FOUND} ${MPI_Fortran_LIBRARIES})
message(STATUS CUDAToolkitFOUND ":" ${CUDAToolkit_FOUND})

message(STATUS BLAS_FOUND ":" ${BLAS_LIBRARIES})
message(STATUS LAPACK_FOUND ":" ${LAPACK_LIBRARIES})
message(STATUS SCALAPACK_FOUND ":" ${SCALAPACK_LIBRARIES})
message(STATUS METIS_FOUND ":" ${METIS_FOUND})
message(STATUS ParMETIS_FOUND ":" ${ParMETIS_FOUND})
message(STATUS SCOTCH_FOUND ":" ${SCOTCH_FOUND})
message(STATUS PTSCOTCH_FOUND ":" ${PTSCOTCH_FOUND})

message(STATUS slate_FOUND ":" ${slate_FOUND})

message(STATUS ZFP_FOUND ":" ${ZFP_FOUND})
message(STATUS ButterflyPACK_FOUND ":" ${ButterflyPACK_FOUND})

message(STATUS MKL_FOUND ":" ${MKL_FOUND})

# prepare some compile/link flags
set(FPIC " -fPIC ")
set(LINK_FLAGS ${FPIC})

if (APPLE)
    set(SHARED_SC_COMPILE_FLAGS " -fPIC ")
    set(SHARED_SC_LINK_FLAGS_1 "-Wl,-force_load")
    set(SHARED_SC_LINK_FLAGS_2 "")
    set(SYMBOL_FLAG1  "-Wl,-exported_symbols_list")
    set(SYMBOL_FLAG2  ${CMAKE_CURRENT_SOURCE_DIR}/exported_symbols_list.txt)
    set(CMAKE_BUILD_WITH_INSTALL_NAME_DIR true)  # this writes full path using install_name_dir  
else()
    set(SHARED_SC_COMPILE_FLAGS " -fPIC")
    set(SHARED_SC_LINK_FLAGS_1 "-Wl,-whole-archive")
    set(SHARED_SC_LINK_FLAGS_2 "-Wl,-no-whole-archive")
    set(SYMBOL_FLAG1  "-Wl,--version-script=../exported_version_script.txt")
    set(SYMBOL_FLAG2  "")
endif()
set( IFLAG " -I")  
set(CMP_FLAG ${SHARED_SC_COMPILE_FLAGS}${IFLAG}${STRUMPACK_PREFIX}"/include")

# make target
add_library(strumpack_solve SHARED strumpack_solve.cpp)
target_compile_features(strumpack_solve PUBLIC cxx_std_14)

target_link_libraries(strumpack_solve PUBLIC
  ${SHARED_SC_LINK_FLAGS_1}
  ${STRUMPACK_PREFIX}/lib/libstrumpack.a
  ${SHARED_SC_LINK_FLAGS_2}
  )

if(USE_MPI)
  target_link_libraries(strumpack_solve PUBLIC
    MPI::MPI_CXX MPI::MPI_C ${MPI_Fortran_LIBRARIES})
  ## adding the MPI::MPI_Fortran target risks adding unwanted compile flags
endif()

if(OpenMP_FOUND)
  # if(OpenMP_C_FOUND)
  #   target_link_libraries(strumpack PRIVATE OpenMP::OpenMP_C)
  # endif()
  if(OpenMP_CXX_FOUND)
    target_link_libraries(strumpack_solve PUBLIC OpenMP::OpenMP_CXX)
  endif()
  # if(OpenMP_Fortran_FOUND)
  #   target_link_libraries(strumpack PRIVATE OpenMP::OpenMP_Fortran)
  # endif()
endif()

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

if(ParMETIS_FOUND)
  target_link_libraries(strumpack_solve PUBLIC ParMETIS::parmetis)
endif()
target_link_libraries(strumpack_solve PUBLIC METIS::metis)
if(SCOTCH_FOUND)
  target_link_libraries(strumpack_solve PUBLIC SCOTCH::scotch)
  if(SCOTCH_USES_PTHREADS)
    target_link_libraries(strumpack_solve PUBLIC Threads::Threads)
  endif()
endif()
if(PTSCOTCH_FOUND)
  target_link_libraries(strumpack_solve PUBLIC PTSCOTCH::ptscotch)
endif()

if(ZFP_FOUND)
  target_link_libraries(strumpack_solve PUBLIC zfp::zfp)
endif()

if(ButterflyPACK_FOUND)
  target_link_libraries(strumpack_solve PUBLIC
    ButterflyPACK::sbutterflypack
    ButterflyPACK::dbutterflypack
    ButterflyPACK::cbutterflypack
    ButterflyPACK::zbutterflypack)
endif()

if(slate_FOUND)
  target_link_libraries(strumpack_solve PUBLIC slate lapackpp blaspp)
endif()

if(CUDAToolkit_FOUND)
  target_link_libraries(strumpack_solve PUBLIC
    CUDA::cudart CUDA::cusolver CUDA::cublas)
endif()
if(MAGMA_FOUND)
  target_link_libraries(strumpack_solve PUBLIC MAGMA::magma)
endif()

if(hipblas_FOUND)
  target_link_libraries(strumpack_solve PUBLIC
    roc::hipblas roc::rocblas roc::rocsolver roc::hipsparse)
endif()

if(CombBLAS_FOUND)
  target_link_libraries(strumpack_solve PUBLIC CombBLAS::CombBLAS)
  target_include_directories(strumpack PRIVATE $ENV{COMBBLASAPP_DIR})
endif()

target_link_libraries(strumpack_solve PUBLIC
  ${SYMBOL_FLAG1}
  ${SYMBOL_FLAG2}			    
)
  
set_target_properties(strumpack_solve PROPERTIES 
                      COMPILE_FLAGS ${CMP_FLAG}
                      LINK_FLAGS ${LINK_FLAGS}
		      LINKER_LANGUAGE CXX
                      OUTPUT_NAME strumpack_solve )

install(TARGETS strumpack_solve
        DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
        )
