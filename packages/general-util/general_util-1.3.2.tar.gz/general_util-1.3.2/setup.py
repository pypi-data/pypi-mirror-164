from setuptools import setup, find_packages

VERSION = '1.3.2'
DESCRIPTION = 'General utilities for python scripts.'

# Read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Add resource links
project_urls = {
  'Documentation': 'https://johnhal.gitlab.io/util_python',
  'Repository': 'https://github.com/johnhalz/general_util'
}

# Setting up
setup(
    name="general_util",
    version=VERSION,
    author="John Halazonetis",
    author_email="<john.halazonetis@icloud.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['pathlib', 'bokeh', 'datetime'],
    keywords=['python', 'utilities'],
    project_urls = project_urls,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
