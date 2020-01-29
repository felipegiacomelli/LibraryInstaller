import os, tempfile, shutil

from Library import Library

class Muparser(Library):
    def __init__(self, options, version):
        name = "muparser"
        Library.__init__(self, options, name, version)

        self.flags["configure"] = "-DBUILD_SAMPLES=OFF"
        self.flags["static"]    = "-DBUILD_SHARED_LIBS=OFF"
        self.flags["shared"]    = "-DBUILD_SHARED_LIBS=ON"
        self.flags["debug"]     = "-DCMAKE_BUILD_TYPE=debug"
        self.flags["release"]   = "-DCMAKE_BUILD_TYPE=release"

        self.downloadLink = "https://github.com/beltoforion/muparser/archive/v%s.tar.gz" % self.version

    def install(self):
        Library.setDefaultPathsAndNames(self)

        Library.setup(self)

        Library.extractLibrary(self)

        Library.writeMessage(self, "Moving to source directory")
        os.chdir(self.sourceDirectory)

        self.setPrecision()

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

    def setPrecision(self):
        file = "./include/muParserDef.h"
        fh, path = tempfile.mkstemp()
        with os.fdopen(fh, "w") as new:
            with open(file) as old:
                for line in old:
                    new.write(line.replace("#define MUP_BASETYPE double", "#define MUP_BASETYPE long double"))
        os.remove(file)
        shutil.move(path, file)

        file = "./include/muParserDLL.h"
        fh, path = tempfile.mkstemp()
        with os.fdopen(fh, "w") as new:
            with open(file) as old:
                for line in old:
                    new.write(line.replace("typedef double muFloat_t;           // floating point type", "typedef long double muFloat_t;           // floating point type"))
        os.remove(file)
        shutil.move(path, file)
