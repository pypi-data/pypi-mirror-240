import os
import argparse


def parseArgs():
    # Create a parser
    parser = argparse.ArgumentParser(description="Lotus Design prints utility")

    # Define optional arguments
    parser.add_argument('--version', action='store_true', help="Get version.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose mode.")
    parser.add_argument('-t', '--template', metavar='templateFilePath', default=None, help="Specify a custom template json file.")
    parser.add_argument('-o', '--outDir', metavar='dir', default=None, help="Specify a custom output directory.")

    # Define a positional argument for the path
    current_directory = os.getcwd()
    parser.add_argument('art_path', nargs='?', default=current_directory, help="The path that contains art.")

    # Parse the command-line arguments
    args = parser.parse_args()

    return args
