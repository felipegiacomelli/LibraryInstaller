import os
import subprocess

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

        self.pythonConfigureFlags="--with-python=/usr/bin/python2.7 -with-python-root=/usr --with-python-version=2.7"

        self.downloadLink = "https://downloads.sourceforge.net/project/boost/boost/1.68.0/boost_1_68_0.tar.gz"

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.setup(self)

        Library.extractLibrary(self)
        if not os.path.exists(self.sourceDirectory):
            Library.runCommand(self, "mv %s/boost_1_68_0 %s" % (self.buildDirectory, self.sourceDirectory))

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        self.writeMessage("Running configure")
        self.runCommand("./bootstrap.sh %s --prefix=%s" % (self.pythonConfigureFlags, self.installDirectory))

        self.writeMessage("Add \"using mpi ;\" to file %s/project-config.jam" % self.sourceDirectory)
        projectConfig = open("%s/project-config.jam" % self.sourceDirectory, "a")
        projectConfig.write("using mpi ;")
        projectConfig.close()

        self.writeMessage("Building and installing")
        self.runCommand("./b2 variant=%s %s --prefix=%s -j %s install" % (self.buildType.lower(), self.flags["configure"], self.installDirectory, self.numberOfCores))

        Library.displayEndMessage(self)

        Library.exportEnvironmentVariables(self)
