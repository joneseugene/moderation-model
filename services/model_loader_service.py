from pathlib import Path
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from config import MODEL_DIRECTORY_ENV, MODEL_NAME_ENV

MODEL_NAME = MODEL_NAME_ENV
MODEL_DIR = Path(MODEL_DIRECTORY_ENV)


def get_classifier():
    if MODEL_DIR.exists():
        print("Loading AI model from local ai/ folder...")
        model_path = str(MODEL_DIR)
    else:
        print("AI model not found. Downloading and saving to ai/ folder...")

        MODEL_DIR.mkdir(parents=True, exist_ok=True)

        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

        tokenizer.save_pretrained(MODEL_DIR)
        model.save_pretrained(MODEL_DIR)

        model_path = str(MODEL_DIR)

    return pipeline(
        "text-classification",
        model=model_path,
        tokenizer=model_path,
        top_k=None
    )
