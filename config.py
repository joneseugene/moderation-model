import os
from dotenv import load_dotenv

load_dotenv()

MODERATION_API_KEY = os.getenv("MODERATION_API_KEY")

PORT = os.getenv("PORT")

MODEL_NAME_ENV = os.getenv(
    "MODEL_NAME",
    "unitary/multilingual-toxic-xlm-roberta"
)

MODEL_DIRECTORY_ENV = os.getenv(
    "MODEL_DIRECTORY",
    "ai/multilingual-toxic-xlm-roberta"
)

ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000"
).split(",")
