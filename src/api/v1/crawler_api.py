from fastapi import APIRouter, HTTPException

from pydantic import BaseModel
from src.services.crawler_service import crawler_service

router = APIRouter()
class CrawlRequest(BaseModel):
    url: str
    crawler_name: str

@router.post("/crawl")
def run_crawler(request: CrawlRequest):
    try:
        data = crawler_service.run_crawler(request.crawler_name, request.url)
        return {"status": "success", "data" : data}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"unexpected error: {str(e)}")
