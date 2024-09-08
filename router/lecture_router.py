from fastapi import APIRouter, Depends, HTTPException
from repository.LectureRepository import LectureRepository
from sqlalchemy.orm import Session
from config.database.db_config import get_db

router = APIRouter()


@router.get("/{lecture_id}")
def get_lecture(lecture_id: int, db: Session = Depends(get_db)):
    lecture_repository = LectureRepository(db)
    lecture = lecture_repository.get_lecture(lecture_id)
    sections = lecture.sections
    for section in sections:
        print(section)
