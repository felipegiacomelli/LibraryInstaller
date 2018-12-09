# Find the CGNS includes and library
#
# CGNS_INCLUDE_DIR - where to find cgns.h, etc.
# CGNS_LIBRARIES   - list of fully qualified libraries to link against when using CGNS.
# CGNS_FOUND       - do not attempt to use CGNS if "no" or undefined.

find_path(CGNS_INCLUDE_DIR cgnslib.h ${CGNS_DIR}/include NO_DEFAULT_PATH)

find_library(CGNS_LIBRARY cgns ${CGNS_DIR}/lib NO_DEFAULT_PATH)

set(CGNS_FOUND "NO")
if (CGNS_INCLUDE_DIR)
    if (CGNS_LIBRARY)
        set(CGNS_LIBRARIES ${CGNS_LIBRARY})
        set(CGNS_FOUND "YES")
    endif ()
endif ()

if (CGNS_FIND_REQUIRED AND NOT CGNS_FOUND)
    message(SEND_ERROR "Unable to find the requested CGNS libraries.")
endif ()

# handle the QUIETLY and REQUIRED arguments and set CGNS_FOUND to TRUE if
# all listed variables are TRUE
include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(CGNS DEFAULT_MSG CGNS_LIBRARY CGNS_INCLUDE_DIR)

mark_as_advanced(CGNS_INCLUDE_DIR CGNS_LIBRARY)
