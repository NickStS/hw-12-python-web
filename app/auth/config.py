from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

settings = Settings(
    SECRET_KEY="your-secret-key",
    ALGORITHM="HS256",
    ACCESS_TOKEN_EXPIRE_MINUTES=30
)
