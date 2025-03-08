from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncResult

from src.helpers.celery_worker import run_crawler_task

router = APIRouter()


class CrawlRequest(BaseModel):
    crawler_name: str
    url: str

    @router.get("/crawl/{task_id}")
    def get_crawler_status(task_id: str):
        """Check the status of a crawler task by task_id"""
        result = AsyncResult(task_id)

        # Debugging Logs
        print(f"Task ID: {task_id}, State: {result.state}, Result: {result.result}")

        if result.state == "PENDING":
            return {"status": "PENDING"}

        elif result.state == "SUCCESS":
            if isinstance(result.result, str):
                return {"status": "SUCCESS", "data": result.result}  # <-- Fixes the str issue

            return {"status": "SUCCESS", "result": result.result}

        elif result.state == "FAILURE":
            return {"status": "FAILED", "error": str(result.info)}

        else:
            return {"status": result.state}


@router.post("/crawl")
def run_crawler(request: CrawlRequest):
    try:
        task = run_crawler_task.delay(request.crawler_name, request.url)
        return {"status": "success", "task_id": task.id}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"unexpected error: {str(e)}")



