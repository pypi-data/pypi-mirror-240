from pydantic import BaseModel


class UpdateStateRequest(BaseModel):
    remote_url: str
    remote_token: str
