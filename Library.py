import os
import subprocess
import multiprocessing

class Library(object):
    def __init__(self, rootBuildDirectory, rootInstallDirectory, buildType, libraryType, environmentVariables, name, version):
        self.buildType = buildType
        self.libraryType = libraryType
        self.environmentVariables = environmentVariables

        self.flags = {"Configure" : "", "Static" : "", "Shared" : "", "Debug" : "", "Release" : "", "" : ""}

        self.downloadLink = ""

        self.library = "%s-%s" % (name, version)
        self.buildDirectory = "%s/%s/%s/%s" % (rootBuildDirectory, self.library, buildType, libraryType)
        self.installDirectory = "%s/%s/%s/%s" % (rootInstallDirectory, self.library, buildType, libraryType)
        self.logFile = open("%s/%s.log" % (self.buildDirectory, self.library), "w")
        self.compressedLibrary = "%s/%s.tar.gz" % (os.environ["LIBRARIES_FILES"], self.library)
        self.sourceDirectory = "%s/%s" % (self.buildDirectory, self.library)
        self.libraryDirectory = "%s/%s" % (rootInstallDirectory, self.library)
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

        # self.writeMessage("Running configure")
        # self.runCommand("./configure %s --prefix=%s" % (self.flags["Configure"], self.installDirectory))

        # self.writeMessage("Building")
        # self.runCommand("make -j %s" % str(multiprocessing.cpu_count()))

        # self.writeMessage("Installing")
        # self.runCommand("make install")

        self.writeMessage("Build directory: %s" % self.buildDirectory)
        self.writeMessage("Compressed library: %s" % self.compressedLibrary)
        self.writeMessage("Install directory: %s" % self.installDirectory)
        self.writeMessage("Log file: %s" % self.logFile.name)

    def setup(self):
        if not os.path.exists(self.buildDirectory):
            os.makedirs(self.buildDirectory)

        self.writeMessage("Initializing log file")
        self.logFile.write("\n")

        self.writeMessage("Building %s" % self.library)

        self.writeMessage("Creating install directory")
        if not os.path.exists(self.installDirectory):
            os.makedirs(self.installDirectory)

        self.flags["Configure"] = "%s %s %s" % (self.flags["Configure"], self.flags[self.buildType], self.flags[self.libraryType])

    def extractLibrary(self):
        if not os.path.exists(self.sourceDirectory):
            if os.path.exists(self.compressedLibrary):
                self.writeMessage("Extracting %s" % self.compressedLibrary)
                self.runCommand("tar -x -z -f %s -C %s" % (self.compressedLibrary, self.buildDirectory))
            else:
                self.writeMessage("Downloading %s" % self.library)
                self.runCommand("wget %s -O %s" % (self.downloadLink, self.compressedLibrary))
                self.runCommand("tar -x -z -f %s -C %s" % (self.compressedLibrary, self.buildDirectory))

    def exportEnvironmentVariables(self, extra):
        if self.environmentVariables:
            self.exportName(self.libraryEnvironmentVariable, "%s/%s" % (self.libraryDirectory, extra))

    def exportName(self, name, value):
        bashrc = open("%s/.bashrc" % os.environ["HOME"], "a")
        bashrc.write("export %s=%s\n" % (name, value))
        bashrc.close()

    def __del__(self):
        self.logFile.close()
