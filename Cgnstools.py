import os
import subprocess

from Library import Library
from Hdf5 import Hdf5
from Cgns import Cgns

class Cgnstools(Library):
    def __init__(self, options, name, version):
        Library.__init__(self, options, name, version)
        self.options = options

    def install(self):
        hdf5  = Hdf5(self.options, "hdf5", "1.8.19")
        hdf5.flags["Configure"] = "--disable-shared --enable-static --enable-cxx --disable-fortran --with-zlib --enable-static-exec --disable-debug --enable-production"
        hdf5.buildType = ""
        hdf5.libraryType = ""
        hdf5.buildDirectory = "%s/%s/%s" % (self.options["rootBuildDirectory"], self.library, hdf5.library)
        hdf5.installDirectory = "%s/%s/%s" % (self.options["rootInstallDirectory"], self.library, hdf5.library)
        hdf5.sourceDirectory = "%s/%s" % (hdf5.buildDirectory, hdf5.library)
        hdf5.libraryDirectory = "%s/%s/%s" % (self.options["rootInstallDirectory"], self.library, hdf5.library)
        hdf5.environmentVariable = False
        hdf5Directory = hdf5.libraryDirectory = "%s/%s/%s" % (self.options["rootInstallDirectory"], self.library, hdf5.library)
        # hdf5.install()

        cgns  = Cgns(self.options, "cgns", "3.3.1")
        cgns.flags["Configure"] = "--without-fortran --disable-shared --with-zlib --enable-cgnstools --disable-debug --with-hdf5=%s" % hdf5Directory
        cgns.buildType = ""
        cgns.libraryType = ""
        cgns.buildDirectory = "%s/%s/%s" % (self.options["rootBuildDirectory"], self.library, cgns.library)
        cgns.installDirectory = "%s/%s/%s" % (self.options["rootInstallDirectory"], self.library, cgns.library)
        cgns.sourceDirectory = "%s/%s" % (cgns.buildDirectory, cgns.library)
        cgns.libraryDirectory = "%s/%s/%s" % (self.options["rootInstallDirectory"], self.library, cgns.library)
        cgns.environmentVariable = False
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

    def exportPath(self):
        if self.environmentVariables:
            Library.exportName(self, name="PATH", value="%s/bin:%s/lib:%s/include:$PATH" % (self.libraryDirectory, self.libraryDirectory, self.libraryDirectory))
