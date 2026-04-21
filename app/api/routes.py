from fastapi import APIRouter
from app.schemas.guard import AnalyzeRequest, AnalyzeResponse
from app.services.detection_service import DetectionService

router = APIRouter()
detection_service = DetectionService()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_prompt(request: AnalyzeRequest):
    return detection_service.analyze(request.prompt)

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()


class ChatRequest(BaseModel):
    prompt: str


@router.post("/chat")
def chat(request: ChatRequest):
    return chat_service.handle_chat(request.prompt)