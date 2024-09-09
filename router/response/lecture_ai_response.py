from pydantic import BaseModel


class LectureAllResponse(BaseModel):
    id: int
    title: str
    instructor: str
    price: int
    image_url: str
    lecture_url: str
    goals: list[str]
    target: list[str]
    section_names: list[str]
    sub_sections: list[str]

    class Config:
        from_attributes = True
