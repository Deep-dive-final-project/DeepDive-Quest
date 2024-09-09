from sqlalchemy.orm import Session

from repository.plan_repository import PlanRepository


class PlanService:
    def __init__(self, db: Session):
        self.plan_repository = PlanRepository(db)

    def get_on_going_plans(self):
        return self.plan_repository.get_on_going_plans()

    def get_latest_plan(self):
        return self.plan_repository.get_latest_plan()

    def get_plan(self, plan_id: int):
        return self.plan_repository.get_plan(plan_id)