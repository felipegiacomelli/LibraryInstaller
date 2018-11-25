import os

from Library import Library

class Openmpi(Library):
    def __init__(self, rootBuildDirectory, rootInstallDirectory, buildType, libraryType, environmentVariables, name, version):
        buildType = ""
        Library.__init__(self, rootBuildDirectory, rootInstallDirectory, buildType, libraryType, environmentVariables, name, version)

        self.flags["Configure"] = "--enable-cxx-exceptions=yes --enable-binaries=yes"
        self.flags["Static"]    = "--enable-static=yes --disable-shared"
        self.flags["Shared"]    = ""
        self.flags["Debug"]     = ""
        self.flags["Release"]   = ""

        self.downloadLink = "https://download.open-mpi.org/release/open-mpi/v3.0/openmpi-3.0.1.tar.gz"

    def install(self):
        Library.install(self)
        Library.exportEnvironmentVariables(self, self.libraryType)
        self.exportPath()

    def exportPath(self):
        if self.environmentVariables:
            Library.exportName(self, "PATH", "%s/%s/bin:%s/%s/lib:%s/%s/include:$PATH" % (self.libraryDirectory, self.libraryType, self.libraryDirectory, self.libraryType, self.libraryDirectory, self.libraryType))
