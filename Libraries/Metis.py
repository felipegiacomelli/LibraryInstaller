import os

from Library import Library

class Metis(Library):
    def __init__(self, options, version):
        name = "metis"
        Library.__init__(self, options, name, version)

        self.flags["configure"] = ""
        self.flags["static"]    = "debug=1 assert=1 assert2=1"
        self.flags["shared"]    = ""
        self.flags["debug"]     = ""
        self.flags["release"]   = "shared=1"

        self.downloadLink = "http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz"

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.setup(self)

        Library.extractLibrary(self)

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        Library.writeMessage(self, "Running configure")
        Library.runCommand(self, "make %s prefix=%s -j %s config" % (self.flags["configure"], self.installDirectory, self.numberOfCores))

        Library.writeMessage(self, "Building")
        Library.runCommand(self, "make -j %s" % self.numberOfCores)

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, "make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)
