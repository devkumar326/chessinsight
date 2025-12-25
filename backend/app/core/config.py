from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ChessInsight"
    environment: str = "development"

settings = Settings()