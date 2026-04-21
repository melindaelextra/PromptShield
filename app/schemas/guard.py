from typing import List
from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="User prompt to analyze")


class AnalyzeResponse(BaseModel):
    risk_score: float
    label: str
    action: str
    reasons: List[str]