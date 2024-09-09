import logging

from sqlalchemy import update
from sqlalchemy.orm import Session

from repository.models import Quest


class QuestRepository:
    def __init__(self, db: Session):
        self.db = db

    def update_question(self, quest_id: int, feedback: str):
        try:
            stmt = (
                update(Quest)
                .where(Quest.quest_id == quest_id)
                .values(feedback=feedback)
            )

            self.db.execute(stmt)
            self.db.commit()

            logging.info(f"Quest {quest_id} successfully updated with new feedback.")
        except Exception as e:
            logging.error(f"Error updating Quest {quest_id}: {e}")
            self.db.rollback()
            raise
