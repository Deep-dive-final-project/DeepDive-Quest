from langchain_openai import ChatOpenAI
from service.prompt import get_summary_prompt
from router.request.note_request import NotePydantic
from config.ai.ai_env import OPENAI_API_KEY


class AiService:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", openai_api_key=OPENAI_API_KEY)

    def summary(self, note: NotePydantic):
        content = note.content
        response = self.llm.invoke(get_summary_prompt(content))
        return response.content

