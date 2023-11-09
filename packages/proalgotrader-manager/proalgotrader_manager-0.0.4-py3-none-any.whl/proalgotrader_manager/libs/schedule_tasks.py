from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from proalgotrader_manager.libs.tasks.local_task import local_task
from proalgotrader_manager.libs.tasks.production_task import production_task


def schedule_tasks(app):
    host = app.state["host"]
    port = app.state["port"]
    key = app.state["key"]
    secret = app.state["secret"]
    environment = app.state["environment"]

    args = f"--host {host} --port {port} --key {key} --secret {secret} --environment {environment}"

    task = (
        lambda: local_task(args)
        if environment == "local"
        else lambda: production_task(args)
    )

    trigger = CronTrigger(
        year="*", month="*", day="*", hour="17", minute="58", second="1"
    )

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        task,
        trigger=trigger,
        name="scheduled",
    )

    scheduler.add_job(
        task,
        name="instant",
    )

    scheduler.start()
