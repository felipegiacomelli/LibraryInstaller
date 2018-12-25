# MSHTOCGNS_FOUND
# MSHTOCGNS_INCLUDE_DIR
# MSHTOCGNS_LIBRARIES

include (${MSHTOCGNS_DIR}/MSHtoCGNSConfig.cmake)
find_path (MSHTOCGNS_INCLUDE_DIR MSHtoCGNS/CgnsInterface/CgnsCreator.hpp ${MSHTOCGNS_DIR}/include)
if (BUILD_SHARED_LIBS)
    find_library (MSHTOCGNS_LIBRARY_DIR CgnsInterface.so ${MSHTOCGNS_DIR}/libs)
else ()
    find_library (MSHTOCGNS_LIBRARY_DIR CgnsInterface.a ${MSHTOCGNS_DIR}/libs)
endif()

set (MSHTOCGNS_COMPONENTS BoostInterface CgnsInterface MshInterface)

set (MSHTOCGNS_FOUND FALSE)
if (MSHTOCGNS_INCLUDE_DIR)
    if (MSHTOCGNS_LIBRARY_DIR)
        set (MSHTOCGNS_FOUND TRUE)
        set (MSHTOCGNS_INCLUDE_DIR ${MSHTOCGNS_INCLUDE_DIR})
        set (MSHTOCGNS_LIBRARIES ${MSHTOCGNS_COMPONENTS})
    endif ()
endif ()

if (MSHTOCGNS_FOUND)
    message (STATUS "Found MSHtoCGNS: ${MSHTOCGNS_DIR}")
else ()
    message (STATUS"\n\nCould not find MSHtoCGNS\n\n")
endif ()