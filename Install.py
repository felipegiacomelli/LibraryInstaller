import os
import io

import Settings

from Openmpi import Openmpi
from Boost import Boost
from Petsc import Petsc
from Cgns import Cgns
from Muparser import Muparser
from Hdf5 import Hdf5
from Metis import Metis
from Cgnstools import Cgnstools

def red(message):
    return "%s%s%s%s" % ("\n", "\033[1;31m", message, "\033[0m")

def printOptions(options):
    print(red("options"))
    for key,value in options.items():
        if key is not "path":
            print("\t%s : %s" % (key, value))
        else:
            print("\tpath:")
            for directory in options["path"].split(":"):
                print("%s%s" % ("\t\t", directory))

if __name__ == "__main__":

    rootDirectory = os.path.dirname(os.path.abspath(__file__))

    options = {
        "compressedFiles" : Settings.compressedFiles,
        "rootBuildDirectory" : Settings.rootBuildDirectory,
        "rootInstallDirectory" : Settings.rootInstallDirectory,
        "buildType" : Settings.buildType,
        "libraryType" : Settings.libraryType,
        "environmentVariables" : Settings.environmentVariables,
        "numberOfCores" : Settings.numberOfCores,
        "path": os.environ["PATH"]
    }

    printOptions(options)

    if Settings.libraries["openmpi"]["install"] == True:
        openmpi = Openmpi(options, "openmpi", Settings.libraries["openmpi"]["version"])
        openmpi.install()

    if Settings.libraries["boost"]["install"] == True:
        boost = Boost(options, "boost", Settings.libraries["boost"]["version"])
        boost.install()

    if Settings.libraries["petsc"]["install"] == True:
        petsc = Petsc(options, "petsc", Settings.libraries["petsc"]["version"])
        petsc.install()

    if Settings.libraries["cgns"]["install"] == True:
        cgns = Cgns(options, "cgns", Settings.libraries["cgns"]["version"])
        cgns.install()

    if Settings.libraries["muparser"]["install"] == True:
        muparser = Muparser(options, "muparser", Settings.libraries["muparser"]["version"])
        muparser.install()

    if Settings.libraries["hdf5"]["install"] == True:
        hdf5 = Hdf5(options, "hdf5", Settings.libraries["hdf5"]["version"])
        hdf5.install()

    if Settings.libraries["metis"]["install"] == True:
        metis = Metis(options, "metis", Settings.libraries["metis"]["version"])
        metis.install()

    if Settings.libraries["cgnstools"]["install"] == True:
        cgnstools = Cgnstools(options, "cgnstools", Settings.libraries["cgnstools"]["version"])
        cgnstools.install()
