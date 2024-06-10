"""


"""

# ----

import os
from abc import ABC, abstractmethod
from utils.logger_interface import Logger
from typing import Dict, Tuple, Generic
from confs.yaml_interface import YAML
from tools import parser_interface

# ----

# Define all available module properties.
__all__ = ["WorkfloadManager"]

# ----


class WorkloadManager:
    """

    """

    def __init__(self: Generic, wrkldmngr: str, bash: bool = True, *args: Tuple, **kwargs: Dict):
        """
        Description
        -----------

        Creates a new WorkflowManager object.

        """

        # Define the base-class attributes.
        self.logger = Logger(
            caller_name=f"{__name__}.{self.__class__.__name__}")
        self.wrkldmngr_obj = self.config()
        if bash:
            self.header = "!/usr/bin/env bash"

    def config(self: Generic) -> SimpleNamespace:
        """

        """

        schema_file = os.path.join(parser_interface.enviro_get(envvar="WRKLDMNGR_ROOT"),
                                   "wrkldmngr", "schema", "wrkldmngr.yaml")
        wrkldmngr_obj = parser_interface.object_getattr(
            object_in=YAML().read_yaml(yaml_file=schema_file, return_obj=True),
            key=wrkldmngr, force=True)

        return wrkldmngr_obj

    def submit(self: Generic) -> None:
        """

        """

    def write(self: Generic) -> None:
        """

        """
