# `general_util` - General Python Utility Repository

This repository is meant to contain general tools and utilities that are reliable and can be used in many software projects.

## Installing Package

### PyPI
You can install this package with the following command:
``` bash
pip install general-util
```

> You can also use all of the corresponding commands for other package managers that support PyPI.

### Installing for Development
For development, it is recommended to clone this repo and install the requirements:
``` bash
git clone https://github.com/johnhalz/general_util.git
pip install -r requirements.txt --user --upgrade
```

## Current Utilities:
- `repeated_timer.py`: Perform iterations at a specified frequency with accurate timing in a separate thread (this timer will not be affected by any other processes you have running)
- `file.py`: Perform operations in the filesystem (regardless of the OS)
- `timestring.py`: Return current or predefined time in a string format (used for file logging and file naming)
- `plotting.py`: Ability to easily create Bokeh plots (with preffered tools and options) in one line of code.
- `argument_handling.py`: Boilerplate code with useful functions to filter erroneous input argument.

## Todos:

- [ ] Finish documentation
