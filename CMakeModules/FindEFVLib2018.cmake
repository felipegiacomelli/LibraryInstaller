# Find EFVLib2018
#
# BUILD_TYPE_OUTPUT_DIRECTORY   - Release or Debug (CASE SENSITIVE)
# LIBRARY_TYPE_OUTPUT_DIRECTORY - Shared or Static (CASE SENSITIVE)
#
# The EFVLibConfig.cmake file is by default at <$ENV{EFVLIB2018_DIR}/BUILD_TYPE_OUTPUT_DIRECTORY/LIBRARY_TYPE_OUTPUT_DIRECTORY>
# NOTE: ${EFVLIB2018_DIR} = $ENV{EFVLIB2018_DIR}/BUILD_TYPE_OUTPUT_DIRECTORY/LIBRARY_TYPE_OUTPUT_DIRECTORY
#
# EFVLIB2018_FOUND              -
# EFVLIB2018_INCLUDE_DIR        -
# EFVLIB2018_LIBRARIES          -

include (${EFVLIB2018_DIR}/EFVLib2018Config.cmake)
find_path (EFVLIB2018_INCLUDE_DIR Utils/Point.hpp ${EFVLIB2018_DIR}/include)
if (BUILD_SHARED_LIBS)
    find_library (EFVLIB2018_LIBRARY_DIR Utils.so ${EFVLIB2018_DIR}/libs)
else ()
    find_library (EFVLIB2018_LIBRARY_DIR Utils.a ${EFVLIB2018_DIR}/libs)
endif()

set (EFVLIB2018_COMPONENTS BoostInterface BoundaryCondition Fields Grid Operators Utils PetscInterface Simulator VariableComputer)

set (EFVLIB2018_FOUND FALSE)
if (EFVLIB2018_INCLUDE_DIR)
    if (EFVLIB2018_LIBRARY_DIR)
        set (EFVLIB2018_FOUND TRUE)
        set (EFVLIB2018_INCLUDE_DIR ${EFVLIB2018_INCLUDE_DIR})
        set (EFVLIB2018_LIBRARIES ${EFVLIB2018_COMPONENTS})
    endif ()
endif ()

if (EFVLIB2018_FOUND)
    message (STATUS "Found EFVLib: ${EFVLIB2018_DIR}")
else ()
    message (STATUS "Could not find EFVLib")
endif ()

# Debug this script - useful information
# message ("\n-- EFVLIB2018_FOUND: ${EFVLIB2018_FOUND}")
# message ("\n-- EFVLIB2018_INCLUDE_DIR: ${EFVLIB2018_INCLUDE_DIR}")
# message ("\n-- EFVLIB2018_LIBRARIES: ${EFVLIB2018_LIBRARIES}")
