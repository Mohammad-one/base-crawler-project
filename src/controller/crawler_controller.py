from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.helpers.celery_worker import run_crawler_task

router = APIRouter()


class CrawlRequest(BaseModel):
    crawler_name: str
    url: str


@router.post("/crawl")
def run_crawler(request: CrawlRequest):
    try:
        task = run_crawler_task.delay(request.crawler_name, request.url)
        return {"status": "success", "task_id": task.id}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"unexpected error: {str(e)}")
