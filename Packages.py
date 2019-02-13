import os, subprocess

packages = []
packages.append("cmake")
packages.append("bison")
packages.append("flex")
packages.append("diffutils")
packages.append("wget")
packages.append("dos2unix")
packages.append("tcl")
packages.append("tk")

def installSystemPackages():
    # subprocess.call(["sh", "-c", "sudo pacman -Syu --noconfirm"])

    for package in packages:
        subprocess.call(["sh", "-c", "sudo pacman -S --noconfirm --needed " + package])
