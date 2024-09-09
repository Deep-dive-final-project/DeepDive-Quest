from fastapi import APIRouter, Depends, HTTPException
from repository.lecture_repository import LectureRepository
from sqlalchemy.orm import Session
from config.database.dbconfig import get_db
from service.lecture_service import LectureService

router = APIRouter()


@router.get("/recommend/study-plan")
def get_lecture_recommend(plan_id: int, db: Session = Depends(get_db)):
    lecture_service = LectureService(db)
    return lecture_service.recommend_lecture(plan_id)


@router.get("/recommend")
def get_lecture_recommend(db: Session = Depends(get_db)):
    lecture_service = LectureService(db)
    return lecture_service.recommend_latest_lecture()


@router.get("/{lecture_id}")
def get_lecture(lecture_id: int, db: Session = Depends(get_db)):
    lecture_repository = LectureRepository(db)
    lecture = lecture_repository.get_lecture(lecture_id)
    sections = lecture.sections
    return sections
