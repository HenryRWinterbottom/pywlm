"""

"""

# ----

from pywlm.wlm import WorkloadManager
from typing import Dict, Tuple
from tools import system_interface

# ----

# Define all available module properties.
__all__ = ["SLURM"]

# ----


class SLURM(WorkloadManager):
    """

    """

    def __init__(self: WorkloadManager, shell: str = "bash", *args: Tuple, **kwargs: Dict):
        """
        Description
        -----------

        Creates a new SLURM object.

        """

        # Define the base-class attributes.
        super().__init__(wrkldmngr="slurm", shell=shell, *args, **kwargs)
