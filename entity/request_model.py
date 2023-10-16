from pydantic import BaseModel

class VideoCreateRequest(BaseModel):
    english_sentence: str