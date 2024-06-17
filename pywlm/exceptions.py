"""

"""

# ----

from utils.error_interface import Error

# ----

# Define all available module properties
__all__ = [
    "WorkflowManagerError"
]

# ----


class WorkloadManagerError(Error):
    """
    Description
    -----------

    This is the base-class for exceptions encountered while execution
    applications within the WorkloadManager base-class; it is a
    sub-class of Error.

    """
