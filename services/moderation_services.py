

from services.model_loader_service import get_classifier


classifier = get_classifier()


def moderate_text(
    challenge: str,
    recommendation: str = ""
):
    text = f"{challenge} {recommendation}".strip()

    results = classifier(text)[0]

    scores = {
        item["label"]: round(float(item["score"]), 4)
        for item in results
    }

    toxic = scores.get("toxic", 0)
    severe_toxic = scores.get("severe_toxic", 0)
    threat = scores.get("threat", 0)
    obscene = scores.get("obscene", 0)
    insult = scores.get("insult", 0)

    action = "allow"

    if severe_toxic >= 0.65 or threat >= 0.75 or toxic >= 0.90:
        action = "block"

    elif (
        toxic >= 0.45
        or obscene >= 0.45
        or insult >= 0.50
        or threat >= 0.35
    ):
        action = "review"

    flagged_categories = [
        key
        for key, value in scores.items()
        if value >= 0.45
    ]

    return {
        "success": True,
        "action": action,
        "flagged": action != "allow",
        "categories": flagged_categories,
        "scores": scores
    }