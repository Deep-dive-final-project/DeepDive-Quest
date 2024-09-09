from typing import Type

from sqlalchemy.orm import Session
from .models import Member


class MemberRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_member(self, member_id: int) -> Type[Member] | None:
        return self.db.query(Member).filter(Member.member_id == member_id).first()
