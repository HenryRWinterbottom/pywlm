"""
Module
------

    exceptions.py

Description
-----------

    This module loads the exceptions package.

Classes
-------

    WorkloadManagerError(msg)

        This is the base-class for exceptions encountered while
        execution applications within the WorkloadManager base-class;
        it is a sub-class of Error.

Requirements
------------

- ufs_pytils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 18 June 2024

History
-------

    2024-06-18: Henry Winterbottom -- Initial implementation.

"""

# ----

from utils.error_interface import Error

# ----

# Define all available module properties
__all__ = ["WorkloadManagerError"]

# ----


class WorkloadManagerError(Error):
    """
    Description
    -----------

    This is the base-class for exceptions encountered while execution
    applications within the WorkloadManager base-class; it is a
    sub-class of Error.

    """
