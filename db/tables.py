from typing import Optional
from sqlmodel import SQLModel, Field

class ESL(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    en_word: str
    video_link: str