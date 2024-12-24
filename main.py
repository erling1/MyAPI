from fastapi import FastAPI
from pydantic import BaseModel
from anthropic import AI_respons
from fastapi.middleware.cors import CORSMiddleware
import uuid
import asyncio
from fastapi.responses import StreamingResponse

app = FastAPI()

class Payload(BaseModel):
    Message: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/chats")
async def create_chat():
    chat_id = str(uuid.uuid4())
    return {"id": chat_id}


@app.post("/chats/{chatID}")
async def post_message( chatID: str, payload: Payload):

    chat_id = chatID

    message = payload.Message

    #stream = AI_respons(message=message)


    return StreamingResponse(AI_respons(message=message), media_type="text/event-stream")



@app.post("/camera")
async def get_camera_feed():
    None






"""@app.get("/chats")
async def read_root():

    return {"Message": "Congrats! This is your first API!"}"""