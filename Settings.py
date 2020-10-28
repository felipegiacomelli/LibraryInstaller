import os
import multiprocessing

systemPackages = True

rootBuildDirectory = os.environ["HOME"] + "/Delete"
rootInstallDirectory = os.environ["HOME"] + "/Libraries"
compressedFiles = rootInstallDirectory + "/targz"

releaseBuild = True
sharedLibrary = True

numberOfCores = str(multiprocessing.cpu_count())

libraries = {
    "openmpi"  : {"version" : "4.0.5" , "install" : True},

    "boost"    : {"version" : "1.74.0", "install" : True},

    "metis"    : {"version" : "5.1.0" , "install" : True},
    "petsc"    : {"version" : "3.12.4", "install" : True},

    "hdf5"     : {"version" : "1.10.5", "install" : True},
    "cgns"     : {"version" : "4.1.2" , "install" : True},
    "mshtocgns": {"version" : "7.0.0" , "install" : True},

    "dei"      : {"version" : "4.0.0" , "install" : True},

    "muparser" : {"version" : "2.2.6" , "install" : True},

    "triangle" : {"version" : "1.6.0" , "install" : False},
    "tetgen"   : {"version" : "1.5.1" , "install" : False}
}
