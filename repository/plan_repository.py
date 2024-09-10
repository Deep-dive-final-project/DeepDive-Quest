from typing import Type

from sqlalchemy import desc
from sqlalchemy.orm import Session

from repository.models import Plan


class PlanRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_on_going_plans(self):
        return self.db.query(Plan).filter(Plan.state == "on_going").all()

    def get_latest_plan(self):
        return self.db.query(Plan).filter(Plan.state == 'on_going').order_by(desc(Plan.modified_date)).first()

    def get_plan(self, plan_id: int) -> Type[Plan] | None:
        return self.db.query(Plan).filter(Plan.plan_id == plan_id).first()
