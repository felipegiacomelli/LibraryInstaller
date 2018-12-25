# Find tetgen

include (${TETGEN_DIR}/tetgen_config.cmake)

find_path (TETGEN_INCLUDE_DIR tetgen.h ${TETGEN_DIR})
find_library (TETGEN_LIBRARY_DIR tetgen.so ${TETGEN_DIR})

set (TETGEN_COMPONENTS tetgen)

set (TETGEN_FOUND FALSE)
if (TETGEN_INCLUDE_DIR)
    if (TETGEN_LIBRARY_DIR)
        set (TETGEN_FOUND TRUE)
        set (TETGEN_INCLUDE_DIR ${TETGEN_INCLUDE_DIR})
        set (TETGEN_LIBRARIES ${TETGEN_COMPONENTS})
    endif ()
endif ()

if (TETGEN_FOUND)
    message (STATUS "Found tetgen: ${TETGEN_DIR}")
else ()
    message (STATUS "\n\nCould not find tetgen.\n\n")
endif ()

# Debugging
# message ("\n")
# message (STATUS "TETGEN_FOUND: ${TETGEN_FOUND}")
# message (STATUS "TETGEN_INCLUDE_DIR: ${TETGEN_INCLUDE_DIR}")
# message (STATUS "TETGEN_LIBRARIES: ${TETGEN_LIBRARIES}")
# message ("\n")
