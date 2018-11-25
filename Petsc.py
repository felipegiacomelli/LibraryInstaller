from Library import Library

class Cgns(Library):
    def __init__(self, rootBuildDirectory, rootInstallDirectory, buildType, libraryType, exportEnvironmentVariables, name, version):
        buildType = ""
        Library.__init__(self, rootBuildDirectory, rootInstallDirectory, buildType, libraryType, exportEnvironmentVariables, name, version)

        self.flags["Configure"] = "---with-mpi --download-f2cblaslapack=yes --download-hypre=yes --with-fc=0"
        self.flags["Static"]    = "-with-shared-libraries=0"
        self.flags["Shared"]    = "-with-shared-libraries=1"
        self.flags["Debug"]     = "--with-debugging=1"
        self.flags["Release"]   = "--with-debugging=0 COPTFLAGS=-O3 CXXOPTFLAGS=-O3"

        self.downloadLink = "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.10.2.tar.gz"

    def install(self):
        Library.install(self)
