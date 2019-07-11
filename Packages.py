import os
import subprocess

packages = []
packages.append("gcc")
packages.append("make")
packages.append("cmake")
packages.append("bison")
packages.append("flex")
packages.append("diffutils")
packages.append("wget")
packages.append("dos2unix")
packages.append("tcl")
packages.append("tk")

def installSystemPackages(rootBuildDirectory):
    if not os.path.exists(rootBuildDirectory):
        os.makedirs(rootBuildDirectory)

    logFile = open("%s/packages.log" % rootBuildDirectory, "w")
    logFile.write("\n")

    isPackageInstalled = []
    for package in packages:
        child = subprocess.Popen(["sh", "-c", "pacman -Qi %s 2>>%s" % (package, "/dev/null")], stdout=logFile)
        child.wait()
        if child.returncode == 1:
            isPackageInstalled.append(False)
        else:
            isPackageInstalled.append(True)

    if False in isPackageInstalled:
        print("\n\tMust install packages")
        subprocess.call(["sh", "-c", "sudo pacman -Syu --noconfirm"])
    else:
        print("\n\tAll packages are already installed")
        logFile.close()
        return

    for package in packages:
        subprocess.call(["sh", "-c", "sudo pacman -S --noconfirm --needed %s 2>>%s >> %s" % (package, "/dev/null", "/dev/null")])

    logFile.close()
    return
