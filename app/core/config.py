from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    API_KEY: str = ""
    REDIS_URL: str = "redis://localhost:6379/0"

    LOCALHOST_URL: str = "http://localhost:3000"
    STAGING_URL: str = ""
    PROD_URL: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
