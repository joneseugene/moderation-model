from fastapi import HTTPException
from config import MODERATION_API_KEY


def verify_api_key(api_key: str | None):

    if not api_key:
        raise HTTPException(
            status_code=401,
            detail="API key missing"
        )

    if api_key != MODERATION_API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid API key"
        )
