from Library import Library

class Openmpi(Library):
    def __init__(self, options, version):
        name = "openmpi"
        Library.__init__(self, options, name, version)
        self.buildType = ""
        self.libraryType = ""

        self.flags["Configure"] = "--enable-cxx-exceptions=yes --enable-binaries=yes --enable-static=yes"
        self.flags["Static"]    = ""
        self.flags["Shared"]    = ""
        self.flags["Debug"]     = ""
        self.flags["Release"]   = ""

        self.downloadLink = "https://download.open-mpi.org/release/open-mpi/v3.0/openmpi-3.0.1.tar.gz"

        self.path ="%s/bin:%s/lib:%s/include" % (self.libraryDirectory, self.libraryDirectory, self.libraryDirectory)

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.install(self)

        Library.exportEnvironmentVariables(self, extra=self.libraryType)

        self.exportPath()

    def exportPath(self):
        if self.environmentVariables:
            Library.exportName(self, name="PATH", value="%s:$PATH" % (self.path))
