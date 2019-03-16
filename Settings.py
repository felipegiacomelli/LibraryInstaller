import os
import multiprocessing

systemPackages = True

compressedFiles = os.environ["LIBRARIES_FILES"]
rootBuildDirectory = os.environ["HOME"] + "/Delete"
rootInstallDirectory = os.environ["HOME"] + "/Libraries"

buildType = "Release"
libraryType = "Shared"

environmentVariables = True

numberOfCores = str(multiprocessing.cpu_count())

libraries = {
    "openmpi"  : {"version" : "3.0.1" , "install" : True},
    "boost"    : {"version" : "1.69.0", "install" : True},
    "petsc"    : {"version" : "3.10.2", "install" : True},
    "cgns"     : {"version" : "3.3.1" , "install" : True},
    "muparser" : {"version" : "2.2.6" , "install" : True},
    "mshtocgns": {"version" : "0.15.0", "install" : True},
    "cgnstools": {"version" : "3.3.1" , "install" : True},
    "triangle" : {"version" : "1.6.0" , "install" : False},
    "tetgen"   : {"version" : "1.5.1" , "install" : False},
    "hdf5"     : {"version" : "1.8.19", "install" : False},
    "metis"    : {"version" : "5.1.0" , "install" : False}
}
