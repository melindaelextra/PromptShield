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