from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database.db_config import get_db
from router.request.QuestAnswerRequest import QuestAnswerRequest
from service.QuestService import QuestService

router = APIRouter()


@router.post("/{quest_id}")
def get_member(quest_id: int, request: QuestAnswerRequest, db: Session = Depends(get_db)):
    try:
        question = request.content
        answer = request.content
        quest_service = QuestService(db)
        response = quest_service.get_feedback(quest_id, question, answer)
        print(response)
        return {
            "success": True,
            "data": {
                "contents": response
            },
            "error": None
        }
    except:
        return {
            "success": False,
            "data": None,
            "error": "Failed to get feedback"
        }
