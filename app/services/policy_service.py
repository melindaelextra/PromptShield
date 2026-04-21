class PolicyService:
    """
    Maps risk scores to actions.
    """

    def decide_action(self, risk_score: float) -> str:
        if risk_score >= 0.8:
            return "block"
        if risk_score >= 0.4:
            return "warn"
        return "allow"