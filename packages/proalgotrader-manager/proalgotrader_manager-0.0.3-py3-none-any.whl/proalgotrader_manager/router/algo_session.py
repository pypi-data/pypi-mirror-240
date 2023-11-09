import requests

from fastapi import Request

from fastapi.responses import JSONResponse

from proalgotrader_manager.libs.router import router

from proalgotrader_manager.payloads.update_state_request import UpdateStateRequest


@router.post("/api/algo-session/{algo_session_key}/state")
async def update_state(
    algo_session_key: str, item: UpdateStateRequest, request: Request
):
    try:
        if algo_session_key != request.app.state["key"]:
            return JSONResponse({"success": False}, status_code=403)

        request.app.state["remote_url"] = item.remote_url
        request.app.state["remote_token"] = item.remote_token

        return JSONResponse({"success": True}, status_code=200)
    except Exception as e:
        print(e)


@router.get("/api/algo-session/{algo_session_key}/overview")
async def overview(algo_session_key: str, request: Request):
    try:
        remote_url = request.app.state["remote_url"]
        remote_token = request.app.state["remote_token"]

        overview_url = f"{remote_url}/api/algo-session/{algo_session_key}/overview"

        response = requests.get(
            overview_url,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {remote_token}",
            },
        )

        return JSONResponse(response.json(), status_code=200)
    except Exception as e:
        print(e)


@router.get("/api/algo-session/{algo_session_key}/trading-days")
async def trading_days(algo_session_key: str, request: Request):
    try:
        remote_url = request.app.state["remote_url"]
        remote_token = request.app.state["remote_token"]

        overview_url = f"{remote_url}/api/algo-session/{algo_session_key}/trading-days"

        response = requests.get(
            overview_url,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {remote_token}",
            },
        )

        return JSONResponse(response.json(), status_code=200)
    except Exception as e:
        print(e)


@router.get("/api/algo-session/{algo_session_key}/base-symbols")
async def trading_days(algo_session_key: str, request: Request):
    try:
        remote_url = request.app.state["remote_url"]
        remote_token = request.app.state["remote_token"]

        overview_url = f"{remote_url}/api/algo-session/{algo_session_key}/base-symbols"

        response = requests.get(
            overview_url,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {remote_token}",
            },
        )

        return JSONResponse(response.json(), status_code=200)
    except Exception as e:
        print(e)
