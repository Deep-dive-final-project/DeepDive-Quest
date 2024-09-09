from fastapi import FastAPI
from config.cors.corsconfig import add_cors_config
from repository import models
from config.database.db_config import engine
from config.router.router_config import init_router
from dotenv import load_dotenv


app = FastAPI()

load_dotenv()
add_cors_config(app)
init_router(app)

models.Base.metadata.create_all(bind=engine)
