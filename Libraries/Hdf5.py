import os

from Library import Library

class Hdf5(Library):
    def __init__(self, options, version):
        name = "hdf5"
        Library.__init__(self, options, name, version)

        self.flags["configure"] = "-DHDF5_BUILD_CPP_LIB=FALSE -DHDF5_BUILD_FORTRAN=FALSE -DHDF5_ENABLE_PARALLEL=TRUE -DMPIEXEC_MAX_NUMPROCS=4"
        self.flags["static"]    = "-DBUILD_SHARED_LIBS=FALSE"
        self.flags["shared"]    = "-DBUILD_SHARED_LIBS=TRUE -DH5_ENABLE_STATIC_LIB=FALSE -DBUILD_STATIC_EXECS=FALSE"
        self.flags["debug"]     = "-DCMAKE_BUILD_TYPE=debug"
        self.flags["release"]   = "-DCMAKE_BUILD_TYPE=release"

        self.downloadLink = "https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-%s.%s/hdf5-%s/src/hdf5-%s.tar.gz" % (self.versionMajor, self.versionMinor, self.version, self.version)

        Library.setDefaultPathsAndNames(self)

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.setup(self)

        Library.extractLibrary(self)

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        if not os.path.exists("./build"):
            os.makedirs("./build")
        os.chdir("./build")

        Library.writeMessage(self, "Running cmake")
        Library.runCommand(self, "cmake .. %s -DCMAKE_INSTALL_PREFIX=%s" % (self.flags["configure"], self.installDirectory))

        Library.writeMessage(self, "Building")
        Library.runCommand(self, "make -j %s" % self.numberOfCores)

        # Library.writeMessage(self, "Testing")
        # Library.runCommand(self, "make test")

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, "make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariable(self)
