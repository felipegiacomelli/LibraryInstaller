import os, sys, re

import Settings, Packages

sys.path.append("./Libraries")
from Openmpi import Openmpi
from Boost import Boost
from Petsc import Petsc
from Hdf5 import Hdf5
from Cgns import Cgns
from Muparser import Muparser
from MshToCgns import MshToCgns
from Triangle import Triangle
from Tetgen import Tetgen
from Metis import Metis
from DivideEtImpera import DivideEtImpera

def main():
    options = {
        "systemPackages" : Settings.systemPackages,
        "compressedFiles" : Settings.compressedFiles,
        "rootDirectory" : os.getcwd(),
        "rootBuildDirectory" : Settings.rootBuildDirectory,
        "rootInstallDirectory" : Settings.rootInstallDirectory,
        "buildType" : "release" if Settings.releaseBuild else "debug",
        "libraryType" : "shared" if Settings.sharedLibrary else "static",
        "environmentVariables" : Settings.environmentVariables,
        "numberOfCores" : Settings.numberOfCores,
    }

    printOptions(options)

    if options["systemPackages"]:
        Packages.installSystemPackages(options["rootBuildDirectory"])

    if not os.path.exists(options["compressedFiles"]):
        os.makedirs(options["compressedFiles"])

    checkDependencies()

    installLibraries(options)

def checkDependencies():
    checkDependency("openmpi", "OPENMPI_DIR", "4.0.1")

    if Settings.libraries["petsc"]["install"]:
        checkDependency("metis", "METIS_DIR", "5.1.0")

    if Settings.libraries["dei"]["install"]:
        checkDependency("mshtocgns", "MSHTOCGNS_DIR", "2.0.0")

    if Settings.libraries["mshtocgns"]["install"]:
        checkDependency("boost", "BOOST_DIR", "1.70.0")
        checkDependency("cgns", "CGNS_DIR", "3.4.0")

    if Settings.libraries["cgns"]["install"]:
        checkDependency("hdf5", "HDF5_DIR", "1.10.5")

def checkDependency(name, environmentVariable, requiredVersion):
    if not Settings.libraries[name]["install"]:
        if environmentVariable not in os.environ:
            Settings.libraries[name]["install"] = True
        elif not os.path.exists(os.environ[environmentVariable]):
            Settings.libraries[name]["install"] = True
        else:
            if re.findall(r"\d*\.\d*\.\d*", os.environ[environmentVariable])[0] != requiredVersion:
                Settings.libraries[name]["install"] = True

def installLibraries(options):
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

    if Settings.libraries["metis"]["install"]:
        metis = Metis(options, Settings.libraries["metis"]["version"])
        metis.install()

    if Settings.libraries["petsc"]["install"]:
        petsc = Petsc(options, Settings.libraries["petsc"]["version"])
        petsc.install()

    if Settings.libraries["hdf5"]["install"]:
        hdf5 = Hdf5(options, Settings.libraries["hdf5"]["version"])
        hdf5.install()

    if Settings.libraries["cgns"]["install"]:
        cgns = Cgns(options, Settings.libraries["cgns"]["version"])
        cgns.install()

    if Settings.libraries["mshtocgns"]["install"]:
        mshToCgns = MshToCgns(options, Settings.libraries["mshtocgns"]["version"])
        mshToCgns.install()

    if Settings.libraries["dei"]["install"]:
        dei = DivideEtImpera(options, Settings.libraries["dei"]["version"])
        dei.install()

    if Settings.libraries["muparser"]["install"]:
        muparser = Muparser(options, Settings.libraries["muparser"]["version"])
        muparser.install()

    if Settings.libraries["triangle"]["install"]:
        triangle = Triangle(options, Settings.libraries["triangle"]["version"])
        triangle.install()

    if Settings.libraries["tetgen"]["install"]:
        tetgen = Tetgen(options, Settings.libraries["tetgen"]["version"])
        tetgen.install()

def purple(message):
    return "%s%s%s" % ("\033[1;35m", message, "\033[0m")

def yellow(message):
    return "%s%s%s" % ("\033[1;33m", message, "\033[0m")

def printOptions(options):
    print(purple("\noptions"))
    for key, value in options.items():
        if key == "buildType" or key == "libraryType" or key == "environmentVariables" or key == "systemPackages":
            print("\t%s : %s" % (key, yellow(value)))
        else:
            print("\t%s : %s" % (key, value))

    print("\tPATH:")
    for directory in os.environ["PATH"].split(":"):
        print("%s%s" % ("\t\t", directory))

if __name__ == "__main__":
    main()
