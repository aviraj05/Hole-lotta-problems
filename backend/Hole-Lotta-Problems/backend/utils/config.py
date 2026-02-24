from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str = "redis://localhost:6379/0"
    YOLO_MODEL_PATH: str = "model/weights/yolov8_pothole.pt"
    DEVICE: str = "cuda"
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
