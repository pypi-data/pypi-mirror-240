"""FlashXTest library to interface with backend.FlashTest"""

from datetime import date
import os, sys, subprocess
import itertools
import glob
import argparse
import shlex

from .. import backend
from .. import lib

sys.tracebacklimit = 1

# Create a test suite parser
SuiteParser = argparse.ArgumentParser(description="Parser for test suite")
SuiteParser.add_argument("-t", "--test", help="Test node", type=str)
SuiteParser.add_argument("-np", "--nprocs", help="Num procs", type=int)
SuiteParser.add_argument(
    "-cbase", "--cbase", help="Date for comparison benchmark", type=str
)
SuiteParser.add_argument(
    "-rbase", "--rbase", help="Date for restart benchmark", type=str
)
SuiteParser.add_argument("-tol", "--tolerance", help="Error tolerance", type=float)
SuiteParser.add_argument(
    "-e", "--env", action="append", nargs="+", help="Environment variable", type=str
)
SuiteParser.add_argument("-debug", "--debug", action="store_true")
SuiteParser.add_argument(
    "-as", "--add-setup-opts", help="Additional setup options", type=str
)
SuiteParser.set_defaults(
    debug=False,
    nprocs=1,
    test="",
    env=None,
    cbase=None,
    rbase=None,
    tolerance=0.0,
    add_setup_opts="",
)


class TestSpec:
    """
    Class TestSpec to handle test specifications
    """

    def __init__(self):
        """
        Constructor
        """
        for attr in [
            "setupName",
            "nodeName",
            "setupOptions",
            "numProcs",
            "parfiles",
            "restartParfiles",
            "transfers",
            "environment",
            "checkpointBasename",
            "comparisonNumber",
            "comparisonBenchmark",
            "restartNumber",
            "restartBenchmark",
            "shortPathToBenchmark",
            "debug",
            "cbase",
            "rbase",
            "errTol",
        ]:
            setattr(self, attr, None)

    def getXmlText(self):
        """
        get Xml text from test specifications
        """

        # Create an empty list
        xmlText = []

        # Deal with parfile paths
        if self.parfiles:
            if self.parfiles == "<defaultParfile>":
                pass
            else:
                parFileList = self.parfiles.split(" ")
                parFileList = [
                    "<pathToSimulations>" + "/" + self.setupName + "/tests/" + parfile
                    for parfile in parFileList
                ]
                self.parfiles = " ".join(parFileList)

        else:
            mainDict["log"].err(
                f"'parfiles' not defined for test {self.nodeName!r} for setup {self.setupName!r}"
            )
            raise ValueError()

        # Deal with debug flags
        if self.debug:
            self.setupOptions = self.setupOptions + " -debug"

        if self.add_setup_opts:
            self.setupOptions = " ".join(
                [self.setupOptions, self.add_setup_opts.strip()]
            )

        # Deal with restartParfiles path
        if self.restartParfiles:
            parFileList = self.restartParfiles.split(" ")
            parFileList = [
                "<pathToSimulations>" + "/" + self.setupName + "/tests/" + parfile
                for parfile in parFileList
            ]
            self.restartParfiles = " ".join(parFileList)

        if self.nodeName.split("/")[0] == "Composite":

            self.checkpointBasename = "flashx_hdf5_chk_"
            self.comparisonNumber = "0001"
            self.restartNumber = "0002"

            if self.cbase:
                self.comparisonBenchmark = f"<siteDir>/{self.cbase}/<buildDir>/<runDir>/<checkpointBasename><comparisonNumber>"

            if self.rbase:
                self.restartBenchmark = f"<siteDir>/{self.rbase}/<buildDir>/<runDir>/<checkpointBasename><restartNumber>"

        if self.nodeName.split("/")[0] == "Comparison" and self.cbase:
            self.shortPathToBenchmark = (
                f"<siteDir>/{self.cbase}/<buildDir>/<runDir>/<chkMax>"
            )

        # Deal with environment variables
        if self.environment:
            self.environment = " ".join(
                list(itertools.chain.from_iterable(self.environment))
            )

        # append to xmlText
        for xmlKey in list(self.__dict__.keys()):
            if (getattr(self, xmlKey)) and (
                xmlKey not in ["cbase", "rbase", "debug", "add_setup_opts"]
            ):
                xmlText.append(f"{xmlKey}: {getattr(self, xmlKey)}")

        return xmlText


