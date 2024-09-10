from router.member_router import router as member_router
from router.lecture_router import router as lecture_router
from router.note_router import router as note_router
from router.quest_router import router as quest_router
from router.health_check import router as health_check


def init_router(app):
    app.include_router(lecture_router, prefix="/ai/lecture")
    app.include_router(member_router, prefix="/ai/member")
    app.include_router(note_router, prefix="/ai/note")
    app.include_router(quest_router, prefix="/ai/quest")
    app.include_router(health_check, prefix="/ai")
