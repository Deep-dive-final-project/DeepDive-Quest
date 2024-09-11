import logging

from sqlalchemy.orm import Session

from repository.quest_repository import QuestRepository
from service.ai_service import AiService
from json import loads
import random
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
        data = {}
        tasks = self.task_service.get_todays_task()
        if not tasks:
            return []
        for task in tasks:
            if task.plan.title not in data:
                data[task.plan.title] = []
            data[task.plan.title].append({
                'task_id': task.task_id,
                'title': task.title
            })
        # 랜덤하게 키 하나 선택
        plan = random.choice(list(data.keys()))

        # 선택된 키의 value에서 랜덤하게 값 하나 선택
        selected_section = random.choice(data[plan])
        selected_task = self.task_service.get_task(selected_section['task_id'])
        sub_sections = selected_task.section.sub_section
        title = selected_task.title
        task_id = selected_section['task_id']
        quest = self.ai_service.create_quest(plan, title, sub_sections, task_id)
        quest = self.quest_repository.save(quest)
        return quest
