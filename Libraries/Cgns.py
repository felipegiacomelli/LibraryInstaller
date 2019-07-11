import os
import tempfile
import shutil

from Library import Library

class Cgns(Library):
    def __init__(self, options, version):
        name = "cgns"
        Library.__init__(self, options, name, version)

        self.flags["configure"] = "-DCGNS_ENABLE_FORTRAN=FALSE -DCGNS_ENABLE_PARALLEL=TRUE -DCGNS_ENABLE_HDF5=TRUE -DHDF5_NEED_ZLIB=TRUE -DHDF5_NEED_MPI=TRUE -DCGNS_BUILD_CGNSTOOLS=TRUE -DCGNS_ENABLE_TESTS=TRUE -DCGNS_BUILD_TESTING=TRUE"
        self.flags["static"]    = "-DCGNS_BUILD_SHARED=FALSE"
        self.flags["shared"]    = "-DCGNS_BUILD_SHARED=TRUE"
        self.flags["debug"]     = "-DCMAKE_BUILD_TYPE=debug"
        self.flags["release"]   = "-DCMAKE_BUILD_TYPE=release"

        self.downloadLink = "https://github.com/CGNS/CGNS/archive/v%s.tar.gz" % self.version

        if "HDF5_DIR" not in os.environ:
            environ = os.environ.copy()
            environ["HDF5_DIR"] = "%s/%s" % (self.rootInstallDirectory, "hdf5-1.10.5")
            os.environ.update(environ)

        self.hdf5Path = "%s/%s/%s" % (os.environ["HDF5_DIR"], self.buildType, self.libraryType)

        if self.buildType == "debug":
            self.hdf5Libraries = "'%s/lib/libhdf5_debug.so;%s/lib/libhdf5_hl_debug.so;%s/lib/libhdf5_tools_debug.so'" % (self.hdf5Path, self.hdf5Path, self.hdf5Path)
        else:
            self.hdf5Libraries = "'%s/lib/libhdf5.so;%s/lib/libhdf5_hl.so;%s/lib/libhdf5_tools.so'" % (self.hdf5Path, self.hdf5Path, self.hdf5Path)

        Library.setDefaultPathsAndNames(self)

    def install(self):
        Library.setup(self)

        Library.extractLibrary(self)
        if not os.path.exists(self.sourceDirectory):
            Library.runCommand(self, "mv %s/CGNS-%s %s" % (self.buildDirectory, self.version, self.sourceDirectory))

        self.setCMakeInstallation()

        Library.writeMessage(self, "Moving to source directory")
        os.chdir("%s" % self.sourceDirectory)

        self.fixCMakeFindHDF5()

        if not os.path.exists("./build"):
            os.makedirs("./build")
        os.chdir("./build")

        environ = os.environ.copy()
        environ["LIBS"] = "\"-ldl\""
        environ["CLIBS"] = "\"-ldl\""
        os.environ.update(environ)

        Library.writeMessage(self, "Running cmake")
        Library.runCommand(self, "cmake .. %s -DCMAKE_INSTALL_PREFIX=%s -DCMAKE_PREFIX_PATH=%s -DHDF5_LIBRARIES=%s" % (self.flags["configure"], self.installDirectory, self.hdf5Path, self.hdf5Libraries))

        Library.writeMessage(self, "Building")
        Library.runCommand(self, "make -j %s" % self.numberOfCores)

        Library.writeMessage(self, "Testing")
        Library.runCommand(self, "make test")

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, "make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)

    def setCMakeInstallation(self):
        Library.runCommand(self, "cp  %s/CMakeIncludes/ProjectConfig.cmake.in %s" % (self.rootDirectory, self.sourceDirectory))
        Library.runCommand(self, "cat %s/CMake/CgnsInstall.txt >> %s/CMakeLists.txt" % (self.rootDirectory, self.sourceDirectory))

    def fixCMakeFindHDF5(self):
        file = "CMakeLists.txt"
        fh, path = tempfile.mkstemp()
        with os.fdopen(fh, "w") as new:
            with open(file) as old:
                for line in old:
                    new.write(line.replace("set (FIND_HDF_COMPONENTS C shared)", "set (FIND_HDF_COMPONENTS C)"))
        os.remove(file)
        shutil.move(path, file)
