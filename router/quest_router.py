import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database.dbconfig import get_db
from router.request.quest_answer_request import QuestAnswerRequest
from service.quest_service import QuestService

router = APIRouter()


@router.post("/{quest_id}")
def get_member(quest_id: int, request: QuestAnswerRequest, db: Session = Depends(get_db)):
    try:
        question = request.content
        answer = request.answer
        quest_service = QuestService(db)
        response = quest_service.get_feedback(quest_id, question, answer)
        logging.info(f'[quest_router] Response: {response}')

        return {
            "success": True,
            "data": {
                "contents": response
            },
            "error": None
        }
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {
            "success": False,
            "data": None,
            "error": "Failed to get feedback"
        }


@router.post("")
def create_quest(db: Session = Depends(get_db)):
    quest_service = QuestService(db)
    return quest_service.create_quest()


