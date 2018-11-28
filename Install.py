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

    if Settings.libraries[0][0] == "openmpi" and Settings.libraries[0][1] == "3.0.1" and Settings.libraries[0][2]:
        openmpi = Openmpi(options, Settings.libraries[0][0], Settings.libraries[0][1])
        openmpi.install()

    if Settings.libraries[1][0] == "boost" and Settings.libraries[1][1] == "1.68.0" and Settings.libraries[1][2]:
        boost = Boost(options, Settings.libraries[1][0], Settings.libraries[1][1])
        boost.install()

    if Settings.libraries[2][0] == "petsc" and Settings.libraries[2][1] == "3.10.2" and Settings.libraries[2][2]:
        petsc = Petsc(options, Settings.libraries[2][0], Settings.libraries[2][1])
        petsc.install()

    if Settings.libraries[3][0] == "cgns" and Settings.libraries[3][1] == "3.3.1" and Settings.libraries[3][2]:
        cgns = Cgns(options, Settings.libraries[3][0], Settings.libraries[3][1])
        cgns.install()

    if Settings.libraries[4][0] == "muparser" and Settings.libraries[4][1] == "2.2.5" and Settings.libraries[4][2]:
        muparser = Muparser(options, Settings.libraries[4][0], Settings.libraries[4][1])
        muparser.install()

    if Settings.libraries[5][0] == "hdf5" and Settings.libraries[5][1] == "1.8.19" and Settings.libraries[5][2]:
        hdf5 = Hdf5(options, Settings.libraries[5][0], Settings.libraries[5][1])
        hdf5.install()

    if Settings.libraries[6][0] == "metis" and Settings.libraries[6][1] == "5.1.0" and Settings.libraries[6][2]:
        metis = Metis(options, Settings.libraries[6][0], Settings.libraries[6][1])
        metis.install()

    if Settings.libraries[7][0] == "cgnstools" and Settings.libraries[7][1] == "3.3.1" and Settings.libraries[7][2]:
        cgnstools = Cgnstools(options, Settings.libraries[7][0], Settings.libraries[7][1])
        cgnstools.install()
