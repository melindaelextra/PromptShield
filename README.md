## Initial Evaluation

The first rule-based version achieved 0.64 accuracy on a small evaluation set. It correctly classified all safe prompts but missed several attack variants due to narrow phrase coverage.

## Improved Evaluation

After expanding the rule set with additional instruction-override, jailbreak, system prompt extraction, and confidential-data patterns, the detector achieved 1.00 accuracy on the same evaluation set.

## Key Insight

The main limitation of the original detector was low recall on paraphrased attacks. Expanding phrase coverage substantially improved performance, demonstrating the importance of adversarial variation in prompt attack detection.