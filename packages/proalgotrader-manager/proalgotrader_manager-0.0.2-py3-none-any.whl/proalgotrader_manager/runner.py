import uvicorn

from proalgotrader_manager.main import app


def run(host="127.0.0.1", port=5555):
    app.state = {"host": host, "port": port}
    uvicorn.run(app, host=host, port=port)
