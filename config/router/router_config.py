from router.member_router import router as member_router
from router.lecture_router import router as lecture_router
from router.ai_router import router as ai_router


def init_router(app):
    app.include_router(lecture_router)
    app.include_router(member_router)
    app.include_router(ai_router)
