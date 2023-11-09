import sys

import subprocess

from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler.triggers.cron import CronTrigger

from fastapi import FastAPI, Request

from fastapi.responses import JSONResponse


async def on_startup():
    sys.argv.extend(["--host", app.state["host"], "--port", str(app.state["port"])])

    trigger = CronTrigger(
        year="*", month="*", day="*", hour="17", minute="58", second="1"
    )

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        run_server,
        trigger=trigger,
        name="scheduled",
    )

    scheduler.add_job(
        run_server,
        name="instant",
    )

    scheduler.start()


def run_server():
    args = " ".join(sys.argv[1:])

    subprocess.run(
        f"trader_core {args}",
        shell=True,
        check=True,
    )


app = FastAPI(on_startup=[on_startup])


@app.get("/")
async def home(request: Request):
    return JSONResponse(
        {
            "status": "okay",
        }
    )


@app.post("/api/state")
async def state(request: Request):
    return JSONResponse(
        {
            "status": "okay",
        }
    )
