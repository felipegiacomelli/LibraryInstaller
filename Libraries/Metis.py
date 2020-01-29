import os

from Library import Library

class Metis(Library):
    def __init__(self, options, version):
        name = "metis"
        Library.__init__(self, options, name, version)

        self.flags["configure"] = "-DMETIS_USE_LONGINDEX=FALSE -DMETIS_USE_DOUBLEPRECISION=FALSE -DGKLIB_PATH=../GKlib"
        self.flags["static"]    = "-DSHARED=0"
        self.flags["shared"]    = "-DSHARED=1"
        self.flags["debug"]     = "-DCMAKE_BUILD_TYPE=debug"
        self.flags["release"]   = "-DCMAKE_BUILD_TYPE=release"

        self.downloadLink = "https://github.com/felipegiacomelli/metis/archive/v%s.tar.gz" % self.version

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.setup(self)

        Library.extractLibrary(self)
        if not os.path.exists(self.sourceDirectory):
            Library.runCommand(self, "mv %s/Metis_%s %s" % (self.buildDirectory, self.version, self.sourceDirectory))

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        if not os.path.exists("./build"):
            os.makedirs("./build")
        os.chdir("./build")

        Library.writeMessage(self, "Running configure")
        Library.runCommand(self, "cmake .. %s -DCMAKE_INSTALL_PREFIX=%s" % (self.flags["configure"], self.installDirectory))

        Library.writeMessage(self, "Building")
        Library.runCommand(self, "make -j %s" % self.numberOfCores)

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, "make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariable(self)
