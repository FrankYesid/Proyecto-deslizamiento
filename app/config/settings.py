from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Satellite Image Classification"
    API_V1_STR: str = "/api/v1"

    # API Credentials
    CLIENT_ID: str
    CLIENT_SECRET: str
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./satellite.db"
    
    # MLflow settings
    MLFLOW_TRACKING_URI: str = "http://127.0.0.1:5000"

    # ML Model settings
    MODEL_DIR: str = "models"
    DEFAULT_MODEL: str = "satellite_classifier"
    
    # Satellite imagery settings
    MAX_IMAGE_SIZE: int = 10485760  # 10MB in bytes
    SUPPORTED_IMAGE_FORMATS: List[str] = [".jpg", ".jpeg", ".png", ".tiff"]
    
    # CORS settings
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
