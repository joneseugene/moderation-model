from fastapi import APIRouter, Header
from services.moderation_services import moderate_text
from utils.security import verify_api_key
from models.moderation_model import ModerationRequest

router = APIRouter()

@router.post("/moderate")
def moderate(
    payload: ModerationRequest,
    x_api_key: str | None = Header(default=None)
):
    verify_api_key(x_api_key)

    return moderate_text(
        payload.challenge,
        payload.recommendation or ""
    )