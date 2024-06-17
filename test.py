from pywlm.slurm import SLURM
import asyncio

slurm = SLURM(bash=True)


wlm_dict = {"name": "wlm_test.py", "account": "gsienkf", "time": "01:00:00"
            }
asyncio.run(slurm.run(wlm_dict=wlm_dict, output_file="test_slurm.out", annotate=True))
