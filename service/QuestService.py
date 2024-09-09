from sqlalchemy.orm import Session

from repository.QuestRepository import QuestRepository
from service.AiService import AiService
from json import loads


class QuestService:
    def __init__(self, db: Session):
        self.ai_service = AiService()
        self.quest_repository = QuestRepository(db)

    def get_feedback(self, quest_id: int, question: str, answer: str):
        feedback = self.ai_service.feedback(question, answer)

        response = loads(feedback)
        print('response')
        print(response)

        print('feedback')
        print(feedback)

        self.quest_repository.update_question(quest_id, feedback)
        print('saved')
        return response
