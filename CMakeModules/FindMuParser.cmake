# Find the MUPARSER includes and library
#
# MUPARSER_INCLUDE_DIR - where to find MUPARSER.h, etc.
# MUPARSER_LIBRARIES   - list of fully qualified libraries to link against when using MUPARSER.
# MUPARSER_FOUND       - do not attempt to use MUPARSER if "no" or undefined.

find_path(MUPARSER_INCLUDE_DIR muParser.h ${MUPARSER_DIR}/include)

find_library(MUPARSER_LIBRARY muparser ${MUPARSER_DIR}/lib)

set(MUPARSER_FOUND "NO")
if (MUPARSER_INCLUDE_DIR)
    if (MUPARSER_LIBRARY)
        set(MUPARSER_LIBRARIES ${MUPARSER_LIBRARY})
        set(MUPARSER_FOUND "YES")
    endif ()
endif ()

if (MUPARSER_FIND_REQUIRED AND NOT MUPARSER_FOUND)
    message(SEND_ERROR "Unable to find the requested MUPARSER libraries.")
endif ()

# handle the QUIETLY and REQUIRED arguments and set MUPARSER_FOUND to TRUE if
# all listed variables are TRUE
include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(MUPARSER DEFAULT_MSG MUPARSER_LIBRARY MUPARSER_INCLUDE_DIR)

mark_as_advanced(MUPARSER_INCLUDE_DIR MUPARSER_LIBRARY)
