from fastapi import APIRouter, Depends, HTTPException
from repository.LectureRepository import LectureRepository
from sqlalchemy.orm import Session
from config.database.db_config import get_db
from service.LectureService import LectureService

router = APIRouter()


@router.get("/recommend")
def get_lecture_recommend(db: Session = Depends(get_db)):
    lecture_service = LectureService(db)
    return lecture_service.recommend_lecture()


@router.get("/{lecture_id}")
def get_lecture(lecture_id: int, db: Session = Depends(get_db)):
    lecture_repository = LectureRepository(db)
    lecture = lecture_repository.get_lecture(lecture_id)
    sections = lecture.sections
    return sections
