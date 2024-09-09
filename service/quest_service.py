import logging

from sqlalchemy.orm import Session

from repository.quest_repository import QuestRepository
from service.ai_service import AiService
from json import loads

from service.task_service import TaskService


class QuestService:
    def __init__(self, db: Session):
        self.ai_service = AiService()
        self.task_service = TaskService(db)
        self.quest_repository = QuestRepository(db)

    def get_feedback(self, quest_id: int, question: str, answer: str):
        feedback = self.ai_service.feedback(question, answer)
        logging.info(f'[quest service] feedback: {feedback}')
        response = loads(feedback)
        logging.info(f'[quest service] response: {response}')
        self.quest_repository.update_question(quest_id, feedback)
        return response

    def create_quest(self):
        lecture_names = set()
        tasks = self.task_service.get_todays_task()

        # self.ai_service.create_quest()
        # self.quest_repository.create_quest()