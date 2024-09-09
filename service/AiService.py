from langchain_openai import ChatOpenAI

from repository.vector.VectorRepository import VectorRepository
from service.prompt import get_summary_prompt, get_answer_prompt
from router.request.note_request import NotePydantic
from config.ai.ai_env import OPENAI_API_KEY


class AiService:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", openai_api_key=OPENAI_API_KEY)
        self.vector_repository = VectorRepository()

    def summary(self, note: NotePydantic):
        content = note.content
        response = self.llm.invoke(get_summary_prompt(content))
        return response.content

    def feedback(self, question: str, answer: str):
        response = self.llm.invoke(get_answer_prompt(question, answer))
        return response.content

    def recommend(self, context: str):
        return self.vector_repository.get_retriever(context)
