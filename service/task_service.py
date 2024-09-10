from sqlalchemy.orm import Session

from repository.models import Task
from repository.task_repository import TaskRepository


class TaskService:
    def __init__(self, db: Session):
        self.task_repository = TaskRepository(db)

    def get_task(self, task_id: int) -> Task | None:
        return self.task_repository.get_task(task_id)

    def get_todays_task(self) -> list[Task]:
        return self.task_repository.get_todays_task()
