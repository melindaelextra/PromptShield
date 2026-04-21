import json
from app.services.detection_service import DetectionService

detector = DetectionService()


def load_data(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def evaluate():
    safe_prompts = load_data("data/safe_prompts.json")
    attack_prompts = load_data("data/attack_prompts.json")

    safe_correct = 0
    attack_correct = 0
    false_positives = []
    false_negatives = []

    print("\n--- SAFE PROMPTS ---")
    for prompt in safe_prompts:
        result = detector.analyze(prompt)
        label = result["label"]
        print(f"{prompt} -> {label}")

        if label == "safe":
            safe_correct += 1
        else:
            false_positives.append((prompt, label, result["reasons"]))

    print("\n--- ATTACK PROMPTS ---")
    for prompt in attack_prompts:
        result = detector.analyze(prompt)
        label = result["label"]
        print(f"{prompt} -> {label}")

        if label != "safe":
            attack_correct += 1
        else:
            false_negatives.append((prompt, label, result["reasons"]))

    total = len(safe_prompts) + len(attack_prompts)
    correct = safe_correct + attack_correct

    accuracy = correct / total if total else 0.0
    safe_accuracy = safe_correct / len(safe_prompts) if safe_prompts else 0.0
    attack_recall = attack_correct / len(attack_prompts) if attack_prompts else 0.0

    print("\n=== Evaluation Summary ===")
    print(f"Total prompts: {total}")
    print(f"Safe prompts: {len(safe_prompts)}")
    print(f"Attack prompts: {len(attack_prompts)}")
    print(f"Correct safe classifications: {safe_correct}")
    print(f"Correct attack detections: {attack_correct}")
    print(f"False positives: {len(false_positives)}")
    print(f"False negatives: {len(false_negatives)}")
    print(f"Overall accuracy: {accuracy:.2f}")
    print(f"Safe accuracy: {safe_accuracy:.2f}")
    print(f"Attack recall: {attack_recall:.2f}")

    if false_positives:
        print("\nExamples of false positives:")
        for prompt, label, reasons in false_positives[:5]:
            print(f"- Prompt: {prompt}")
            print(f"  Predicted: {label}")
            print(f"  Reasons: {reasons}")

    if false_negatives:
        print("\nExamples of false negatives:")
        for prompt, label, reasons in false_negatives[:5]:
            print(f"- Prompt: {prompt}")
            print(f"  Predicted: {label}")
            print(f"  Reasons: {reasons}")


if __name__ == "__main__":
    evaluate()