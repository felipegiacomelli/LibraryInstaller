import os
import subprocess

from Library import Library
from Hdf5 import Hdf5
from Cgns import Cgns

class Cgnstools(Library):
    def __init__(self, options, version):
        self.options = options
        name = "cgnstools"
        Library.__init__(self, options, name, version)

        self.buildType = ""
        self.libraryType = ""

    def install(self):
        Library.setDefaultPathsAndNames(self)
        Library.setup(self)

        self.installHdf5()

        cgns  = Cgns(self.options, "3.3.1")
        cgns.flags["Configure"] = "--without-fortran --disable-shared --with-zlib --enable-cgnstools --disable-debug --with-hdf5=%s" % self.installDirectory
        cgns.buildType = ""
        cgns.libraryType = ""
        cgns.environmentVariables = False
        cgns.setDefaultPathsAndNames()
        cgns.buildDirectory = "%s/%s" % (self.buildDirectory, cgns.library)
        cgns.installDirectory = "%s" % (self.installDirectory)
        cgns.sourceDirectory = "%s/%s" % (cgns.buildDirectory, cgns.library)
        cgns.libraryDirectory = "%s" % (self.installDirectory)
        self.libraryDirectory = cgns.libraryDirectory

        cgns.setup()

        cgns.extractLibrary()
        if not os.path.exists(cgns.sourceDirectory):
            cgns.runCommand("mv %s/CGNS-3.3.1 %s" % (cgns.buildDirectory, cgns.sourceDirectory))

        cgns.writeMessage("Moving to source directory")
        os.chdir("%s/src" % cgns.sourceDirectory)
        cgns.runCommand("sed -i \"23,24d\" cgnstools/cgnscalc/calcwish.c")
        cgns.runCommand("sed -i \"23,24d\" cgnstools/cgnsplot/plotwish.c")
        cgns.runCommand("sed -i \"23,24d\" cgnstools/cgnsview/cgiowish.c")

        commands =            cgns.appendCommand(message="Running configure", command="./configure %s --prefix=%s --datadir=%s/share/" % (cgns.flags["Configure"], cgns.installDirectory, cgns.installDirectory))
        commands = commands + cgns.appendCommand(message="Building", command="make -j %s" % cgns.numberOfCores)
        commands = commands + cgns.appendCommand(message="Testing", command="make test")
        commands = commands + cgns.appendCommand(message="Installing", command="make install")

        p = subprocess.Popen(["sh", "-c", commands], env=dict(os.environ, LIBS="-ldl", CLIBS="-ldl", FLIBS="-ldl"), stdout=cgns.logFile)
        p.wait()

        cgns.displayEndMessage()

        self.exportPath()

    def installHdf5(self):
        hdf5  = Hdf5(self.options, "1.8.19")
        hdf5.flags["Configure"] = "--disable-shared --enable-static --enable-cxx --disable-fortran --with-zlib --enable-static-exec --disable-debug --enable-production"
        hdf5.buildType = ""
        hdf5.libraryType = ""
        hdf5.environmentVariables = False
        hdf5.setDefaultPathsAndNames()
        hdf5.buildDirectory = "%s/%s" % (self.buildDirectory, hdf5.library)
        hdf5.installDirectory = "%s" % (self.installDirectory)
        hdf5.sourceDirectory = "%s/%s" % (hdf5.buildDirectory, hdf5.library)
        hdf5.libraryDirectory = "%s" % (self.installDirectory)
        hdf5.install()
        hdf5.displayEndMessage()

    def exportPath(self):
        if self.environmentVariables:
            Library.exportName(self, name="PATH", value="%s/bin:%s/lib:%s/include:$PATH" % (self.libraryDirectory, self.libraryDirectory, self.libraryDirectory))
