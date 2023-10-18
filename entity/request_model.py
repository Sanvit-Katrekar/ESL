from pydantic import BaseModel
from typing import Optional

class VideoCreateRequest(BaseModel):
    english_sentence: str
    video_name: Optional[str] = None