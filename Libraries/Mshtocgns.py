import os, subprocess

from Library import Library

class Mshtocgns(Library):
    def __init__(self, options, version):
        name = "mshtocgns"
        Library.__init__(self, options, name, version)

        self.flags["configure"] = ""
        self.flags["static"]    = "-DBUILD_SHARED_LIBS=OFF"
        self.flags["shared"]    = "-DBUILD_SHARED_LIBS=ON"
        self.flags["debug"]     = "-DCMAKE_BUILD_TYPE=debug"
        self.flags["release"]   = "-DCMAKE_BUILD_TYPE=release"

        self.downloadLink = "https://github.com/felipegiacomelli/MSHtoCGNS/archive/v%s.tar.gz" % self.version

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.setup(self)

        Library.extractLibrary(self)
        if not os.path.exists(self.sourceDirectory):
            Library.runCommand(self, "mv %s/MSHtoCGNS-%s %s" % (self.buildDirectory, self.version, self.sourceDirectory))

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        Library.writeMessage(self, "Running configure")
        if "BOOST_DIR" in os.environ and "CGNS_DIR" in os.environ:
            Library.runCommand(self, "cmake . %s -DCMAKE_INSTALL_PREFIX=%s" % (self.flags["configure"], self.installDirectory))
        else:
            command = "export BOOST_DIR=%s/%s;export CGNS_DIR=%s/%s;cmake . %s -DCMAKE_INSTALL_PREFIX=%s" % (self.rootInstallDirectory, "boost-1.68.0", self.rootInstallDirectory, "cgns-3.3.1", self.flags["configure"], self.installDirectory)
            Library.displayCommand(self, command)
            subprocess.check_call(["sh", "-c", "%s 2>>%s >> %s" % (command, self.logFile.name, self.logFile.name)], stdout=self.logFile)

        Library.writeMessage(self, "Building")
        Library.runCommand(self, "make -j %s" % self.numberOfCores)

        Library.writeMessage(self, "Testing")
        Library.runCommand(self, "make test")

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, "make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)
