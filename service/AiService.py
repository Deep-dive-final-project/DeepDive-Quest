import io

from config.ai.ai_env import OPENAI_API_KEY
from langchain_openai import ChatOpenAI


class AiService:
    def __init__(self):
        self.client = ChatOpenAI(model="gpt-4o")

    def translate(self, audio):
        print('audio=', audio)
        transcription = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=audio
        )
        return transcription.text

    def summary(self, text: str):
        pass
