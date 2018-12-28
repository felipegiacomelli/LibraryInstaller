import os

from Library import Library

class Tetgen(Library):
    def __init__(self, options, version):
        name = "tetgen"
        Library.__init__(self, options, name, version)
        self.buildType = ""
        self.libraryType = ""

        self.flags["configure"] = ""
        self.flags["static"]    = ""
        self.flags["shared"]    = ""
        self.flags["debug"]     = ""
        self.flags["release"]   = ""

        self.downloadLink = ""

    def install(self):
        Library.setDefaultPathsAndNames(self)
        self.compressedLibrary = "%s/%s.zip" % (self.compressedFiles, self.library)

        Library.setup(self)

        self.extractLibrary()
        if not os.path.exists(self.sourceDirectory):
            Library.runCommand(self, "mv %s/tetgen1.5.1 %s" % (self.buildDirectory, self.sourceDirectory))

        Library.writeMessage(self, "Copying CMakeLists.txt to %s" % self.sourceDirectory)
        Library.runCommand(self, "cp CMake/tetgen.txt %s/CMakeLists.txt" % self.sourceDirectory)

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
                Library.runCommand(self, "unzip -x %s -d %s" % (self.compressedLibrary, self.buildDirectory))
            else:
                raise Exception("No download link available")
