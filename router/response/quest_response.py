
from pydantic import BaseModel


class CreateQuestResponse(BaseModel):
    quest_id: int
    content: str

    class Config:
        from_attributes = True
