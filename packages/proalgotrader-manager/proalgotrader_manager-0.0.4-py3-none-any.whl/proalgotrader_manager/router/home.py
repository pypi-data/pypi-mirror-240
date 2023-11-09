from fastapi.responses import JSONResponse

from proalgotrader_manager.libs.router import router


@router.get("/")
async def home():
    return JSONResponse(
        {
            "status": "okay",
        }
    )
