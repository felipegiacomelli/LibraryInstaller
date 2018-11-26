import os
import subprocess

from Library import Library

class Petsc(Library):
    def __init__(self, options, name, version):
        Library.__init__(self, options, name, version)

        self.flags["Configure"] = "---with-mpi --download-f2cblaslapack=yes --with-fc=0"
        self.flags["Static"]    = "-with-shared-libraries=0"
        self.flags["Shared"]    = "-with-shared-libraries=1"
        self.flags["Debug"]     = "--with-debugging=1"
        self.flags["Release"]   = "--with-debugging=0 COPTFLAGS=-O3 CXXOPTFLAGS=-O3"

        self.downloadLink = "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.10.2.tar.gz"

    def install(self):
        Library.setup(self)

        Library.extractLibrary(self)

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        commands = self.appendCommand(message="Running configure", command="python2 ./configure CC=$CC CXX=$CXX %s --prefix=%s" % (self.flags["Configure"], self.installDirectory))
        commands = commands + self.appendCommand(message="Building", command="make MAKE_NP=%s all" % self.numberOfCores)
        commands = commands + self.appendCommand(message="Installing", command="make install")

        p = subprocess.Popen(["sh", "-c", commands], env=dict(os.environ, CC="mpicc", CXX="mpicxx", PETSC_ARCH=self.buildType, PETSC_DIR=self.sourceDirectory), stdout=self.logFile)
        p.wait()

        Library.writeMessage(self, "Build directory: %s" % self.buildDirectory)
        Library.writeMessage(self, "Compressed library: %s" % self.compressedLibrary)
        Library.writeMessage(self, "Install directory: %s" % self.installDirectory)
        Library.writeMessage(self, "Log file: %s" % self.logFile.name)

        Library.exportEnvironmentVariables(self, extra="")

    def appendCommand(self, message, command):
        return "echo -e \"\n%s\n\" | tee -a %s && echo -e \"\n`pwd`\$ %s\n\" && %s 2>>%s >> %s;" % (message, self.logFile.name, command, command, self.logFile.name, self.logFile.name)
