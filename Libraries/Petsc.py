import os

from Library import Library

class Petsc(Library):
    def __init__(self, options, version):
        name = "petsc"
        Library.__init__(self, options, name, version)

        self.metisPath = "%s/%s/%s" % (os.environ["METIS_DIR"], self.buildType, self.libraryType)

        self.flags["configure"] = "--with-mpi --download-f2cblaslapack=yes --with-fc=0 --with-metis-dir=%s --with-cxx-dialect=C++11 --download-superlu_dist --download-parmetis --download-ptscotch --download-hypre" % self.metisPath
        self.flags["static"]    = "--with-shared-libraries=0"
        self.flags["shared"]    = "--with-shared-libraries=1"
        self.flags["debug"]     = "--with-debugging=1"
        self.flags["release"]   = "--with-debugging=0 COPTFLAGS=-O3 CXXOPTFLAGS=-O3"

        self.downloadLink = "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-%s.tar.gz" % self.version

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.setup(self)

        Library.extractLibrary(self)

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        environ = os.environ.copy()
        environ["PETSC_ARCH"] = self.buildType
        environ["PETSC_DIR"] = self.sourceDirectory
        os.environ.update(environ)

        Library.writeMessage(self, "Running configure")
        Library.runCommand(self, command="python3 ./configure %s --prefix=%s" % (self.flags["configure"], self.installDirectory))

        Library.writeMessage(self, "Building")
        Library.runCommand(self, command="make MAKE_NP=%s all" % self.numberOfCores)

        # It takes too long starting version 3.13
        # Library.writeMessage(self, "Testing")
        # Library.runCommand(self, command="make test")

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, command="make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariable(self)
