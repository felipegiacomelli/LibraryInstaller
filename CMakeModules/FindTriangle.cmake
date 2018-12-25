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

if (TRIANGLE_FOUND)
    message (STATUS "Found triangle: ${TRIANGLE_DIR}")
else ()
    message (STATUS "\n\nCould not find triangle.\n\n")
endif ()

# Debugging
# message ("\n")
# message (STATUS "TRIANGLE_FOUND: ${TRIANGLE_FOUND}")
# message (STATUS "TRIANGLE_INCLUDE_DIR: ${TRIANGLE_INCLUDE_DIR}")
# message (STATUS "TRIANGLE_LIBRARIES: ${TRIANGLE_LIBRARIES}")
# message ("\n")
