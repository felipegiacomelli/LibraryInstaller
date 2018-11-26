from Library import Library

class Petsc(Library):
    def __init__(self, options, name, version):
        Library.__init__(self, options, name, version)

        self.flags["Configure"] = "---with-mpi --download-f2cblaslapack=yes --download-hypre=yes --with-fc=0"
        self.flags["Static"]    = "-with-shared-libraries=0"
        self.flags["Shared"]    = "-with-shared-libraries=1"
        self.flags["Debug"]     = "--with-debugging=1"
        self.flags["Release"]   = "--with-debugging=0 COPTFLAGS=-O3 CXXOPTFLAGS=-O3"

        self.downloadLink = "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.10.2.tar.gz"

    def install(self):
        Library.setup()

        Library.extractLibrary()

        Library.writeMessage("Moving to source directory")
        os.chdir(self.sourceDirectory)

        Library.writeMessage("Running configure")
        Library.runCommand("python2 ./configure CC=mpicc CXX=mpicxx %s --prefix=%s" % (self.flags["Configure"], self.installDirectory))

        Library.writeMessage("Building")
        Library.runCommand("make -j %s" % str(multiprocessing.cpu_count()))

        Library.writeMessage("Installing")
        Library.runCommand("make install")

        Library.writeMessage("Build directory: %s" % self.buildDirectory)
        Library.writeMessage("Compressed library: %s" % self.compressedLibrary)
        Library.writeMessage("Install directory: %s" % self.installDirectory)
        Library.writeMessage("Log file: %s" % self.logFile.name)
