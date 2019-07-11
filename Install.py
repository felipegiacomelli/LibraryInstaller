import os
import sys

import Settings
import Packages

sys.path.append("./Libraries")
from Openmpi import Openmpi
from Boost import Boost
from Petsc import Petsc
from Cgns import Cgns
from Muparser import Muparser
from Hdf5 import Hdf5
from Metis import Metis
from Triangle import Triangle
from Tetgen import Tetgen
from Mshtocgns import Mshtocgns

def purple(message):
    return "%s%s%s" % ("\033[1;35m", message, "\033[0m")

def yellow(message):
    return "%s%s%s" % ("\033[1;33m", message, "\033[0m")

def printOptions(options):
    print(purple("\noptions"))
    for key, value in options.items():
        if key is "buildType" or key is "libraryType" or key is "environmentVariables" or key is "systemPackages":
            print("\t%s : %s" % (key, yellow(value)))
        else:
            print("\t%s : %s" % (key, value))

    print("\tPATH:")
    for directory in os.environ["PATH"].split(":"):
        print("%s%s" % ("\t\t", directory))

if __name__ == "__main__":

    options = {
        "systemPackages" : Settings.systemPackages,
        "compressedFiles" : Settings.compressedFiles,
        "rootDirectory" : os.getcwd(),
        "rootBuildDirectory" : Settings.rootBuildDirectory,
        "rootInstallDirectory" : Settings.rootInstallDirectory,
        "buildType" : Settings.buildType.lower(),
        "libraryType" : Settings.libraryType.lower(),
        "environmentVariables" : Settings.environmentVariables,
        "numberOfCores" : Settings.numberOfCores,
    }

    printOptions(options)

    if options["systemPackages"]:
        Packages.installSystemPackages(options["rootBuildDirectory"])

    if not os.path.exists(options["compressedFiles"]):
        os.makedirs(options["compressedFiles"])

    openmpi = Openmpi(options, Settings.libraries["openmpi"]["version"])
    if Settings.libraries["openmpi"]["install"]:
        openmpi.install()

    if openmpi.path not in os.environ["PATH"]:
        environ = os.environ.copy()
        environ["PATH"] = "%s:%s" % (openmpi.path, environ["PATH"])
        os.environ.update(environ)

    if "CC" not in os.environ or "CXX" not in os.environ:
        environ = os.environ.copy()
        environ["CC"] = "mpicc"
        environ["CXX"] = "mpicxx"
        os.environ.update(environ)

    if Settings.libraries["boost"]["install"]:
        boost = Boost(options, Settings.libraries["boost"]["version"])
        boost.install()

    if Settings.libraries["petsc"]["install"]:
        petsc = Petsc(options, Settings.libraries["petsc"]["version"])
        petsc.install()

    if Settings.libraries["hdf5"]["install"]:
        hdf5 = Hdf5(options, Settings.libraries["hdf5"]["version"])
        hdf5.install()

    if Settings.libraries["cgns"]["install"]:
        cgns = Cgns(options, Settings.libraries["cgns"]["version"])
        cgns.install()

    if Settings.libraries["muparser"]["install"]:
        muparser = Muparser(options, Settings.libraries["muparser"]["version"])
        muparser.install()

    if Settings.libraries["mshtocgns"]["install"]:
        mshtocgns = Mshtocgns(options, Settings.libraries["mshtocgns"]["version"])
        mshtocgns.install()

    if Settings.libraries["triangle"]["install"]:
        triangle = Triangle(options, Settings.libraries["triangle"]["version"])
        triangle.install()

    if Settings.libraries["tetgen"]["install"]:
        tetgen = Tetgen(options, Settings.libraries["tetgen"]["version"])
        tetgen.install()

    if Settings.libraries["metis"]["install"]:
        metis = Metis(options, Settings.libraries["metis"]["version"])
        metis.install()
