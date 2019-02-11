# Find WIAS' TetGen

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

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Tetgen REQUIRED_VARS TETGEN_LIBRARY_DIR TETGEN_LIBRARIES TETGEN_INCLUDE_DIR VERSION_VAR ${TETGEN_VERSION})

mark_as_advanced(TETGEN_INCLUDE_DIR TETGEN_LIBRARY_DIR)
