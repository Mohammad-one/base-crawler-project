from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.repositories.crawled_data_repo import CrawledDataRepository

router = APIRouter()


@router.get("/crawled_data/{data_id}")
def get_crawled_data(data_id: int, db: Session = Depends(get_db)):
    repo = CrawledDataRepository(db)
    data = repo.get_crawled_data(data_id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data


@router.get("/crawled_data")
def get_all_crawled_data(limit: int = 10, db: Session = Depends(get_db)):
    repo = CrawledDataRepository(db)
    return repo.get_all_crawled_data(limit)
