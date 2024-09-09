from pydantic import BaseModel


class LectureResponse(BaseModel):
    title: str
    instructor: str
    goals: list[str]
    target: list[str]
    section_name: str
    sub_sections: list[str]

    class Config:
        from_attributes = True
