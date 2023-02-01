from pydantic import BaseModel, Field


class ShortUrlCreate(BaseModel):
    url: str = Field(..., min_length=1)
