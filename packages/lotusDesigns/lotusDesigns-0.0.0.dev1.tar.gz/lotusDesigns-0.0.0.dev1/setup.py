#!/usr/bin/env python3

import os
import sys
import re
import subprocess
from setuptools import setup
import importlib.metadata

here = os.path.abspath(os.path.dirname(__file__))


# ------------------------------------------------------------------------------


#__version__ = importlib.metadata.version('lotusDesigns')
#print(f"Version:  {__version__}")
#sys.exit(1)

def get_version():
	def is_canonical(version):
		return re.match(r'^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$', version) is not None

	version = importlib.metadata.version('lotusDesigns')

	if not is_canonical(version):
		raise Exception(f"Invalid version: {version}")

	return version



def get_version2():
	version = None
	try:
		# Run 'git describe' to get the tag from the current commit
		result = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], capture_output=True, text=True, check=True)

		# Extract the version from the tag
		version_from_tag = result.stdout.strip()

		# Run 'git rev-list' to count the number of commits since the last tag
		result_commits = subprocess.run(['git', 'rev-list', '--count', f'{version_from_tag}..HEAD'], capture_output=True, text=True, check=True)

		# Extract the number of commits
		num_commits = int(result_commits.stdout.strip())

		# If there are no commits since the last tag, return the tag as the version
		if num_commits == 0:
			return version_from_tag

		# If there are commits, append the number of commits as the local version
		version = f'{version_from_tag}.dev{num_commits}'
	except subprocess.CalledProcessError as e:
		print(f"Error: {e}")

	if version is not None:
		version = version.lstrip('v')

	#if version is None or not is_canonical(version):
	#	raise Exception(f"Invalid version: {version}")

	return version


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
about = {}
with open(os.path.join(here, f"{packageName}/__init__.py"), 'r', encoding='utf-8') as f:
	exec(f.read(), about)

# Long description
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

# Requirements
with open("requirements.txt") as f:
	dependencies = [line for line in f if "==" in line]
	dependencies = [s.rstrip() for s in dependencies]

# dependencies.append('builtins')

# print(dependencies)
# sys.exit(1)

# ------------------------------------------------------------------------------
# Setup config
setup(
	use_scm_version=True,
	setup_requires=['setuptools_scm'],

	name=packageName,
	packages=[packageName],
	version=get_version(),
	# license=about['__license__'],
	description='Utility for the lotusDesignPrints shop',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author=about['__author__'],
	author_email=about['__email__'],
	# url=f"https://github.com/TediCreations/{packageName}",
	# download_url=f"https://github.com/TediCreations/{packageName}/archive/" + about['__version__'] + '.tar.gz',
	keywords=['build', 'make', 'util'],
	install_requires=dependencies,
	package_data={'lotusDesigns': ["../" + filepath for filepath in list_all_files_recursively('static/')]},
	include_package_data=True,
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

#		'License :: OSI Approved :: MIT License',
