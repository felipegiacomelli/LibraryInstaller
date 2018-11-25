from Library import Library

class Cgns(Library):
    def __init__(self, rootBuildDirectory, rootInstallDirectory, buildType, libraryType, exportEnvironmentVariables, name, version):
        buildType = ""
        Library.__init__(self, rootBuildDirectory, rootInstallDirectory, buildType, libraryType, exportEnvironmentVariables, name, version)

        self.flags["Configure"] = "--without-fortran --disable-cgnstools"
        self.flags["Static"]    = "--disable-shared"
        self.flags["Shared"]    = "--enable-shared"
        self.flags["Debug"]     = "--enable-debug"
        self.flags["Release"]   = "--disable-debug"

        self.downloadLink = "https://github.com/CGNS/CGNS/archive/v3.3.1.tar.gz"

        # export LIBS="-ldl"
        # export CLIBS="-ldl"
        # export FLIBS="-ldl"

    def install(self):
        Library.install(self)
