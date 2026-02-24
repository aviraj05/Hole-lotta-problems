from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./hole_lotta_problems.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    YOLO_MODEL_PATH: str = "yolov8n.pt"
    DEVICE: str = "cpu"
    GROQ_API_KEY: str = ""
    TWITTER_API_KEY: str = ""
    TWITTER_API_SECRET: str = ""
    TWITTER_ACCESS_TOKEN: str = ""
    TWITTER_ACCESS_SECRET: str = ""
    HOTSPOT_THRESHOLD: int = 10
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
