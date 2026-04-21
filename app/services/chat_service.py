from app.services.detection_service import DetectionService


class ChatService:
    def __init__(self):
        self.detector = DetectionService()

    def handle_chat(self, prompt: str) -> dict:
        analysis = self.detector.analyze(prompt)

        label = analysis["label"]

        # 🚫 Block high-risk prompts
        if label == "high_risk":
            return {
                "status": "blocked",
                "message": "Request blocked due to high-risk prompt.",
                "analysis": analysis
            }

        # ⚠️ Warn for suspicious prompts
        elif label == "suspicious":
            return {
                "status": "warning",
                "message": "Prompt may be unsafe. Proceeding with caution.",
                "response": self._fake_llm_response(prompt),
                "analysis": analysis
            }

        # ✅ Allow safe prompts
        else:
            return {
                "status": "allowed",
                "response": self._fake_llm_response(prompt),
                "analysis": analysis
            }

    def _fake_llm_response(self, prompt: str) -> str:
        # Placeholder for real LLM call
        return f"LLM response to: {prompt}"