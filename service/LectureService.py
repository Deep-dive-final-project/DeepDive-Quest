from sqlalchemy.orm import Session

from repository.LectureRepository import LectureRepository
from repository.models import Section
from router.response.LectureListResponse import LectureListResponse
from service.AiService import AiService
from service.PlanService import PlanService


class LectureService:
    def __init__(self, db: Session):
        self.lecture_repository = LectureRepository(db)
        self.plan_service = PlanService(db)
        self.ai_service = AiService()

    def recommend_lecture(self):
        plan = self.plan_service.get_latest_plan()
        lecture_title: str = plan.lecture.title
        section_names: list[str] = [section.name for section in plan.lecture.sections]
        context: str = lecture_title + ',' + ','.join(section_names)
        results = self.ai_service.recommend(context)

        return [LectureListResponse(
            id=result.metadata['id'],
            title=result.metadata['title'],
            instructor=result.metadata['instructor'],
            price=result.metadata['price'],
            image_url=result.metadata['image_url'],
            lecture_url=result.metadata['lecture_url']
        ) for result in results[1:]]
