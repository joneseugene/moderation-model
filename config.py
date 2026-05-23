import os
from dotenv import load_dotenv

load_dotenv()


MODERATION_API_KEY = os.getenv("MODERATION_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")
PORT = int(os.getenv("PORT", 8000))

ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000"
).split(",")
