from fastapi import FastAPI
from pydantic import BaseModel


class NotePydantic(BaseModel):
    content: str
