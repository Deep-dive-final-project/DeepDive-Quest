from pydantic import BaseModel


class LectureListResponse(BaseModel):
    title: str
    instructor: str
    price: int
    lecture_url: str
    image_url: str

    class Config:
        from_attributes = True
