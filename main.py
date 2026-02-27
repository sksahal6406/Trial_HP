from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MessageRequest(BaseModel):
    message: str


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/heah")
def health_check2():
    return {"status": "ok"}


@app.post("/message")
def post_message(body: MessageRequest):
    return {"received": body.message}

