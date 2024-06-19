"""

"""

# ----

from pywlm.pywlm import WorkloadManager
from typing import Dict, Tuple
from tools import system_interface

from pyslurmutils import submit_job

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

    def submit(self: WorkloadManager, job_script_path: str) -> None:
        """

        """

        job_id = submit_job(job_script_path)

        return job_id
