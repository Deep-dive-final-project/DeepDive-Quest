from fastapi import APIRouter, Depends, HTTPException
from repository.member_repository import MemberRepository
from sqlalchemy.orm import Session
from config.database.dbconfig import get_db
from router.response.member_response import MemberResponse


router = APIRouter()


@router.get("/{member_id}", response_model=MemberResponse)
def get_member(member_id: int, db: Session = Depends(get_db)):
    member_repository = MemberRepository(db)
    member = member_repository.get_member(member_id)
    if member is None:
        raise HTTPException(status_code=500, detail="사용자가 존재하지 않습니다")
    return member
