from Library import Library

class Mpich(Library):
    def __init__(self, options, version):
        name = "mpich"
        Library.__init__(self, options, name, version)
        self.buildType = ""
        self.libraryType = ""

        self.flags["configure"] = "--with-device=ch4:ofi --enable-fast=all,O3 --enable-shared FFLAGS=-fallow-argument-mismatch"
        self.flags["static"]    = ""
        self.flags["shared"]    = ""
        self.flags["debug"]     = ""
        self.flags["release"]   = ""

        self.downloadLink =  "http://www.mpich.org/static/downloads/%s/mpich-%s.tar.gz" % (self.version, self.version)

        libraryDirectory = "%s/%s-%s" % (self.rootInstallDirectory, self.name, self.version)
        self.path = "%s/bin:%s/lib:%s/include" % (libraryDirectory, libraryDirectory, libraryDirectory)

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.install(self)

        Library.exportEnvironmentVariable(self)

        Library.exportPath(self)
