from fastapi import FastAPI

from proalgotrader_manager.libs.args_manager import args_manager

from proalgotrader_manager.libs.schedule_tasks import schedule_tasks

from proalgotrader_manager.router import home, algo_session


def on_startup():
    schedule_tasks(app)


app = FastAPI(on_startup=[on_startup])

app.state = args_manager.state

app.include_router(home.router)

app.include_router(algo_session.router)
