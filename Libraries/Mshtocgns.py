import os

from Library import Library

class Mshtocgns(Library):
    def __init__(self, options, version):
        name = "mshtocgns"
        Library.__init__(self, options, name, version)

        self.flags["configure"] = ""
        self.flags["static"]    = "-DBUILD_SHARED_LIBS=OFF"
        self.flags["shared"]    = "-DBUILD_SHARED_LIBS=ON"
        self.flags["debug"]     = "-DCMAKE_BUILD_TYPE=debug"
        self.flags["release"]   = "-DCMAKE_BUILD_TYPE=release"

        self.downloadLink = "https://github.com/felipegiacomelli/MSHtoCGNS/archive/master.zip"

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.setup(self)

        self.extractLibrary()
        if not os.path.exists(self.sourceDirectory):
            Library.runCommand(self, "mv %s/MSHtoCGNS-master %s" % (self.buildDirectory, self.sourceDirectory))

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        Library.writeMessage(self, "Running configure")
        Library.runCommand(self, "cmake %s -DCMAKE_INSTALL_PREFIX=%s" % (self.flags["configure"], self.installDirectory))

        Library.writeMessage(self, "Building")
        Library.runCommand(self, "make -j %s" % self.numberOfCores)

        Library.writeMessage(self, "Testing")
        Library.runCommand(self, "make test")

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, "make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)

    def extractLibrary(self):
        if not os.path.exists(self.sourceDirectory):
            if os.path.exists(self.compressedLibrary):
                Library.writeMessage(self, "Extracting %s" % self.compressedLibrary)
                Library.runCommand(self, "unzip -x %s -d %s" % (self.compressedLibrary, self.buildDirectory))
            else:
                Library.writeMessage(self, "Downloading %s" % self.library)
                Library.runCommand(self, "wget %s -O %s" % (self.downloadLink, self.compressedLibrary))
                Library.runCommand(self, "unzip -x %s -d %s" % (self.compressedLibrary, self.buildDirectory))
