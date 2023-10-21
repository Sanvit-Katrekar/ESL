from pydantic import BaseModel
from typing import Optional,List

class Images(BaseModel):
    image_list:List[str]