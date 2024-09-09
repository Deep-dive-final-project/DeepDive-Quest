from sqlalchemy.orm import Session

from repository.PlanRepository import PlanRepository


class PlanService:
    def __init__(self, db: Session):
        self.plan_repository = PlanRepository(db)

    def get_on_going_plans(self):
        return self.plan_repository.get_on_going_plans()

    def get_latest_plan(self):
        return self.plan_repository.get_latest_plan()
