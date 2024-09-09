from pydantic import BaseModel


class QuestAnswerRequest(BaseModel):
    content: str
    answer: str
