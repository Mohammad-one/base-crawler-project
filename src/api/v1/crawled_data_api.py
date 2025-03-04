from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.v1.crawler_api import router
from src.core.database import get_db
from src.repositories.crawled_data_repo import CrawledDataRepository

router = APIRouter()

@router.get("/crawled-data/{data_id}")
def get_crawled_data(data_id: int, db : Session = Depends(get_db)):
    repo = CrawledDataRepository(db)
    data = repo.get_crawled_data(data_id)
    if not data:
        raise HTTPException(status_code=404, detail="data not found")
    return data

@router.get("/crawled-data")
def get_all_crawled_data(limit: int = 10, db : Session = Depends(get_db)):
    repo = CrawledDataRepository(db)
    data = repo.get_all_crawled_data(limit)
