import os
import multiprocessing

systemPackages = True

rootBuildDirectory = os.environ["HOME"] + "/Delete"
rootInstallDirectory = os.environ["HOME"] + "/Libraries"
compressedFiles = rootInstallDirectory + "/targz"

releaseBuild = True
sharedLibrary = True

environmentVariables = True

numberOfCores = str(multiprocessing.cpu_count())

libraries = {
    "openmpi"  : {"version" : "4.0.2" , "install" : False},

    "boost"    : {"version" : "1.72.0", "install" : False},

    "metis"    : {"version" : "5.1.0" , "install" : False},
    "petsc"    : {"version" : "3.12.2", "install" : False},

    "hdf5"     : {"version" : "1.10.5", "install" : False},
    "cgns"     : {"version" : "3.4.0" , "install" : False},
    "mshtocgns": {"version" : "3.0.0" , "install" : False},

    "dei"      : {"version" : "1.0.0" , "install" : False},

    "muparser" : {"version" : "2.2.6" , "install" : True},

    "triangle" : {"version" : "1.6.0" , "install" : False},
    "tetgen"   : {"version" : "1.5.1" , "install" : False}
}
