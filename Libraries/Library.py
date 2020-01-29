import os, io, subprocess, tarfile
import urllib.request

def cyan(message):
    return "%s %s %s" % ("\033[1;36m", message, "\033[0m")

class Library(object):
    def __init__(self, options, name, version):
        self.compressedFiles = options["compressedFiles"]
        self.rootDirectory = options["rootDirectory"]
        self.rootBuildDirectory = options["rootBuildDirectory"]
        self.rootInstallDirectory = options["rootInstallDirectory"]
        self.buildType = options["buildType"]
        self.libraryType = options["libraryType"]
        self.numberOfCores = options["numberOfCores"]
        self.name = name
        self.version = version
        self.versionMajor = version.split(".")[0]
        self.versionMinor = version.split(".")[1]
        self.versionPatch = version.split("%s.%s." % (self.versionMajor, self.versionMinor))[1]

        self.flags = {"configure" : "", "static" : "", "shared" : "", "debug" : "", "release" : "", "" : ""}

        self.downloadLink = ""

        self.logFile = io.StringIO()
        self.library = ""
        self.buildDirectory = ""
        self.installDirectory = ""
        self.compressedLibrary = ""
        self.sourceDirectory = ""
        self.libraryDirectory = ""
        self.libraryEnvironmentVariable = ""
        self.path = ""

    def setDefaultPathsAndNames(self):
        self.library = "%s-%s" % (self.name, self.version)
        self.buildDirectory = "%s/%s/%s/%s" % (self.rootBuildDirectory, self.library, self.buildType, self.libraryType)
        self.installDirectory = "%s/%s/%s/%s" % (self.rootInstallDirectory, self.library, self.buildType, self.libraryType)
        self.compressedLibrary = "%s/%s.tar.gz" % (self.compressedFiles, self.library)
        self.sourceDirectory = "%s/%s" % (self.buildDirectory, self.library)
        self.libraryDirectory = "%s/%s" % (self.rootInstallDirectory, self.library)
        self.libraryEnvironmentVariable = "%s_DIR" % self.name.upper()

    def writeMessage(self, message):
        self.logFile.write("\n%s\n" % message)
        self.logFile.flush()
        print("\n%s\n" % message)

    def runCommand(self, command):
        self.displayCommand(command)
        subprocess.check_call(["sh", "-c", "%s" % command], stdout=self.logFile, stderr=self.logFile)

    def displayCommand(self, command):
        self.logFile.write("\n%s$ %s\n" % (os.getcwd(), command))
        self.logFile.flush()

    def install(self):
        self.setup()

        self.extractLibrary()

        self.writeMessage("Moving to source directory")
        os.chdir(self.sourceDirectory)

        self.writeMessage("Running configure")
        self.runCommand("./configure %s --prefix=%s" % (self.flags["configure"], self.installDirectory))

        self.writeMessage("Building")
        self.runCommand("make -j %s" % self.numberOfCores)

        self.writeMessage("Installing")
        self.runCommand("make install")

        self.displayEndMessage()

    def setup(self):
        if not os.path.exists(self.buildDirectory):
            os.makedirs(self.buildDirectory)

        self.logFile = open("%s/%s.log" % (self.buildDirectory, self.library), "w")
        self.logFile.write("\n")

        self.writeMessage("Building%s" % cyan(self.library))

        self.writeMessage("Creating install directory")
        if not os.path.exists(self.installDirectory):
            os.makedirs(self.installDirectory)

        self.flags["configure"] = "%s %s %s" % (self.flags["configure"], self.flags[self.buildType], self.flags[self.libraryType])

    def extractLibrary(self):
        if not os.path.exists(self.sourceDirectory):
            if not os.path.exists(self.compressedLibrary):
                self.writeMessage("Downloading %s" % self.library)
                urllib.request.urlretrieve(self.downloadLink, self.compressedLibrary)

            self.writeMessage("Extracting %s" % self.compressedLibrary)
            tar = tarfile.open(self.compressedLibrary)
            tar.extractall(path=self.buildDirectory)
            tar.close()

    def displayEndMessage(self):
        self.writeMessage("Build directory: %s" % self.buildDirectory)
        self.writeMessage("Compressed library: %s" % self.compressedLibrary)
        self.writeMessage("Install directory: %s" % self.installDirectory)
        self.writeMessage("Log file: %s" % self.logFile.name)

    def exportEnvironmentVariable(self, extra=""):
        environment = "export %s=%s/%s" % (self.libraryEnvironmentVariable, self.libraryDirectory, extra)
        environment = environment.replace(os.environ["HOME"], "$HOME")

        if not self.lineExists(environment):
            self.exportName(self.libraryEnvironmentVariable, "%s/%s" % (self.libraryDirectory, extra))
            environ = os.environ.copy()
            environ[self.libraryEnvironmentVariable] = "%s/%s" % (self.libraryDirectory, extra)
            os.environ.update(environ)

    def lineExists(self, target):
        with open("%s/.bashrc" % os.environ["HOME"], "r") as bashrc:
            for line in bashrc:
                if target == line.rstrip():
                    return True
        return False

    def exportName(self, name, value):
        bashrc = open("%s/.bashrc" % os.environ["HOME"], "a")
        bashrc.write("export %s=%s\n" % (name, value.replace(os.environ["HOME"], "$HOME")))
        bashrc.close()

    def exportPath(self, extra=""):
        path = ("export %s=%s:%s" % ("PATH", self.path.replace(os.environ["HOME"], "$HOME"), "$PATH"))

        if not self.lineExists(path):
            self.exportName(name="PATH", value="%s:$PATH" % self.path)

    def __del__(self):
        self.logFile.close()
