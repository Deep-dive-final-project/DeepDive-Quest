import logging

from sqlalchemy.orm import Session

from repository.lecture_repository import LectureRepository
from router.response.lecture_list_response import LectureListResponse
from service.ai_service import AiService
from service.plan_service import PlanService


class LectureService:
    def __init__(self, db: Session):
        self.lecture_repository = LectureRepository(db)
        self.plan_service = PlanService(db)
        self.ai_service = AiService()

    def recommend_lecture(self, plan_id: int):
        try:
            plan = self.plan_service.get_plan(plan_id)
            lecture_title: str = plan.lecture.title
            section_names: list[str] = [section.name for section in plan.lecture.sections]
            context: str = lecture_title + ',' + ','.join(section_names)
            results = self.ai_service.recommend(context)

            return {
                "success": True,
                "data": {
                    "contents": [LectureListResponse(
                        id=result.metadata['id'],
                        title=result.metadata['title'],
                        instructor=result.metadata['instructor'],
                        price=result.metadata['price'],
                        image_url=result.metadata['image_url'],
                        lecture_url=result.metadata['lecture_url']
                    ) for result in results[1:]]},
                "error": None
            }
        except Exception as e:
            logging.error(f"Error updating Quest {e}")
            return {
                "success": False,
                "data": None,
                "error": "Failed to recommend lecture"
            }

    def recommend_latest_lecture(self):
        try:
            plan = self.plan_service.get_latest_plan()
            lecture_title: str = plan.lecture.title
            section_names: list[str] = [section.name for section in plan.lecture.sections]
            context: str = lecture_title + ',' + ','.join(section_names)
            results = self.ai_service.recommend(context)

            return {
                "success": True,
                "data": {
                    "contents": [LectureListResponse(
                        id=result.metadata['id'],
                        title=result.metadata['title'],
                        instructor=result.metadata['instructor'],
                        price=result.metadata['price'],
                        image_url=result.metadata['image_url'],
                        lecture_url=result.metadata['lecture_url']
                    ) for result in results[1:]]},
                "error": None
            }
        except Exception as e:
            logging.error(f"[LectureService] recommend_latest_lecture {e}")
            return {
                "success": False,
                "data": None,
                "error": "Failed to recommend lecture"
            }
