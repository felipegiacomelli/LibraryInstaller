import os

from Library import Library

class Hdf5(Library):
    def __init__(self, options, version):
        name = "hdf5"
        Library.__init__(self, options, name, version)

        self.flags["configure"] = "--enable-cxx --disable-fortran --with-zlib"
        self.flags["static"]    = "--enable-debug=all"
        self.flags["shared"]    = "--disable-debug --enable-production"
        self.flags["debug"]     = "--disable-shared --enable-static --enable-static-exec"
        self.flags["release"]   = "--enable-shared  --disable-static"

        self.downloadLink = "https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.19/src/hdf5-1.8.19.tar.gz"

        Library.setDefaultPathsAndNames(self)

    def install(self):
        Library.install(self)

        Library.exportEnvironmentVariables(self)