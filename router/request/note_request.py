from pydantic import BaseModel


class NotePydantic(BaseModel):
    content: str
