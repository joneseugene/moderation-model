from huggingface_hub import InferenceClient
from config import HF_TOKEN

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN,
)


def moderate_text(challenge: str, recommendation: str = ""):
    text = f"{challenge} {recommendation}".strip()

    result = client.text_classification(
        text,
        model="unitary/toxic-bert",
    )

    scores = {
        item.label.lower(): round(float(item.score), 4)
        for item in result
    }

    toxic = scores.get("toxic", 0)
    obscene = scores.get("obscene", 0)
    insult = scores.get("insult", 0)
    threat = scores.get("threat", 0)
    severe_toxic = scores.get("severe_toxic", 0)
    identity_hate = scores.get("identity_hate", 0)

    block = (
        threat >= 0.55
        or severe_toxic >= 0.60
        or identity_hate >= 0.60
        or insult >= 0.60
        or obscene >= 0.85
        or (
            toxic >= 0.95
            and insult >= 0.50
        )
    )

    action = "block" if block else "allow"

    categories = []

    if toxic >= 0.60:
        categories.append("toxic")

    if obscene >= 0.75:
        categories.append("obscene")

    if insult >= 0.50:
        categories.append("insult")

    if threat >= 0.55:
        categories.append("threat")

    if severe_toxic >= 0.60:
        categories.append("severe_toxic")

    if identity_hate >= 0.60:
        categories.append("identity_hate")

    return {
        "success": True,
        "action": action,
        "flagged": block,
        "categories": categories,
        "scores": scores
    }
