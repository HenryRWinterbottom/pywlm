"""
Module
------

    slurm.py

Description
-----------

    This module contains the Simple Linux Utility for Resource
    Management (SLURM) base-class object.

Classes
-------

    SLURM(shell, *args, **kwargs)

        This is the base-class object for all Simple Linux Utility for
        Resource Management (SLURM) applications; it is a sub-class of
        WorkloadManager.

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

from typing import Dict, Tuple

from pywlm.pywlm import WorkloadManager

# ----

# Define all available module properties.
__all__ = ["SLURM"]

# ----


class SLURM(WorkloadManager):
    """
    Description
    -----------

    This is the base-class object for all Simple Linux Utility for
    Resource Management (SLURM) applications; it is a sub-class of
    WorkloadManager.

    Parameters
    ----------

    shell: ``str``

        A Python string specifying the supported Linux shell.

    Other Parameters
    ----------------

    args: ``Tuple``

        A Python tuple containing additional arguments passed to the
        constructor.

    kwargs: ``Dict``

        A Python dictionary containing additional key and value pairs
        to be passed to the constructor.

    """

    def __init__(self: WorkloadManager, shell: str, *args: Tuple, **kwargs: Dict):
        """
        Description
        -----------

        Creates a new SLURM object.

        """

        # Define the base-class attributes.
        super().__init__(wrkldmngr="slurm", shell=shell, *args, **kwargs)
