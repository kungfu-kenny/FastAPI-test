from typing import Optional
from pydantic import BaseModel


class DataFlow(BaseModel):
    event:str
    character_id:str
    comment: Optional[str] = None