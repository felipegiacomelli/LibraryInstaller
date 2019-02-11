# Find Jonathan Richard Shewchuk's triangle

include (${TRIANGLE_DIR}/triangle_config.cmake)

find_path (TRIANGLE_INCLUDE_DIR triangle.h ${TRIANGLE_DIR})
find_library (TRIANGLE_LIBRARY_DIR triangle.so ${TRIANGLE_DIR})

set (TRIANGLE_COMPONENTS triangle)

set (TRIANGLE_FOUND FALSE)
if (TRIANGLE_INCLUDE_DIR)
    if (TRIANGLE_LIBRARY_DIR)
        set (TRIANGLE_FOUND TRUE)
        set (TRIANGLE_INCLUDE_DIR ${TRIANGLE_INCLUDE_DIR})
        set (TRIANGLE_LIBRARIES ${TRIANGLE_COMPONENTS})
    endif ()
endif ()

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Triangle REQUIRED_VARS TRIANGLE_LIBRARY_DIR TRIANGLE_LIBRARIES TRIANGLE_INCLUDE_DIR VERSION_VAR ${TRIANGLE_VERSION})

mark_as_advanced(TRIANGLE_INCLUDE_DIR TRIANGLE_LIBRARY_DIR)
