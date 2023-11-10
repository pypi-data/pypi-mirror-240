import os
import sys
from .photo import Photo
from .args import parseArgs
from .config import ensure_config
from .config import getConfig
from .utils import get_version
from .utils import expand_path
from .utils import readJsonFile
from .utils import pretty_print_json
from .bl import taxinomizeArtProjects


def do_work(isVerbose, templateImage, out_directory_path, setOfArt, templateConfig):
    name = setOfArt["name"]
    photos = setOfArt["photos"]

    placeholders = templateConfig["placeholders"]
    templateName = templateConfig["name"]

    if isVerbose:
        print(f"Generating project '{name}' with template '{templateName}'." )

    for photo, placeholder in zip(photos, placeholders):
        x = int(placeholder["x"])
        y = int(placeholder["y"])
        dx = int(placeholder["Dx"])
        dy = int(placeholder["Dy"])

        width = dx-x
        height = dy-y
        if width <= 0 or height <=0:
            raise Exception(f"Width and/or heigth is zero or negative")

        overlayImagePath = photo
        overlayImage = Photo(overlayImagePath)
        overlayImage.scale(width, height)
        templateImage.addOverlay(overlayImage, x, y)

    directory_path = os.path.join(out_directory_path, name )
    outImagePath = os.path.join(directory_path, f"{templateName}.png")
    os.makedirs(directory_path, exist_ok=True)
    templateImage.save(outImagePath)
    print(f"Saved '{outImagePath}'")


def app():
    try:
        args = parseArgs()

        if args.version:
            version = get_version()
            print(version)
            sys.exit(0)

        ensure_config()

        # Template path
        templateFilePath=expand_path(getConfig("templateFilePath"))
        if args.template is not None:
            arg_templateFilePath= expand_path(args.template)
            if not os.path.isfile(arg_templateFilePath):
                raise Exception(f"No template file named '{arg_templateFilePath}'.")
            else:
                templateFilePath = arg_templateFilePath

        # Out dir path
        outDirPath=expand_path(getConfig("out_directory_path"))
        if args.outDir is not None:
            outDirPath = expand_path(args.outDir)

        # Art dir path
        art_directory_path=expand_path(args.art_path)

        # --------------
        configData = readJsonFile(templateFilePath)
        artData = taxinomizeArtProjects(art_directory_path)

        if args.verbose:
            pretty_print_json(artData)

        for config in configData:
            templateImagePath = config["template"]
            templateName = config["name"]
            templateImage = Photo(templateImagePath)
            placeholders = config["placeholders"]
            numberOfPlaceholders = len(placeholders)

            for setOfArt in artData.get(numberOfPlaceholders, []):
                do_work(args.verbose, templateImage, outDirPath, setOfArt, config)

    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
        sys.exit(1)

if __name__ == "__main__":
    App()
