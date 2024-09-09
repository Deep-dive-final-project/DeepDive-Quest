from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database.db_config import get_db
from service.AiService import AiService

router = APIRouter()