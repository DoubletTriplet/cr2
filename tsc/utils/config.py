from pydantic_settings import BaseSettings, SettingsConfigDict
import logging

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TSC_", case_sensitive=True)
    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_USER: str
    MONGODB_PASSWORD: str
    MONGODB_DATABASE: str
    MONGODB_COLLECTION: str
    DEBUG: bool


SETTINGS = Settings()
logging.info('API Settings loaded')