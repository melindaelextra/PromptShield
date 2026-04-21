from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="PromptShield API",
    version="0.1.0",
    description="A simple LLM prompt risk analyzer and firewall."
)

app.include_router(router)