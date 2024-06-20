[![License](https://img.shields.io/badge/license-LGPL_v2.1-black)](https://github.com/HenryWinterbottom-NOAA/pywlm/LICENSE.md)
![Linux](https://img.shields.io/badge/linux-ubuntu%7Ccentos-lightgrey)
![Python Version](https://img.shields.io/badge/python-3.5|3.6|3.7-blue)
[![Code style: black](https://img.shields.io/badge/Code%20Style-black-purple.svg)](https://github.com/psf/black)
[![Documentation Status](https://readthedocs.org/projects/ufs-workflow/badge/?version=latest)](https://ufs-workflow.readthedocs.io/en/latest/?badge=latest)

# Overview

 This repository contains a workload (e.g., resource) manager
 application.

- **Authors:** [Henry R. Winterbottom](mailto:henry.winterbottom@noaa.gov)
- **Maintainers:** Henry R. Winterbottom
- **Version:** 0.0.1
- **License:** LGPL v2.1
- **Copyright**: Henry R. Winterbottom

# Cloning

This repository utilizes several sub-modules from various sources. To
obtain the entire system, do as follows.

~~~shell
user@host:$ git clone --recursive https://github.com/HenryWinterbottom-NOAA/pywlm
~~~

# Installing Package Dependencies

In order to install the respective Python packages upon which
`pywlm` is dependent, do as follows.

~~~shell
user@host:$ cd /path/to/pywlm
user@host:$ /path/to/pip install update
user@host:$ /path/to/pip install -r /path/to/pywlm/requirements.txt
~~~

For additional information using `pip` and `requirements.txt` type files, see [here](https://pip.pypa.io/en/stable/reference/requirements-file-format/).

# Forking

If a user wishes to contribute modifications done within their
respective fork(s) to the authoritative repository, we request that
the user first submit an issue and that the fork naming conventions
follow those listed below.

- `docs/user_fork_name`: Documentation additions and/or corrections
  for the workload manager applications.

- `feature/user_fork_name`: Additions, enhancements, and/or upgrades
  for the workload manager applications.

- `fix/user_fork_name`: Bug-type fixes for the workload manager
  applications that do not require immediate attention.

- `hotfix/user_fork_name`: Bug-type fixes which require immediate
  attention to fix issues that compromise the integrity of the
  respective workload manager applications.
