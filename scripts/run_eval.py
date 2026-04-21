import json
from app.services.detection_service import DetectionService

detector = DetectionService()


def load_data(path):
    with open(path, "r") as f:
        return json.load(f)


def evaluate():
    safe_prompts = load_data("data/safe_prompts.json")
    attack_prompts = load_data("data/attack_prompts.json")

    correct = 0
    total = 0

    print("\n--- SAFE PROMPTS ---")
    for p in safe_prompts:
        result = detector.analyze(p)
        print(p, "->", result["label"])

        if result["label"] == "safe":
            correct += 1
        total += 1

    print("\n--- ATTACK PROMPTS ---")
    for p in attack_prompts:
        result = detector.analyze(p)
        print(p, "->", result["label"])

        if result["label"] != "safe":
            correct += 1
        total += 1

    accuracy = correct / total
    print(f"\nAccuracy: {accuracy:.2f}")


if __name__ == "__main__":
    evaluate()