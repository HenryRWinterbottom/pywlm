"""

"""

# ----

from wrkldmngr.wrkldmngr import WorkloadManager
from typing import Dict, Tuple
from tools import system_interface

# ----

# Define all available module properties.
__all__ = ["SLURM"]

# ----


class SLURM(WorkloadManager):
    """

    """

    def __init__(self: WorkloadManager, bash: bool = True, *args: Tuple, **kwargs: Dict):
        """
        Description
        -----------

        Creates a new SLURM object.

        """

        # Define the base-class attributes.
        super().__init__(wrkldmngr="slurm", bash=bash, *args, **kwargs)

    def run(self: WorkloadManager) -> None:
        """

        """

        self.write()
        self.submit()
