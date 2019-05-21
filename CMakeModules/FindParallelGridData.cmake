# PGD_FOUND
# PGD_INCLUDE_DIR
# PGD_LIBRARIES

include (${PGD_DIR}/ParallelGridDataConfigVersion.cmake)
include (${PGD_DIR}/ParallelGridDataConfig.cmake)
include (${PGD_DIR}/ParallelGridDataTargets.cmake)

include (FindPackageHandleStandardArgs)
find_package_handle_standard_args (ParallelGridData REQUIRED_VARS PGD_LIBRARY_DIR PGD_LIBRARIES PGD_INCLUDE_DIR VERSION_VAR PACKAGE_VERSION)
mark_as_advanced (PGD_INCLUDE_DIR PGD_LIBRARY_DIR)
