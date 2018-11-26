import os

from Library import Library

class Hdf5(Library):
    def __init__(self, options, name, version):
        Library.__init__(self, options, name, version)

        self.flags["Configure"] = "--enable-cxx --disable-fortran --with-zlib"
        self.flags["Static"]    = "--enable-debug=all"
        self.flags["Shared"]    = "--disable-debug --enable-production"
        self.flags["Debug"]     = "--disable-shared --enable-static --enable-static-exec"
        self.flags["Release"]   = "--enable-shared  --disable-static"

        self.downloadLink = "https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.19/src/hdf5-1.8.19.tar.gz"

    def install(self):
        Library.install(self)

        Library.exportEnvironmentVariables(self)
