import os
import subprocess


def local_task(args):
    proalgotrader_core_directory = "/mnt/WorkSpace/Code/proalgotrader_core"
    venv_path = f"{proalgotrader_core_directory}/.venv/bin/python"

    if os.path.exists(proalgotrader_core_directory):
        os.chdir(proalgotrader_core_directory)

        subprocess.run(
            f"{venv_path} main.py {args}",
            shell=True,
            check=True,
        )
    else:
        print("The specified directory does not exist.")
