from fastapi import FastAPI
from config.cors.corsconfig import add_cors_config
from repository import models
from router.api_router import router
from config.database.db_config import engine


app = FastAPI()

add_cors_config(app)

models.Base.metadata.create_all(bind=engine)

app.include_router(router)