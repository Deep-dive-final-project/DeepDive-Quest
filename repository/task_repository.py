from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from repository.models import Task


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_task(self, task_id: int):
        return self.db.query(Task).filter(Task.task_id == task_id).first()

    def get_todays_task(self):
        today = datetime.now().date()

        return self.db.query(Task).filter(
            Task.complete_date >= today,
            Task.complete_date < today + timedelta(days=1)
        ).all()
