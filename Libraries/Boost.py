import os

from Library import Library

class Boost(Library):
    def __init__(self, options, version):
        name = "boost"
        Library.__init__(self, options, name, version)

        self.flags["configure"] = "threading=multi"
        self.flags["static"]    = "link=static runtime-link=static"
        self.flags["shared"]    = "--cxxflags=-fPIC link=shared runtime-link=shared"
        self.flags["debug"]     = ""
        self.flags["release"]   = ""

        self.downloadLink = "https://downloads.sourceforge.net/project/boost/boost/%s/boost_%s_%s_%s.tar.gz" % (self.version, self.versionMajor, self.versionMinor, self.versionPatch)

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.setup(self)

        Library.extractLibrary(self)
        if not os.path.exists(self.sourceDirectory):
            Library.runCommand(self, "mv %s/boost_%s_%s_%s %s" % (self.buildDirectory, self.versionMajor, self.versionMinor, self.versionPatch, self.sourceDirectory))

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        self.writeMessage("Copying user-config.jam")
        Library.runCommand(self, "cp  %s/CMake/user-config.jam %s" % (self.rootDirectory, os.environ["HOME"]))

        self.writeMessage("Running configure")
        self.runCommand("./bootstrap.sh --prefix=%s" % (self.installDirectory))

        self.writeMessage("Adding 'using mpi ;' to %s/project-config.jam" % self.sourceDirectory)
        projectConfig = open("%s/project-config.jam" % self.sourceDirectory, "a")
        projectConfig.write("using mpi ;")
        projectConfig.close()

        self.writeMessage("Building and installing")
        self.runCommand("./b2 variant=%s %s --prefix=%s -j %s install" % (self.buildType.lower(), self.flags["configure"], self.installDirectory, self.numberOfCores))

        self.writeMessage("Removing user-config.jam")
        Library.runCommand(self, "rm  %s/user-config.jam" % (os.environ["HOME"]))

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)
