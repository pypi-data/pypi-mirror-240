import os
from .utils import readJsonFile

def taxinomizeArtProjects(root_dir):
    rv = dict()
    for foldername, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == "config.json":
                config_file_path = os.path.join(foldername, filename)
                data = readJsonFile(config_file_path)
                name = data["project_name"]
                relative_photo_paths = data["photos"]

                imageCount = len(relative_photo_paths)

                photos = [os.path.join(foldername, photo) for photo in relative_photo_paths]

                d = dict()
                d["name"] = name
                d["photos"] = photos

                # Create an empty list for the key only if it doesn't exist
                if imageCount not in rv:
                    rv[imageCount] = list()

                rv[imageCount].append(d)
    return rv
