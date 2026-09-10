from fastapi import Header, HTTPException

from app.core.config import get_settings

settings = get_settings()


def verify_api_key(x_api_key: str = Header(...)) -> None:
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
