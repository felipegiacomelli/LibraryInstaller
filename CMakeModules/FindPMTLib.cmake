# Find the glorious and almighty PMTLib
#
# BUILD_TYPE_OUTPUT_DIRECTORY   - Release or Debug (CASE SENSITIVE)
# LIBRARY_TYPE_OUTPUT_DIRECTORY - Shared or Static (CASE SENSITIVE)
#
# The PMTLibConfig.cmake file is by default at <$ENV{PMTLIB_DIR}/BUILD_TYPE_OUTPUT_DIRECTORY/LIBRARY_TYPE_OUTPUT_DIRECTORY>
# NOTE: ${PMTLIB_DIR} = $ENV{PMTLIB_DIR}/BUILD_TYPE_OUTPUT_DIRECTORY/LIBRARY_TYPE_OUTPUT_DIRECTORY
#
# PMTLIB_FOUND       		- 
# PMTLIB_INCLUDE_DIR 		- 
# PMTLIB_LIBRARIES 			-

include (${PMTLIB_DIR}/PMTLibConfig.cmake)
find_path (PMTLIB_INCLUDE_DIR DarcyFlow/CompressiveAccumulationAdder.h ${PMTLIB_DIR}/include)
if (BUILD_SHARED_LIBS)
	find_library (PMTLIB_LIBRARY_DIR DarcyFlow.so ${PMTLIB_DIR}/libs)
else ()
	find_library (PMTLIB_LIBRARY_DIR DarcyFlow.a ${PMTLIB_DIR}/libs)
endif()

set (PMTLIB_COMPONENTS DarcyFlow Geomechanics HeatTransfer Structural)

set (PMTLIB_FOUND FALSE)
if (PMTLIB_INCLUDE_DIR)
	if (PMTLIB_LIBRARY_DIR)
		set (PMTLIB_FOUND TRUE)
		set (PMTLIB_INCLUDE_DIR ${PMTLIB_INCLUDE_DIR})
		set (PMTLIB_LIBRARY_DIR ${PMTLIB_COMPONENTS})
	endif ()
endif ()

if (PMTLIB_FOUND)
	message ("-- Found PMTLib: ${PMTLIB_DIR}")
else ()
	message ("\n\n-- Could not find PMTLib.\n\n")
endif ()

# Debug this script - useful information
#message ("\n-- PMTLIB_FOUND: ${PMTLIB_FOUND}")
#message ("\n-- PMTLIB_INCLUDE_DIR: ${PMTLIB_INCLUDE_DIR}")
#message ("\n-- PMTLIB_LIBRARIES: ${PMTLIB_LIBRARIES}")
