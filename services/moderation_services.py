from services.model_loader_service import get_classifier

classifier = get_classifier()


def moderate_text(challenge: str, recommendation: str = ""):
    text = f"{challenge} {recommendation}".strip()

    results = classifier(text)[0]

    scores = {
        item["label"].lower(): round(float(item["score"]), 4)
        for item in results
    }

    toxic_score = scores.get("toxic", 0)

    action = "allow"

    if toxic_score >= 0.85:
        action = "block"
    elif toxic_score >= 0.45:
        action = "review"

    return {
        "success": True,
        "action": action,
        "flagged": action != "allow",
        "categories": ["toxic"] if action != "allow" else [],
        "scores": scores
    }
