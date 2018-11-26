import os

import Settings

from Openmpi import Openmpi

if __name__ == "__main__":

    rootDirectory = os.path.dirname(os.path.abspath(__file__))

    options = {
        "rootBuildDirectory" : Settings.rootBuildDirectory,
        "rootInstallDirectory" : Settings.rootInstallDirectory,
        "buildType" : Settings.buildType,
        "libraryType" : Settings.libraryType,
        "environmentVariables" : Settings.environmentVariables,
        "numberOfCores" : Settings.numberOfCores
    }
    print("\noptions: ")
    for keys,values in options.items():
        print("\t%s : %s" % (keys, values))

    # if Settings.libraries[0][0] == "openmpi" and Settings.libraries[0][1] == "3.0.1" and Settings.libraries[0][2]:
    #     openmpi = Openmpi(options, Settings.libraries[0][0], Settings.libraries[0][1])
    #     openmpi.install()

    # if Settings.libraries[1][0] == "boost" and Settings.libraries[1][1] == "1.68.0" and Settings.libraries[1][2]:
    #     boost = Boost(options, Settings.libraries[1][0], Settings.libraries[1][1])
    #     boost.install()

    if Settings.libraries[2][0] == "petsc" and Settings.libraries[2][1] == "3.10.2" and Settings.libraries[2][2]:
        boost = Boost(options, Settings.libraries[2][0], Settings.libraries[2][1])
        boost.install()
