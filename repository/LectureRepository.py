from typing import Type

from sqlalchemy import func
from sqlalchemy.orm import Session
from repository.models import Lecture
from router.response.LectureAllResponse import LectureAllResponse
from router.response.LectureResponse import LectureResponse


class LectureRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_lecture(self, lecture_id: int) -> Type[Lecture] | None:
        return self.db.query(Lecture).filter(Lecture.lecture_id == lecture_id).first()

    def get_lecture_info(self, lecture_id: int, response_model=LectureResponse):
        lecture = self.get_lecture(lecture_id)
        sections = lecture.sections
        return LectureResponse(
            title=lecture.title,
            instructor=lecture.instructor,
            goals=lecture.goals.split('|') if lecture.goals else [],
            target=lecture.target.split('|') if lecture.target else [],
            section_name=sections[0].name,
            sub_sections=[subsection.name for subsection in sections]
        )

    def get_all_lectures(self):
        lectures = self.db.query(Lecture).all()
        return [LectureAllResponse(
            title=lecture.title,
            instructor=lecture.instructor,
            goals=lecture.goals.split('|') if lecture.goals else [],
            target=lecture.target.split('|') if lecture.target else [],
            section_names=[section.name for section in lecture.sections],
            sub_sections=[section.sub_section if section.sub_section is not None else "" for section in
                          lecture.sections] if lecture.sections else []
        ) for lecture in lectures]

    def count_lectures(self) -> int:
        return self.db.query(func.count(Lecture.lecture_id)).scalar()
