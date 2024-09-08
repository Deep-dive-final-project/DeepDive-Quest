from router.member_router import router as member_router
from router.lecture_router import router as lecture_router
from router.note_router import router as note_router


def init_router(app):
    app.include_router(lecture_router, prefix="/api/lecture")
    app.include_router(member_router, prefix="/api/member")
    app.include_router(note_router, prefix="/api/note")
