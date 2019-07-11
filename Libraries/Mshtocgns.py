import os

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

        if "BOOST_DIR" not in os.environ:
            environ = os.environ.copy()
            environ["BOOST_DIR"] = "%s/%s" % (self.rootInstallDirectory, "boost-1.70.0")
            os.environ.update(environ)

        if "CGNS_DIR" not in os.environ:
            environ = os.environ.copy()
            environ["CGNS_DIR"] = "%s/%s" % (self.rootInstallDirectory, "cgns-3.4.0")
            os.environ.update(environ)

        Library.writeMessage(self, "Running cmake")
        Library.runCommand(self, "cmake . %s -DCMAKE_INSTALL_PREFIX=%s" % (self.flags["configure"], self.installDirectory))

        Library.writeMessage(self, "Building")
        Library.runCommand(self, "make -j %s" % self.numberOfCores)

        Library.writeMessage(self, "Testing")
        Library.runCommand(self, "make test")

        Library.writeMessage(self, "Installing")
        Library.runCommand(self, "make install")

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)
