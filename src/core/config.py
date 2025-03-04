import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    SELENIUM_DRIVER_PATH: str = os.getenv("SELENIUM_DRIVER_PATH", "chromedriver")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/postgres")
    HEADLESS_MODE: bool = os.getenv("HEADLESS", True).lower() == "true"

    SELENIUM_TIMEOUT: int = os.getenv("SELENIUM_TIMEOUT", 10)
    SELENIUM_WINDOW_SIZE: int = os.getenv("SELENIUM_WINDOW_SIZE", "1920, 1080")
    SELENIUM_USER_AGENT: str = os.getenv("SELENIUM_USER_AGENT", "Mozilla/5.0")


settings = Settings()

