#!/usr/bin/env python3

import os
import sys
import re
import subprocess
from setuptools import setup, find_packages
import importlib.metadata

here = os.path.abspath(os.path.dirname(__file__))

# ------------------------------------------------------------------------------

def list_all_files_recursively(dirpath):
	filepath_list = list()
	for parent_path, _, filenames in os.walk(dirpath):
		for filename in filenames:
			filepath = os.path.join(parent_path, filename)
			filepath_list.append(filepath)

	return filepath_list


# ------------------------------------------------------------------------------

# Package name
packageName = "lotusDesigns"

# Load information needed by setup
init_file_path = os.path.join(here, f"{packageName}/__init__.py")
spec = importlib.util.spec_from_file_location(packageName, init_file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

#version = module.__version__
#author = module.__author__
#email = module.__email__
#mylicense = module.__license__

# Long description
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

# Requirements
with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
        dependencies = [line.strip() for line in f if "==" in line]

# ------------------------------------------------------------------------------
# Setup config
setup(
	name=packageName,
	packages=find_packages(),
	version=module.__version__,
	license=module.__license__,
	description='Utility for the lotusDesignPrints shop',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author=module.__author__,
	author_email=module.__email__,
	url=f"https://git.kentavros.lan/leniko/{packageName}",
	keywords=['image', 'lotusDesigns', 'util'],
	install_requires=dependencies,
	package_data={'lotusDesigns': ["../" + filepath for filepath in list_all_files_recursively('lotusDesigns/skeleton')]},
	include_package_data=True,
	data_files=[("", ["requirements.txt"])],
	entry_points={
		"console_scripts": [
			"lotus = lotusDesigns.app:app",
		]
	},
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.10',
	],
)
