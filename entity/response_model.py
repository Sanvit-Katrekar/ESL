from pydantic import BaseModel
from typing import Optional

class ResponseBase(BaseModel):
    status: int = 1
    message: str = "Success"

class Response(ResponseBase):
    video_path: Optional[str] = None