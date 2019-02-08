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
find_path (EFVLIB2018_INCLUDE_DIR Utils/Point.hpp HINTS ${EFVLIB2018_DIR}/include NO_DEFAULT_PATH)
find_library (EFVLIB2018_LIBRARY_DIR NAMES Utils.so Utils.a HINTS ${EFVLIB2018_DIR}/libs NO_DEFAULT_PATH)

set (EFVLIB2018_COMPONENTS BoostInterface BoundaryCondition Fields Grid Operators Utils PetscInterface Simulator VariableComputer)

set (EFVLIB2018_FOUND FALSE)
if (EFVLIB2018_INCLUDE_DIR)
    if (EFVLIB2018_LIBRARY_DIR)
        set (EFVLIB2018_FOUND TRUE)
        set (EFVLIB2018_INCLUDE_DIR ${EFVLIB2018_INCLUDE_DIR})
        set (EFVLIB2018_LIBRARIES ${EFVLIB2018_COMPONENTS})
    endif ()
endif ()

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(EFVLib2018 REQUIRED_VARS EFVLIB2018_LIBRARY_DIR EFVLIB2018_LIBRARIES EFVLIB2018_INCLUDE_DIR VERSION_VAR ${EFVLIB2018_VERSION})

mark_as_advanced(EFVLIB2018_INCLUDE_DIR EFVLIB2018_LIBRARY_DIR)
