import requests
from config import HF_TOKEN

API_URL = "https://api-inference.huggingface.co/models/facebook/roberta-hate-speech-dynabench-r4-target"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def moderate_text(challenge: str, recommendation: str = ""):
    text = f"{challenge} {recommendation}".strip()

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": text},
        timeout=30
    )

    response.raise_for_status()

    results = response.json()
    labels = results[0]

    scores = {
        item["label"].lower(): round(float(item["score"]), 4)
        for item in labels
    }

    hate_score = scores.get("hate", 0)

    action = "allow"

    if hate_score >= 0.85:
        action = "block"
    elif hate_score >= 0.45:
        action = "review"

    return {
        "success": True,
        "action": action,
        "flagged": action != "allow",
        "categories": ["hate"] if action != "allow" else [],
        "scores": scores
    }
