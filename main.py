from fastapi import FastAPI
from config.cors.corsconfig import add_cors_config

app = FastAPI()

add_cors_config(app)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
