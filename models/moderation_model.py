from pydantic import BaseModel, Field

class ModerationRequest(BaseModel):
    challenge: str = Field(..., min_length=1, max_length=1000)
    recommendation: str | None = Field(default="", max_length=1000)