def __continuationLines(fin):
    for line in fin:
        line = line.rstrip("\n")
        while line.endswith("\\"):
            line = line[:-1] + next(fin).rstrip("\n")
        yield line


def __continuedLineFromPrevLine(prevLine, continuedLine):
    if prevLine[0] != "#" and prevLine[0] != "\n":
        if prevLine.split("#")[0].split("\\")[0] == prevLine.split("#")[0]:
            continuedLine = ""
        else:
            continuedLine = continuedLine + prevLine.split("#")[0]
    else:
        continuedLine = ""

    return continuedLine


def __removeBaseline(line, baseKey, baseDate):

    line = line.strip("\n")
    lineComments = line.replace(line.split("#")[0], "")
    lineList = (line.replace(lineComments, "")).split(" ")

    try:
        baseIndex = lineList.index(baseKey)
    except:
        baseIndex = None

    if baseIndex is not None:
        if baseDate is None or baseDate == lineList[baseIndex + 1]:
            lineList.pop(baseIndex)
            lineList.pop(baseIndex)

    return " ".join(lineList) + lineComments + "\n"


def __addBaseline(line, baseKey, baseDate):

    line = line.strip("\n")
    lineComments = line.replace(line.split("#")[0], "")
    line = line.split("#")[0]

    if baseKey not in line:
        line = line + f" {baseKey} {baseDate}"

    if lineComments:
        lineComments = " " + lineComments

    return line + lineComments + "\n"


def removeBenchmarks(mainDict):
    """
    Remove benchmarks from a list of suite files

    Arguments
    ---------
    mainDict : Dicitionary for the API
    """

    # Check if pathToSuites is defined, if not use
    # all *.suite files from the working directory
    if not mainDict["pathToSuites"]:
        mainDict["pathToSuites"] = glob.glob("*.suite")

    # Loop over suite and start removing benchmarks
    for suiteFile in mainDict["pathToSuites"]:

        # Handle exceptions
        if not suiteFile.endswith(".suite"):
            mainDict["log"].err(f'File {suiteFile} must have a ".suite" suffix')
            raise ValueError

        if not os.path.exists(suiteFile):
            mainDict["log"].err(f"Cannot find {suiteFile}")
            raise ValueError

        # Read lines from the suite file and append to a list
        origLines = []
        with open(suiteFile, "r") as sfile:
            origLines = sfile.readlines()

        # Create an empty to list to store new lines and start
        # looping over original lines and handle conditions to
        # remove -cbase and -rbase values
        newLines = []
        continuedLine = ""
        for index, line in enumerate(origLines):

            if index > 0:
                prevLine = origLines[index - 1]
                continuedLine = __continuedLineFromPrevLine(prevLine, continuedLine)

            evalLine = continuedLine + line
            evalLine = evalLine.replace("\n", "").replace("\\", "")

            # Test if the line starts with a comment or is empty
            # and apply logic for Comparison and Composite tests
            if line[0] != "#" and line[0] != "\n":

                if "Comparison" in evalLine:
                    line = __removeBaseline(line, "-cbase", mainDict["cbaseDate"])
                if "Composite" in evalLine:
                    line = __removeBaseline(line, "-cbase", mainDict["cbaseDate"])
                    line = __removeBaseline(line, "-rbase", mainDict["cbaseDate"])

            # Append the updated line to new lines
            if mainDict["stripComments"]:
                if line[0] != "#":
                    newLines.append(line.strip("\n").split("#")[0] + "\n")
            else:
                newLines.append(line)

        # new lines == original line do not rewrite the suite file
        # to preserve time stamp. Display relevant output
        if newLines != origLines:
            with open(suiteFile, "w") as sfile:
                sfile.writelines(newLines)
            mainDict["log"].warn(f"{suiteFile} CHANGED")
        else:
            mainDict["log"].warn(f"{suiteFile} UNCHANGED")


