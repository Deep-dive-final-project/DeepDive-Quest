from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database.db_config import get_db
from repository.LectureRepository import LectureRepository
from repository.MemberRepository import MemberRepository
from router.request.note_request import NotePydantic
from router.response.MemberResponse import MemberResponse
from service.AiService import AiService

router = APIRouter()


@router.get("/api/member/{member_id}", response_model=MemberResponse)
def get_member(member_id: int, db: Session = Depends(get_db)):
    member_repository = MemberRepository(db)
    member = member_repository.get_member(member_id)
    if member is None:
        raise HTTPException(status_code=500, detail="사용자가 존재하지 않습니다")
    return member


@router.get("/api/lecture/{lecture_id}")
def get_lecture(lecture_id: int, db: Session = Depends(get_db)):
    lecture_repository = LectureRepository(db)
    lecture = lecture_repository.get_lecture(lecture_id)
    sections = lecture.sections
    for section in sections:
        print(section)


@router.post("/api/note/summary")
async def post_summary(note: NotePydantic):
    ai_service = AiService()
    summary = ai_service.summary(note)
    if summary is None:
        return {
            "success": False,
            "data": {},
            "error": 'HTTPException(status_code=500, detail="강의 노트 요약 중 에러가 발생했습니다")'
        }

    return {
        "success": True,
        "data": {
            "summary": summary
        },
        "error": None
    }
