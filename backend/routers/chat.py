from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

router = APIRouter()

GEMINI_API_URL = "https://api.openai.com/v1/chat/completions"

class ChatMessage(BaseModel):
    message: str

@router.post("/chat")
async def chat_completion(chat_message: ChatMessage):
#     if not chat_message.message:
#         raise HTTPException(status_code=400, detail="Not product found")
    try:
        # response = requests.post(GEMINI_API_URL, json={"message": message})
        # response.raise_for_status()
        # return response.json()

        # use fake response and echo user input
        response = {"message": chat_message.message}
        return response

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
