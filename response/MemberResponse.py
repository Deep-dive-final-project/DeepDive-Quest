from pydantic import BaseModel


class MemberResponse(BaseModel):
    member_id: int
    name: str
    email: str

    class Config:
        from_attributes = True
