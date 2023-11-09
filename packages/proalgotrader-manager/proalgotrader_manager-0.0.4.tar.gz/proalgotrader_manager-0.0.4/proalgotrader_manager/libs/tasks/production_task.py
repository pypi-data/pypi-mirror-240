import subprocess


def production_task(args):
    subprocess.run(
        f"trader_core {args}",
        shell=True,
        check=True,
    )
