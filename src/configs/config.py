import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/postgres")

    SELENIUM_DRIVER_PATH = "/snap/bin/geckodriver"
    #HEADLESS_MODE: bool = os.getenv("HEADLESS", True).lower() == "true"

    SELENIUM_TIMEOUT: int = os.getenv("SELENIUM_TIMEOUT", 10)
    SELENIUM_WINDOW_SIZE: int = os.getenv("SELENIUM_WINDOW_SIZE", "1920, 1080")
    SELENIUM_USER_AGENT: str = os.getenv("SELENIUM_USER_AGENT", "Mozilla/5.0")

    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")

settings = Settings()
