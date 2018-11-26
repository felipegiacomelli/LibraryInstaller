import os
import subprocess

from Library import Library

class Muparser(Library):
    def __init__(self, options, name, version):
        Library.__init__(self, options, name, version)

        self.flags["Configure"] = "-DBUILD_SAMPLES=OFF"
        self.flags["Static"]    = "-DBUILD_SHARED_LIBS=OFF"
        self.flags["Shared"]    = "-DBUILD_SHARED_LIBS=ON"
        self.flags["Debug"]     = "-DCMAKE_BUILD_TYPE=Debug"
        self.flags["Release"]   = "-DCMAKE_BUILD_TYPE=Release"

        self.downloadLink = "https://github.com/beltoforion/muparser/archive/v2.2.5.tar.gz"

    def install(self):
        Library.setup(self)

        Library.extractLibrary(self)

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        Library.writeMessage(self, "Running configure")
        Library.runCommand(self, "cmake %s -DCMAKE_INSTALL_PREFIX=%s" % (self.flags["Configure"], self.installDirectory))

        Library.writeMessage(self, "Building")
        Library.runCommand(self, "make -j %s" % self.numberOfCores)

        Library.writeMessage(self, "Testing")
        Library.runCommand(self, "make test")

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, "make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self, extra="")
