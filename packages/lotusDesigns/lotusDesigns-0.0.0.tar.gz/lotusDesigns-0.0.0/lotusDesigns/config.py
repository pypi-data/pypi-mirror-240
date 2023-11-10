import os
import yaml
import shutil
from xdg_base_dirs import xdg_config_home


def getPackageName():
    return "lotusDesigns"


def getSkeletonRootDir():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    templateRootDir = os.path.join(script_directory, "skeleton")
    return templateRootDir


def ensure_config():
    """Make sure that the configs are present. Create default ones if not present from the skeleton files."""

    packageName = getPackageName()
    configFileName = "config.yml"
    templateConfigFileName = "template.json"
    imageFileName = "template.jpg"

    # We want to ensure that the configuration directory is present.
    configFileDir = os.path.join(xdg_config_home(), packageName)
    if not os.path.exists(configFileDir):
        os.makedirs(configFileDir, exist_ok=True)

    # We want to ensure that the configuration file is present.
    configFilePath = os.path.join(configFileDir, configFileName)
    if not os.path.exists(configFilePath):

        # Read the contents of the template config file
        configFilePath_skeleton = os.path.join(getSkeletonRootDir(), configFileName)
        contents = ""
        with open(configFilePath_skeleton, 'r') as file:
            contents = file.read()

        # Write the contents to the config file
        with open(configFilePath, 'w') as file:
            file.write(contents)

    # We want to ensure that the template configuration file is present.
    templateConfigFilePath = os.path.join(configFileDir, templateConfigFileName)
    if not os.path.exists(templateConfigFilePath):

        # Read the contents of the template config file
        templateConfigFilePath_skeleton = os.path.join(getSkeletonRootDir(), templateConfigFileName)
        contents = ""
        with open(templateConfigFilePath_skeleton, 'r') as file:
            contents = file.read()

        # Write the contents to the config file
        with open(templateConfigFilePath, 'w') as file:
            file.write(contents)

    # This photo is used by the default template configuration
    imageFilePath = os.path.join(configFileDir, imageFileName)
    if not shutil.os.path.exists(imageFilePath):
        # Copy the file if the destination file does not exist
        imageFilePath_skeleton = os.path.join(getSkeletonRootDir(), imageFileName)
        shutil.copy2(imageFilePath_skeleton, imageFilePath)


def getConfig(key):
    packageName = getPackageName()
    configFileName = "config.yml"
    configFileDir = os.path.join(xdg_config_home(), packageName)
    configFilePath = os.path.join(configFileDir, configFileName)

    with open(configFilePath, 'r') as file:
        configData = yaml.safe_load(file)

    value = None
    if key in configData:
        value = configData[key]

    if value is None:
        raise Exception(f"The value of '{key}' is '{value}'")

    return value
