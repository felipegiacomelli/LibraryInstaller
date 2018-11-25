import os

import Settings

from Openmpi import Openmpi

if __name__ == "__main__":

    rootDirectory = os.path.dirname(os.path.abspath(__file__))

    if Settings.libraries[0][0] == "openmpi" and Settings.libraries[0][1] == "3.0.1" and Settings.libraries[0][2]:
        openmpi = Openmpi(Settings.rootBuildDirectory, Settings.rootInstallDirectory, Settings.buildType, Settings.libraryType, Settings.environmentVariables, Settings.libraries[0][0], Settings.libraries[0][1])
        openmpi.install()
