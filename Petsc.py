import os
import subprocess

from Library import Library

class Petsc(Library):
    def __init__(self, options, version):
        name = "petsc"
        Library.__init__(self, options, name, version)

        self.flags["Configure"] = "---with-mpi --download-f2cblaslapack=yes --with-fc=0"
        self.flags["Static"]    = "-with-shared-libraries=0"
        self.flags["Shared"]    = "-with-shared-libraries=1"
        self.flags["Debug"]     = "--with-debugging=1"
        self.flags["Release"]   = "--with-debugging=0 COPTFLAGS=-O3 CXXOPTFLAGS=-O3"

        self.downloadLink = "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.10.2.tar.gz"

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.setup(self)

        Library.extractLibrary(self)

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        commands = Library.appendCommand(self, message="Running configure", command="python2 ./configure CC=$CC CXX=$CXX %s --prefix=%s" % (self.flags["Configure"], self.installDirectory))
        commands = commands + Library.appendCommand(self, message="Building", command="make MAKE_NP=%s all" % self.numberOfCores)
        commands = commands + Library.appendCommand(self, message="Testing", command="make test")
        commands = commands + Library.appendCommand(self, message="Installing", command="make install")

        p = subprocess.Popen(["sh", "-c", commands], env=dict(os.environ, CC="mpicc", CXX="mpicxx", PETSC_ARCH=self.buildType, PETSC_DIR=self.sourceDirectory), stdout=self.logFile)
        p.wait()

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)
