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

def purple(message):
    return "%s%s%s" % ("\033[1;35m", message, "\033[0m")

def yellow(message):
    return "%s%s%s" % ("\033[1;33m", message, "\033[0m")

def printOptions(options):
    print(purple("\noptions"))
    for key,value in options.items():
        if key is "path":
            print("\tpath:")
            for directory in options["path"].split(":"):
                print("%s%s" % ("\t\t", directory))
        elif key is "buildType" or key is "libraryType" or key is "environmentVariables":
            print("\t%s : %s" % (key, yellow(value)))
        else:
            print("\t%s : %s" % (key, value))

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

    openmpi = Openmpi(options, Settings.libraries["openmpi"]["version"])
    if Settings.libraries["openmpi"]["install"] == True:
        openmpi.install()

    if openmpi.path in options["path"]:
        pass
    else:
        options["path"] = "%s:%s" % (openmpi.path, options["path"])

    if Settings.libraries["boost"]["install"] == True:
        boost = Boost(options, Settings.libraries["boost"]["version"])
        boost.install()

    if Settings.libraries["petsc"]["install"] == True:
        petsc = Petsc(options, Settings.libraries["petsc"]["version"])
        petsc.install()

    if Settings.libraries["cgns"]["install"] == True:
        cgns = Cgns(options, Settings.libraries["cgns"]["version"])
        cgns.install()

    if Settings.libraries["muparser"]["install"] == True:
        muparser = Muparser(options, Settings.libraries["muparser"]["version"])
        muparser.install()

    if Settings.libraries["hdf5"]["install"] == True:
        hdf5 = Hdf5(options, Settings.libraries["hdf5"]["version"])
        hdf5.install()

    if Settings.libraries["metis"]["install"] == True:
        metis = Metis(options, Settings.libraries["metis"]["version"])
        metis.install()

    if Settings.libraries["cgnstools"]["install"] == True:
        cgnstools = Cgnstools(options, Settings.libraries["cgnstools"]["version"])
        cgnstools.install()
