from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    MODEL_PATH: str = "ml/saved_model"
    
    class Config:
        env_file = ".env"

settings = Settings()