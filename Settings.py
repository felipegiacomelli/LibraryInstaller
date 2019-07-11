import os
import multiprocessing

systemPackages = True

rootBuildDirectory = os.environ["HOME"] + "/Delete"
rootInstallDirectory = os.environ["HOME"] + "/Libraries"
compressedFiles = rootInstallDirectory + "/targz"

buildType = "Release"
libraryType = "Shared"

environmentVariables = True

numberOfCores = str(multiprocessing.cpu_count())

libraries = {
    "openmpi"  : {"version" : "4.0.1" , "install" : True},
    "boost"    : {"version" : "1.70.0", "install" : True},
    "petsc"    : {"version" : "3.11.3", "install" : True},
    "hdf5"     : {"version" : "1.10.5", "install" : True},
    "cgns"     : {"version" : "3.4.0" , "install" : True},
    "muparser" : {"version" : "2.2.6" , "install" : True},
    "mshtocgns": {"version" : "1.0.0" , "install" : True},
    "triangle" : {"version" : "1.6.0" , "install" : False},
    "tetgen"   : {"version" : "1.5.1" , "install" : False},
    "metis"    : {"version" : "5.1.0" , "install" : False}
}
