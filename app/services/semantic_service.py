from sentence_transformers import SentenceTransformer
import numpy as np
import json


class SemanticService:
    """
    Computes semantic similarity between an incoming prompt
    and known attack prompts using sentence embeddings.
    """

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.attack_prompts = self._load_attack_prompts()
        self.attack_embeddings = self.model.encode(self.attack_prompts)

    def _load_attack_prompts(self):
        with open("data/attack_prompts.json", "r", encoding="utf-8") as f:
            return json.load(f)

    def compute_similarity(self, prompt: str) -> float:
        prompt_embedding = self.model.encode([prompt])[0]

        similarities = np.dot(self.attack_embeddings, prompt_embedding) / (
            np.linalg.norm(self.attack_embeddings, axis=1) * np.linalg.norm(prompt_embedding)
        )

        return float(np.max(similarities))