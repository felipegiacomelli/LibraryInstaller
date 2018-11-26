import os
import multiprocessing

rootBuildDirectory = os.environ["HOME"] + "/Delete"
rootInstallDirectory = os.environ["HOME"] + "/libraries"

buildType = "Debug"
libraryType = "Shared"

environmentVariables = True

numberOfCores = str(multiprocessing.cpu_count())

libraries = [
    ["openmpi"  , "3.0.1" , False],
    ["boost"    , "1.68.0", False],
    ["petsc"    , "3.10.2", False],
    ["hdf5"     , "1.8.19", True],
    ["cgns"     , "3.3.1" , False],
    ["muparser" , "2.2.5" , True],
    ["metis"    , "5.1.0" , True],
    ["cgnstools", "3.3.1" , True]
]
