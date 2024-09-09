from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database.dbconfig import get_db
from service.ai_service import AiService
from router.request.note_request import NotePydantic

router = APIRouter()


@router.post("/summary")
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
