import os

from Library import Library

class Triangle(Library):
    def __init__(self, options, version):
        name = "triangle"
        Library.__init__(self, options, name, version)
        self.buildType = ""
        self.libraryType = ""

        self.flags["configure"] = ""
        self.flags["static"]    = ""
        self.flags["shared"]    = ""
        self.flags["debug"]     = ""
        self.flags["release"]   = ""

        self.downloadLink = "http://www.netlib.org/voronoi/triangle.zip"

    def install(self):
        Library.setDefaultPathsAndNames(self)
        self.compressedLibrary = "%s/%s.zip" % (self.compressedFiles, self.library)

        Library.setup(self)

        self.extractLibrary()

        Library.writeMessage(self, "Copying CMakeLists.txt to %s" % self.sourceDirectory)
        Library.runCommand(self, "cp CMake/triangle.txt %s/CMakeLists.txt" % self.sourceDirectory)

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        if not os.path.exists("./build"):
            os.makedirs("./build")

        os.chdir("./build")

        Library.writeMessage(self, "Running configure")
        Library.runCommand(self, "cmake .. -DCMAKE_INSTALL_PREFIX=%s" % self.installDirectory)

        Library.writeMessage(self, "Building")
        Library.runCommand(self, "make -j %s" % self.numberOfCores)

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, "make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)

    def extractLibrary(self):
        if not os.path.exists(self.sourceDirectory):
            if os.path.exists(self.compressedLibrary):
                Library.writeMessage(self, "Extracting %s" % self.compressedLibrary)
                Library.runCommand(self, "unzip -x %s -d %s" % (self.compressedLibrary, self.sourceDirectory))
            else:
                Library.writeMessage(self, "Downloading %s" % self.library)
                Library.runCommand(self, "wget %s -O %s" % (self.downloadLink, self.compressedLibrary))
                Library.runCommand(self, "unzip -x %s -d %s" % (self.compressedLibrary, self.sourceDirectory))
