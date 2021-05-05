import os
import multiprocessing

systemPackages = True

rootBuildDirectory = os.environ["HOME"] + "/Delete"
rootInstallDirectory = os.environ["HOME"] + "/Libraries"
compressedFiles = rootInstallDirectory + "/targz"

releaseBuild = False
sharedLibrary = True
mpi = "openmpi"

numberOfCores = str(multiprocessing.cpu_count())

libraries = {
    "mpich"    : {"version" : "3.4.1" , "install" : False},
    "openmpi"  : {"version" : "4.0.5" , "install" : False},

    "boost"    : {"version" : "1.74.0", "install" : True},

    "metis"    : {"version" : "5.1.0" , "install" : True},
    "petsc"    : {"version" : "3.14.3", "install" : True},

    "hdf5"     : {"version" : "1.10.5", "install" : True},
    "cgns"     : {"version" : "4.1.2" , "install" : True},
    "mshtocgns": {"version" : "8.0.0" , "install" : True},

    "dei"      : {"version" : "2.0.0" , "install" : True},

    "muparser" : {"version" : "2.3.2" , "install" : True},

    "triangle" : {"version" : "1.6.0" , "install" : False},
    "tetgen"   : {"version" : "1.5.1" , "install" : False}
}
