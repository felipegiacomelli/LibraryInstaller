# PGD_FOUND
# PGD_INCLUDE_DIR
# PGD_LIBRARIES

include (${PGD_DIR}/PGDConfigVersion.cmake)
include (${PGD_DIR}/PGDConfig.cmake)
include (${PGD_DIR}/PGDTargets.cmake)

include (FindPackageHandleStandardArgs)
find_package_handle_standard_args (PGD REQUIRED_VARS PGD_LIBRARY_DIR PGD_LIBRARIES PGD_INCLUDE_DIR VERSION_VAR PACKAGE_VERSION)
mark_as_advanced (PGD_INCLUDE_DIR PGD_LIBRARY_DIR)
