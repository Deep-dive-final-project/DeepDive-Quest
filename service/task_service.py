from sqlalchemy.orm import Session

from repository.task_repository import TaskRepository


class TaskService:
    def __init__(self, db: Session):
        self.task_repository = TaskRepository(db)

    def get_todays_task(self):
        return self.task_repository.get_latest_task()