def addBenchmarks(mainDict):
    """
    Remove benchmarks from a list of suite files

    Arguments
    ---------
    mainDict : Dicitionary for the API
    """

    # Check if pathToSuites is defined, if not use
    # all *.suite files from the working directory
    if not mainDict["pathToSuites"]:
        mainDict["pathToSuites"] = glob.glob("*.suite")

    # Loop over suite and start removing benchmarks
    for suiteFile in mainDict["pathToSuites"]:

        # Handle exceptions
        if not suiteFile.endswith(".suite"):
            mainDict["log"].err(f'File {suiteFile} must have a ".suite" suffix')
            raise ValueError

        if not os.path.exists(suiteFile):
            mainDict["log"].err(f"Cannot find {suiteFile}")
            raise ValueError

        with open(suiteFile, "r") as sfile:
            origLines = sfile.readlines()

        newLines = []
        continuedLine = ""

        for index, line in enumerate(origLines):

            if index > 0:
                prevLine = origLines[index - 1]
                continuedLine = __continuedLineFromPrevLine(prevLine, continuedLine)

            evalLine = continuedLine + line
            evalLine = evalLine.replace("\n", "").replace("\\", "")

            if line[0] != "#" and line[0] != "\n":

                lineContd = line.split("#")[0].split("\\")[0] != line.split("#")[0]

                if "Comparison" in evalLine and not lineContd:
                    if mainDict["cbaseAdd"]:
                        if "-cbase" not in evalLine:
                            line = __addBaseline(line, "-cbase", mainDict["cbaseDate"])

                if "Composite" in evalLine and not lineContd:
                    if mainDict["cbaseAdd"]:
                        if "-cbase" not in evalLine:
                            line = __addBaseline(line, "-cbase", mainDict["cbaseDate"])

                    if mainDict["rbaseAdd"]:
                        if "-rbase" not in evalLine:
                            if "-cbase" not in evalLine:
                                raise ValueError(
                                    f"Cannot add rbase without cbase for {evalLine} in {suiteFile}"
                                )
                            else:
                                line = __addBaseline(
                                    line, "-rbase", mainDict["rbaseDate"]
                                )

            newLines.append(line)

        if newLines != origLines:
            with open(suiteFile, "w") as sfile:
                sfile.writelines(newLines)
            mainDict["log"].warn(f"{suiteFile} CHANGED")
        else:
            mainDict["log"].warn(f"{suiteFile} UNCHANGED")


def parseSuite(mainDict):
    """
    Arguments
    ---------
    mainDict : Dicitionary for the API

    Returns
    specList : List of test specifications
    """
    # Set an empty dictionary to populate
    specList = []

    # Check if pathToSuites is defined, if not use
    # all *.suite files from the working directory
    if not mainDict["pathToSuites"]:
        mainDict["pathToSuites"] = glob.glob("*.suite")

    # Loop over all suite files and populate
    # suite dictionary
    for suiteFile in mainDict["pathToSuites"]:

        # Handle exceptions
        if not suiteFile.endswith(".suite"):
            mainDict["log"].err(f'File {suiteFile} must have a ".suite" suffix')
            raise ValueError

        if not os.path.exists(suiteFile):
            mainDict["log"].err(f"Cannot find {suiteFile}")
            raise ValueError

        suiteList = []

        with open(suiteFile, "r") as sfile:
            for line in __continuationLines(sfile):
                suiteList.append(line.split("#")[0])

        suiteList = [spec for spec in suiteList if spec]

        for spec in suiteList:

            testSpec = TestSpec()
            testSpec.setupName = shlex.split(spec)[0]

            testArgs = SuiteParser.parse_args(shlex.split(spec)[1:])
            testSpec.nodeName = testArgs.test

            for currSpec in specList:
                if testSpec.nodeName == currSpec.nodeName:
                    mainDict["log"].err(
                        f"Duplicate for {testSpec.nodeName!r} detected in {sfile.name!r}"
                    )
                    raise ValueError()

            testSpec.numProcs = testArgs.nprocs
            testSpec.environment = testArgs.env
            testSpec.debug = testArgs.debug
            testSpec.cbase = testArgs.cbase
            testSpec.rbase = testArgs.rbase
            testSpec.errTol = testArgs.tolerance
            testSpec.add_setup_opts = testArgs.add_setup_opts

            if testSpec.nodeName.split("/")[0] == "UnitTest" and (
                testSpec.cbase or testSpec.rbase
            ):
                mainDict["log"].err(
                    f"{testSpec.nodeName!r} in {sfile.name!r} cannot have cbase, rbase"
                )
                raise ValueError()

            if testSpec.nodeName.split("/")[0] == "Comparison" and testSpec.rbase:
                mainDict["log"].err(
                    f"{testSpec.nodeName!r} in {sfile.name!r} cannot have rbase"
                )
                raise ValueError()

            if (
                testSpec.nodeName.split("/")[0] == "Composite"
                and testSpec.rbase
                and (not testSpec.cbase)
            ):
                mainDict["log"].err(
                    f"{testSpec.nodeName!r} in {sfile.name!r} cannot set rbase before cbase"
                )
                raise ValueError()

            specList.append(testSpec)

    return specList


