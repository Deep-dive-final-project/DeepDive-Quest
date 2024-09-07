from pydantic import BaseModel


class LectureAllResponse(BaseModel):
    title: str
    instructor: str
    goals: list[str]
    target: list[str]
    section_names: list[str]
    sub_sections: list[str]

    class Config:
        from_attributes = True
