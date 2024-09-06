from pydantic import BaseModel
from typing import Optional


class MemberResponse(BaseModel):
    member_id: int
    name: str
    email: str

    class Config:
        orm_mode = True  # SQLAlchemy ORM 모델과 호환되도록 설정
