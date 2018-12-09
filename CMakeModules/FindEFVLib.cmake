# Find the glorious and almighty EFVLib
#
# BUILD_TYPE_OUTPUT_DIRECTORY   - Release or Debug (CASE SENSITIVE)
# LIBRARY_TYPE_OUTPUT_DIRECTORY - Shared or Static (CASE SENSITIVE)
#
# The EFVLibConfig.cmake file is by default at <$ENV{EFVLIB_DIR}/BUILD_TYPE_OUTPUT_DIRECTORY/LIBRARY_TYPE_OUTPUT_DIRECTORY>
# NOTE: ${EFVLIB_DIR} = $ENV{EFVLIB_DIR}/BUILD_TYPE_OUTPUT_DIRECTORY/LIBRARY_TYPE_OUTPUT_DIRECTORY
#
# EFVLIB_FOUND       		-
# EFVLIB_INCLUDE_DIR 		-
# EFVLIB_LIBRARIES 			-

include (${EFVLIB_DIR}/EFVLibConfig.cmake)
find_path (EFVLIB_INCLUDE_DIR Utils/Array3D.h ${EFVLIB_DIR}/include)
if (BUILD_SHARED_LIBS)
	find_library (EFVLIB_LIBRARY_DIR Utils.so ${EFVLIB_DIR}/libs)
else ()
	find_library (EFVLIB_LIBRARY_DIR Utils.a ${EFVLIB_DIR}/libs)
endif()

set (EFVLIB_COMPONENTS BoostInterface BoundaryCondition Fields Grid IO MuParser NumericalAnalysis Operators ParallelToolkit ScriptSystem Utils PetscInterface Simulator SolverMask VariableComputer)

set (EFVLIB_FOUND FALSE)
if (EFVLIB_INCLUDE_DIR)
	if (EFVLIB_LIBRARY_DIR)
		set (EFVLIB_FOUND TRUE)
		set (EFVLIB_INCLUDE_DIR ${EFVLIB_INCLUDE_DIR})
		set (EFVLIB_LIBRARIES ${EFVLIB_COMPONENTS})
	endif ()
endif ()

if (EFVLIB_FOUND)
	message ("-- Found EFVLib: ${EFVLIB_DIR}")
else ()
	message ("\n\n-- Could not find EFVLib.\n\n")
endif ()

# Debug this script - useful information
# message ("\n-- EFVLIB_FOUND: ${EFVLIB_FOUND}")
# message ("\n-- EFVLIB_INCLUDE_DIR: ${EFVLIB_INCLUDE_DIR}")
# message ("\n-- EFVLIB_LIBRARIES: ${EFVLIB_LIBRARIES}")
