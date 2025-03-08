from celery import Celery
from src.services.crawler_service import crawler_service
import os

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_BACKEND = os.getenv("CELERY_BACKEND", "redis://localhost:6379/0")

celery_app = Celery("crawler_tasks", broker=CELERY_BROKER_URL, backend=CELERY_BACKEND)


@celery_app.task()
def run_crawler_task(crawler_name: str, url: str):
    return crawler_service.run_crawler(crawler_name, url)
