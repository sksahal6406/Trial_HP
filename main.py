from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MessageRequest(BaseModel):
    message: str





@app.post("/message")
def post_message(body: MessageRequest):
    return {"received": body.message}

