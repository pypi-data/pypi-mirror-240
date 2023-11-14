"""FlashXTest library to interface with backend.FlashTest"""

import os, subprocess

from .. import backend
from .. import lib


def getMainDict(apiDict):
    """
    Arguments
    --------
    apiDict  : Dictionary to override values from Config file

    Returns
    -------
    mainDict: Dictionary for keys in the config file
    """
    # Build Config file for mainDict.
    # Read the user Config file (configApi), append it to Base Config from backend (configBase),
    # and create a new Config (configMain) in 'testDir/.fxt' folder
    configApi = apiDict["pathToConfig"]
    configMain = configApi

    # Parse the configMain file
    mainDict = backend.flashTestParser.parseFile(configMain)

    # Update mainDict with values from apiDict
    mainDict.update(apiDict)

    return mainDict


def setExe(apiDict):
    """
    Arguments
    ---------
    apiDict : API dictionary
    """
    exeBase = os.path.dirname(backend.__file__) + "/FlashTest/exeScript"
    exeFile = apiDict["pathToExeScript"]

    with open(exeBase, "r") as ebase, open(exeFile, "w") as efile:
        lines = ebase.readlines()
        for line in lines:
            line = line.replace("mpiexec", apiDict["pathToMPI"])
            efile.write(line)

    apiDict["log"].note(f'Wrote "execfile" to {exeFile}')


def setConfig(apiDict):
    """
    Setup configuration

    Arguments
    ---------
    apiDict    : API dictionary
    """
    # Get path to configuration template from FlashTest backend
    configTemplate = os.path.dirname(backend.__file__) + "/FlashTest/configTemplate"

    # Get path to configuration base from FlashTest backend
    configBase = os.path.dirname(backend.__file__) + "/FlashTest/configBase"

    # Get path to user configuration file from apiDict
    configFile = apiDict["pathToConfig"]

    # Start building configFile from configTemplate
    #
    # configTemplate in read mode as ctemplate
    # configFile in write mode as cfile
    #
    with open(configTemplate, "r") as ctemplate, open(configFile, "w") as cfile:

        # Read lines from ctemplate
        lines = ctemplate.readlines()

        # Iterate over lines and set values defined in apiDict
        for line in lines:

            # Set default baseLineDir
            line = line.replace(
                "pathToMainArchive:",
                str("pathToMainArchive:  " + apiDict["pathToMainArchive"]),
            )

            # Set path to Archive
            line = line.replace(
                "pathToLocalArchive:",
                str("pathToLocalArchive: " + apiDict["pathToLocalArchive"]),
            )

            # Set default pathToOutdir
            line = line.replace(
                "pathToOutdir:",
                str("pathToOutdir:       " + apiDict["pathToOutdir"]),
            )

            # Set 'pathToFlash' if defined in apiDict
            line = line.replace(
                "pathToFlash:",
                str("pathToFlash:        " + str(apiDict["pathToFlash"])),
            )

            # Set 'pathToViewArchive' if defined in apiDict
            line = line.replace(
                "pathToViewArchive:",
                str("pathToViewArchive:  " + str(apiDict["pathToViewArchive"])),
            )

            # Set default pathToGmake
            line = line.replace(
                "pathToGmake:",
                str("pathToGmake:        " + apiDict["pathToGmake"]),
            )

            # Set 'flashSite' if define in apiDict
            if "flashSite" in apiDict:
                line = line.replace(
                    "flashSite:",
                    str("flashSite:          " + str(apiDict["flashSite"])),
                )

            cfile.write(line)

    # Append additional options from configBase
    #
    with open(configBase, "r") as cbase, open(configFile, "a") as cfile:
        cfile.write("\n")
        cfile.write("# Following options are default values that should\n")
        cfile.write("# not be changed for most cases \n")

        lines = cbase.readlines()

        for line in lines:
            cfile.write(line)

    apiDict["log"].note(f'Wrote "config" to {configFile}')
