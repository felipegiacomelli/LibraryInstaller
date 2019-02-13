import os
import subprocess

from Library import Library

class Cgns(Library):
    def __init__(self, options, version):
        name = "cgns"
        Library.__init__(self, options, name, version)

        self.flags["configure"] = "--without-fortran --disable-cgnstools"
        self.flags["static"]    = "--disable-shared"
        self.flags["shared"]    = "--enable-shared"
        self.flags["debug"]     = "--enable-debug"
        self.flags["release"]   = "--disable-debug"

        self.downloadLink = "https://github.com/CGNS/CGNS/archive/v%s.tar.gz" % self.version

        Library.setDefaultPathsAndNames(self)

    def install(self):
        Library.setup(self)

        Library.extractLibrary(self)
        if not os.path.exists(self.sourceDirectory):
            Library.runCommand(self, "mv %s/CGNS-%s %s" % (self.buildDirectory, self.version, self.sourceDirectory))

        Library.writeMessage(self, "Moving to source directory")
        os.chdir("%s/src" % self.sourceDirectory)

        commands = Library.appendCommand(self, message="Running configure", command="./configure %s --prefix=%s" % (self.flags["configure"], self.installDirectory))
        commands = commands + Library.appendCommand(self, message="Building", command="make -j %s" % self.numberOfCores)
        commands = commands + Library.appendCommand(self, message="Testing", command="make test")
        commands = commands + Library.appendCommand(self, message="Installing", command="make install")

        p = subprocess.Popen(["sh", "-c", commands], env=dict(os.environ, LIBS="-ldl", CLIBS="-ldl", FLIBS="-ldl"), stdout=self.logFile)
        p.wait()

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)
