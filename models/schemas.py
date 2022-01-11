from typing import Optional
from pydantic import BaseModel
from config import DefaultValues


class DataFlow(BaseModel):
    event: Optional[str] = DefaultValues.event
    character_id: Optional[str] = DefaultValues.character_id
    comment: Optional[str] = DefaultValues.comment