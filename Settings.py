import os
import multiprocessing

rootBuildDirectory = os.environ["HOME"] + "/Delete"
rootInstallDirectory = os.environ["HOME"] + "/Libraries"

buildType = "Release"
libraryType = "Shared"

environmentVariables = True

numberOfCores = str(multiprocessing.cpu_count())

libraries = [
    ["openmpi"  , "3.0.1" , False],
    ["boost"    , "1.68.0", False],
    ["petsc"    , "3.10.2", False],
    ["cgns"     , "3.3.1" , False],
    ["muparser" , "2.2.5" , False],
    ["hdf5"     , "1.8.19", False],
    ["metis"    , "5.1.0" , False],
    ["cgnstools", "3.3.1" , True]
]
