import os
import io
import subprocess

class Library(object):
    def __init__(self, options, name, version):
        self.buildType = options["buildType"]
        self.libraryType = options["libraryType"]
        self.environmentVariables = options["environmentVariables"]
        self.numberOfCores = options["numberOfCores"]

        self.flags = {"Configure" : "", "Static" : "", "Shared" : "", "Debug" : "", "Release" : "", "" : ""}

        self.downloadLink = ""

        self.library = "%s-%s" % (name, version)
        self.buildDirectory = "%s/%s/%s/%s" % (options["rootBuildDirectory"], self.library, self.buildType, self.libraryType)
        self.installDirectory = "%s/%s/%s/%s" % (options["rootInstallDirectory"], self.library, self.buildType, self.libraryType)
        self.logFile = io.StringIO()
        self.compressedLibrary = "%s/%s.tar.gz" % (options["compressedFiles"], self.library)
        self.sourceDirectory = "%s/%s" % (self.buildDirectory, self.library)
        self.libraryDirectory = "%s/%s" % (options["rootInstallDirectory"], self.library)
        self.libraryEnvironmentVariable = "%s_DIR" % name.upper()

    def writeMessage(self, message):
        subprocess.check_call(["sh", "-c", "echo -e \"\n%s\n\" | tee -a %s" % (message, self.logFile.name)])

    def runCommand(self, command):
        self.displayCommand(command)
        subprocess.check_call(["sh", "-c", "%s 2>>%s >> %s" % (command, self.logFile.name, self.logFile.name)], stdout=self.logFile)

    def displayCommand(self, command):
        subprocess.check_call(["sh", "-c", "echo -e \"\n`pwd`\$ %s\n\"" % command], stdout=self.logFile)

    def install(self):
        self.setup()

        self.extractLibrary()

        self.writeMessage("Moving to source directory")
        os.chdir(self.sourceDirectory)

        self.writeMessage("Running configure")
        self.runCommand("./configure %s --prefix=%s" % (self.flags["Configure"], self.installDirectory))

        self.writeMessage("Building")
        self.runCommand("make -j %s" % self.numberOfCores)

        self.writeMessage("Installing")
        self.runCommand("make install")

        self.displayEndMessage()

    def setup(self):
        # self.setDefaultPathsAndNames()

        if not os.path.exists(self.buildDirectory):
            os.makedirs(self.buildDirectory)

        self.logFile = open("%s/%s.log" % (self.buildDirectory, self.library), "w")
        self.logFile.write("\n")

        self.writeMessage("Building %s" % self.library)

        self.writeMessage("Creating install directory")
        if not os.path.exists(self.installDirectory):
            os.makedirs(self.installDirectory)

        self.flags["Configure"] = "%s %s %s" % (self.flags["Configure"], self.flags[self.buildType], self.flags[self.libraryType])

    # def setDefaultPathsAndNames(self):

    def extractLibrary(self):
        if not os.path.exists(self.sourceDirectory):
            if os.path.exists(self.compressedLibrary):
                self.writeMessage("Extracting %s" % self.compressedLibrary)
                self.runCommand("tar -x -z -f %s -C %s" % (self.compressedLibrary, self.buildDirectory))
            else:
                self.writeMessage("Downloading %s" % self.library)
                self.runCommand("wget %s -O %s" % (self.downloadLink, self.compressedLibrary))
                self.runCommand("tar -x -z -f %s -C %s" % (self.compressedLibrary, self.buildDirectory))

    def displayEndMessage(self):
        self.writeMessage("Build directory: %s" % self.buildDirectory)
        self.writeMessage("Compressed library: %s" % self.compressedLibrary)
        self.writeMessage("Install directory: %s" % self.installDirectory)
        self.writeMessage("Log file: %s" % self.logFile.name)

    def exportEnvironmentVariables(self, extra=""):
        if self.environmentVariables:
            self.exportName(self.libraryEnvironmentVariable, "%s/%s" % (self.libraryDirectory, extra))

    def exportName(self, name, value):
        bashrc = open("%s/.bashrc" % os.environ["HOME"], "a")
        bashrc.write("export %s=%s\n" % (name, value))
        bashrc.close()

    def appendCommand(self, message, command):
        final = "echo -e \"\n%s\n\" | tee -a %s && " % (message, self.logFile.name)

        final = final + "echo -e \"\n`pwd`\$ %s\n\" && " % command

        return final + "%s 2>>%s >> %s;" % (command, self.logFile.name, self.logFile.name)

    def __del__(self):
        self.logFile.close()
