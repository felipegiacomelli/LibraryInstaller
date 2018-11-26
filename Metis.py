import os

from Library import Library

class Metis(Library):
    def __init__(self, options, name, version):
        Library.__init__(self, options, name, version)

        self.flags["Configure"] = ""
        self.flags["Static"]    = "debug=1 assert=1 assert2=1"
        self.flags["Shared"]    = ""
        self.flags["Debug"]     = ""
        self.flags["Release"]   = "shared=1"

        self.downloadLink = "http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz"

    def install(self):
        Library.setup(self)

        Library.extractLibrary(self)

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        Library.writeMessage(self, "Running configure")
        Library.runCommand(self, "make %s prefix=%s -j %s config" % (self.flags["Configure"], self.installDirectory, self.numberOfCores))

        Library.writeMessage(self, "Building")
        Library.runCommand(self, "make -j %s" % self.numberOfCores)

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, "make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)
