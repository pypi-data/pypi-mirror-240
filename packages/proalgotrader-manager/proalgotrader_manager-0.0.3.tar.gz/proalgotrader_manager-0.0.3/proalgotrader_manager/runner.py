import uvicorn

from proalgotrader_manager.libs.args_manager import args_manager


def run():
    uvicorn.run(
        f"proalgotrader_manager.main:app",
        host=args_manager.host,
        port=args_manager.port,
        reload=args_manager.environment == "local",
    )