def checkSuiteWithInfo(mainDict, infoNode):
    """
    Arguments
    ---------
    mainDict : Dicitionary for the API
    """
    infoNode = infoNode.findChild(f'{mainDict["flashSite"]}')

    # Check if pathToSuites is defined, if not use
    # all *.suite files from the working directory
    if not mainDict["pathToSuites"]:
        mainDict["pathToSuites"] = glob.glob("*.suite")

    mainDict["log"].note('Comparing changes to "test.info" with "*.suite* files:')
    mainDict["log"].brk()

    # Loop over all suite files and populate
    # suite dictionary
    for suiteFile in mainDict["pathToSuites"]:

        # Handle exceptions
        if not suiteFile.endswith(".suite"):
            mainDict["log"].err(f'File {suiteFile!r} must have a ".suite" suffix')
            raise ValueError()

        if not os.path.exists(suiteFile):
            mainDict["log"].err(f"Cannot find {suiteFile!r}")
            raise ValueError()

        with open(suiteFile, "r") as sfile:

            # loop over lines
            for line in __continuationLines(sfile):
                if line.split("#")[0]:
                    spec = shlex.split(line.split("#")[0])
                    testArgs = SuiteParser.parse_args(spec[1:])
                    if testArgs.test.split("/")[0] in ["Composite", "Comparison"]:
                        xmlText = infoNode.findChildrenWithPath(testArgs.test)[0].text
                        for entries in xmlText:
                            if entries.split(":")[0] == "restartBenchmark":
                                rbase = [
                                    value
                                    for value in entries.split(":")[1]
                                    .replace(" ", "")
                                    .split("/")
                                    if value
                                    not in [
                                        "<siteDir>",
                                        "<buildDir>",
                                        "<runDir>",
                                        "<checkpointBasename><restartNumber>",
                                    ]
                                ][0]
                                if (not testArgs.rbase) or (testArgs.rbase != rbase):
                                    mainDict["log"].note(
                                        f'Set "rbase" to "{rbase}" for "{testArgs.test}" in "{sfile.name}"'
                                    )

                            elif entries.split(":")[0] == "comparisonBenchmark":
                                cbase = [
                                    value
                                    for value in entries.split(":")[1]
                                    .replace(" ", "")
                                    .split("/")
                                    if value
                                    not in [
                                        "<siteDir>",
                                        "<buildDir>",
                                        "<runDir>",
                                        "<checkpointBasename><comparisonNumber>",
                                    ]
                                ][0]
                                if (not testArgs.cbase) or (testArgs.cbase != cbase):
                                    mainDict["log"].note(
                                        f'Update "cbase" to "{cbase}" for "{testArgs.test}" in "{sfile.name}"'
                                    )

                            elif entries.split(":")[0] == "shortPathToBenchmark":
                                cbase = [
                                    value
                                    for value in entries.split(":")[1]
                                    .replace(" ", "")
                                    .split("/")
                                    if value
                                    not in [
                                        "<siteDir>",
                                        "<buildDir>",
                                        "<runDir>",
                                        "<chkMax>",
                                    ]
                                ][0]
                                if (not testArgs.cbase) or (testArgs.cbase != cbase):
                                    mainDict["log"].note(
                                        f'Update "cbase" to "{cbase}" for "{testArgs.test}" in "{sfile.name}"'
                                    )
