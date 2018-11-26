import os

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
        hdf5.buildDirectory = "%s/%s/%s" % (options["rootBuildDirectory"], self.library, hdf5.library)
        hdf5.installDirectory = "%s/%s/%s" % (options["rootInstallDirectory"], self.library, hdf5.library)
        hdf5.sourceDirectory = "%s/%s/%s" % (hdf5.buildDirectory, self.library, hdf5.library)
        hdf5.libraryDirectory = "%s/%s/%s" % (options["rootInstallDirectory"], self.library, hdf5.library)
        hdf5.environmentVariable = False
        hdf5Directory = hdf5.libraryDirectory = "%s/%s/%s" % (options["rootInstallDirectory"], self.library, hdf5.library)
        hdf5.install()

        cgns  = Cgns(self.options, "cgns", "3.3.1")
        cgns.flags["Configure"] = "--without-fortran --disable-shared --with-zlib --enable-cgnstools --disable-debug --with-hdf5=%s" % hdf5Directory
        cgns.buildType = ""
        cgns.libraryType = ""
        cgns.buildDirectory = "%s/%s/%s" % (options["rootBuildDirectory"], self.library, cgns.library)
        cgns.installDirectory = "%s/%s/%s" % (options["rootInstallDirectory"], self.library, cgns.library)
        cgns.sourceDirectory = "%s/%s/%s" % (cgns.buildDirectory, self.library, cgns.library)
        cgns.libraryDirectory = "%s/%s/%s" % (options["rootInstallDirectory"], self.library, cgns.library)
        cgns.environmentVariable = False

        Library.writeMessage(self, "Moving to CGNS source directory")
        os.chdir("%s/src" % self.sourceDirectory)
        Library.runCommand(self, "sed -i "23,24d" cgnstools/cgnscalc/calcwish.c")
        Library.runCommand(self, "sed -i "23,24d" cgnstools/cgnsplot/plotwish.c")
        Library.runCommand(self, "sed -i "23,24d" cgnstools/cgnsview/cgiowish.c")

        self.exportPath()

    def exportPath(self):
        if self.environmentVariables:
            Library.exportName(self, name="PATH", value="%s/%s/bin:%s/%s/lib:%s/%s/include:$PATH" % (self.libraryDirectory, self.libraryType, self.libraryDirectory, self.libraryType, self.libraryDirectory, self.libraryType))
