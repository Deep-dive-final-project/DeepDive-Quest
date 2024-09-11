from langchain_openai import ChatOpenAI

from repository.cache_repository import QuestCache
from repository.vector.vector_repository import VectorRepository
from service.prompt import get_summary_prompt, get_answer_prompt, create_question_prompt
from router.request.note_request import NotePydantic
import os
import json


class AiService:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", openai_api_key=os.getenv('OPENAI_API_KEY'))
        self.vector_repository = VectorRepository()
        self.cache_repository = QuestCache()

    def summary(self, note: NotePydantic):
        content = note.content
        response = self.llm.invoke(get_summary_prompt(content))
        return response.content

    def feedback(self, question: str, answer: str):
        response = self.llm.invoke(get_answer_prompt(question, answer))
        return response.content

    def recommend(self, context: str):
        return self.vector_repository.get_retriever(context)

    def create_quest(self, plan: str, section: str, sub_sections: str, task_id: int) -> dict:
        response: str
        cache_key = plan + section
        cache = self.cache_repository.get_quest(cache_key)
        if cache:
            response = cache
        if cache is None:
            ai_answer = self.llm.invoke(create_question_prompt(plan, section, sub_sections))
            response = ai_answer.content
            print(response)
            self.cache_repository.save_quest(cache_key, response)

        return {
            'quest_content': json.loads(response)['quest_content'],
            'task_id': task_id
        }
