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
from Mpich import Mpich

def main():
    options = {
        "systemPackages" : Settings.systemPackages,
        "compressedFiles" : Settings.compressedFiles,
        "rootDirectory" : os.getcwd(),
        "rootBuildDirectory" : Settings.rootBuildDirectory,
        "rootInstallDirectory" : Settings.rootInstallDirectory,
        "buildType" : "release" if Settings.releaseBuild else "debug",
        "libraryType" : "shared" if Settings.sharedLibrary else "static",
        "mpi" : Settings.mpi,
        "numberOfCores" : Settings.numberOfCores,
    }

    printOptions(options)

    if options["systemPackages"]:
        Packages.installSystemPackages(options["rootBuildDirectory"])

    if not os.path.exists(options["compressedFiles"]):
        os.makedirs(options["compressedFiles"])

    checkArgv()

    checkDependencies()

    installLibraries(options)

def checkArgv():
    if len(sys.argv) >= 2:
        for library in Settings.libraries.keys():
            Settings.libraries[library]["install"] = False

        libraries = iter(sys.argv)
        next(libraries)
        for library in libraries:
            Settings.libraries[library]["install"] = True

def checkDependencies():
    if Settings.mpi == "openmpi":
        checkDependency("openmpi", "OPENMPI_DIR", Settings.libraries["openmpi"]["version"])
    elif Settings.mpi == "mpich":
        checkDependency("mpich", "MPICH_DIR", Settings.libraries["mpich"]["version"])
    else:
        raise

    if Settings.libraries["petsc"]["install"]:
        checkDependency("metis", "METIS_DIR", "5.1.0")

    if Settings.libraries["dei"]["install"]:
        if Settings.libraries["dei"]["version"] == "5.0.0":
            checkDependency("mshtocgns", "MSHTOCGNS_DIR", "8.0.0")
        if Settings.libraries["dei"]["version"] == "4.0.0":
            checkDependency("mshtocgns", "MSHTOCGNS_DIR", "7.0.0")
        elif Settings.libraries["dei"]["version"] == "3.0.0":
            checkDependency("mshtocgns", "MSHTOCGNS_DIR", "6.0.0")
        elif Settings.libraries["dei"]["version"] == "0.0.0" or Settings.libraries["dei"]["version"] == "0.0.1":
            checkDependency("mshtocgns", "MSHTOCGNS_DIR", "2.0.0")
        else:
            checkDependency("mshtocgns", "MSHTOCGNS_DIR", "3.0.0")

    if Settings.libraries["mshtocgns"]["install"]:
        version = Settings.libraries["mshtocgns"]["version"]
        if version == "7.0.0" or version == "8.0.0":
            checkDependency("cgns", "CGNS_DIR", "4.1.2")
            checkDependency("boost", "BOOST_DIR", "1.74.0")
        elif Settings.libraries["mshtocgns"]["version"] == "2.0.0":
            checkDependency("cgns", "CGNS_DIR", "3.4.0")
            checkDependency("boost", "BOOST_DIR", "1.70.0")
        else:
            checkDependency("cgns", "CGNS_DIR", "3.4.0")
            checkDependency("boost", "BOOST_DIR", "1.72.0")

    if Settings.libraries["cgns"]["install"]:
        checkDependency("hdf5", "HDF5_DIR", "1.10.5")

def checkDependency(name, environmentVariable, requiredVersion):
    if not Settings.libraries[name]["install"]:
        if environmentVariable not in os.environ:
            Settings.libraries[name]["install"] = True
            Settings.libraries[name]["version"] = requiredVersion
        elif not os.path.exists(os.environ[environmentVariable]):
            Settings.libraries[name]["install"] = True
            Settings.libraries[name]["version"] = requiredVersion
        else:
            if re.findall(r"\d*\.\d*\.\d*", os.environ[environmentVariable])[0] != requiredVersion:
                Settings.libraries[name]["install"] = True
                Settings.libraries[name]["version"] = requiredVersion

def installLibraries(options):
    openmpi = Openmpi(options, Settings.libraries["openmpi"]["version"])
    if Settings.libraries["openmpi"]["install"]:
        openmpi.install()

    mpich = Mpich(options, Settings.libraries["mpich"]["version"])
    if Settings.libraries["mpich"]["install"]:
        mpich.install()

    if Settings.mpi == "openmpi" and openmpi.path not in os.environ["PATH"]:
        environ = os.environ.copy()
        environ["PATH"] = "%s:%s" % (openmpi.path, environ["PATH"])
        os.environ.update(environ)
    elif Settings.mpi == "mpich" and mpich.path not in os.environ["PATH"]:
        environ = os.environ.copy()
        environ["PATH"] = "%s:%s" % (mpich.path, environ["PATH"])
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
        if key == "buildType" or key == "libraryType" or key == "systemPackages" or key == "mpi":
            print("\t%s : %s" % (key, yellow(value)))
        else:
            print("\t%s : %s" % (key, value))

    print("\tPATH:")
    for directory in os.environ["PATH"].split(":"):
        print("%s%s" % ("\t\t", directory))

if __name__ == "__main__":
    main()
