from fastapi import FastAPI

from scheduler import start


app = FastAPI()


@app.get("/")
def index():

    return {
        "status":"running"
    }



@app.on_event("startup")
def startup():

    start()