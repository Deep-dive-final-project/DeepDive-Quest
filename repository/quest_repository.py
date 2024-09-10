import logging
from datetime import datetime

from sqlalchemy import update
from sqlalchemy.orm import Session

from repository.models import Quest, QuestState


class QuestRepository:
    def __init__(self, db: Session):
        self.db = db

    def update_question(self, quest_id: int, feedback: str) -> None:
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

    def save(self, quest_data: dict) -> Quest:
        try:
            new_quest = Quest(content=quest_data['quest_content'],
                              task_id=quest_data['task_id'],
                              created_date=datetime.now().date(),
                              state=QuestState.UNSOLVED,
                              member_id=1)

            self.db.add(new_quest)
            self.db.commit()
            self.db.refresh(new_quest)

            return new_quest
        except Exception as e:
            logging.error(f"Error saving new Quest: {e}")
            self.db.rollback()
            raise
