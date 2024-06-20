"""
Module
------

    pywlm.py

Description
-----------

    This module contains the base-class object for all workload
    manager sub-class applications.

Classes
-------

    WorkloadManager(wrkldmngr, shell, *args, **kwargs)

        This is the base-class object for all WorkloadManager
        sub-classes.


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

# pylint: disable=unused-argument

# ----

import os
from types import SimpleNamespace
from typing import Dict, Generic, Tuple

from confs.jinja2_interface import write_from_template
from confs.yaml_interface import YAML
from execute.executable_interface import app_exec
from tools import parser_interface
from tools.system_interface import get_app_path
from utils.decorator_interface import privatemethod
from utils.logger_interface import Logger

from exceptions import WorkloadManagerError

# ----

# Define all available module properties.
__all__ = ["WorkloadManager"]

# ----

WRKLDMNGR_LIST = ["slurm"]

# ----


class WorkloadManager:
    """
    Description
    -----------

    This is the base-class object for all WorkloadManager sub-classes.

    Parameters
    ----------

    wrkldmngr: ``str``

        A Python string specifying the supported workload manager.

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

    def __init__(
        self: Generic, wrkldmngr: str, shell: str, *args: Tuple, **kwargs: Dict
    ):
        """
        Description
        -----------

        Creates a new WorkflowManager object.

        """

        # Define the base-class attributes.
        self.logger = Logger(caller_name=f"{__name__}.{self.__class__.__name__}")
        if wrkldmngr.lower() not in WRKLDMNGR_LIST:
            msg = (
                f"The specified workload manager {wrkldmngr} is not "
                "supported. Aborting!!!"
            )
            raise WorkloadManagerError(msg=msg)
        self.wrkldmngr = wrkldmngr
        self.schema_file = os.path.join(
            parser_interface.enviro_get(envvar="WRKLDMNGR_ROOT"),
            "schema",
            "wrkldmngr.yaml",
        )
        self.wrkldmngr_dict = self.config()
        self.shell_obj = self.shell_info(shell=shell)
        self.wrkldmngr_dict = parser_interface.dict_merge(
            dict1=self.wrkldmngr_dict,
            dict2=parser_interface.object_todict(object_in=self.shell_obj),
        )
        self.wrkldmngr_dict = dict(
            parser_interface.dict_merge(dict1=dict(self.wrkldmngr_dict), dict2=kwargs)
        )

    @privatemethod
    def config(self: Generic) -> Dict:
        """
        Description
        -----------

        This method collects the attributes for the respective workload manager.

        Returns
        -------

        wrkldmngr_dict: ``Dict``

            A Python dictionary containg the respective, supported,
            workload manager attributes.

        Raises
        ------

        WorkloadManager

            - raised if the specified workload manager is not
              supported within the respective schema file.

        """

        # Collect the respective workload manager attributes.
        wrkldmngr_dict = parser_interface.object_getattr(
            object_in=YAML().read_yaml(yaml_file=self.schema_file, return_obj=True),
            key=self.wrkldmngr,
            force=True,
        )
        if wrkldmngr_dict is None:
            msg = (
                f"The attributes for workload manager {self.wrkldmngr} could not "
                f"be determined from the schema file path {self.schema_file}. Aborting!!!"
            )
            raise WorkloadManagerError(msg=msg)

        return wrkldmngr_dict

    @privatemethod
    def shell_info(self: Generic, shell: str) -> SimpleNamespace:
        """
        Description
        -----------

        This method returns the attributes for the workload manager
        application shell.

        Parameters
        ----------

        shell: ``str``

            A Python string specifying the supported Linux shell.

        Returns
        -------

        shell_obj: ``SimpleNamespace``

            A Python SimpleNamespace object containing the supported
            Linux shell attributes.

        Raises
        ------

        WorkloadManager:

            - raised if the path for the respective Linux shell cannot
              be determined for the respective platform.

        """

        # Collect the execution shell attributes.
        shell_obj = parser_interface.object_define()
        shell_obj.shell = shell
        shell_obj.path = get_app_path(app=shell_obj.shell)
        if shell_obj.path is None:
            msg = (
                f"The shell {shell} is not supported and/or could not be "
                "determined for the respective platform. Aborting!!!"
            )
            raise WorkloadManagerError(msg=msg)
        shell_obj.header = f"#!{shell_obj.path}"

        return shell_obj

    @app_exec
    async def submit(self: Generic, output_file: str) -> None:
        """
        Description
        -----------

        This method submits the respective workload manager script accordingly.

        Parameters
        ----------

        output_file: ``str``

            A Python string specifying the path to the respective
            workload manager script.

        Raises
        ------

        WorkloadManagerError:

            - raised if `launcher` attribute is not specified workload
              manager schema file.

            - raised if the respective/specified launcher executable
              can not be determined and/or located.

        """

        # Launch the workload manager script accordingly.
        launcher = parser_interface.dict_key_value(
            dict_in=self.wrkldmngr_dict, key="launcher", force=True, no_split=True
        )
        if launcher is None:
            msg = (
                "The launcher attribute could not be determined from "
                f"{self.schema_file}. Aborting!!!"
            )
            raise WorkloadManagerError(msg=msg)
        app_path = get_app_path(app=launcher)
        if app_path is None:
            msg = (
                f"The executable file {launcher} could not be determined "
                "and/or located. Aborting!!!"
            )
            raise WorkloadManagerError(msg=msg)
        exec_obj = parser_interface.object_define()
        exec_obj.exec_path = f"{app_path} {output_file}"
        exec_obj.run_path = os.path.dirname(output_file)
        if len(exec_obj.run_path) == 0:
            exec_obj.run_path = os.getcwd()
        exec_obj.scheduler = self.wrkldmngr

        return exec_obj

    @privatemethod
    async def write(self: Generic, wlm_dict: Dict, output_file: str) -> None:
        """
        Description
        -----------

        This method writes the workload manager job script.

        Parameters
        ----------

        wlm_dict: ``Dict``

            A Python dictionary containing the workload manager
            attributes.

        output_file: ``str``

            A Python string specifying the path to the workflow
            manager job script.

        Raises
        ------

        WorkloadManagerError:

            - raised if an exception is encountered while
              building/writing the workload manager job script.

        """

        # Write the workload manager script.
        try:
            wlm_dict["header"] = self.shell_obj.header
            wlm_dict = parser_interface.dict_key_case(
                dict_in=wlm_dict, lowercase=True, uppercase=True
            )
            tmpl_path = parser_interface.dict_key_value(
                dict_in=self.wrkldmngr_dict, key="template", force=True, no_split=True
            )
            write_from_template(
                tmpl_path=tmpl_path,
                output_file=output_file,
                in_dict=wlm_dict,
                skip_missing=True,
            )
        except Exception as errmsg:
            msg = (
                f"Writing workload manager job script {output_file} failed "
                f"with error {errmsg}. Aborting!!!"
            )
            raise WorkloadManagerError(msg=msg) from errmsg

    async def run(
        self: Generic, wlm_dict: Dict, output_file: str, annotate: str
    ) -> None:
        """
        Description
        -----------

        This method performs the following tasks:

        (1) Builds the submission script for the respective workload
            manager.

        (2) Submits the respective submission script for the
            respective workload manager.

        """

        # Build and submit the workload manager script.
        await self.write(wlm_dict=wlm_dict, output_file=output_file)
        await self.submit(output_file=output_file)
