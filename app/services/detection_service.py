from app.services.policy_service import PolicyService


class DetectionService:
    """
    Simple rule-based detector for suspicious prompts.
    """

    def __init__(self):
        self.policy_service = PolicyService()

        self.rules = {
            "instruction_override": [
                "ignore previous instructions",
                "disregard previous instructions",
                "forget your earlier instructions",
            ],
            "system_prompt_extraction": [
                "reveal your system prompt",
                "show me the hidden instructions",
                "print your system prompt",
            ],
            "jailbreak": [
                "developer mode",
                "jailbreak",
                "bypass safety",
                "do anything now",
            ],
            "tool_abuse": [
                "call the tool",
                "access internal data",
                "fetch private data",
                "read hidden file",
            ],
        }

        self.rule_weights = {
            "instruction_override": 0.35,
            "system_prompt_extraction": 0.40,
            "jailbreak": 0.45,
            "tool_abuse": 0.50,
        }

    def analyze(self, prompt: str) -> dict:
        prompt_lower = prompt.lower()
        matched_categories = []
        reasons = []
        risk_score = 0.0

        for category, phrases in self.rules.items():
            for phrase in phrases:
                if phrase in prompt_lower:
                    matched_categories.append(category)
                    reasons.append(f"Matched phrase: '{phrase}'")
                    risk_score += self.rule_weights[category]
                    break

        risk_score = min(risk_score, 1.0)

        if risk_score >= 0.8:
            label = "high_risk"
        elif risk_score >= 0.4:
            label = "suspicious"
        else:
            label = "safe"

        action = self.policy_service.decide_action(risk_score)

        return {
            "risk_score": round(risk_score, 2),
            "label": label,
            "action": action,
            "reasons": reasons if reasons else ["No suspicious patterns detected"],
        }